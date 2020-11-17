import time
# O(Nlog(N)) time complexity


def createHeap(arr, size, i, draw, timeTick):
    largest = i  # Initialize largest as root
    left = 2 * i + 1     # left = 2*i + 1
    right = 2 * i + 2     # right = 2*i + 2
    draw(arr, getColourArray(len(arr), i, left, right))
    time.sleep(timeTick)
    # See if left child of root exists and is
    # greater than root
    if left < size and arr[i] < arr[left]:
        largest = left

    # See if right child of root exists and is
    # greater than root
    if right < size and arr[largest] < arr[right]:
        largest = right

    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
        draw(arr, getColourArray(len(arr), i, left, right))
        time.sleep(timeTick)
        # createHeap the root.
        createHeap(arr, size, largest, draw, timeTick)

# The main function to sort an array of given size


def heap_sort(arr, draw, timeTick):
    size = len(arr)

    # Build a maxheap.
    for i in range(size//2 - 1, -1, -1):
        createHeap(arr, size, i, draw, timeTick)

    # One by one extract elements
    for i in range(size-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        createHeap(arr, i, 0, draw, timeTick)


def getColourArray(size, i, left, right):
    colourArray = []

    for j in range(size):
        if j == i:
            colourArray.append("yellow")  # green elements are selected
        else:
            colourArray.append("red")  # blue
    return colourArray
