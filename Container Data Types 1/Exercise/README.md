# Exercise: Word game

## Background
Imagine a game where two players are presented with a matrix of letters. They must independently find words within those letters within a certain time limit. Once time has expired, each player removes duplicate words from the list of words they found, and the two players compare lists. Only words found by both players that are at least three letters long are worth points. A word is worth the number of letters it contains minus 2.

### Example
Tyrone and Alice play the game. Tyrone’s list contains the words "apple", "app", "pal", "leap", "a", and "app". Alice’s list contains the words "pale", "pal", "a", "leap", and "parlor". Tyrone realizes he listed "app" twice and crosses the second instance of this word off his list. Tyrone and Alice compare notes; they have both found "pal", "leap", and "a". "pal" is worth one point, "leap" is worth two points, and "a" is not worth any points. Their total score is 3.

## Problem Statement
For this exercise you will develop a PlayerWords class capable of reading in words from a file and calculating two players' score for the fictional word game described above. You will also write a main() function outside that class that will create two instances of the class (one for each partner on a team), compute the team’s score, and print it to the console.

## Instructions
Use the provided template, *word_game.py*. Ensure that your program is called *word_game.py*.

### PlayerWords class
Write a class called *PlayerWords*. This class will have one attribute, a set of strings containing the unique words found by one player.

#### __init__() method
Give uour class an __init__() method. This method should take one argument, a string containing the path to a text file. The text file will consist of one word per line. You can assume that each word will be spelled using only lower-case letters.

Open the file for reading and read in the words. Strip off any leading or trailing whitespace from each word. Store the words as a set in an attribute called *words*.

#### score() method
Give your class a *score()* method. This method should take one argument, another *PlayerWords* object representing the words found by the partner.

Determine which words the two players (*self* and the partner) both found (hint: there’s a set operation that does this!). Calculate a score for the team and return it.

### main() function
Outside of the class, write a function called main() that takes two arguments:

- a string consisting of a path to a text file containing the 
  words found by player 1

- a string consisting of a path to a text file containing the 
  words found by player 2

Create one instance of your *PlayerWords* class for each player. Using one of the instances (doesn’t matter which one), compute the team’s score and print it out in a message formatted like the following one:

*Your team scored 3 points!*
(Hint: f-strings are a nice way to do this.)

### Other instructions
- Please write docstrings for your class, each of your methods, 
  and your function.

    * Your class docstring should start with a brief statement of the purpose of the class. It should then document the attributes of the class in an Attributes: section.

    * Your method/function docstrings should start with a brief statement of the function’s purpose.

    * If your method or function takes arguments, provide an Args: section to document them, including their names, data types, and a brief description of the purpose of each. You do not need to document self in the Args: section.

    * If your method or function returns a value, write a Returns: section to describe the return value, including its data type and a brief description of its purpose.

    * If your method causes side effects, include a Side effects: section to describe the side effects. Examples of side effects include setting or changing an attribute’s value and printing information to the console.

Docstrings were covered in the lectures here: https://youtu.be/jHTv83PlQYw?t=1415. There’s an ELMS page about them here: https://umd.instructure.com/courses/1312228/pages/docstrings.

- Please keep your lines of code to 80 characters or less. If you need help breaking up long lines of code, please see https://umd.instructure.com/courses/1312228/pages/how-to-break-up-long-lines-of-code.

## Submitting your code
Upload your *word_game.py* file to Gradescope. An autograder script will give you (near-)instant feedback. If you did not pass all the test cases, you can revise your code and resubmit as many times as you want until the deadline.

If you and your partner(s) finish in class, please make a single submission; the submitter should add their partner(s) as group members. If you do not finish in class, the driver should send a copy of the unfinished program to the navigator(s) and each person should finish and submit the assignment on their own.

## Testing your code
To run your program within the VS Code built-in terminal, first make sure you have opened (in VS Code) the directory where your program is saved. If necessary, you can go to the VS Code File menu and select "Open…​​" on macOS or "Open Folder…​" on Windows, and navigate to the directory where your program is.

Then, open the VS Code built-in terminal. Type *python3* (on macOS) or *python* (on Windows) followed by a space and the name of your program. The program expects two command-line arguments, one for each player’s word list. Sample word lists (*player1_words.txt* and *player2_words.txt*) were provided. Below is an example of how to run the program:

*python3 word_game.py player1_words.txt player2_words.txt*