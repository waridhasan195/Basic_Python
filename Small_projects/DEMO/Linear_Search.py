

def Search(list, search_value, list_length):
    for value in range(0, list_length):
        if list[value] == search_value:
            return value
    return -1


if __name__ == "__main__":

    list = [2,55,58,95,4,3,62,100,58,61,12,34,91,7,99]
    search_value = 12
    list_length = len(list)


    result = Search(list, search_value, list_length)
    if(result==-1):
        print('Sorry, Result Not Found.')
    else:
        print('Success, Result Index is ', result)


