# Sorting-Visualizer
A sorting visualizer written in [Python](https://docs.python.org/3/)


# Inspiration
In the summer of 2021, I was taking a course on **Design and Analysis of Algorithms**. One of the major parts of the course was to get use to implementing and analyzing algorithms on the daily. This was difficult for someone didn't wasn't use to analyzing time and space from a asymptotic perspective. However, we spent two weeks covering sorting, which I saw as the perfect opportunity to improve my algorithm implementation and analysis skills! I have seen many sorting visualizers written in different programming languages (some more aesthetic than others). I wrote my Sorting Visualizer in Python because it is the language I am most comfortable with and seeking to master. I found that implementing sorting algorithms aid in understanding three key factors of **Algorithm Analysis**.<br /> 
1. Time Complexity<br />
2. Space Complexity<br />
3. Recursion<br />

I found that visualizing algorithms were useful in helping me understand how data was manipulated and what comparisions were happening during each iteration, which allowed me to grasp a better understanding of Time Complexity and Space Complexity. This README will be a documentation of what I learned, used, and benefitted from writing this program!

# Time Complexity
When writing algorithms counting primitive operations such as: indexing, comparing, mathematical operations etc are important in analyzing the time complexity. The more comparisons and array accesses, the longer your algorithm will take. When analyzing algorithms from a big O perspective, its easier when we are just counting iterations (loops), however when recursion comes into the picture, it makes it a little more difficult to analyze the time complexity of an algorithm (I will touch on this later). I've implemented **6** algorithms in my visualizer each with the Big-O Time Complexities listed below:<br />

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


# How to Run Locally
**Clone the Repository**<br />
.<br />
git clone [link above]
.<br />
**Make sure you have Python with Tkinter installed**<br />
.<br />
pip install tk<br />
.<br />
python main.py<br />
.<br />
