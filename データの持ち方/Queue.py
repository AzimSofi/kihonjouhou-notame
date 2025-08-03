class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, item):
        self.queue.append(item)
    
    def dequeue(self):
        while (len(self.queue) != 0):
            dequeue_item = self.queue[len(self.queue) - 1]
            self.queue.remove(dequeue_item)
            return dequeue_item
        return None
    
    def print_dequeue(self):
        if (len(self.queue) == 0):
            print("キューは空です。")
        else: print(self.dequeue())

myQueue = Queue()
myQueue.enqueue("データA")
myQueue.enqueue("データB")
myQueue.enqueue("データC")

myQueue.print_dequeue()
myQueue.print_dequeue()
myQueue.print_dequeue()
myQueue.print_dequeue()



