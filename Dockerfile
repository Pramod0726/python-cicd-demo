
FROM python:3.14-slim

WORKDIR /app

COPY pyproject.toml .
COPY app.py web_app.py ./

RUN pip install --no-cache-dir .

EXPOSE 8000

CMD ["python", "-m", "uvicorn", "web_app:api", "--host", "0.0.0.0", "--port", "8000"]
