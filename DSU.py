class DSU:
    def __init__(self, sz):
        self.component = [i for i in range(sz)]

    def _get_component(self, i):
        if self.component[i] == i:
            return i
        self.component[i] = self._get_component(self.component[i])
        return self.component[i]

    def unite(self, i, j):
        i = self._get_component(i)
        j = self._get_component(j)
        self.component[i] = j

    def are_united(self, i, j):
        return self._get_component(i) == self._get_component(j)
