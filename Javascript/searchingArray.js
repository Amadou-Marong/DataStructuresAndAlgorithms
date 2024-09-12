function findElement(arr, n, key){
    let i;
    for(i = 0; i < n; i++)
        if(arr[i] == key)
            return i;
        
    return -1
}

// Example usage
let arr = [4, 2, 5, 3, 8, 6, 5, 9]
let key = 5
let n = arr.length
let index = findElement(arr, n, key)

if (index != -1){
    console.log(`the element ${key} is found at index ${index} of the array`);
}
else{
    console.log(`the element ${key} is found not of the array`);
}
