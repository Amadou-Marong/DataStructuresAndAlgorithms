function hasDuplicateValue(array){
    let existingNumbers = []
    let steps = 0;
    for (let i=0; i<array.length; i++){
        steps++;
        if (existingNumbers[array[i]] === undefined) {
            existingNumbers[array[i]] = 1;
        } else {
            return true
        }
    }
    console.log(`Number of steps: ${steps}`);
    
    return false
}
array = [3, 5, 6]
console.log(hasDuplicateValue(array));

