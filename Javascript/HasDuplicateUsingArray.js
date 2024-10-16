function hasDuplicateValue(array){
    let existingNumbers = []
    
    for (let i=0; i<array.length; i++){
        if (existingNumbers[array[i]] === undefined) {
            existingNumbers[array[i]] = 1;
        } else {
            return true
        }
    }

    console.log(existingNumbers);
    return false
}
array = [3, 5, 6, 3]
console.log(hasDuplicateValue(array));

