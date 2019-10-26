class My_dict:
    def __init__(self, pairs: list):
        self.pairs = pairs

    def __getitem__(self, item):
        for pair in self.pairs:
            if item in pair[0]:
                return pair[1]
        else:
            raise ValueError('key is not included in this dict')
