
#Sort

def sortFunction(array):
    array_length = int(len(array))
    
    for i in range(array_length):
        for j in range(array_length - i - 1):
            if array[j] > array[j+1]:
                array[j + 1], array[j] = array[j], array[j+1]
        
    return array




if __name__ == '__main__':
    array = [3,4,6,2,43,4,2,4,6,2,98,65,-2,4,0,32]
    print("Main Array: ", array)

    print(sortFunction(array))

