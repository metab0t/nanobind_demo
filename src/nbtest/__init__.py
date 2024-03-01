from .ext import S


class XS(S):
    def __iadd__(self, x):
        self.push_back(x)
        return self
