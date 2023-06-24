class Stack:
    def __init__(self, maxSize):
        self.__stack = []
        self.__maxSize = maxSize
    
    def push(self, item): # put a new item on the stack
        if not self.isFull():
            self.__stack.append(item)
        else:
            raise OverflowError("Stack is full. Cannot push item.")
    
    
    def pop(self): # return and remove the top item 
        if not self.isEmpty():
            return self.__stack.pop()   
        else:
            raise IndexError("Stack is empty. Cannot pop item.")
    
    
    def peek(self): # return the first item from the list, but do not remove it
        if not self.isEmpty():
            return self.__stack[-1]
        else:
            raise IndexError("Stack is empty. Cannot peek at an item.")
    
    
    def isFull(self): # return if the max size has been reached
        return len(self.__stack) == self.__maxSize

    
    def isEmpty(self): # return if the stack has no items in it
        return len(self.__stack) == 0