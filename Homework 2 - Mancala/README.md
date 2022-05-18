# Homework: Mancala
<hr/>

## Table of Contents
[Problem statement](#problem-statement)<br/>
[Background](#background)<br/>
&emsp;[Rules of the game](#rules-of-the-game)<br/>
&emsp;[Computational model](#computational-model)<br/>
&emsp;&emsp;[Attributes of Mancala instances](#attributes-of-mancala-instances)<br/>
&emsp;&emsp;[Tracking whose turn it is (the current player index)](#tracking-whose-turn-it-is-the-current-player-index)<br/>
&emsp;&emsp;[Turn functions](#turn-functions)<br/>
&emsp;&emsp;[Template file (mancala.py)](#template-file-mancalapy)<br/>
&emsp;[Some notes about lists](#some-notes-about-lists)<br/>
[Instructions](#instructions)<br/>
&emsp;[__init__()](#init)<br/>
&emsp;[validate_move()](#validatemove)<br/>
&emsp;[check_capture()](#checkcapture)<br/>
&emsp;[distribute_seeds()](#distributeseeds)<br/>
&emsp;[play_round()](#playround)<br/>
&emsp;[Docstrings](#docstrings)<br/>
[Running your program](#running-your-program)<br/>
[Submitting your code](#submitting-your-code)<br/>
<hr/>

## Problem statement
Using the provided template script, complete the *Mancala* class to implement a terminal-based version of the game mancala. Your completed class will include

- a class docstring

- an *__init__()* method to initialize instances of the class

- a *validate_move()* method to determine if a given player can play from a particular pit

- a *check_capture()* method to determine if a given player has captured seeds from an opponent’s pit, and if so, to move those seeds to the player’s store

- a *distribute_seeds()* method to distribute seeds from one pit to the subsequent pits

- a *play_round()* method to run a single round of game play

- docstrings for all of the above methods

Detailed [instructions](#instructions) for each method are provided below.
<hr/>

## Background
The name *mancala* describes a number of related board games involving an arrangement of pits or cups in which small objects (stones, marbles, seeds, etc.) are placed. The primary action of play is to remove all the items from one pit and redistribute them in sequence to the following pits. This action mimics the process of sowing seeds. Mancala has a history dating back well over a thousand years, and variants of the game can be found throughout Africa, Asia, and the Carribean.

### Rules of the game
For this homework, we will use the layout, rules, and terminology specified in this document: https://harriscenter.org/wp-content/uploads/2020/03/mancala_rules.pdf. Specifically:

- Each player has six pits and one store.

- At the beginning of the game, each pit contains four seeds, and each store is empty.

- On a player’s turn, the player selects one of their pits that contains seeds. Those seeds are removed from that pit and distributed counterclockwise to the subsequent pits, one seed per pit.

    * If the player has placed a seed in their last pit and has seeds left to distribute, the next seed goes in their store, the seed after that (if any) goes in their opponent’s first pit, and so on. However, if a player still has seeds to distribute after reaching their opponent’s last pit, they skip the opponent’s store and continue placing seeds in their own pits. A player never places seeds in their opponent’s store.

- If a player’s last seed lands in their store, the player gets another turn.

- If a player’s last seed lands in an empty pit (but not the store) on their own side of the board, the player "captures" the seed and any seeds in the opponent’s pit directly opposite this pit. All captured seeds are placed in the player’s store.

- The game ends when one player has no seeds left in any of their pits (not including the store).

- At the end of the game, the winner is the player with the most total seeds in their store and pits (if applicable).

### Computational model
#### Attributes of Mancala instances
Our mancala game is designed to be played in the terminal by two human players. At the heart of the game is the *Mancala* class. Instances of the class will have three attributes:

- *board*: a list of 14 integers. Indexes 0 through 5 (inclusive) represent the first player’s pits; index 6 represents the first player’s store. Indexes 7-12 represent the second player’s pits, and index 13 represents the second player’s store.

- *names*: a list of two items: the first and second players' names, respectively.

- *turn_funcs*: a list of two items: the turn functions for each player, respectively. For more on these, see the [Turn functions](#turn-functions) section below.

#### Tracking whose turn it is (the current player index)
During a round, the game will use an integer to keep track of whose turn it is; a value of 0 means it is the first player’s turn, while a value of 1 means it is the second player’s turn. A lot of the methods in the class include a paramter for this value. The value can be used as an index into the lists stored in the *names* and *turn_funcs* attributes.

An easy way to toggle the player index between values 0 and 1 is to subtract the current value from 1 (e.g., *player = 1 - player*).

#### Turn functions
A turn function is a function that takes two arguments (an instance of the *Mancala* class and the [index of the current player](#tracking-whose-turn-it-is-the-current-player-index)) and returns an index to a pit in the list representing the board. The index that is returned must refer to a non-empty pit belonging to the current player.

The template includes a turn function called *get_move()*. This function uses Python’s built-in *input()* function to ask a human player which pit they wish to select. It asks for the player’s selection repeatedly until the player makes a valid choice.

*get_move()* will be used as the default turn function; indeed, it is the only turn function we will write for this assignment. However, the turn function mechanism could also be used to write an AI player. As far as the program is concerned, the only requirements would be for the function to

1. take the same arguments as *get_move()* in the same order

2. return an index to a non-empty pit belonging to the current player

#### Template file (mancala.py)
Template file (mancala.py)
A template file, *mancala.py*, has been provided for you. It contains the following elements:

- **Import statements** for all external dependencies

- A set of **constants** for printing information about the board

- The *get_move()* function (described under [Turn functions](#turn-functions) above)

- The header of the *Mancala* class

- The following methods of the *Mancala* class:

    * *game_over()*: determines if the [game is over](#rules-of-the-game)

    * *score()*: computes a single player’s score; meant to be used at the end of a round only

    * *is_own_pit()*: determines if a given pit belongs to a given player

    * *play()*: enables players to play multiple rounds; restores terminal after game

    * *play_again()*: asks players if they want to play another round and validates their response

    * *print_board()*: populates the board template and displays it to the players; pauses temporarily to help the players notice what changed

    * *print_winner()*: determines the winner of the round and displays information about the outcome in the terminal

- The *parse_args()* function, which gets the player’s names from the command line

- An if *__name__ == "__main__"*: statement which gets command-line arguments, uses them in the creation of an instance of the *Mancala* class, and starts the game.

### Some notes about lists
List objects can be concatenated with the + operator:

&emsp;*list1 = [1, 2, 3]*<br/>
&emsp;*list2 = [4, 5, 6]*<br/>
&emsp;*list3 = list1 + list2*<br/>

The * operator repeats lists; for example, the following code snippet creates a list containing six instances of the number 4:

&emsp;*six_fours = [4] * 6*<br/>
(Exercise for the reader: figure out what ([4]*6 + [0]) * 2 evaluates to.)

You can redefine individual elements in a list based on their index. Consider the following code snippet:

&emsp;*lst = ["Hello", "world!"]*<br/>
&emsp;*lst[1] = "Maryland!"*<br/>
The second line of the snippet replaced the item at index 1 ("world!") with "Maryland!". The new value of lst is ["Hello", "Maryland!"]. As you may have noticed, changing list items in this way is analogous to the way you would modify individual key/value pairs in a dictionary.
<hr/>

## Instructions
Complete the *Mancala* class from the template file *mancala.py* by adding a class docstring and the following methods, including method docstrings:

### __init__()
This method should have three required parameters and two optional parameters, defined in the following order. If names are specified below, please use those exact names in your program.

- *self*

- the name of player 0 (you choose the name for this parameter; you can assume its value will be a string)

- the name of player 1 (you choose the name for this parameter; you can assume its value will be a string)

- *func0*: the [turn function](#turn-functions) to call on player 0’s turn (use *get_move* as the default value)

- *func1*: the [turn function](#turn-functions) to call on player 1’s turn (use *get_move* as the default value)

The function should initialize three attributes:

- the *names* attribute should be initialized to a list of the two players' names, starting with the name of player 0.

- the *turn_funcs* attribute should be initialized to a list of the two players' turn functions, starting with *func0*.

- the *board* attribute should be initialized to an empty list. (We will give it a more useful value in the *play_round()* method.)

### validate_move()
This method checks whether a player is allowed to play from a particular pit. If not, it raises a *ValueError* with a short error message explaining why the selection is invalid. If the method finishes without raising an exception, the requested move is valid.

This method has three required parameters:

- *self*

- the index of a pit, expressed as an integer

- [the index of the player](#tracking-whose-turn-it-is-the-current-player-index) (an integer with a value of either 0 or 1)

If the specified pit index is a store, raise a *ValueError* with the message *"Sorry, you can’t select the store."* (The global variable *STORES* may be helpful here.)

If the specified pit index doesn’t belong to the player, raise a *ValueError* with the message *"Sorry, you don’t control that pit."* (The method *is_own_pit()* may be helpful here.)

If the specified pit has nothing in it (e.g., *self.board[pit]* has a value of 0), raise a *ValueError* with the message *"Sorry, that pit is empty."*

Note that you will need to include a *Raises*: section in this method’s docstring.

### check_capture()
This method determines if a player has qualified to [capture seeds](#rules-of-the-game) and carries out the capture if the conditions have been met. It has three required parameters:

- *self*

- the index of the pit in which a player has placed the last seed from a seed distribution action, expressed as an integer

- the [index of the player](#tracking-whose-turn-it-is-the-current-player-index) who placed the seed (an integer with a value of either 0 or 1)

A player qualifies to capture seeds if all of the following conditions are met:

- the pit in question is one of the player’s own pits (and not the player’s store; the global variable *STORES* and the method *is_own_pit()* may be helpful here)

- the only contents of the pit are the seed the player just placed there (in other words, the value of the pit is 1)

If the player qualifies to capture:

- You will need to determine the index of the opposite pit, which is simply 12 minus the index of the player’s pit.

- You will also need the index of the player’s store, which is 6 for player 0 and 13 for player 1.

- Add the value of the player’s pit and the opposite pit to the player’s store.

- Then set the value of both pits to 0.

- Call the *print_board()* method to display the updated board.

- Print a message in the following format: *"<Player’s name> captured the contents of pits <opponent pit letter> and <player pit letter>"*. (For example: Janelle captured the contents of pits e and h.) You can get the player’s name from the *names* attribute of the Mancala object. You can get the pit letters by looking up each pit index in the global variable *PITS*.

Note that displaying information on the terminal and updating the value of an attribute are considered side effects.

### distribute_seeds()
This method distributes seeds that were in a specified pit to the subsequent pits and the player’s store, if applicable. Every time the value of a pit changes, this method should call the *print_board()* method so the players can see what is happening at each step of this process.

This method has three required parameters:

- *self*

- the index of a non-empty pit belonging to the player, expressed as an integer

- the [index of the player](#tracking-whose-turn-it-is-the-current-player-index) (an integer with a value of either 0 or 1)

This method should capture the number of seeds in the specified pit and then set the value of that pit to zero. At this point, it should call the *print_board()* method for the first time.

It should then put one seed in each of the following pits or the player’s own store, if applicable, until all the seeds have been distributed. Each time a seed is added to a pit or store, the method should call the *print_board()* method. As a reminder, this method should never put a seed in the opponent’s store.

When all seeds have been distributed, this method should return the index of the last pit (or the store) into which a seed was placed. Note that modifying attributes and displaying information on the terminal are considered side effects.

### play_round()
This method manages one round of game play. It initializes the board for the new round, prints the board, manages turns until one player wins, then prints the results of the round.

This method has one required parameter (*self*).

In this method, you should:

- Redefine the board attribute as a list where indexes 0-5 and 7-12 each have a value of 4 and indexes 6 and 13 each have a value of 0.

- Call the print_board() method.

- Set a variable to keep track of the [index of the current player](#tracking-whose-turn-it-is-the-current-player-index); give it an initial value of 0 (representing the first player).

- Until the game is over (use the game_over() method to check this), do the following steps for each turn:

    * Call the current player’s [turn function](#turn-functions); this will give you the index of the pit the player has selected.

    * Call the *distribute_seeds()* method; this will give you the index of the pit (or store) where the last seed was placed.

    * Call the *check_capture()* method to determine whether the player’s turn should result in capture of seeds from pits, and make the capture happen if applicable.

    * If the last seed was placed in the player’s store, print a message in the following format: *"<Player’s name> gets an extra turn!"* (For example: Darren gets an extra turn!) Otherwise, **switch the current player index to the other player’s index** so the next turn goes to the other player.

Once the game is over, call the *print_winner()* method.

### Docstrings
Please write clear, specific docstrings for each of the above methods as well as for the Mancala class. Please follow the guidelines specified in https://umd.instructure.com/courses/1320803/pages/docstrings.
<hr/>

## Running your program
The provided template requires the [blessed](https://pypi.org/project/blessed/) module. Install this module at the command prompt using the following sequence of commands (Windows users, type *python* instead of *python3*):

&emsp;*python3 -m pip install --upgrade pip*<br/>
&emsp;*python3 -m pip install blessed*<br/>
Your program is designed to run from the terminal. To run it, open a terminal and ensure you are in the directory where your script is saved.

The program takes two required command-line arguments (the names of the two players). Below is an example of how to run the program. Windows users, type *python* instead of *python3* when you run your program.

&emsp;*python3 mancala.py Alice Michael*<br/>
<hr/>

## Submitting your code
Upload your *mancala.py* script to Gradescope. An autograder script will give you near-instant feedback. If you did not pass all the test cases, you can revise your code and resubmit as many times as you want until the deadline.
<hr/>