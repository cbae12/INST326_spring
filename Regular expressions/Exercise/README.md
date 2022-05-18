# Exercise: Parsing addresses
<hr/>

## Table of Contents
[Problem statement](#problem-statement)<br/>
[Background](#background)<br/>
[Instructions](#instructions)<br/>
&emsp;[Address class](#address-class)<br/>
&emsp;[__init__() method](#init-method)<br/>
&emsp;[read_addresses() function](#readaddresses-function)<br/>
&emsp;[Docstrings](#docstrings)<br/>
[Using your script](#using-your-script)<br/>
<hr/>

## Problem statement
Following the instructions below, write an *Address* class that represents an address. The class’s *__init__()* method should take a string consisting of a US street address. It should use regular expressions to parse the address and populate attributes for the house number, street, city, state, zip, and the address as a whole.

Outside of the class, write a *read_addresses()* function that reads addresses from a file and builds a list of Address objects.
<hr/>

## Background
In this exercise you use will use regular expressions to parse American street addresses from a text file. Each address will consist of a house number, a street name, a city, a state, and a zip code. Here’s an example of an address:

5173B 63rd Ave NE, Lake Forest Park WA 98155

You can make the following assumptions:

- The parts of the address (house number, street name, etc.) always occur in the same order

- The house number will never contain a space, but it could contain other characters besides numbers

- There is always a comma after the street name; the only other punctuation in an address is spaces in between words

- The state always consists of two capital letters

- The zip code always consists of five digits

A sample file, *addresses.txt*, is provided for testing purposes. This file is slightly modified from this file: https://gist.github.com/HeroicEric/1102788#file-gistfile1-txt.

The main goal of today’s exercise is to practice writing regular expressions.
<hr/>

## Instructions
Modify the provided template script to include an *Address* class and a *read_addresses()* function, as described below.

### Address class
Instances of the *Address* class will have the following attributes:

- *address* (str): the entire address as a string (should not contain leading or trailing spaces)

- *house_number* (str): the house number of the address (e.g., 5173B)

- *street* (str): the street name (e.g., 63rd Ave NE)

- *city* (str): the city (e.g., Lake Forest Park)

- *state* (str): the state (e.g., WA)

- *zip* (str): the zip code (e.g., 98155)

They will also have two methods, *__init__()* and *__repr__()*. *__repr__()* has been provided for you in the template; you will need to uncomment it and include it in your class.

### __init__() method
*__init__()* will take a single line of text as an argument and set the attributes described above.

Use a regular expression to match the address, with separate capturing groups for the house number, the street name, the city, the state, and the zip code. If your regular expression fails (in other words, if *re.search()* returns *None*), raise a ValueError indicating that the address string could not be parsed. If your regular expression succeeds, use the strings from your capturing groups to populate the attributes of the instance.

You may find it useful to develop your regular expression using [regex101.com](regex101.com). Once you have an expression that parses all the addresses in *addresses.txt*, you can paste the expression into your code as a raw string (a string with an r immediately before the opening quotation mark).

### read_addresses() function
*read_addresses()* will take one argument, a path to a file containing one address per line. It will open the file, convert each line to an Address object, and return a list with one instance of Address per line in the file.

Use a *with* statement to open the file for reading (make sure you use the parameter to the function instead of a hard-coded path). Use a list comprehension to build the list of Address objects.

### Docstrings
Write docstrings for your class, your *__init__()* method, and your *read_addresses()* function.
<hr/>

## Using your script
The template script is meant to take one command-line argument, the path to a file of addresses. Assuming your script is called parse_addresses.py and that addresses.txt is in the same directory, here is how you could run the script (Windows users, replace python3 with python):

&emsp;*python3 parse_addresses.py addresses.txt*<br/>

The script should print information about each address in the file.
<hr/>