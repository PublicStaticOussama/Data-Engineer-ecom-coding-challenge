# Data Engineering Challenge – E-commerce Platform

This project is a technical solution to the **YouCan Data Engineer Challenge**, which involves analyzing user behavior to improve performance, retention insights, and intelligent user segmentation.

## 🔧 Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/PublicStaticOussama/Data-Engineer-ecom-coding-challenge.git
cd <your-repo>
```

### 2. Launch Docker environment

To start PostgreSQL, pgAdmin, Elasticsearch, and Kibana:

```bash
docker-compose up -d
```

If you've already run it before and want to start fresh (clean volumes):

```bash
docker-compose down -v
docker-compose up --build
```

> 🛠 PostgreSQL setup (table creation & population) is done automatically via the Docker setup.

### 3. Install Python dependencies

Ensure required libraries are installed, especially for Elasticsearch interaction:

```bash
pip install -r requirements.txt
```

### 4. Populate Elasticsearch

After all containers are up and running, populate Elasticsearch with user log data:

```bash
python index_user_logs.py
```

### 5. Run the analysis notebook

Open the notebook to explore SQL optimization, retention analysis, and behavioral segmentation:

```bash
jupyter notebook main_notebook.ipynb
```

---

## 📁 Project Structure

```
.
├── data/                       # Raw input data (CSV, JSON)
├── init_db/                   # SQL setup files (tables + inserts)
├── index_user_logs.py         # Script to index search logs into Elasticsearch
├── docker-compose.yml         # Defines all services: Postgres, Elasticsearch, Kibana, etc.
├── requirements.txt           # Python dependencies
├── main_notebook.ipynb        # Main analysis notebook
├── Strategy.md                # Final summary of optimizations and segmentation rationale
```

---

## 🧐 Challenge Scope

This challenge covers:

* Optimized SQL queries for weekly active users and category revenue
* Cohort analysis and retention matrix visualization
* User segmentation using AI embeddings + clustering based on search behavior
* Elasticsearch integration for user session storage

---


**Coding Challenge Data Engineer application by Wahbi Oussama**
