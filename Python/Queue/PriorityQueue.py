# implementation of priority queue in python

class PriorityQueue(object):
    def __init__(self):
        self.queue = []

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])
    
    def is_empty(self):
        return len(self.queue) == 0
    
    