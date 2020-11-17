import time


def partition(data, head, tail, draw, tick):
    border = head
    pivot = data[tail]

    draw(data, colorarray(len(data), head, tail, border, border))
    time.sleep(tick)

    for j in range(head, tail):
        if data[j] < pivot:
            draw(data, colorarray(len(data), head, tail, border, j, True))
            time.sleep(tick)
            data[border], data[j] = data[j], data[border]
            border += 1

        draw(data, colorarray(len(data), head, tail, border, j))
        time.sleep(tick)

    draw(data, colorarray(len(data), head, tail, border, j, True))
    time.sleep(tick)
    data[border], data[tail] = data[tail], data[border]
    return border


def quick_sort(data, head, tail, draw, tick):

    if head < tail:

        partition_index = partition(data, head, tail, draw, tick)

        quick_sort(data, head, partition_index-1, draw, tick)

        quick_sort(data, partition_index + 1, tail, draw, tick)


def colorarray(datalen, head, tail, border, currentindex, isSwapping=False):
    colorArray = []
    for i in range(datalen):
        if i >= head and i <= tail:
            colorArray.append("gray")
        else:
            colorArray.append("white")

        if i == tail:
            colorArray[i] = "blue"
        elif i == border:
            colorArray[i] = "red"
        elif i == currentindex:
            colorArray[i] = "yellow"

        if isSwapping:
            if i == border or i == currentindex:
                colorArray[i] = "green"

    return colorArray
