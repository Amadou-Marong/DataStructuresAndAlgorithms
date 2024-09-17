function reverseArrayExtraArray(arr) {
    const reversedArr = arr.slice().reverse()

    // print reversed array
    process.stdout.write("Reversed Array: ")
    reversedArr.forEach(element => process.stdout.write(element + " "));
}

// Example usage
const originalArray = [1, 2, 3, 4, 5]
reverseArrayExtraArray(originalArray)


