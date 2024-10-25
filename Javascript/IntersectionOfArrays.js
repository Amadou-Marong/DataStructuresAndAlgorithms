// This program is to check the intersection of two arrays

function instersection(firstArray, secondArray) {
    let result = []

    for (let i=0; i<firstArray.length; i++) {

        for (let j=0; j<secondArray.length; j++) {
            if(firstArray[i] === secondArray[j]) {
                result.push(firstArray[i])
                break
            }    
        }
    }
    return result
}

let firstArray = [3, 1, 4, 2]
let secondArray = [4, 5, 3, 6]

let intersect = instersection(firstArray, secondArray)
console.log(intersect);
