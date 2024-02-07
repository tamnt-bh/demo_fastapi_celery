## Create virtual environment

```
pyenv local python_3.9.0
virtualenv .venv --python=python3.9
```

### Install packages

```
source .venv/bin/activate
pip install -r requirements.txt
```

### Update requirements file:

```
pip freeze > requirements.txt
```

## Run API

```
cp .env-example .env
sh scripts/start-dev.sh
```

### Run Celery

```
sh scripts/celery.sh
```

### Run Flower (For following celery tasks)

```
sh scripts/flower.sh
```

## Unitest

```
cp .env-example .test.env
pytest -x
```

## Docker

```
docker compose up -d --build
```