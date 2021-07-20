from tkinter import *
from tkinter import ttk
import random


class SortingVisualizer:
    def __init__(self):
        # create root for Tkinter GUI
        self.root = Tk()
        # current sorting algorithm
        self.sorter = StringVar()

    def popupmsg(self, msg):
        popup = Tk()
        popup.wm_title("Error")
        label = ttk.Label(popup, text=msg)
        label.pack(side="top", fill="x", pady=10)
        B1 = ttk.Button(popup, text="Okay", command = popup.destroy)
        B1.pack()
        popup.mainloop()


    # Draw Data
    def drawData(self, canvas, arr):
        canvas.delete("all")
        # Canvas Height
        c_height = 380
        # Canvas Width
        c_width = 600
        # Width of the bar graphs
        x_width = c_width / (len(arr) + 1)
        # offset
        offset = 30
        # spacing
        spacing = 10
        # normalize data
        normalizedData = [ i / max(arr) for i in arr]
        for i, height in enumerate(normalizedData):
            # top left
            x0 = i * x_width + offset + spacing
            y0 = c_height - height * 340
            # bottom right
            x1 = (i + 1) * x_width + offset
            y1 = c_height

            # draw rectangle
            canvas.create_rectangle(x0, y0, x1, y1, fill="red")
            # display text
            canvas.create_text(x0+2, y0, anchor=SW, text=str(arr[i]))


    # Generate New Array
    def generateNewArray(self, canvas, sizeEntry, minEntry, maxEntry):

        try:
            # size of Array
            size = int(sizeEntry.get())
        except:
            size = 10
            self.popupmsg("Must enter input for Size")
            
        try:
            # minVal of Array
            minVal = int(minEntry.get())
        except:
            self.popupmsg("Must enter input for minVal")

        try:
            # maxVal of Array
            maxVal = int(maxEntry.get())
        except:
            maxVal = 10
            self.popupmsg("Must enter input for maxVal")


        if minVal > maxVal:
            self.popupmsg("Minimum Value has to be least than Maximum Value")
            return

        if size > 30:
            self.popupmsg("Size cannot be greater than 30 given default dimensions")
            return

        # empty dataset
        data = []

        # loop through appending random integers to array
        for i in range(size):
            data.append(random.randrange(minVal, maxVal+1))


        # draw bar graphs
        self.drawData(canvas,data)


    # Run Tkinter GUI
    def run(self):
        # set title for Tkinter GUI
        self.root.title('Sorting Algorithm Visualizer')
        # set size for Tkinter GUI
        self.root.maxsize(900, 600)
        # set background  color
        self.root.config(bg='black')

        # frame  / base layout
        UI_frame =  Frame(self.root, width=600, height=200, bg='grey')
        UI_frame.grid(row=0, column=0, padx=10, pady=5)

        canvas = Canvas(self.root, width=600, height=380, bg='white')
        canvas.grid(row=1, column=0, padx=10, pady=5)

        # User Interface Area
        # Row[0]
        Label(UI_frame, text="Algorithm: ", bg="grey").grid(row=0, column=0, padx=5, pady=5, sticky=W)
        algMenu = ttk.Combobox(UI_frame, textvariable=self.sorter, values=["Insertion Sort", "Selection Sort", "Quicksort", "Merge Sort"], state="readonly")
        algMenu.grid(row=0, column=1, padx=5, pady=5)
        # Default sorter is "Insertion Sort"
        algMenu.current(0)
        
        # Row[1]
        Label(UI_frame, text="Size: ", bg="grey").grid(row=1, column=0, padx=5, pady=5, sticky=W)
        sizeEntry= Entry(UI_frame)
        sizeEntry.grid(row=1, column=1, padx=5, pady=5, sticky=W)
        

        Label(UI_frame, text="Min Value: ", bg="grey").grid(row=1, column=2, padx=5, pady=5, sticky=W)
        minEntry= Entry(UI_frame)
        minEntry.grid(row=1, column=3, padx=5, pady=5, sticky=W)
        

        Label(UI_frame, text="Max Value: ", bg="grey").grid(row=1, column=4, padx=5, pady=5, sticky=W)
        maxEntry= Entry(UI_frame)
        maxEntry.grid(row=1, column=5, padx=5, pady=5, sticky=W)
        
        ttk.Button(UI_frame, text="Generate New Array", command=lambda: self.generateNewArray(canvas, sizeEntry, minEntry, maxEntry)).grid(row=0, column=2, padx=5, pady=5)

        self.root.mainloop()