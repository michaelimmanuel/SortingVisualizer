import time


def selection_sort(data, draw, tick):

    indexing_length = range(0, len(data)-1)

    for i in indexing_length:
        min_value = i

        for j in range(i + 1, len(data)):
            if data[j] < data[min_value]:
                min_value = j

        draw(data, ["green" if x == i or x == i +
                    1 else 'red' for x in range(len(data))])
        time.sleep(tick)

        if min_value != i:
            data[min_value], data[i] = data[i], data[min_value]

    draw(data, ["green" for i in range(len(data))])
