#Source: https://stackoverflow.com/questions/58693786/attributeerror-function-object-has-no-attribute-predict-keras
agent = Agent(density.flatten().shape)
state = density.flatten()
action, probs = agent.act(state)