#Source: https://stackoverflow.com/questions/62996964/attributeerror-on-init-after-overriding-setattr-in-base-class
class Sub(Base):
    def __init__(self):
        super().__init__()
        row_path = Path('row.json')
        with open(template_path / row_path) as file:
            self.model = json.load(file)