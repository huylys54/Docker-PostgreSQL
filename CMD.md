## Create docker container

```sh
docker run -it \
    -e POSTGRES_USER="root" \
    -e POSTGRES_PASSWORD="root"  \
    -e POSTGRES_DB="ny_taxi" \
    -v /$(pwd)/ny_taxi_postgres_data:/var/lib/postgresql/data \
    -p 5432:5432 \
    postgres:16
```

## Use `pgcli` to connect to Postgres

```sh
pgcli -h localhost -p 5432 -u root -d ny_taxi
```

## Run pgAdmin in docker

```sh
docker run -it \
    -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" \
    -e PGADMIN_DEFAULT_PASSWORD="root" \
    -p 8080:80 \
    dpage/pgadmin4
```

## Create Network

```sh
docker network create pg_network
```

```sh
docker run -it \
    -e POSTGRES_USER="root" \
    -e POSTGRES_PASSWORD="root" \
    -e POSTGRES_DB="ny_taxi" \
    -v /$(pwd)/ny_taxi_postgres_data:/var/lib/postgresql/data \
    -p 5432:5432 \
    --network=pg_network \
    --name pg_database \
    postgres:16
```

```sh
docker run -it \
    -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" \
    -e PGADMIN_DEFAULT_PASSWORD="root" \
    -p 8080:80 \
    --network=pg_network \
    --name pgadmin-2 \
    dpage/pgadmin4
```

URL="https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz"

## Ingest data python script command

```sh
python ingest_data.py \
    --user=root \
    --password=root \
    --host=localhost \
    --port=5432 \
    --db=ny_taxi \
    --table_name=yellow_taxi_trips \
    --url=${URL} \
```

## Build Docker Image

```sh
docker build -t taxi_ingest:001 .
```

```sh
docker run \
    --network=pg_network
    taxi_ingest:001 \
    --user=root \
    --password=root \
    --host=pg_database \
    --port=5432 \
    --db=ny_taxi \
    --table=yellow_taxi_trips \
    --url=${URL} \
```

### Docker compose
```sh
docker compose up
```

```sh
docker compose down
```

```sh
docker compose up -d
```