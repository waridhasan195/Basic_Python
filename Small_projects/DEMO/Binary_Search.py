
from aa import Short_Function

def Short_Function(array):
    array_length = int(len(array))

    for i in range(array_length):
        for j in range(array_length - i -1):
            if array[j] >= array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return Short_Function()


def Search_Function(Array, Value, length, min_Value):
    if length >= min_Value:
        middle = (length+min_Value) // 2

        if Array[middle] == Value:
            return Value
        
        elif Array[middle] > Value:
             return Search_Function(Array, Value, middle-1, min_Value)
        else:
            return Search_Function(Array, Value, length, middle+1)
    else:
        return -1




if __name__ == '__main__':

    Number = int(input("How many numbers are you input in array ?\n"))
    Array = []
    
    for array_value in range(Number):
        Array.append(int(input("--> ")))

    
    print(Array)
    

    if len(Array) <= 1 :
        print('Array Empty or contain only 1 Value')
    else:
        Value = int(input("what value are you search . . . . "))
        Array_length = len(Array) -1
        Short_Function(Array_length)


        result = Search_Function(Array, Value, Array_length, min_Value=0)
        if result != -1:
            print("Success, Value Found", str(result))
        else:
            print("Failed, Try another way")
    