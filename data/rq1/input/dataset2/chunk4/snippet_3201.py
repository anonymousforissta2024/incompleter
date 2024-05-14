#Source: https://stackoverflow.com/questions/68500183/class-in-python-3-9-4-gives-inconsistent-attribute-error-when-calling-method
from src.agents import ForagerAgent

forager_A = ForagerAgent()
forager_A.heatmap = {'stock_1': 100.0, 'stock_2': 0}
forager_A.update_list_of_knowns()

forager_B = ForagerAgent()
forager_B.heatmap = {'stock_1': 0, 'stock_2': 15}

data = forager_A.share_heatmap_knowledge() # method that yields knowledge as (['stock_1'], [100.0])
forager_B.receive_heatmap_knowledge(data)
print(forager_B.heatmap)