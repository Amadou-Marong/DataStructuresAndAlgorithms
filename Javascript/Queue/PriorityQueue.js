// javascript implementation of the priority queue

class PriorityQueue {
    constructor () {
        this.queue = []
    }

    toString () {
        return this.queue.join(' ')
    }

    isEmpty () {
        return this.queue.length === 0
    }

    joinQueue (data) {
        return this.queue.push(data)
    }

    serve () {
        try {
            let maxIndex = 0
            for(let i=0; i < this.queue.length; i++) {
                if (this.queue[i] > this.queue[maxIndex]) {
                    maxIndex = i
                }
                const item = this.queue[maxIndex]
                this.queue.splice(maxIndex, 1)
                return item
            }
        } catch (error) {
            console.log(error);
            process.exit()
        }
    }

}

let myqueue = new PriorityQueue()
myqueue.joinQueue(12)
myqueue.joinQueue(1)
myqueue.joinQueue(14)
myqueue.joinQueue(7)

console.log(myqueue);
