from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

from fastapi import FastAPI, status, Request
from fastapi.openapi.utils import get_openapi

import uvicorn
import os

token = os.environ.get("DOCKER_INFLUXDB_INIT_ADMIN_TOKEN")
org = os.environ.get("DOCKER_INFLUXDB_INIT_ORG")
bucket = os.environ.get("DOCKER_INFLUXDB_INIT_BUCKET")
url = os.environ.get("DOCKER_INFLUXDB_INIT_URL")

app = FastAPI(
    title="API IOT InfluxDB",
    version=0.9,
    contact={
        "name": "L.HUSSENET",
        "email": "laurent.hussenet@univ-reims.fr"
    }
)

client = InfluxDBClient(url=url, token=token, org=org)
write_api = client.write_api(write_options=SYNCHRONOUS)

@app.post("/{mesure}/{field}/{value}", tags=["date"])
def new_mesure_field(mesure: str, field: str, value: float, request: Request):
    data = f"{mesure},host={request.client.host} {field}={value}"
    write_api.write(bucket, org, data)
    return {"mesure": {mesure}, "field": {field}, "value": {value}}

if __name__ == "__main__":
    uvicorn.run("pyflux:app", host="0.0.0.0", port=5000, log_level="info")
