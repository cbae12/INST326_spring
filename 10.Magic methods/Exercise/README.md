# Exercise: Note class
<hr/>

## Table of Contents
[Problem statement](#problem-statement)<br/>
[Background](#background)<br/>
[Instructions](#instructions)<br/>
&emsp;[Attributes](#attributes)<br/>
&emsp;[Initialization](#initialization)<br/>
&emsp;[Inversion](#inversion)<br/>
&emsp;[Addition](#addition)<br/>
&emsp;[Subtraction](#subtraction)<br/>
&emsp;[Right shift (>>)](#right-shift)<br/>
&emsp;[Left shift (<<)](#left-shift)<br/>
&emsp;[Formal representation](#formal-representation)<br/>
&emsp;[Informal representation](#informal-representation)<br/>
&emsp;[Docstrings](#docstrings)<br/>
[Testing your code](#testing-your-code)<br/>
<hr/>

## Problem statement
Implement a *Note* class that represents a musical note from the twelve-tone chromatic scale. Instances of the class will two attributes, *position* and *perspective*, and work with a number of features of Python.
<hr/>

## Background
Modern western music is built on a scale of twelve semitones. In English-speaking countries, we assign letters A-G to seven of the pitches in the scale; these pitches are called "naturals" (meaning they are neither sharp nor flat). The other five pitches are halfway between two lettered pitches and can be viewed from two different perspectives: they can be said to be "sharps" of the preceding pitch or "flats" of the following pitch. Thus, the note midway between F and G can be referred to as F sharp or G flat. (Note that there is no pitch between B and C and no pitch between E and F.) Whether a note is viewed as a sharp or a flat depends on a number of music-theoretical considerations that we won’t worry about here. For this assignment, we will assume that if one note is viewed from a sharp or flat perspective, other notes relative to that note should be viewed from the same perspective.

Musical notation uses the special symbol ♯ to represent the concept of sharp and ♭ to represent the concept of flat. For convenience, we will use "*#*" instead of *♯* and "*b*" instead of *♭*.
<hr/>

## Instructions
Using the provided template, *note.py*, define a *Note* class that meets the following specifications.

### Attributes
Your class should have two attributes, *position* and *perspective*.

position should be an integer representing the position of the pitch on the chromatic scale, where 0 represents A, 1 represents A♯/B♭, 2 represents B, and so on. The value of position should always be between 0 and 11.

perspective should have one of three values: "*#*", "*b*", or *None*. "#" means that the note should be viewed as a sharp, if applicable. "*b*" means that the note should be viewed as a flat, if applicable. None means the note should be viewed both ways.

**NOTE**<hr/>
Note objects representing natural pitches can still have a perspective attribute that is "*#*" or "*b*". Although it will not have any effect on a Note object representing a natural note, if addition or subtraction is applied to such a Note object, its perspective attribute will propagate to the objects that are created as the result of those operations. Consider the following code:

&emsp;*n1 = Note("C", "#")  # C natural       (sharp perspective)*
&emsp;*n2 = Note("C", "b")  # C natural       (flat perspective)*
&emsp;*n3 = n1 + 1          # C sharp/D flat  (sharp perspective)*
&emsp;*n4 = n2 + 1          # C sharp/D flat  (flat perspective)*
&emsp;*print(n3, n4)*
n1 and n2 are both C natural (position 3), but they have different perspectives (sharp for *n1*, flat for *n2*). *n3* is created with a sharp perspective because it derives from *n1*; *n4* is created with a flat perspective because it derives from *n2*. *n3* and *n4* both represent position 4, but when we print them, *n3* prints as *C#* whereas *n4* prints as *Db*.<hr/>

### Initialization
It should be possible to instantiate your class with one or two values. The first value could be a pitch name such as "A", "C#", or "Gb", or it could be an integer between 0 and 11, inclusive. The second value could be "b", "#", or None. If there is no second value, use None as the default.

The first value should be used to set the value of the position attribute. You can use the global variable *POSITIONS* from the template to help you determine the position of a specific pitch name on the chromatic scale.

If there is a second value that is not None, set the perspective attribute to this value (see the first three examples below). If there is no second value or if the second value is *None*, and the first value is a pitch name with a "#" or "b", set the perspective attribute to the "#" or "b" in the specified pitch name (see the fourth example below). Otherwise, set perspective to None (see the last two examples below).

Examples:

- Note("F", "#"): set position to 8 and perspective to "#"

- Note(4, "b"): set position to 4 and perspective to "b"

- Note("C", "#"): set position to 3 and perspective to "#"

- Note("Ab"): set position to 11 and perspective to "b"

- Note("C"): set position to 3 and perspective to None

- Note(6): set position to 6 and perspective to None

### Inversion
Define your class in such a way that if note is an instance of the *Note* class, the expression *~note* evaluates to a new Note object with the same position but the opposite perspective. If the perspective was *None*, the new Note object should also have None as its perspective.

Examples:

- If *note.position* is 4 and *note.perspective* is "*b*", *~note* should evaluate to a Note object whose position attribute is 4 and whose perspective attribute is "*#*"

- If *note.position* is 8 and *note.perspective* is "*#*", *~note* should evaluate to a Note object whose position attribute is 8 and whose perspective attribute is "*b*"

- If *note.position* is 1 and *note.perspective* is None, *~note* should evaluate to a Note object whose position attribute is 1 and whose perspective attribute is *None*

### Addition
Define your class in such a way that adding an integer to a Note object results in a new instance of *Note* with the same perspective as the original note and with a position that is the specified number of steps above the position of the original note (wrapping around if necessary so that the value of the *position* attribute is always between 0 and 11, inclusive; the modulo operator is your friend here).

Examples:

- If *note.position* is 4 and *note.perspective* is "*b*", *note* + 3 should evaluate to a Note object whose position attribute is 7 and whose perspective attribute is "*b*"

- If *note.position* is 10 and *note.perspective* is *None*, *note* + 4 should evaluate to a *Note* object whose position attribute is 2 and whose perspective attribute is *None*

### Subtraction
Define your class in such a way that subtracting an integer from a Note object results in a new instance of Note with the same perspective as the original note and with a position that is the specified number of steps below the position of the original note (wrapping around if necessary so that the value of the *position* attribute is always between 0 and 11, inclusive; the modulo operator is your friend here).

Examples:

- If *note.position* is 4 and *note.perspective* is "*#*", *note* - 3 should evaluate to a *Note* object whose position attribute is 1 and whose perspective attribute is "*#*"

- If *note.position* is 2 and *note.perspective* is *None*, note - 3 should evaluate to a *Note* object whose position attribute is 11 and whose perspective attribute is *None*
### Right shift (>>)
Define your class in such a way that *note1 >> note2* gives you the distance (i.e., number of positions) from *note1* to *note2*, assuming note1 is higher than note2. The result should always be between 0 and 11.

Examples:

- If *note1* has a *position* of 8 and *note2* has a *position* of 3, *note1 >> note2* should evaluate to 5 (*note1* is five positions above *note2*).

- If *note1* has a *position* of 0 and *note2* has a *position* of 10, *note1 >> note2* should evaluate to 2 (*note1* is two positions above *note2*).

### Left shift (<<)
Define your class in such a way that *note1 << note2* gives you the distance (i.e., number of positions) from note1 to note2, assuming note1 is lower than note2. The result should always be between 0 and 11.

Examples:

- If *note1* has a position of 0 and *note2* has a position of 10, *note1 << note2* should evaluate to 10 (*note1* is ten positions below *note2*).

- If *note1* has a position of 8 and *note2* has a position of 3, *note1 << note2* should evaluate to 7 (*note1* is seven positions below *note2*).

### Formal representation
Define your class so that instances have a formal string representation that could be used to recreate the class.

Examples:

- If *note* has a position of 2 and "*b*" as its perspective, *repr(note)* should evaluate to the string "*Note(2, 'b')*".

- If *note* has a position of 8 and "*#*" as its perspective, *repr(note)* should evaluate to the string "*Note(8, '#')*".

- If *note* has a position of 4 and *None* as its perspective, *repr(note)* should evaluate to the string "*Note(4, None)*".

### Informal representation
Define your class so that instances have an informal string representation that is the pitch of the note from the note’s perspective. If the note has two possible pitch names and the perspective is None, give the sharp name first, then a forward slash, then the flat name. You can use the PITCHES global variable from the template to help you determine the name(s) of a given position in the chromatic scale.

Examples:

- If *note* has a position of 1 and "*#*" as its *perspective*, *str(note)* should evaluate to the string "*A#*".

- If *note* has a position of 1 and "b" as its *perspective*, *str(note)* should evaluate to the string "*Bb*".

- If *note* has a position of 1 and None as its *perspective*, *str(note)* should evaluate to the string "*A#/Bb*".

- If *note* has a position of 0, *str(note)* should evaluate to the string "*A*" regardless of the value of the *perspective* attribute.

### Docstrings
Write a docstring for the class. You do not need to write docstrings for the magic methods.
<hr/>

## Testing your code
You can test your code by importing your *Note* class into another script in the same directory, creating Note objects, and applying the appropriate operations or functions to test their features. You can also do this kind of testing in an interactive Python session or in a Jupyter notebook in the same directory as your script.
<hr/>