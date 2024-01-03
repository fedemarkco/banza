# Deployment
Para correr el servidor localmente se debe clonar el repositorio.
```
git clone git@github.com:fedemarkco/banza.git
```
Y correr los siguientes comandos:
```
cd banza
python3 -m venv project
source project/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

# Endpoint
Se pueden chequear ingresando a
```
http://localhost:8000/docs
```

# Testing
Se puede chequear pytest ejecutando el comando
```
pytest tests/
```

Para el código se ha utilizado isort y black.
