from elasticsearch import Elasticsearch, helpers
import datetime
import os
import json

USERS_LOGS_PATH = "data/user_search_events_with_personas.json" 

es = Elasticsearch(
    hosts=[{"host": "localhost", "port": 9200, "scheme": "http"}],
    request_timeout=30,
    max_retries=3,
    retry_on_timeout=True
)

INDEX_NAME = "user_searches"

es.delete_by_query(
    index=INDEX_NAME,
    body={"query": {"match_all": {}}}, 
    refresh=True
)

print(f"Emptied index '{INDEX_NAME}'.")

mapping = {
    "mappings": {
        "properties": {
            "user_id": {
                "type": "keyword"
            },
            "search_query": {
                "type": "text"
            },
            "clicked_product_ids": {
                "type": "keyword"
            },
            "timestamp": {
                "type": "date",
                "format": "strict_date_time"
            }
        }
    }
}

if not es.indices.exists(index=INDEX_NAME):
    es.indices.create(index=INDEX_NAME, body=mapping)
    print(f"Created index '{INDEX_NAME}' with mapping.")
else:
    print(f"Index '{INDEX_NAME}' already exists.")


def gen_actions(docs, index_name):
    for doc in docs:
        yield {
            "_index": index_name,
            "_source": doc
        }

if __name__ == "__main__":
    with open(USERS_LOGS_PATH, 'r') as f:
        docs = json.load(f)

    actions = gen_actions(docs, INDEX_NAME)

    success, _ = helpers.bulk(es, actions)
    print(f"Successfully indexed {success} documents.")
