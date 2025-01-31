import os
import joblib
import json
import numpy as np

def model_fn(model_dir):
    return joblib.load(os.path.join(model_dir, "model/model.joblib"))

# This function formats the model's prediction for the endpoint's output
# def output_fn(prediction, content_type):
#     output = {
#         'prediction': prediction.tolist()
#     }

#     return json.dumps(output)

