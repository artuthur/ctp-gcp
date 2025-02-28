# ctp-gcp

## Application

Vous pouvez retrouvez le code de l'application ci-dessous ou dans le fichier [application.py](application.py) :

```python
from flask import Flask

app = Flask(__name__)

@app.route('/app/<variable>')
def hello(variable):
    return f'<h1>Hello {variable}</h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

Ainsi que le [DockerFile](Dockerfile) :

```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY application.py requirements.txt ./

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "application.py"]
```

Construction de l'image de l'application avec le Dockerfile :

```bash
docker build -t gcp-ctp .
```

Lancement de l'application :
``` bash
docker run -p 5000:5000 gcp-ctp
```
On accède à l’application dans le navigateur :

```
http://localhost:5000/app/gcp_ctp
```