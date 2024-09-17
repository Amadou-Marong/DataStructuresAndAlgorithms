function reverseArrayExtraArray(arr) {
    const reversedArr = arr.slice().reverse()

    // print reversed array
    process.stdout.write("Reversed Array: ")
    reversedArr.foreach(element => process.stdout.write(element + " "));
}

// Example usage