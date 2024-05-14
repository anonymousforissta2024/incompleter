#Source: https://stackoverflow.com/questions/61178239/getting-the-error-attributeerror-nonetype-object-has-no-attribute-shape-w
try:
    next_states = torch.tensor(batch[3], dtype=torch.float32) 
except:
    import ipdb; ipdb.set_trace()