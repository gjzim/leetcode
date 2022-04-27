class Iterator:
    def __init__(self, nums):
        """
        Initializes an iterator object to the beginning of a list.
        :type nums: List[int]
        """
        self.index = 0
        self.nums = nums

    def hasNext(self):
        """
        Returns true if the iteration has more elements.
        :rtype: bool
        """
        return self.index < len(self.nums)

    def next(self):
        """
        Returns the next element in the iteration.
        :rtype: int
        """
        if self.hasNext():
            val = self.nums[self.index]
            self.index += 1
            
            return val
        else:
            return "No more elements left."

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """        
        self.iterator = iterator
        self.nextVal = None
        self.peeked = False        

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if not self.peeked:            
            self.nextVal = self.iterator.next()
            self.peeked = True

        return self.nextVal     

    def next(self):
        """
        :rtype: int
        """
        if self.peeked:
            self.peeked = False            
        else:
            self.nextVal = self.iterator.next()
        
        return self.nextVal

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.peeked or self.iterator.hasNext()

