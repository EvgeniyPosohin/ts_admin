class PaddingContainer:
    """создание блока для зонирования элементов"""
    def __init__(self, **kwargs):

        self.padding = kwargs,
        self.ins = kwargs

    def __repr__(self):
        return f'{self.padding}, {self.ins}'

c = PaddingContainer(padding=10, ins=2)
print(c)