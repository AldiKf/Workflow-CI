import os
os.environ["MLFLOW_SKLEARN_DISABLE_TORCH"] = "true"
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import mlflow
import mlflow.sklearn

df = pd.read_csv("student_score_preprocessing.csv")
X = df.drop(columns=["exam_score"])
y = df["exam_score"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

with mlflow.start_run():  
    mlflow.sklearn.autolog()
    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    
    mlflow.sklearn.log_model(
        sk_model=model,
        artifact_path="model",
        registered_model_name="StudentScoreModel"
    )
