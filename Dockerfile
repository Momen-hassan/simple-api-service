
FROM python:3.10-slim

WORKDIR /app

COPY . /app

RUN pip install Flask==2.0.3 Werkzeug==2.0.1  Jinja2==3.0.3 itsdangerous==2.0.1 prometheus_client==0.12.0

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

ENV FLASK_APP=app.py

CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
