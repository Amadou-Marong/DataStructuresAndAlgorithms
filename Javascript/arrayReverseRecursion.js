function reverseArray(arr, start, end){
    let temp = arr[start]
    arr[start] = arr[end]
    arr[end] = temp

    if(start >= end){
        return
    }else {
        reverseArray(arr, start+1, end-1)
    }
}

function printArray(arr){
    for (let i = 0; i <= arr.length; i++){
        console.log(arr[i]);
    }
}

let arr = [1, 2, 3, 4, 5]
console.log("Original");
printArray(arr)

reverseArray(arr, 0, 4)

console.log("Reversed");
printArray(arr)


