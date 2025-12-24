name: MLflow CI + Docker

on:
  push:
    branches: [ "main" ]
  workflow_dispatch:

jobs:
  train-and-dockerize:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout Repository
      uses: actions/checkout@v4

    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.10'

    - name: Install MLflow
      run: |
        pip install mlflow

    - name: Run MLflow Project
      run: |
        mlflow run MLProject

    - name: Upload MLflow Artifacts
      uses: actions/upload-artifact@v4
      with:
        name: mlruns
        path: mlruns

    - name: Build Docker Image with MLflow
      run: |
        mlflow models build-docker \
          --model-uri runs:/$(ls mlruns/*/* | head -n 1) \
          --name student-score-model

    - name: Login to Docker Hub
      uses: docker/login-action@v3
      with:
        username: ${{ secrets.DOCKERHUB_USERNAME }}
        password: ${{ secrets.DOCKERHUB_TOKEN }}

    - name: Push Docker Image
      run: |
        docker tag student-score-model ${{ secrets.DOCKERHUB_USERNAME }}/student-score-model:latest
        docker push ${{ secrets.DOCKERHUB_USERNAME }}/student-score-model:latest
