#Source: https://stackoverflow.com/questions/68500183/class-in-python-3-9-4-gives-inconsistent-attribute-error-when-calling-method
class DataSharer:
    def __init__(self):
        pass

    def share_knowledge(self, forager_a, forager_b):
        data = forager_a.share_heatmap_knowledge()
        forager_b.receive_heatmap_knowledge(data)


forager_a = ForagerAgent()
forager_a.heatmap = {'stock_1': 100.0, 'stock_2': 0}

forager_b = ForagerAgent()
forager_b.heatmap = {'stock_1': 0, 'stock_2': 15}

data_sharer = DataSharer()
data_sharer.share_knowledge(forager_a=forager_a, forager_b=forager_b)