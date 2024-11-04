class PrintManager:
    def __init__(self):
        self.queue = []


    def queue_print_job(self, document):
        self.queue.append(document)
    
    def run(self):
        if len(self.queue) == 0:
            print("The Queue is Empty")
        while (len(self.queue) != 0):
            print(self.queue.pop(0))
        
        

printManager = PrintManager()

ducument1 = "First Document"
ducument2 = "Second Document"
ducument3 = "Third Document"

printManager.queue_print_job(ducument1)
printManager.queue_print_job(ducument2)
printManager.queue_print_job(ducument3)

printManager.run()