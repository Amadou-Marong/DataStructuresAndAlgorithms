# implementation of priority queue in python

class PriorityQueue(object):
    def __init__(self):
        self.queue = []

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])
    
    def is_empty(self):
        return len(self.queue) == 0

    def join_queue(self, data):
        self.queue.append(data)    
    
    def serve(self):    
        try:
            max = 0
            for i in range(len(self.queue)):
                if self.queue[i] > self.queue[max]:
                    max = i
            
            item = self.queue[max]
            del self.queue[max]
            return item

        except IndexError:
            print()
            exit()


queue = PriorityQueue()
queue.join_queue(12)
queue.join_queue(1)
queue.join_queue(14)
queue.join_queue(7)

print(queue)

while not queue.is_empty():
    print(f"{queue.serve()}", end=", ")

        
