import time
# O(Nlog(N)) Time Complexity
# O(N) Space Complexity


def mergeSort(data, draw, timeTick):
    mergeSortAlg(data, 0, len(data)-1, draw, timeTick)


def mergeSortAlg(data, left, right, draw, timeTick):
    if left < right:
        midpoint = (left + right) // 2
        mergeSortAlg(data, left, midpoint, draw, timeTick)
        mergeSortAlg(data, midpoint+1, right, draw, timeTick)
        merge(data, left, midpoint, right, draw, timeTick)


def merge(data, left, midpoint, right, draw, timeTick):
    draw(data, getColourArray(len(data), left, midpoint, right))
    time.sleep(timeTick)

    leftPart = data[left:midpoint+1]
    rightPart = data[midpoint+1:right+1]

    left_pointer = right_pointer = 0

    for i in range(left, right+1):
        if left_pointer < len(leftPart) and right_pointer < len(rightPart):
            if leftPart[left_pointer] < rightPart[right_pointer]:
                data[i] = leftPart[left_pointer]
                left_pointer += 1
            else:
                data[i] = rightPart[right_pointer]
                right_pointer += 1
        elif left_pointer < len(leftPart):
            data[i] = leftPart[left_pointer]
            left_pointer += 1
        else:
            data[i] = rightPart[right_pointer]
            right_pointer += 1
    draw(data, ["green" if x >= left and x <=
                right else "white" for x in range(len(data))])
    time.sleep(timeTick)


def getColourArray(length, left, middle, right):
    colourArray = []
    for i in range(length):
        if i >= left and i <= right:
            if i <= middle:
                colourArray.append("green")  # green
            else:
                colourArray.append("red")  # pink
        else:
            colourArray.append("white")  # blue

    return colourArray
