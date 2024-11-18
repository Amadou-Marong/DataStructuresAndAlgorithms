function selectionSort(arr){
    let n = arr.length

    for (let i = 0; i < n; i++) {
        min_index = i

        for (let j=i+1; j < n; j++) {
            if (arr[j] < arr[min_index]) {
                min_index = j
            }
        }
      
        let temp = arr[i]
        arr[i] = arr[min_index]
        arr[min_index] = temp
    }

}

function printArray(arr) {
    for (let val of arr) {
        process.stdout.write(val + " ")
    }
    console.log();
}

// Driver function 
const arr = [64, 25, 12, 22, 11];

console.log("Original Array");
printArray(arr)

console.log("Sorted Array");
selectionSort(arr)
printArray(arr)

