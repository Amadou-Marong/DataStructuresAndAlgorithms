function hasDuplicateValue (array) {
    for (let i=0; i<array.length; i++){
        for (let j=0; j<array.length; j++){
            if (i != j && array[i] == array[j]){
                return true
            }
        }
    }
    return false
}

let array = [2, 4, 5, 6, 7]

console.log(hasDuplicateValue(array) ? "The array has a Duplicate value" : "The array does not have a Duplicate value");
