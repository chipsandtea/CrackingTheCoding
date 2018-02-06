def solution(string):
    charDict = dict((char, string.count(char)) for char in string)
    odd = False
    for char, count in charDict.items():
        if count % 2 != 0:
            if odd:
                return False
            else:
                odd = True
                continue
        else:
            continue
    return True

print(solution(''))
