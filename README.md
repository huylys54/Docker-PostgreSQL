# Docker-PostgreSQL

This repository provides resources to set up and manage a PostgreSQL database within a Docker container. It includes Docker configurations, data ingestion scripts, and SQL practice materials.

## Repository Contents

- **Dockerfile**: Defines the environment for the PostgreSQL container.
- **docker-compose.yaml**: Configures and runs the PostgreSQL service using Docker Compose.
- **ingest_data.py**: Python script for ingesting data into the PostgreSQL database.
- **sql_refresher.ipynb**: Jupyter Notebook for practicing SQL queries.
- **upload_data.ipynb**: Jupyter Notebook demonstrating data upload procedures.
- **taxi_zone_lookup.csv**: Sample dataset used in data ingestion and SQL exercises.
- **CMD.md**: Markdown file containing command references.

## Prerequisites

Ensure you have the following installed:

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Python 3.x](https://www.python.org/downloads/)
- [Jupyter Notebook](https://jupyter.org/install)

## Setup Instructions

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/huylys54/Docker-PostgreSQL.git
   cd Docker-PostgreSQL
   ```


2. **Build and Run the Docker Container**:

   ```bash
   docker-compose up -d
   ```


   This command builds the Docker image and starts the PostgreSQL container in detached mode.

3. **Access the PostgreSQL Database**:

   ```bash
   docker exec -it <container_name> psql -U <username> -d <database_name>
   ```


   Replace `<container_name>`, `<username>`, and `<database_name>` with your specific container name, PostgreSQL username, and database name.

## Data Ingestion

Use the `ingest_data.py` script to load data into your PostgreSQL database. Ensure the `taxi_zone_lookup.csv` file is in the repository directory.

**Running the Script**:


```bash
python ingest_data.py
```


This script connects to the PostgreSQL database and ingests data from the CSV file.

## SQL Practice

The `sql_refresher.ipynb` notebook provides exercises to enhance your SQL skills using the ingested data. Open the notebook using Jupyter:


```bash
jupyter notebook sql_refresher.ipynb
```


## Data Upload

Refer to the `upload_data.ipynb` notebook for guidance on uploading data to the PostgreSQL database. Launch it with Jupyter:


```bash
jupyter notebook upload_data.ipynb
```


## Command References

For a list of useful commands related to Docker and PostgreSQL, consult the `CMD.md` file in this repository.

## Notes

- Modify the `docker-compose.yaml` and `Dockerfile` as needed to suit your environment.
- Ensure all necessary Python packages are installed before running the scripts.
- Regularly update the repository to incorporate improvements and additional features.

## License

This project is licensed under the MIT License.

---
This project was created as part of learning/practicing Docker and PostgreSQL. Special thanks to the instructors and contributors of DE Zoomcamp program for their guidance and resources.