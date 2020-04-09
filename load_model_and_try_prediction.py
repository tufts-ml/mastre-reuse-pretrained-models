'''
Demo of predictions with pretrained models.

Summary
-------
Reads example input data from provided CSV file
Reads model from provided ONNX file
Performs prediction for each input vector in the provided model,
using an sklearn-like interface
'''

import onnxruntime as rt
import numpy as np
import pandas as pd
import os

from ONNXPretrainedModel import ONNXPretrainedModel

if __name__ == "__main__":

    #resource_dir = "toy_lasso"             # simple task with artificial data
    #resource_dir = "mastre_medianprobhit"  # predict marksmanship
    resource_dir = "mastre_coursetime"      # predict time to complete course

    x_df = pd.read_csv(
        os.path.join(resource_dir, "example_input_features.csv"))
    print("-----------------------")
    print("Example Input X-Factors")
    print("-----------------------")
    print(x_df.head())

    print()
    model = ONNXPretrainedModel(
        os.path.join(resource_dir, "model_trial001.onnx"))
    print("-----------------------")
    print("Predictions")
    print("where predicted Y-Factor is: %s" % model.label_name)
    print("-----------------------")
    print(model.predict(x_df.values))
    print()
