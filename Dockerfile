FROM python:3.9-slim

WORKDIR /app

COPY application.py requirements.txt ./

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "application.py"]
