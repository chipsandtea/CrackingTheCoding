def solution(str1, str2):
    dict1 = dict((char, str1.count(char)) for char in str1)
    dict2 = dict((char, str2.count(char)) for char in str2)

    for char, count in dict1.items():
        try:
            if dict2[char] == count:
                continue
            else:
                return False
        except:
            return False
    return True


print(solution('abcd', 'dcab'))
print(solution('abbcd', 'dadas'))
