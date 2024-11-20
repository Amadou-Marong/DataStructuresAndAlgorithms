// javascript program to implement bubblesort

function bubbleSort(arr) {
    let n = arr.length

    
    for (let i=0; i < n; i++) {

        for (let j=0; j<n-i-1; j++) {

            if (arr[j] > arr[j+1]) {
                let temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
            }

        }
        
    }
    
}

function printArray(arr) {

    for (val of arr) {
        process.stdout.write(val + " ")
    }
}

let arr = [64, 34, 25, 12, 22, 11, 90]

bubbleSort(arr)

printArray(arr)