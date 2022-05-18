# Exercise: Reverse Polish notation
<hr/>

## Table of Contents
[Problem statement](#problem-statement)<br/>
[Background](#background)<br/>
[Instructions](#instructions)<br/>
&emsp;[evaluate() function](#evaluate-function)<br/>
&emsp;[main() function](#main-function)<br/>
&emsp;[Other instructions](#other-instructions)<br/>
[Testing your code](#testing-your-code)<br/>
<hr/>

## Problem Statement
Using the provided template (rpn.py), write a program that reads postfix notation expressions from a file (one expression per line), parses and evaluates each line, and prints the results. You will write at least two functions: evaluate() and main(), as described below.
<hr/>

## Background
We are used to writing mathematical expressions with operators in between their operands (for example, 5 + 2 or 7 × 4). This is called infix notation. Sometimes infix notation requires parentheses to clarify the order of operations; for example, (6 + 5) × 7.

An alternative way to write math expressions is to place the operators before their operands; for example, + 5 2 or × 7 4. This is called prefix notation or Polish notation (after the nationality of Jan Łukasiewicz, who invented it).[^1] If we assume that all operations take a fixed, predetermined number of operands, then we can do away with parentheses. The infix expression (6 + 5) × 7 can be rewritten in prefix notation as × + 6 5 7. The multiplication has to wait until there are two operands available. The addition happens as soon as there are two numbers available to add (6 and 5); then the sum of these two numbers (11) is treated as the first operand of the multiplication operator, and the final number (7) is the second operand.

A third way to write math expressions is to place the operators after their operands; for example, 5 2 + or 7 4 ×. This is called postfix notation or reverse Polish notation. Like prefix notation, in postfix notation parentheses are not necessary if all operands take a fixed number of operands. The expression (6 + 5) × 7 can be rewritten in postfix notation as 7 6 5 + ×.

Postfix notation is convenient for computing purposes because numbers can be added to a list as they are encountered, and when an operator is encountered, numbers can immediately be removed from the list and evaluated as operands of the operator. A list in which values are removed in the opposite order from the order in which they were added is called a stack. Python lists are easy to use as stacks thanks to their append() and pop() methods.
<hr/>

## Instructions
Implement the following functions in the provided template, rpn.py. The functions should go after the import statements and before the parse_args() function.

### evaluate() function
Write a function named evaluate() that takes one argument, a string containing a postfix expression. All elements of the expression will be separated by spaces. The expression may end in a newline character, which you should remove.

The following operators are permitted in expressions: +, -, *, /. Assume that each of these operators takes two operands. The first operand is always the value that comes earliest, so the result of the expression 5 3 - would be 2, not -2. Treat all numbers as floats.

*Hint: make a list that will contain numbers that haven’t been used as operands yet. Every time you encounter an operator, pop two operands off the end of your list (the number you pop second will be the first operand). Then append the result to the list.*

*For example, if you are reading in the expression 6 2 /, you would first split the expression into tokens. Then you would go through the tokens one at a time. The first token is 6, so you would append 6 to your list. The second token is 2; append 2 to the list. The next token is /; pop 2 off the list to be the second operand, then pop 6 off the list to be the first operand. The result is 3; append 3 to the list. When you are done with the expression, there should be exactly one value left in the list (in this example, 3). That value is your result; remove it from the list and return it.*

### main() function
Write a function named main() that takes one argument, a string containing a path to a file of postfix expressions. This function should open the file for reading, iterate over each line in the file, call the evaluate() function to evaluate each expression, and print the result of each expression in the following format:
*5 4 + = 9.0*<br/>
*9 2 3 - * = -9.0*<br/>
*9 2 3 * - = 3.0*
<hr/>

## Other instructions
Please write docstrings for each of your functions. Your docstrings should start with a brief statement of the function’s purpose. Include an "Args" section to document any arguments, and a "Returns" section to describe the return value (if any). Your main() function will not need a "Returns" section, but it should include a "Side effects" section (because printing is a side effect). Docstrings were covered in the lectures here: https://youtu.be/jHTv83PlQYw?t=1415. There’s an ELMS page about them here: https://umd.instructure.com/courses/1299872/pages/docstrings.

Please keep your lines of code to 80 characters or less. If you need help breaking up long lines of code, please see https://umd.instructure.com/courses/1299872/pages/how-to-break-up-long-lines-of-code.
<hr/>

## Testing your code
The template is designed to use command-line arguments. To run your program within the VS Code built-in terminal, first make sure you have opened (in VS Code) the directory where your program is saved. If necessary, you can go to the VS Code File menu and select "Open…​" on macOS or "Open Folder…​" on Windows, and navigate to the directory where your program is.

Then, open the VS Code built-in terminal. Type python3 (on macOS) or python (on Windows) followed by a space, the name of your program, another space, and the name of a file containing postfix expressions. Below is an example:

*python3 rpn.py postfix_expressions.txt*

[^1]: <link href=https://en.wikipedia.org/wiki/Polish_notation>https://en.wikipedia.org/wiki/Polish_notation<link/>
<hr/>