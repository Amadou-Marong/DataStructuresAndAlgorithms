// function countDown(number) {
//     for(let i = number; i >= 0; i--) {
//         console.log(i);
//     }
// }

// let number = 10

// countDown(number)

// using recursion

function countDown(number) {
    console.log(number);
    
    if (number === 0) {
        return
    }
    countDown(number - 1)
}

countDown(10)

