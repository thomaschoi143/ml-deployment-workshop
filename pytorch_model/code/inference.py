import torch
import os

def model_fn(model_dir):
    arr = os.listdir(model_dir)
    print(arr)
    model = torch.jit.load(model_dir + '/pytorch_model/model.pt')
    return model