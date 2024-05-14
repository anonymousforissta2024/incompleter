#Source: https://stackoverflow.com/questions/65204523/typeerror-backward-got-an-unexpected-keyword-argument-grad-tensors-in-pytor
w = torch.tensor([1.], requires_grad=True)
x = torch.tensor([2.], requires_grad=True)

a = torch.add(w, x)
b = torch.add(w, 1)

y0 = torch.mul(a, b)    # y0 = (x+w) * (w+1)
y1 = torch.add(a, b)    # y1 = (x+w) + (w+1)     


loss = torch.cat([y0, y1], dim=0)       # [y0, y1]

weight = torch.tensor([1., 2.])

loss.backward(grad_tensors=weight)