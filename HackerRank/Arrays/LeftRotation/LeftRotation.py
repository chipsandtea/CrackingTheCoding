def array_left_rotation(data, numOf, rotateBy):
	# Get spots to shift by
    toShift = rotateBy%numOf
    # Convert map (subscriptable) to list
    data = list(data)
    if toShift == 0:
        return data
    # Cut the list accordingly
    front = data[:toShift]
    end = data[toShift:]
    # Construct output
    return(end+front)

n, k = map(int, input().strip().split(' '))
a = map(int, input().strip().split(' '))

answer = array_left_rotation(a, n, k);
print(*answer, sep=' ')