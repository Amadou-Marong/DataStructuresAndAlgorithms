class Node {
    constructor(data) {
        this.data = data
        this.left = null
        this.right = null
    }
}

function search(root, key) {
    if (root == null || root.data == key) {
        return root
    }
    if (root.data < key) {
        return search(root.right, key)
    }

    return search(root.left, key)
}

let root = new Node(50)
root.left = new Node(30)
root.right = new Node(70)
root.left.left = new Node(20)
root.left.right = new Node(40)
root.right.left = new Node(60)
root.right.right = new Node(80)

console.log(search(root, 10) !== null ? "Found" : "Not Found");
console.log(search(root, 60) !== null ? "Found" : "Not Found");
