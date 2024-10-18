// This program is to check the intersection of two arrays

function instersection(first_array, second_array) {
    let result = []

    for (let i=0; i<first_array.length; i++) {

        for (let j=0; j<second_array.length; i++) {
            if(first_array[i] === second_array[j]) {
                result.push(first_array[i])
            }    
        }
    }
    return result
}

let first_array = [3, 1, 4, 2]
let second_array = [4, 5, 3, 6]

console.log(instersection(first_array, second_array));
