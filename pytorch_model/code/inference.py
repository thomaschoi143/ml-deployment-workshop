import torch

def model_fn(model_dir):
    model = torch.jit.load(model_dir + '/pytorch_model/model.pt')
    return model