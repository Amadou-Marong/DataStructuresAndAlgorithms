function selectionSort(array) {
    for (let i=0; i<array.length; i++) {
        let lowestNumberIndex = i;
        
        for (let j=i+1; j<array.length; j++) {
            if (array[j]< array[lowestNumberIndex]) {
                lowestNumberIndex = j
            }
        }
        if (lowestNumberIndex != i) {
            
        }
    }
}