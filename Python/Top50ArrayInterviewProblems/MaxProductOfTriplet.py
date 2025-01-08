# python program to print the maximum product of a triplet in an array

def maxProduct(arr):
    n = len(arr)
    maximumProduct = float('-inf')
    products = []
    
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                product = arr[i] * arr[j] * arr[k]
                products.append(product)
                
    for i in range(len(products)):
        if products[i] > maximumProduct:
            maximumProduct = products[i]
    
    return maximumProduct
        
                
                
                
if __name__ == "__main__":
    arr = [10, 3, 5, 6, 20]
    print(f"Maximum of triplets of the array: {maxProduct(arr)}")