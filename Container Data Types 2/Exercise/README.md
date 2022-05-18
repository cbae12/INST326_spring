# Exercise: Nearby cities
## Table of Contents
[Problem statement](#problem-statement)<br/>
&emsp;[Latitude and longitude](#latitude-and-longitude)<br/>
&emsp;[Data file](#data-file)<br/>
&emsp;[Template](#template)<br/>
&emsp;&emsp;[Dependencies](#dependencies)<br/>
[Instructions](#instructions)<br/>
&emsp;[__init__() method](#init-method)<br/>
&emsp;[nearest() method](#nearest-method)<br/>
&emsp;[Other instructions](#other-instructions)<br/>
&emsp;&emsp;[Length of individual lines of code](#length-of-individual-lines-of-code)<br/>
&emsp;&emsp;[Docstrings](#docstrings)<br/>
[Running your code](#running-your-code)<br/>
[Submitting your code](#submitting-your-code)

## Problem statement
For this exercise you will develop a *Cities* class that will read location and population data about a number of cities from a text file. Your class will be able to take a reference point (expressed in latitude and longitude) and optionally a minimum population and a maximum number of results and find the closest cities to that reference point.

For example, if asked to find the five closest cities to coordinates 38.9897, -76.9378 with a population of at least 50,000, your program should find Silver Spring, Washington, D.C., Bethesda, Bowie, and Arlington.

### Latitude and Longitude
For this program, latitude and longitude will be expressed in [decimal degrees](https://en.wikipedia.org/wiki/Decimal_degrees), with negative latitudes representing the Southern Hemisphere and negative longitudes representing the Western Hemisphere. For example, the location of the Testudo statue outside McKeldin Library would be represented as 38.9860, -76.9446.

The latitude and longitude of many places can be found with a Google search; for example, "College Park MD coordinates". Remember to translate cardinal directions (N, S, E, or W) to positive or negative as described above.

### Data file
A sample data file, *city_data.txt*, is provided. Each line in the file contains four tab-separated values: a city name, a latitude, a longitude, and a population. Here are a few lines from the file:

*Marijampolė&emsp;54.55991&emsp;23.35412&emsp;47613*<br/>
*Lentvaris&emsp;&emsp;&nbsp;54.64364&emsp;25.05162&emsp;11588*<br/>
*Kybartai&emsp;&emsp;&nbsp;54.63858&emsp;22.76316&emsp;6355*

The data in the file comes from the [GeoNames Gazetteer](https://www.geonames.org/), which is licensed under a [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/). Specifically, this data was extracted from the file *cities5000.zip* by removing all fields other than name, latitude, longitude, and population. The file contains cities from around the world with a population of at least 5,000. This data file may be redistributed under the terms of the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) as long as the GeoNames Gazetteer is credited and the above changes are described.

### Template
A program template, cities.py, is provided. The template imports a number of functions and libraries for your convenience. It also provides the following functions:

- get_dist(): you will use this function to determine the distance between two coordinates. Read the docstring for details on how to use it.
<details>
<summary>If you want more information on how it works, click here.</summary>
<text>This function attempts to use [Vincenty’s inverse formula](https://en.wikipedia.org/wiki/Vincenty%27s_formulae#Inverse_problem) to calculate a very accurate distance between two points on Earth. In rare cases, the implementation of this algorithm fails to converge; when that happens, it uses the less accurate [haversine formula](https://en.wikipedia.org/wiki/Haversine_formula) as a fallback.</text>
</details>

- *main()*: creates an instance of your class. Calls the *nearest()* method. Prints out the results in a nice tabular format.

- *parse_args()*: processes command-line arguments.

#### Dependencies
The template depends on the *haversine* and *vincenty* modules, which you’ll need to install. To install them, type the following in the VS Code terminal (Windows users, replace *python3* with *python*):

*python3 -m pip install --upgrade pip*<br/>
*python3 -m pip install haversine vincenty*

## Instructions
Using the provided template, write a class called *Cities*. Your class should go after the import statements and before the get_dist() function. Follow the instructions below to implement your class.

Be sure to save your script using the name *cities.py*.

The following information may help you write your class docstring. Your class should have one attribute, named *cities*. (This attribute gets created in your *__init__()* method.) The attribute is a list of dictionaries, where each dictionary has the following key/value pairs:
- "name": a string containing the name of the city in English

- "lat": a float representing the latitude of the city in decimal degrees

- "lon": a float representing the longitude of the city in decimal degrees

- "pop": an int containing the population of the city

The following example may give you an idea of how this list of dictionaries is structured:

*[*<br/>
    &emsp;&emsp;*...*<br/>
    &emsp;&emsp;*{"name": "Marijampolė", "lat": 54.55991, "lon": 23.35412,
    &emsp;&emsp;*<br/>&emsp;&emsp;*"pop": 47613},*<br/>
    &emsp;&emsp;*{"name": "Lentvaris",   "lat": 54.64364, "lon": 25.05162,
    &emsp;&emsp;*<br/>&emsp;&emsp;*"pop": 11588},*<br/>
    &emsp;&emsp;*{"name": "Kybartai",    "lat": 54.63858, "lon": 22.76316,
    &emsp;&emsp;*<br/>&emsp;&emsp;*"pop": 6355},*<br/>
    &emsp;&emsp;*...*<br/>
*]*

### *__init__()* method
Define a method called *__init__()* (note the double underscores). Your method should have two required parameters, in the following order:

- *self*

- a path to a file containing city data (a string[^1]; for a description of the format of the data in this file, see the [Data file](#data-file)

This method will create and populate the attribute *self.cities* using the data in the file that was specified in the second parameter of the method (please don’t hard-code the name of the data file anywhere in your program!). See the [Instructions](#instructions) section for a description of the format of *self.cities*.

### *nearest()* method
Define a method called *nearest()*. Your method should have three required parameters and two optional parameters, in the following order:

- *self*

- a latitude in decimal degrees (a float[^2])

- a longitude in decimal degrees (a float)

- *min_population* (please use this exact name): a minimum population (an int); assign this parameter a default value of 0

- *n* (please use this exact name): a maximum number of results to return (an int); assign this parameter a default value of 10

This method should sort a copy of *self.cities* in increasing order of distance from the latitude and longitude specified in the second and third parameters. (Use the *get_dist()* function from the template to determine distances between points; see the docstring of that function for more details.) It should not modify the value of *self.cities* in any way.

Your method should use a comprehension or generator expression to filter out cities that don’t satisfy the requested minimum population.

The method should return a list of the *n* closest city dictionaries from *self.cities* with a population greater than or equal to the minimum population specified in *min_population*, in increasing order of distance from the specified latitude and longitude. *Hint: you can use a slice to get the first n values from a sequence.*

### Other instructions
#### Length of individual lines of code
Please keep your lines of code to 80 characters or less. If you need help breaking up long lines of code, please see https://umd.instructure.com/courses/1299872/pages/how-to-break-up-long-lines-of-code.

#### Docstrings
Please write docstrings for your class and for your *nearest()* method. Docstrings were covered in the first week’s lecture videos and revisited in the OOP lecture videos. There’s an ELMS page about them which you can find by clicking on the "Pages" link in the sidebar (look for the page titled "Docstrings").

Docstrings are not comments; they are statements. Python recognizes a string as a docstring if it is the first statement in the body of the method, function, class, or script/module it documents. Because docstrings are statements, the quotation mark at the start of the docstring must align exactly with the start of other statements in the method, function, class, or module.

<details>
<summary>General instructions for class docstrings</summary>
Class docstrings should

- start with a brief description of the thing the class implements (e.g., *A catalog of battle aardvarks* and *their stats*.).

- contain any additional information about the class that may be useful to someone who wants to use it in their program. (Many class docstrings will not need this.)

- contain an "Attributes:" section that documents the name, data type, and purpose of each attribute.
</details>

<details>
<summary>General instructions method and function docstrings</summary>
Method and function docstrings should

- start with a brief statement of the action or task performed by the method or function.

- contain any additional information about the class that may be useful to someone who wants to use it in their program. Most docstrings will not need this, but see the *parse_args()* docstring in the template for an example of useful additional information in a docstring. Please note: a docstring should not document the inner workings of a function or method; it should just provide information that would be useful to a user of the function or method.

- contain an "Args:" section that documents the name, expected data type, and purpose of each parameter. You do not need to document *self* in this section. If your method or function has no parameters (other than *self*), omit this section.

- contain a "Returns:" section that documents the data type and purpose of the return value. If your method or function does not contain a *return* statement, omit this section.

- contain a "Side effects:" section that documents any side effects caused by your method or function. Examples of side effects include printing values, creating or overwriting files (but not reading files), and setting or modifying attributes. If your method or function has no side effects, omit this section.

- contain a "Raises:" section that documents any exceptions raised by your method or function and the circumstances under which those exceptions are raised. If your method or function does not contain any *raise* statements, omit this section.
</details>

## Running your code
The template script has dependenices on the *haversine* and *vincenty* modules. You will need to install these in order to run your program. See the **Dependencies** section for installation instructions.

Once the dependencies have been installed, to run your program within the VS Code built-in terminal, first make sure you have opened (in VS Code) the directory where your program is saved. If necessary, you can go to the VS Code File menu and select "Open…​​" on macOS or "Open Folder…​" on Windows, and navigate to the directory where your program is.

Then, open the VS Code built-in terminal. Type *python3* (on macOS) or *python* (on Windows) followed by a space and the name of your program. Specify values for the name of the data file, a latitude, and a longitude, all separated by spaces. You may optionally specify a minimum population by typing -p and an integer, and/or a maximum number of results by typing -n and an integer. Below are some examples of ways to invoke your program:

*python3 cities.py city_data.txt 38.9897 -76.9378*<br/>
*python3 cities.py city_data.txt 38.9897 -76.9378 -p 50_000*<br/>
*python3 cities.py city_data.txt 38.9897 -76.9378 -n 5*<br/>
*python3 cities.py city_data.txt 38.9897 -76.9378 -p 50_000 -n 5*

## Submitting your code
Upload your *cities.py* script to Gradescope. An autograder script will give you near-instant feedback. If you did not pass all the test cases, you can revise your code and resubmit as many times as you want until the deadline.

[^1]: You can assume that the value comes to you as a float. You don’t have to do anything to convert it to a float; just assume it already is one.

[^2]: You can assume that the value comes to you as a float. You don’t have to do anything to convert it to a float; just assume it already is one. You can and should make similar assumptions about other parameters based on the data types specified in the instructions. Also, don’t forget to document the expected data type of each parameter in your docstrings!