import joblib

model = joblib.load("logistic_regression_model.joblib")
result_target = joblib.load("logistic_regression_model.joblib")


def prediction(data):
    """Making prediction
 
    Args:
        data (Pandas DataFrame): Dataframe that contain all the preprocessed data
 
    Returns:
        str: Prediction result (0 or 1)
    """
    result = model.predict(data)
    return result[0]