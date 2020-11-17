from tkinter import *
from tkinter import ttk
import random
from bubblesort import bubble_sort
from quicksort import quick_sort
from mergesort import mergeSort
from insertionsort import insertion_sort
from selectionsort import selection_sort
from heapsort import heap_sort

# setup
root = Tk()

root.title("SORTING VISUALIZER")
root.maxsize(900, 800)
root.config(bg="black")

# var
alg = StringVar()
data = []


def draw(data, color):
    canvas.delete("all")
    c_height = 380
    c_width = 500
    x_width = c_width / (len(data) + 1)
    offset = 30
    spacing = 10

    normalize = [i / max(data) for i in data]

    for i, height in enumerate(normalize):
        x1 = i * x_width + offset + spacing
        y1 = c_height - height * 340

        x2 = (i+1) * x_width + offset
        y2 = c_height

        canvas.create_rectangle(x1, y1, x2, y2, fill=color[i])
       # canvas.create_text(x1+2, y1, anchor=SW, text=str(data[i]))
    root.update_idletasks()


def Generate():

    global data
    """
    minVal = int(minEntry.get())

    maxVal = int(maxEntry.get())
    """

    rangeVal = int(rangeEntry.get())
    size = int(sizeEntry.get())

    data = [i for i in range(1, rangeVal)]
    random.shuffle(data)

    """
    for _ in range(size):
        data.append(random.randrange(minVal, maxVal+1))
    """
    draw(data, ["red" for x in range(len(data))])


def StartAlgorithm():
    global data

    if not data:
        return

    if (algmenu.get() == "Quick Sort"):
        quick_sort(data, 0, len(data) - 1, draw, speedScale.get())

    elif (algmenu.get() == "Bubble Sort"):
        bubble_sort(data, draw, speedScale.get())

    elif (algmenu.get() == "Merge Sort"):
        mergeSort(data, draw, speedScale.get())

    elif (algmenu.get() == "Insertion Sort"):
        insertion_sort(data, draw, speedScale.get())

    elif (algmenu.get() == "Selection Sort"):
        selection_sort(data, draw, speedScale.get())

    elif (algmenu.get() == "Heap Sort"):
        heap_sort(data, draw, speedScale.get())

    draw(data, ["green" for x in range(len(data))])


frame = Frame(root, width=600, height=200, bg="grey")
frame.grid(row=0, column=0, padx=10, pady=5)

canvas = Canvas(root, width=600, height=380, bg="white")
canvas.grid(row=1, column=0, padx=5, pady=10)


# [0]

Label(frame, text="algorithm", bg="grey").grid(
    row=0, column=0, padx=5, pady=5, sticky=W)
algmenu = ttk.Combobox(frame, textvariable=alg, values=[
    "Bubble Sort", "Quick Sort", "Merge Sort", "Insertion Sort", "Selection Sort", "Heap Sort"])
algmenu.grid(row=0, column=1, padx=5, pady=10)
algmenu.current(0)

speedScale = Scale(frame, from_=0.001, to=2.0, length=200,
                   digits=4, resolution=0.001, orient=HORIZONTAL, label="Speed [s]")
speedScale.grid(row=0, column=2, padx=5, pady=5)

Button(frame, text="start", command=StartAlgorithm,
       bg="red").grid(row=0, column=3, padx=5, pady=5)


# [1]


sizeEntry = Scale(frame, from_=3, to=100, length=200,
                  digits=2, resolution=0.2, orient=HORIZONTAL, label="size")
sizeEntry.grid(row=1, column=0, padx=5, pady=5)

rangeEntry = Scale(frame, from_=1, to=100, length=200,
                   digits=2, resolution=0.1, orient=HORIZONTAL, label="Range")
rangeEntry.grid(row=1, column=1, padx=5, pady=5)

"""
minEntry = Scale(frame, from_=1, to=10, length=200,
                 digits=2, resolution=0.2, orient=HORIZONTAL, label="Min Value")
minEntry.grid(row=1, column=1, padx=5, pady=5)


maxEntry = Scale(frame, from_=10, to=100, length=200,
                 digits=2, resolution=0.2, orient=HORIZONTAL, label="size")
maxEntry.grid(row=1, column=2, padx=5, pady=5)
"""

Button(frame, text="Generate", command=Generate,
       bg="red").grid(row=1, column=3, padx=5, pady=5)

root.mainloop()
