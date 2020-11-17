import time


def insertion_sort(data, draw, tick):
    indexing_length = range(1, len(data))
    for i in indexing_length:
        value_to_sort = data[i]

        while data[i - 1] > value_to_sort and i > 0:
            data[i-1], data[i] = data[i], data[i-1]
            i = i-1
            draw(data, ["green" if x == i or x == i +
                        1 else 'red' for x in range(len(data))])
            time.sleep(tick)
    draw(data, ["green" for i in range(len(data))])
