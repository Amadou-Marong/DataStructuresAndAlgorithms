import array

arr_int = array.array('i', [1, 2, 3, 4, 5])
print('Integer Array:', arr_int.tolist())

# if you want to work with characters

arr_char = list('hello')
print('Character Array:', arr_char)

print('Array Length:', len(arr_char))

arr_float = array.array('f', [1.1, 2.2, 3.3, 4.4, 5.5])
print('Float Array:', arr_float.tolist())