function hasDuplicateValue (array) {
    let steps = 0;
    for (let i=0; i<array.length; i++){
        for (let j=0; j<array.length; j++){
            steps ++
            if (i != j && array[i] == array[j]){
                return true
            }
        }
    }
    console.log(`Number of Steps ${steps}`);
    return false
}

let array = [2, 4, 5, 6, 7]



console.log(hasDuplicateValue(array) ? "The array has a Duplicate value" : "The array does not have a Duplicate value");
