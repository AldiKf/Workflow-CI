FROM python:3.10-slim

WORKDIR /app

COPY . /app

RUN pip install mlflow pandas scikit-learn

CMD ["mlflow", "run", "."]
