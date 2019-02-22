# Binary search for list
pos = -1
def search(list, n):
    lower = 0
    upper = len(list) - 1
    while lower <= upper:
        mid = (lower + upper) // 2

        if list[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if list[mid] < n:
                lower = mid + 1
            else:
                upper = mid - 1
    return False
list = [1,45,563,885,888,5645]

n = 888

if search(list, n):
    print('number found at ', pos)
else:
    print('Not Found')

#End