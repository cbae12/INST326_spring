# Homework: Phone number class
<hr/>

## Table of Contents
[Problem statement](#problem-statement)<br/>
[Background](#background)<br/>
&emsp;[Letters in phone numbers](#letters-in-phone-numbers)<br/>
&emsp;[Provided files](#provided-files)<br/>
&emsp;&emsp;[Sample data (sample_phone_numbers.txt)](#sample-data-samplephonenumberstxt)<br/>
&emsp;&emsp;[Template (phone_numbers.py)](#template-phonenumberspy)<br/>
[Instructions](#instructions)<br/>
&emsp;[PhoneNumber class](#phonenumber-class)<br/>
&emsp;&emsp;[Instantiation](#instantiation)<br/>
&emsp;&emsp;[Attributes](#attributes)<br/>
&emsp;&emsp;[Other functionality](#other-functionality)<br/>
&emsp;[read_numbers() function](#readnumbers-function)<br/>
&emsp;[Docstrings](#docstrings)<br/>
[Running your program](#running-your-program)<br/>
[Subitting your code](#subitting-your-code)<br/>
<hr/>

## Problem statement
Using the provided template, create a program called *phone_numbers.py* that can read phone numbers from the North American numbering plan in a variety of formats, standardize them, and sort them. At the heart of this program will be a *PhoneNumber* class that implements a number of magic methods. You will also write a function called *read_numbers()* that reads names and phone numbers from a file, puts them in a list, and sorts and returns the list.
<hr/>

## Background
Phone numbers in the United States, Canada, and many jurisdictions in the Carribean are based on a system called the [North American numbering plan](https://en.wikipedia.org/wiki/North_American_Numbering_Plan)(NANP). Phone numbers in this system begin with a country code of 1 (often written "+1"), which is usually not needed if you are calling within a NANP country. This is followed by a three-digit *area code*, a three-digit *exchange code* (also called a *central office code*), and a four-digit *line number* (also called a *station code*). In the number 1-301-555-0142, 302 is the area code, 555 is the exchange code, and 0142 is the line number.

There are many ways to write a NANP phone number. Some common formats include:

- (301) 555-0142

- 1-301-555-0142

- +13015550142

Less-common formats use other delimiters between the parts of the phone number, with or without the country code (which may be written with or without a preceding "+").

### Letters in phone numbers
Some letters on a phone keypad are mapped to a set of letters. This makes it possible to devise mnemonics for phone numbers that include words, such as UMD’s COVID hotline, 1-405-HEAL (4325). The table below gives the mapping between digits and letters.
[Conversion](Letters_to_Numbers.png)

### Provided files
#### Sample data (sample_phone_numbers.txt)
This file contains fictional names of people and businesses and their fictional phone numbers. The file is encoded using UTF-8. Each line in the file consists of a name, a tab character ("\t"), and a phone number. Most of the phone numbers are valid numbers according to the North American Numbering Plan, but a handful are invalid. See the description of the [*read_numbers()* function](#readnumbers-function) below for more information on the contents of this file and what your program should do with it.

#### Template (phone_numbers.py)
The provided template imports the *argparse*, *re*, and *sys* modules. *argparse* and *sys* are used to parse command-line arguments; *re* is provided for your convenience should you choose to use it in your implementation of the *PhoneNumber* class and/or the *read_numbers()* function. You should not import any other modules.

A global variable, *LETTER_TO_NUMBER*, is defined to assist you in converting letters in phone numbers to their appropriate digits. *LETTER_TO_NUMBER* is a dictionary where the keys are capital letters and the corresponding values are single-digit integers between 2 and 9, inclusive.

A *main()* function is provided. It calls your *read_numbers()* function and prints the results one line at a time.

A *parse_args()* function is included. It processes command-line arguments and, assuming it received the arguments it expected, returns a namespace object with an attribute called file whose value is a string.

The template ends with an if __name__ == "__main__": statement which runs the program (by calling the *parse_args()* and *main()* functions). As a reminder, this statement allows your program to be used as both a main program and a module (e.g., for testing by the autograder).
<hr/>

## Instructions
Write a Python program from scratch called *phone_numbers.py* that meets the following specifications:

### PhoneNumber class
Write a class called *PhoneNumber* that meets the specifications below.

#### Instantiation
When creating an instance of this class, a user should be able to pass in a string or an integer. As long as that string or integer contains exactly ten letters or digits (plus an optional 1 at the beginning for the country code) and follows the rules below, your class should recognize it as a valid phone number (even if it contains other characters besides letters and numbers). If the argument is not a string or an integer, your class should raise a *TypeError*; if the number is not valid, it should raise a *ValueError*.

**Rules**: your program should raise a *ValueError* if either the area code or the exchange code begins with 0 or 1 or ends with 11.

#### Attributes
Instances of your class should have attributes *area_code*, *exchange_code*, and *line_number*. Each of these should have a string of digits as its value.

#### Other functionality
Your class should implement the behavior shown in the examples below.
[Other_Func](Other_functionality.png)

*Hint: There are a couple of ways that you can use regular expressions in this class if you so choose. You can use them to help you validate phone numbers (using [re.search()](https://docs.python.org/3/library/re.html#re.search)). You can also use them to help you remove extraneous characters and to replace letters with their corresponding digits (using [re.sub()](https://docs.python.org/3/library/re.html#re.sub)). As a reminder, re.sub() can take a callable (such as a function or anonymous function) as its second argument. The callable should have one parameter; its value will be a [regular expression match object](https://docs.python.org/3/library/re.html#match-objects). The callable can use the group() method or the [] operator of the match object to get matches to capturing groups. It should return a string consisting of the replacement for the substring matched by the entire match object (i.e., group(0)).*

### read_numbers() function
Define a function called read_numbers() outside of your class.

This function should take one argument: a string consisting of a path to a UTF-8-encoded text file. Each line in the text file should have the name of a person or business, a tab character ("\t"), and a phone number. The provided file sample_phone_numbers.txt is an example of a file this function should be able to read. A few lines of the file are shown below:

&emsp;*Benjamin Sosa	1 (825) 828-0003*<br/>
&emsp;*Wanda's Vocal Coaching	207-LARYNX-1*<br/>
&emsp;*Taste of Mexico Restaurant	418TAMALE9*<br/>
&emsp;*Hope Tyler	515.720.3628*<br/>
&emsp;*Bernadette Stanley	226-850-6891*<br/>
&emsp;*Subtraction Consulting, Ltd	544-REMOVE-19*<br/>

The function should read each line from the file and extract the name and the phone number. If the phone number is a valid [NANP phone number](#background), it should construct a tuple consisting of the name (as a string) and the phone number (as an instance of *PhoneNumber*), in that order. The function should return a list of these tuples, sorted in ascending order by phone number (note: sorting in Python is based on the *<* operator, and the *PhoneNumber* class should have defined a behavior for the *<* operator, so you should be able to sort *PhoneNumber* objects). For the example lines above, the result would be

*[*
&emsp;&emsp;*("Wanda's Vocal Coaching", PhoneNumber('2075279691')),*
&emsp;&emsp;*('Bernadette Stanley', PhoneNumber('2268506891')),*
&emsp;&emsp;*('Taste of Mexico Restaurant', PhoneNumber('4189262539')),*
&emsp;&emsp;*('Hope Tyler', PhoneNumber('5157203628')),*
&emsp;&emsp;*('Benjamin Sosa', PhoneNumber('8258280003'))*
*]*

Note that Subtraction Consulting is not included in the list because the corresponding phone number is not valid (it contains eleven digits).

### Docstrings
Please write clear, specific docstrings for your class, your *read_numbers()* function, and the methods of your class. Methods that are easy to read and contain fewer than five statements in the method body can be documented with one-line docstrings. For other methods, please write a standard docstring with all applicable sections.
<hr/>

## Running your program
Your program is designed to run from the terminal. To run it, open a terminal and ensure you are in the directory where your script and sample file are saved.

The program takes one required command-line argument (the path to a file of names and phone numbers, such as *sample_phone_numbers*.txt). Below is an example of how to run the program. Windows users, type python instead of *python3* when you run your program.

&emsp;*python3 phone_numbers.py sample_phone_numbers.txt*<br/>
<hr/>

## Subitting your code
Upload your *phone_numbers.py* script to Gradescope. An autograder script will give you near-instant feedback. If you did not pass all the test cases, you can revise your code and resubmit as many times as you want until the deadline.
<hr/>