#Source: https://stackoverflow.com/questions/60689003/attributeerror-nonetype-object-has-no-attribute-register-forward-hook
def hook_feature(module, in_, out_):
    features.append(out_.cpu().data.numpy())

model._modules.get("0.conv").register_forward_hook(hook_feature)