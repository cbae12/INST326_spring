# Exercise: Hangman
<hr/>

## Table of Contents
[Problem statement](#problem-statement)<br/>
[Background](#background)<br/>
&emsp;[Wordlist file](#wordlist-file)<br/>
&emsp;[Template](#template)<br/>
&emsp;[GameState objects](#gamestate-objects)<br/>
[Instructions](#instructions)<br/>
&emsp;[HumanPlayer class](#humanplayer-class)<br/>
&emsp;&emsp;[turn() method](#turn-method)<br/>
&emsp;[ComputerPlayer class](#computerplayer-class)<br/>
&emsp;[__init__() method](#init-method)<br/>
&emsp;&emsp;[turn() method](#turn-method-1)<br/>
&emsp;[Other instructions](#other-instructions)<br/>
&emsp;&emsp;[Length of individual lines of code](#length-of-individual-lines-of-code)<br/>
&emsp;&emsp;[Docstrings](#docstrings)<br/>
[Running your code](#running-your-code)<br/>
[Submitting your code](#submitting-your-code)<br/>
<hr/>

## Problem statement
Write two subclasses of the Player class in the provided template. One should be called *HumanPlayer*; the other should be called *ComputerPlayer*.

For your *HumanPlayer* class, you will override the *turn()* method as described below.

For your *ComputerPlayer* class, you will override both the *__init__()* and *turn()* methods as described below.
<hr/>

## Background
Hangman is a popular game that involves guessing a word one letter at a time. If you are unfamiliar with this game, you may want to watch this video for additional background information: https://www.youtube.com/watch?v=cGOeiQfjYPk.

We will complete a multi-player game based on hangman. Words will be chosen from a wordlist file. Each player will be allowed a certain number of bad guesses; once they reach this limit, they lose and will not be given any more turns. On a player’s turn, they may guess a single letter or try to solve the puzzle by typing in an entire word or phrase. All guesses are converted internally to uppercase.

Your goal is to develop a human player and a computer player as subclasses of the abstract *Player* base class.

### Wordlist file
The file *nounlist.txt* can be used as a wordlist for the game. It comes from http://www.desiquintans.com/nounlist.

### Template
A template script is provided. The template contains the following classes and functions:

- *GameState*: instances of this class are passed to each player’s turn() method to communicate the current state of the game to the player.

- *Game*: this class sets up and manages a game of hangman.

- *Player*: this is the abstract class that you will need to subclass.

- *main()*: this function reads wordlists, instantiates Player objects and a Game object, and starts a game.

- *parse_args()*: this function processes command-line arguments.

### GameState objects
An instance of the *GameState* class is passed to each player’s *turn()* method to provide important information on the current state of the game. When printed, *GameState* objects provide

- a string representation of the current state of the board, showing which letters have been guessed and which have not

- a list of characters that have been guessed that are not found in the word

- the number of bad guesses made by each character

*GameState* objects have a *match()* method that takes a string and returns *True* if the string is compatible with the current letters and blanks on the board (for example, the word "temporary" is compatible with the board *T E • • • R A R •*; the word "temerity" is not). The *match()* method does not take into account whether the string contains "bad guesses" (letters known not to be in the word).

*GameState* objects contain a number of additional potentially interesting attributes; see the class docstring for details on the purpose and structure of each of these.
<hr/>

## Instructions
Please use the template to implement your solution to this homework. Make sure your program is called *hangman.py*. Follow the instructions below.

### HumanPlayer class
Create a class called *HumanPlayer* that is a subclass of the *Player* class. Inherit the *__init__()* method from the parent class.

#### turn() method
Your *HumanPlayer* class should have a *turn()* method with two parameters:

- *self*

- a *GameState* object representing the current state of the game

This method should print the board (you can do this by printing the *GameState* object). It should prompt the user **by name** to guess a letter or solve the entire puzzle. For example:

&emsp;*Mark, guess a letter or type a word to solve the puzzle:*<br/>

It should return the value typed by the user.
### ComputerPlayer class
Create a class called *ComputerPlayer* that is a subclass of the *Player* class.
### __init__() method
Your *ComputerPlayer* class should override the parent class’s *__init__()* method with a method that has three parameters

- *self*

- a name for the computer player (a string)

- a vocabulary list (a list of strings); these are the words your computer player can draw from when taking turns; note that these words are converted to uppercase

Store the name in an attribute called *self.name*. Store the vocabulary list in an attribute called *self.vocab*.

#### turn() method
Your *ComputerPlayer* class should have a *turn()* method with two parameters:

- *self*

- a *GameState* object representing the current state of the game

This method should either guess a letter that has not been guessed yet or guess a word to solve the puzzle. It should return the letter or word.

Note: the *choice()* function from the *random* module has been imported for you. When you pass it a list, it randomly selects one item from the list. For example, choice(["A", "B", "C"]) will randomly select "A", "B", or "C".

For full points, your *turn()* method should beat a ComputerPlayer who just picks an unguessed letter at random on each turn.

### Other instructions
#### Length of individual lines of code
Please keep your lines of code to 80 characters or less. If you need help breaking up long lines of code, please go to the "Pages" link in the ELMS sidebar and find the page titled "How to break up long lines of code".

#### Docstrings
Please write docstrings for your classes and for your turn() methods. Docstrings were covered in the first week’s lecture videos and revisited in the OOP lecture videos. There’s an ELMS page about them that you can access from the "Pages" link in the ELMS sidebar.

Docstrings are not comments; they are statements. Python recognizes a string as a docstring if it is the first statement in the body of the method, function, class, or script/module it documents. Because docstrings are statements, the quotation mark at the start of the docstring must align exactly with the start of other statements in the method, function, class, or module.
<details>
<summary>General instructions for class docstrings</summary>
<text>Class docstrings should

- start with a brief description of the thing the class implements (e.g., A catalog of battle aardvarks and their stats.).

- contain any additional information about the class that may be useful to someone who wants to use it in their program. (Many class docstrings will not need this.)

- contain an "Attributes:" section that documents the name, data type, and purpose of each attribute.</text>
</details>
<details>
<summary>General instructions method and function docstrings</summary>
<text>Method and function docstrings should

- start with a brief statement of the action or task performed by the method or function.

- contain any additional information about the class that may be useful to someone who wants to use it in their program. Most docstrings will not need this, but see the *parse_args()* docstring in the template for an example of useful additional information in a docstring. Please note: a docstring should not document the inner workings of a function or method; it should just provide information that would be useful to a user of the function or method.

- contain an "Args:" section that documents the name, expected data type, and purpose of each parameter. You do not need to document *self* in this section. If your method or function has no parameters (other than *self*), omit this section.

- contain a "Returns:" section that documents the data type and purpose of the return value. If your method or function does not contain a *return* statement, omit this section.

- contain a "Side effects:" section that documents any side effects caused by your method or function. Examples of side effects include printing values, creating or overwriting files (but not reading files), and setting or modifying attributes. If your method or function has no side effects, omit this section.

- contain a "Raises:" section that documents any exceptions raised by your method or function and the circumstances under which those exceptions are raised. If your method or function does not contain any *raise* statements, omit this section.</text>
</details>
<hr/>

## Running your code
To run your program within the VS Code built-in terminal, first make sure you have opened (in VS Code) the directory where your program is saved. If necessary, you can go to the VS Code File menu and select "Open…​​" on macOS or "Open Folder…​" on Windows, and navigate to the directory where your program is.

Then, open the VS Code built-in terminal. Type python3 (on macOS) or python (on Windows) followed by a space and the name of your program. Specify values for the name of the wordlist file and the names of all human players, separated by spaces. You may optionally add a computer player by typing *-c*, and a separate vocabulary file for your computer player by typing *-v* and the path to another wordlist file. Below are some examples of ways to invoke your program:

&emsp;*python3 hangman.py nounlist.txt Sarah Owen*<br/>
&emsp;*python3 hangman.py nounlist.txt Sarah -c*<br/>
&emsp;*python3 hangman.py nounlist.txt Sarah -c -v some_other_wordlist.txt*<br/>
&emsp;*python3 hangman.py nounlist.txt -c*<br/>
<hr/>

## Submitting your code
Upload your *hangman.py* script to Gradescope. An autograder script will give you near-instant feedback. If you did not pass all the test cases, you can revise your code and resubmit as many times as you want until the deadline.

<hr/>