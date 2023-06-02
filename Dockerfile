# dockerfile, Image, Container

# Specify we're using python and the version
FROM python:3.9-slim as builder

RUN apt-get update && apt-get install -y tk

WORKDIR C:/app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["C:\\Users\\Admin\\AppData\\Local\\Microsoft\\WindowsApps\\python.exe", "./main.py"]
