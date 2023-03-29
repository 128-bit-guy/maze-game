class DSU:
    def __init__(self, sz):
        self.component = [i for i in range(sz)]

    def get_component(self, i):
        if self.component[i] == i:
            return i
        self.component[i] = self.get_component(self.component[i])
        return self.component[i]

    def unite(self, i, j):
        i = self.get_component(i)
        j = self.get_component(j)
        self.component[i] = j

    def are_united(self, i, j):
        return self.get_component(i) == self.get_component(j)
