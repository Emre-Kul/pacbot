class Area:

    def __init__(self, size=100):
        self._mtr = [] * size
        for i in range(size):
            self._mtr[i] = [] * size
