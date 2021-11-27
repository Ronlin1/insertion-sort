def insertion(array):
    for index in range(1, len(array)):
        cv = array[index] # cv-> current value
        cp = index # cp-> current position

        while cp > 0 and array[cp-1] > cv:
            array[cp] = array[cp-1]
            # cv = array[index]
            cp -= 1 # cp = cp - 1
        array[cp] = cv

array = [23,43,42,67,891,22,1,8,17,6,30]
insertion(array)
print(array)
