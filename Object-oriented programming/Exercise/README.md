# Exercise Car class

## Problem statement
For this exercise you will develop a Python module containing a Car class. Instances of the class will be able to turn and drive forward. They will have three attributes: x (an x coordinate), y (a y coordinate) and heading (a direction the car will drive, in degrees; for this assignment, a heading of 0 indicates due north, a heading of 90 is due east, etc.). They will have three methods: __init__(), turn(), and drive().

You will also write a sanity_check() function outside of the class that instantiates the class, invokes the methods, and prints the attributes.

## Background: some trigonometry and geometry
For this exercise, you will need to use three trigonometry-related functions from the math module. sin() and cos() compute the sine and cosine, respectively, of a specified angle in radians. radians() converts a measurement in degrees to radians. So, for example, if you wanted to find the cosine of 30 degrees, here’s how you could calculate it with these functions:

*cos(radians(30))*

We will use these functions to convert movement along some heading to x and y coordinates. If you think of the heading as an angle and the distance traveled as the hypoteneuse of a triangle whose other two sides are parallel to the x and y axes of a coordinate system, then the lengths of those other two sides tell us how far the car has traveled in terms of x, y coordinates. By adding those distances to the car’s starting coordinate, we can determine the car’s ending coordinate.

[Click here for more information.](Image.png)

## Instructions
Create a Python script from scratch (there is no template). Save the script as car.py. Follow the instructions below to populate this script.

**import statement**<br/>
Either import the entire math module, or just the following functions from that module: cos, radians, sin.

**Car class**<br/>
Create a class called Car. Define the following methods:

**__init__() method**<br/>
Define a method called __init__() (note the double underscores). Your method should have one required parameter (self) and three optional parameters as follows (please use these exact names):

- x: the starting x coordinate of the car, as a float.[1] Default: 0.

- y: the starting y coordinate of the car, as a float. Default: 0.

- heading: the starting heading, as a float. Default: 0.

Your __init__() method should set three attributes (x, y, and heading) to the values of their corresponding parameters.

**turn() method**<br/>
Define a method called turn() that has two required parameters, self and a number of degrees expressed as a float.[2] A positive number of degrees indicates a clockwise turn; a negative number of degrees indicates a counterclockwise turn. Use the following steps to assign a new value to the heading attribute (these can be combined into a single expression):

1. Add the specified number of degrees to the previous value of 
   heading.

2. Reduce the result of step 1 modulo 360 (this ensures that 
   heading is between 0 and 360).

For example, if heading is 270 and the number of degrees is 100, the turn() method should set heading to (270 + 100) mod 360, which is 10.

**drive() method**<br/>
Define a method called drive() that has two required parameters, self and a distance expressed as a float.

In the formulas below, d is the distance; h is the heading in radians (you will need to convert the heading from degrees to radians).

Update the x attribute by adding dsin(h) to the attribute’s current value. (Hint: the += operator is your friend).

Update the y attribute by subtracting dcos(h) from the attribute’s current value. (Hint: the -= operator is your friend).

**sanity_check() function**<br/>
Define a sanity_check() function that takes no arguments. This function should not be part of the Car class—​please de-indent the function header so it is aligned with the header of the Car class.

In this function, create an instance of the Car class. Have your instance follow these steps:

- Turn 90 degrees.

- Drive 10 units.

- Turn 30 degrees.

- Drive 20 units.

Print the location of your instance on one line and the heading on the next line, in the following format:
*Location: 41.34235262, 17.999999999*
*Heading: 75*
At the end of your function, return the instance you created.

**if __name__ == "__main__": statement**
At the end of your code, write an if __name__ == "__main__": statement that invokes your sanity_check() function.

## Other instructions
- Please write docstrings for your class, each of your methods, and your function.

    * Your class docstring should start with a brief statement of the purpose of the class. It should then document the attributes of the class in an Attributes: section.

    * Your method/function docstrings should start with a brief statement of the function’s purpose.

    * If your method or function takes arguments, provide an Args: section to document them, including their names, data types, and a brief description of the purpose of each. You do not need to document self in the Args: section.

    * If your method or function returns a value, write a Returns: section to describe the return value, including its data type and a brief description of its purpose.

    * If your method causes side effects, include a Side effects: section to describe the side effects. Examples of side effects include setting or changing an attribute’s value and printing information to the console.

Docstrings were covered in the lectures here: https://youtu.be/jHTv83PlQYw?t=1415. There’s an ELMS page about them here: https://umd.instructure.com/courses/1312228/pages/docstrings.

- Please keep your lines of code to 80 characters or less. If you need help breaking up long lines of code, please see https://umd.instructure.com/courses/1312228/pages/how-to-break-up-long-lines-of-code.

## Submitting your code

Upload your car.py class to Gradescope. An autograder script will give you (near-)instant feedback. If you did not pass all the test cases, you can revise your code and resubmit as many times as you want until the deadline.

If you and your partner(s) finish in class, please make a single submission; the submitter should add their partner(s) as group members. If you do not finish in class, the driver should send a copy of the unfinished program to the navigator(s) and each person should finish and submit the assignment on their own.

## Testing your code
To run your program within the VS Code built-in terminal, first make sure you have opened (in VS Code) the directory where your program is saved. If necessary, you can go to the VS Code File menu and select "Open…​​" on macOS or "Open Folder…​" on Windows, and navigate to the directory where your program is.

Then, open the VS Code built-in terminal. Type python3 (on macOS) or python (on Windows) followed by a space and the name of your program. Below is an example:
*python3 car.py*

### driving_range.py
The program driving_range.py is designed to import your class and create a graphical representation of two instances of your Car class. Your class serves as the back end for this program. The program depends upon your code following the naming conventions specified in these instructions.

driving_range.py requires the Tkinter module. If you installed Python 3.9 from Python.org, Tkinter should normally have been included. If you run into issues related to Tkinter, please contact the instructor.

To use driving_range.py, ensure that it is in the same directory as car.py. Then, open the VS Code built-in terminal and type python3 (on macOS) or python (on Windows) followed by a space and the name of the program. Below is an example:

*python3 driving_range.py*

Two car objects appear as circles with arrows in the middle. By default, the cars are "self-driving". You can control them in both self-driving mode and regular mode. Here are the keys you can use to control the cars:

[Image](Chart.png)