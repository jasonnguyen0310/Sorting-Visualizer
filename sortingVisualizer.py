'''
sortingVisualizer,py
Aythor : Jason Nguyen
module contains sortingVisualizer class
'''


from tkinter import *
from tkinter import ttk
import random
from sorting import insertionSort, selectionSort


class SortingVisualizer:
    def __init__(self):
        # create root for Tkinter GUI
        self.root = Tk()
        # current sorting algorithm
        self.sorter = StringVar()
        # global data array
        self.data = []
        # pre-sorted data array
        self.preSortedData = []
        # num of comparisons
        self.comparisons = IntVar()
        # time
        self.time = DoubleVar()


    def resetData(self):
        # clears global data array
        self.data.clear()
        # clears comparisons
        self.comparisons = IntVar()
        self.comparisons.set(0)
        # clears time
        self.time = DoubleVar()
        self.time.set(0.0)

    
    def increment_comparisons(self, UI_frame, labelComparisons):
        self.comparisons.set(self.comparisons.get() + 1)
        labelComparisons = Label(UI_frame, textvariable=self.comparisons, bg="grey").grid(row=2, column=1, padx=5, pady=5, sticky=W)
        self.root.update()

    def popupmsg(self, msg):
        popup = Tk()

        # Gets the request values of the height and width.
        windowWidth = popup.winfo_reqwidth()
        windowHeight = popup.winfo_reqheight()

        # Gets both half of the screen width/height and window width/height
        positionRight = int(popup.winfo_screenwidth()/2 - windowWidth/2)
        positionDown = int(popup.winfo_screenheight()/2 - windowHeight/2)


        # positions the window in the center of the page
        popup.geometry("+{}+{}".format(positionRight, positionDown))


        popup.wm_title("Error")
        label = ttk.Label(popup, text=msg)
        label.pack(side="top", fill="x", pady=10)
        B1 = ttk.Button(popup, text="Okay", command = popup.destroy)
        popup.grab_set()
        B1.pack()
        popup.mainloop()
        popup.grab_release()


    # Draw Data
    def drawData(self, canvas, data, colorArray):
        canvas.delete("all")
        # Canvas Height
        c_height = 525
        # Canvas Width
        c_width = 1500
        # Width of the bar graphs
        x_width = c_width / (len(data) + 4)
        # offset
        offset = 30
        # spacing
        spacing = 10
        # normalize data
        normalizedData = [ i / max(self.data) for i in data]
        for i, height in enumerate(normalizedData):
            # top left
            x0 = i * x_width + offset + spacing
            y0 = c_height - height * 340
            # bottom right
            x1 = (i + 1) * x_width + offset
            y1 = c_height

            # draw rectangle
            canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
            # display text
            canvas.create_text(x0+2, y0, anchor=SW, text=str(data[i]))

        
        self.root.update()

    # reset the current array
    def resetCurrentArray(self, canvas):
        self.data = self.preSortedData.copy()
        # clears comparisons
        self.comparisons = IntVar()
        self.comparisons.set(0)
        # clears time
        self.time = DoubleVar()
        self.time.set(0.0)
        # draw bar graphs
        self.drawData(canvas, self.data, ['red' for x in range(len(self.data))])


    def startAlgorithm(self, canvas, UI_frame, labelComparisons, labelTime, speedScale, sorter):
        if sorter == "Insertion Sort":
            time = insertionSort(self.data, lambda x, y: self.drawData(canvas, x, y), lambda: self.increment_comparisons(UI_frame, labelComparisons), speedScale.get())
            self.time.set(time)
            labelTime = Label(UI_frame, textvariable=self.time, bg="grey").grid(row=2, column=4, padx=5, pady=5, sticky=W)
            self.root.update()
        elif (sorter == "Selection Sort"):
            time = selectionSort(self.data, lambda x, y: self.drawData(canvas, x, y), lambda: self.increment_comparisons(UI_frame, labelComparisons), speedScale.get())
            self.time.set(time)
            labelTime = Label(UI_frame, textvariable=self.time, bg="grey").grid(row=2, column=4, padx=5, pady=5, sticky=W)
            self.root.update()

    # Generate New Array
    def generateNewArray(self, canvas, UI_frame, labelComparisons, labelTime, sizeEntry, minEntry, maxEntry):
        self.resetData()
        try:
            # size of Array
            size = int(sizeEntry.get())
        except:
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
            self.popupmsg("Must enter input for maxVal")


        if minVal > maxVal:
            self.popupmsg("Minimum Value has to be least than Maximum Value")
            return
    


        # empty dataset
        self.data = []

        # loop through appending random integers to array
        for i in range(size):
            self.data.append(random.randrange(minVal, maxVal+1))

        # backup
        self.preSortedData = self.data.copy()

        # draw bar graphs
        self.drawData(canvas, self.data, ['red' for x in range(len(self.data))])



    # Run Tkinter GUI
    def run(self):
        # set title for Tkinter GUI
        self.root.title('Sorting Algorithm Visualizer')
        # set size for Tkinter GUI
        self.root.maxsize(1920, 1080)
        # set background  color
        self.root.config(bg='black')

        # frame  / base layout
        UI_frame =  Frame(self.root, width=1500, height=510, bg='grey')
        UI_frame.grid(row=0, column=0, padx=5, pady=5, sticky=W)


        canvas = Canvas(self.root, width=1500, height=525, bg='white')
        canvas.grid(row=1, column=0, padx=5, pady=5)

        # User Interface Area
        # Row 2 (Number of Comparisons and Time)

        Label(UI_frame, text="Number of Comparisons: ", bg="grey").grid(row=2, column=0, padx=5, pady=5, sticky=W)
        labelComparisons = Label(UI_frame, textvariable=self.comparisons, bg="grey").grid(row=2, column=1, padx=5, pady=5, sticky=W)

        Label(UI_frame, text="Time including delay (seconds): ", bg="grey").grid(row=2, column=3, padx=5, pady=5, sticky=W)
        labelTime = Label(UI_frame, textvariable=self.time, bg="grey").grid(row=2, column=4, padx=5, pady=5, sticky=W)

        # Row 1 (Algorithm)
        Label(UI_frame, text="Algorithm: ", bg="grey").grid(row=1, column=0, padx=5, pady=5, sticky=W)
        algMenu = ttk.Combobox(UI_frame, textvariable=self.sorter, values=["Insertion Sort", "Selection Sort", "Quicksort", "Bubble Sort", "Merge Sort", "Heap Sort"], state="readonly")
        algMenu.grid(row=1, column=1, padx=5, pady=5)
        # Default sorter is "Insertion Sort"
        algMenu.current(0)
        
        speedScale = Scale(UI_frame, from_=0.1, to=2.0, length=200, digits=2, resolution=0.25, orient=HORIZONTAL, label="Delay [sec]")
        speedScale.grid(row=1, column=2, padx=5, pady=5)
        ttk.Button(UI_frame, text="Sort", command=lambda: self.startAlgorithm(canvas, UI_frame, labelComparisons, labelTime, speedScale, algMenu.get())).grid(row=1, column=3, padx=5, pady=5)

        ttk.Button(UI_frame, text="Reset Current Array", command=lambda: self.resetCurrentArray(canvas)).grid(row=1, column=6, padx=5, pady=5)
        
        # Row 0 (Generating a random array of size n integers)
        Label(UI_frame, text="Size: ", bg="grey").grid(row=0, column=0, padx=5, pady=5, sticky=W)
        sizeEntry= Entry(UI_frame)
        sizeEntry.insert(0, 10)
        sizeEntry.grid(row=0, column=1, padx=5, pady=5, sticky=W)
        

        Label(UI_frame, text="Min. Value in Array: ", bg="grey").grid(row=0, column=2, padx=5, pady=5, sticky=W)
        minEntry= Entry(UI_frame)
        minEntry.insert(0, 0)
        minEntry.grid(row=0, column=3, padx=5, pady=5, sticky=W)
        

        Label(UI_frame, text="Max. Value in Array: ", bg="grey").grid(row=0, column=4, padx=5, pady=5, sticky=W)
        maxEntry= Entry(UI_frame)
        maxEntry.insert(0, 100)
        maxEntry.grid(row=0, column=5, padx=5, pady=5, sticky=W)
        
        ttk.Button(UI_frame, text="Generate New Array", command=lambda: self.generateNewArray(canvas, UI_frame, labelComparisons, labelTime, sizeEntry, minEntry, maxEntry)).grid(row=0, column=6, padx=10, pady=10)



        self.root.mainloop()