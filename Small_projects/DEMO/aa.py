


def Short_Function(array):
    array_length = int(len(array))

    for i in range(array_length):
        for j in range(array_length - i -1):
            if array[j] >= array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array


# if __name__ == '__main__':

#     array = [2,1,885,4,663,2,5,88,71,455,625,14,52,45]
#     if len(array) <= 1 :
#         print('Array Empty or contain 1 Value')
        
#     else:
#         Short_Function(array)

#         for i in range(len(array)):
#             print(array[i])

