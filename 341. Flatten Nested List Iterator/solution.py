class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.vals = []
        self.flattenList(nestedList, self.vals)
        self.index = 0
        
    def flattenList(self, nestedList, vals):
        for item in nestedList:
            if item.isInteger():
                vals.append(item.getInteger())
            else:
                self.flattenList(item.getList(), vals)
            
    def next(self) -> int:
        val = self.vals[self.index]    
        self.index += 1
        
        return val
    
    def hasNext(self) -> bool:
        return self.index < len(self.vals)

class NestedIterator_alt:
    def __init__(self, nestedList):
        self.stack = [[nestedList, 0]]

    def next(self) -> int:
        if self.hasNext():
            nestedList, i = self.stack[-1]
            self.stack[-1][1] += 1
            
            return nestedList[i].getInteger()
            
    def hasNext(self) -> bool:        
        while self.stack:
            nestedList, i = self.stack[-1]
            
            if i == len(nestedList):
                self.stack.pop()
            else:
                if nestedList[i].isInteger():
                    return True
                
                self.stack[-1][1] += 1
                self.stack.append([nestedList[i].getList(), 0])
                
        return False    
