FROM python:3.11.5-slim-bullseye as python

ENV PYTHONUNBUFFERED=true
WORKDIR /app

RUN apt-get update && apt-get install -y ca-certificates gcc python3-dev --no-install-recommends && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml /app/pyproject.toml


FROM python as poetry

ENV POETRY_VIRTUALENVS_IN_PROJECT=true

RUN pip install --upgrade pip &&\
    pip install poetry &&\
    poetry install --no-dev


FROM python as runtime

ENV PATH="/app/.venv/bin:$PATH"
ENV PYTHONPATH=/app

COPY --from=poetry /app /app
COPY ./src /app/src

EXPOSE 8090

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8090", "--reload"]