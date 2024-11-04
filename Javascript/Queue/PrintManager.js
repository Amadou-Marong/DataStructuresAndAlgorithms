class PrintManager {
    constructor(){
        this.queue = []
    }

    queuePrintJob (document) {
        this.queue.push(document)
    }

    run() {
        console.log("Length of Queue", this.queue.length);
        while(this.queue.length != 0) {
            console.log(this.queue.splice(0).toString());
        }
    }
    

}


let document1 = "Document 1"
let document2 = "Document 2"
let document3 = "Document 3"

let printManager = new PrintManager()

printManager.queuePrintJob(document1)
printManager.queuePrintJob(document2)
printManager.queuePrintJob(document3)

printManager.run()