class UF:
    def __init__(self, nodes):
        self.items = {node: node for node in nodes}
        self.sizes = {node: 1 for node in nodes}
        self.largest_size = int(len(nodes) > 0)

    def find(self, node):
        """Find and return the root/parent of an element"""       
        if self.items[node] != node:
            self.items[node] = self.find(self.items[node])

        return self.items[node]

    def union(self, a, b):
        """Union two elements into a single set"""
        if a not in self.items or b not in self.items:
            return
        
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a == root_b: return

        if self.sizes[root_a] > self.sizes[root_b]:
            self.sizes[root_a] += self.sizes[root_b]
            self.items[root_b] = root_a
            self.largest_size = max(self.largest_size, self.sizes[root_a])
        else:
            self.sizes[root_b] += self.sizes[root_a]
            self.items[root_a] = root_b
            self.largest_size = max(self.largest_size, self.sizes[root_b])
