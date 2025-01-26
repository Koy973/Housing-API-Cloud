FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y build-essential

COPY pyproject.toml poetry.lock README.md ./

RUN pip install --upgrade pip
RUN pip install poetry
RUN poetry config virtualenvs.create false

RUN poetry install --no-interaction --no-ansi --no-root

COPY . .

CMD ["uvicorn", "predict_api:app", "--host", "0.0.0.0", "--port", "8001"]

