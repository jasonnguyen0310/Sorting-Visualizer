# Sorting-Visualizer
A sorting visualizer written in [Python](https://docs.python.org/3/)


# Inspiration
In the summer of 2021, I took a course on **Design and Analysis of Algorithms**. One of the major parts of the course was getting use to implementing and analyzing algorithms. This was difficult for someone who wasn't use to analyzing time and space from a asymptotic perspective. When the course covered sorting algorithm design and analysis, I saw a perfect opportunity to improve my algorithm implementation and analysis skills! I have seen many sorting visualizers written in different programming languages (some more aesthetic than others). I wrote my Sorting Visualizer in Python because it is the language I'm most comfortable with and seeking to master. I found that implementing sorting algorithms aid in understanding three key factors of **Algorithm Analysis**.<br /> 
1. Time Complexity<br />
2. Space Complexity<br />
3. Recursion<br />

Visualizing algorithms were useful in helping me understand how data was arranged and what comparisions were happening during each iteration, which allowed me to grasp a better understanding of algorithm behavior and time complexity. This README will be a documentation of what I learned, used, and benefitted from writing this program!

# Time Complexity
When writing algorithms, counting primitive operations such as: indexing, comparing, and mathematical operations are important in analyzing the time complexity. The more comparisons and array accesses, the longer your algorithm will take. When analyzing algorithms from a big-O perspective, its easier when we are just counting iterations (loops), however when recursion comes into the picture, it makes it a little more difficult to analyze the time complexity of an algorithm (I will touch on this later). I've implemented **6** algorithms in my visualizer each with the Big-O Time Complexities listed below:<br />

**Insertion Sort:** O(n^2))<br /> 
**Selection Sort:** O(n^2)<br /> 
**Quick Sort:** O(n^2)<br /> 
**Bubble Sort:** O(n^2) <br /> 
**Merge Sort:** O(n log(n)) <br /> 
**Heap Sort:** O(n log(n)) <br /> 

# Auxillary Space and Space Complexity
In sorting algorithms, if you are allocating space to new arrays, new partitions, or new variables, this could take up more space. The term Space Complexity is misused for Auxiliary Space at many places. Auxiliary Space is the extra space or temporary space used by an algorithm. Space Complexity of an algorithm is total space taken by the algorithm with respect to the input size. Space complexity includes both Auxiliary space and space used by input. 

For example, if we want to compare standard sorting algorithms on the basis of space, then Auxiliary Space would be a better criteria than Space Complexity. Merge Sort uses O(n) auxiliary space, Insertion sort and Heap Sort use O(1) auxiliary space. Space complexity of all these sorting algorithms is O(n) though. 

# Recursion
Recursive algorithms are quite elegant. However, analyzing the running time of a recursive algorithm takes a bit of additional work. In particular, to analyze such a running time, we use a **recurrence equation**. In mathematics, a recurrence relation is an equation that recursively defines a sequence or multidimensional array of values, once one or more initial terms of the same function are given; each further term of the sequence or array is defined as a function of the preceding terms of the same function. To analyze the time complexity of recursive algorithms such as Quick Sort and Merge Sort we must use their recurrence equation and solve for the running time (when the recursion stack reaches it's last recursive call - (n-1))

# Visualizing with Tkinter
Here is the [Tkinter Documentation](https://docs.python.org/3/library/tk.html) 

Front-end and graphical user interface design aren't my forte, however creating a sorting visualizer with a windowing toolkit such as Tkinter freshened up my memory on skills that are important when designing GUIs. Using a library such as Tkinter is quite simple, just look through the documentation and find what you need from the library and learn how to use that feature! These functions often require input such as the root frame, dimensions, color, etc. The main struggle was brushing up on my geometry skills and understanding dimensions.

# How to Run Locally
**Clone the Repository**<br />
git clone [this repo](https://github.com/jasonnguyen0310/Sorting-Visualizer.git)<br />
........................................................................................................................<br />
**Make sure you have Python with Tkinter installed**<br />
pip install tk<br />
........................................................................................................................<br />
**Run With Python**<br />
python main.py<br />
........................................................................................................................<br />

# Conclusion
I wrote this program during the time of the COVID-19 pandemic. During this time, I was really struggling with motivation for Computer Science and programming. Doing university online and working from home were nice in the beginning, but I realized that my growth began to plataeu because of the inability to work in in-person environments. For any computer scientist, colloborative environments are a way to share ideas and learn. I reached a point where I was fed up with myself and wanted to continue my personal growth. However, I knew that because of the severity of the pandemic, colloboration was going to be difficult, so I took this project upon myself to practice important concepts such as data structures, algorithms, and analysis. While writing this program, I lost track of time and remembered why I chose CS in the first place. I love to solve problems!
