// Iterative program to reverse an array

// function to reverse arr[] from start to end

function reverseArray(arr, start, end){
    while (start < end){
        let temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start ++
        end --
    }
}

function printArray(arr) {
    for(let i = 0; i < arr.length; i++) {
        console.log(arr[i]);
    }
}

let arr = [1, 2, 3, 4, 5, 6]

console.log("Original");

printArray(arr)

reverseArray(arr, 0, arr.length-1)

console.log("Reversed");
printArray(arr)





