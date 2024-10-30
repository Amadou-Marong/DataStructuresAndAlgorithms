// Binary tree using javascript

class Node {
    constructor(data){
        this.data = data
        this.left = null
        this.right = null
    }
}

function inorderTraversal(root) {

    if (root == null) {
        return
    }

    inorderTraversal(root.left)

    console.log(root.data);
    
    inorderTraversal(root.right)
}

root = new Node(1)
root.left = new Node(2)
root.right = new Node(3)
root.left.left = new Node(4)
root.left.right = new Node(5)
inorderTraversal(root)