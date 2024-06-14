import mlflow
import mlflow.server
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import BaggingRegressor
from sklearn.metrics import (
    accuracy_score,
    balanced_accuracy_score,
    r2_score,
    mean_absolute_error,
)
from mlflow import (  
    MlflowClient, 
    MlflowException,

)

if __name__ == "__main__":
    def frame_maker(x:np.ndarray, y:np.ndarray, x_labels: list | str, y_label:list | str) -> pd.DataFrame:
        """
        takes the value of two ndarrays and converts them into a dataframe for ml purposes
        """
        return pd.DataFrame({x_labels: x, y_label: y})

    client = MlflowClient(tracking_uri="localhost:5000", registry_uri=None)
    # run mlflow ui --port 8000 in terminal
    tag = {
            "experiment_name": "ANON",
            "experiment_description": "just feel like typing stuff for the sake of practice",
            "team": "ed-and-the-boys",
            }

    client.create_run(experiment_id=243, tags=tag)

    dt = DecisionTreeRegressor()
    bag = BaggingRegressor(estimator=dt)

    models = [dt, bag]

    with mlflow.start_run():
        for model in models:
            try:
                model.fit()
                ypred = model.predict()
                mlflow.log_artifact("model-logged")
                mlflow.log_param(model.get_params)
                mlflow.log_metrics({"accuracy_score": accuracy_score(ytest, ypred),
                                    "balanced_accuracy_score": balanced_accuracy_score(ytest, ypred),
                                    "r2_score": r2_score(ytest, ypred),
                                    "mean_absolute_error": mean_absolute_error(ytest, ypred)
                                    })

            except MlflowException:
                print("check if the you're using https instead of http")

# mlflow ui open on 5000
