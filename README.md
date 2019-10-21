# Quadratic-Formulas
I was excited to learn to code, so I created a program to help me solve my math homework.
This project was first created early in my semester of learning python, and I set out on my own to test my ability in problem solving.

## Getting Started
The program was created on and runs with the Python IDLE IDE.

## Explaining the Program

### Initialization
The first five lines of the program initialize the variables a, b, c, xVertex, and Vertex.

The initilization of the variables is followed by an output to the user explaining that we are trying to find the vertex and min/max of a parabola.

### Input for the variables
The program then requests the user to input three floating point numbers for the variables a, b, and c.

### Doing the math
The next two lines are the formulas utilized to find the vertex:

xVertex takes the negative form of the input for b and divides that by two multiplied by the input for a.

vertex takes the input for a and multiples it with the results of xVertex, and raises the results of that by two. Which is then added to the input for b multiplies by the results of xVertex, and then that is finally added to the input for c.

### Printing the results for easy access
The following line prints out the vertex.

The last four lines is an if statement where:

If the input for a is greater than zero, it is true and prints the minimum.

If the input for a is less than zero, it is false and prints the maximum.

