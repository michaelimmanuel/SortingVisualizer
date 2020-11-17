import time


def bubble_sort(data, draw, tick):
    for _ in range(len(data)-1):
        for j in range(len(data)-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                draw(data, ["green" if x == j or x == j +
                            1 else 'red' for x in range(len(data))])
                time.sleep(tick)
    draw(data, ["green" for i in range(len(data))])
