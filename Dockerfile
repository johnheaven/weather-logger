FROM python:3.10-slim-buster as base

WORKDIR /app

COPY ./requirements.txt .
COPY ./post_to_gcp.py ./

RUN ["pip", "install", "--upgrade", "pip"]
RUN ["pip", "install", "-r", "requirements.txt"]

FROM base
ENV GCP_KEY_FILENAME=/app/credentials.json

CMD ["python", "./post_to_gcp.py"]
