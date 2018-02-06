def binSearch(string, char, left, right):
    if right >= 1:
        mid = (right-1//2)
        if string[mid] == char:
            return mid
        elif string[mid] > char:
            return binSearch(string, char, left, mid-1)
        else:
            return binSearch(string, char, mid+1, right)
    else:
        return -1


def isUnique(string):
    print('String: ' + string)
    string = ''.join(sorted(string))
    for idx in range(len(string)):
        res = binSearch(string, string[idx], 0, len(string) - 1)
        if res == -1:
            continue
        elif res == idx:
            continue
        else:
            return False
    return True


print(isUnique('abcd'))
print(isUnique('aabcd'))
print(isUnique(''))
