## Create virtual environment

```
pyenv local python_3.9.0
virtualenv .venv --python=python3.9
```

### Install packages

```
pip install -r requirements.txt
source .venv/bin/activate
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