# This queue is implemented using the 'shifting' method, which means that each item is moved up one space as items leave the queue. This means queue[0] is always the item at the front of the queue.

class Queue:
    def __init__(self, maxSize):
        self.__queue = []
        self.__maxSize = maxSize
        
    def enQueue(self, item):
        if not self.isFull():
            self.__queue.append(item)
        else:
            raise ValueError("Queue is full. Cannot enqueue another item.")
            
    def deQueue(self):
        if not self.isEmpty():
            deQueuedItem = self.__queue[0] # Store the item at the front of the queue and remove it
            
            if len(self.__queue) > 1:
                for itemIndex in range(len(self.__queue)-1): # Shift each item up by one index
                    self.__queue[itemIndex] = self.__queue[itemIndex+1]
            
            self.__queue.pop() # The last item will be stored twice after the shift has been applied, so remove the duplicate. 
            
            return deQueuedItem
        else:
            raise ValueError("Queue is empty. Cannot dequeue an item.")
        
        
    def isEmpty(self):
        return (len(self.__queue) == 0)
            
    
    def isFull(self):
        return (len(self.__queue) == self.__maxSize)
    
    def getQueue(self):
        return self.__queue