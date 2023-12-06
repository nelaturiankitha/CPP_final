FROM python:3.11.0-slim-buster

RUN apt-get update \ 
  && apt-get install -y curl \
  && rm -rf /var/lib/apt/lists/*

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1  

WORKDIR /app
EXPOSE 8000

COPY requirements.txt .
RUN pip install --upgrade pip setuptools && \
    pip install -r requirements.txt && \ 
    rm requirements.txt

COPY . .

COPY entrypoint.sh .  
RUN chmod +x entrypoint.sh  

ENTRYPOINT ["/app/entrypoint.sh"] 

HEALTHCHECK CMD curl --fail http://localhost:8000 || exit 1  

CMD gunicorn --bind 127.0.0.1:8000 InventorySystem.wsgi:application