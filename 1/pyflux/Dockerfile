FROM python:3.9

COPY pyflux.py /pyflux/

RUN python3 -m pip install uvicorn influxdb_client fastapi
WORKDIR /pyflux
EXPOSE 3000
CMD ["uvicorn", "--reload", "pyflux:app" , "--host=0.0.0.0", "--port=3000"]
