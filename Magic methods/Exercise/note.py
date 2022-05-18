import re

POSITIONS = {
    "A" :  0,
    "A#":  1,
    "Bb":  1,
    "B" :  2,
    "C" :  3,
    "C#":  4,
    "Db":  4,
    "D" :  5,
    "D#":  6,
    "Eb":  6,
    "E" :  7,
    "F" :  8,
    "F#":  9,
    "Gb":  9,
    "G" : 10,
    "G#": 11,
    "Ab": 11
}

PITCHES = {
    0:  ["A"],
    1:  ["A#", "Bb"],
    2:  ["B"],
    3:  ["C"],
    4:  ["C#", "Db"],
    5:  ["D"],
    6:  ["D#", "Eb"],
    7:  ["E"],
    8:  ["F"],
    9:  ["F#", "Gb"],
    10: ["G"],
    11: ["G#", "Ab"]
}

class Note:
    """A note with access to position and perspective operations.

    Attributes:
        position (int): the position component of the note, expressed as an 
        integer between 0 and 11, inclusive, representing positions A to G.
        perspective (str): the perspective component of the note, expressed 
        as a string as either None, #, or b.
    """
    def __init__(self, pitch, val=None):
        """Initialize a Note object.

        Args:
            pitch (int or str): if int, it is the position component of a Note
                object and must be between 0 and 11, inclusive.

                If str, it is a string representation of a position in the form
                "A", where A represents position.

            val (int, optional): if not None, it is the perspective component
                of a Note object, either #, b, or None.

        Raises:
            ValueError: arguments did not match specifications above.
        """
        if isinstance(pitch, str):
            match = re.search(r"\w*[^\s\"\:\,\d]", pitch.strip())
            if not match:
                raise ValueError("invalid string representation of a position")
            
            self.position = POSITIONS[pitch]
            self.perspective = val
            if (not val) or (val == None):
                if pitch[-1] == '#':
                    self.perspective = '#'
                if pitch[-1] == 'b':
                    self.perspective = 'b'
        else:
            try:
                pitch = int(pitch)
            except ValueError:
                raise ValueError("pitch must be ints")
            if not (0 <= pitch <= 11):
                raise ValueError("pitch must be between 0 and 11, inclusive")
            
            self.position = pitch
            self.perspective = val
    
    def __invert__(self):
        """Compute the complementary perspective of this Note.

        Defines the behavior of the ~ unary operator.

        Returns:
            Note: new_note is a Note obj with the complementary perspective.
        """

        if self.perspective == None:
            self.perspective = None
        elif self.perspective == 'b':
            self.perspective = '#'
        elif self.perspective == '#':
            self.perspective = 'b'
        
        new_note = Note(self.position, self.perspective)
        return new_note

    def __add__(self, other):
        """Redefine the variable containing self as the sum of this Note and
        integer.

        Defines the behavior of the += operator.

        Args:
            other (int): the integer being added to self.position.

        Returns:
            Note: Note obj with its position as sum of self.position and other.

        Raises:
            TypeError: other is not an integer.
        """
        try:
            other = int(other)
        except TypeError as e:
            raise e
        
        self.position = (self.position + other) % 11
        return Note(self.position, self.perspective)

    def __sub__(self, other):
        """Redefine the variable containing self as the sum of this Note's
        position and integer other.

        Defines the behavior of the -= operator.

        Args:
            other (int): the integer being subtracted from self.

        Returns:
            Note: This Note object is returned with its position subtracted
            by integer other. If other is greater than the position
            of this Note, wrap around to remain in between 0 and 11.

        Raises:
            TypeError: other is not integer.
        """
        try:
            other = int(other)
        except TypeError as e:
            raise e

        if self.position < other:
            self.position = (11 + (self.position - other)) % 11
        else:
            self.position = (self.position - other) % 11
        return Note(self.position, self.perspective)

    def __rshift__(self, other):
        """Returns the distance between this Note and other Note in position.
        
        Defines the behavior of the >> operator.

        Args:
            other(Note): the Note's position is used to calculate the distance
            from this self Note.
        
        Returns:
            integer: Integer value that tells you of the distance between this
            Note and other Note from their positions. Wraps around if other Note
            position is greater than this Note position.

        Raises:
            TypeError: other is not a Note object
        """
        if not isinstance(other, Note):
            raise TypeError(f"Cannot compare Note and {type(other).__name__}"
                            " objects")
        if self.position < other.position:
            other.position = 12 - other.position
            return self.position + other.position
        else:
            return self.position - other.position

    def __lshift__(self, other):
        """Returns the distance between this Note and other Note in position.
        
        Defines the behavior of the << operator.

        Args:
            other(Note): the Note's position is used to calculate the distance
            from this self Note.
        
        Returns:
            integer: Integer value that tells you of the distance between this
            Note and other Note from their positions. Wraps around if this Note
            position is greater than other Note position.

        Raises:
            TypeError: other is not a Note object
        """
        if not isinstance(other, Note):
            raise TypeError(f"Cannot compare Note and {type(other).__name__}"
                            " objects")
        if self.position > other.position:
            self.position = 12 - self.position
            return other.position + self.position
        else:
            return other.position - self.position
    
    def __repr__(self):
        """Produce a formal string representation of this Note.

        The formal representation will have the form "Note(position,
        perspective)" where position and perspective are the components of 
        this Note.

        This representation is suitable for debugging and can be used as code
        to recreate this object.

        Returns:
            str: the string representation
        """
        if self.perspective == None:
            return f"Note({self.position}, {self.perspective})"
        else:
            return f"Note({self.position}, '{self.perspective}')"

    def __str__(self):
        """Produce an informal string representation of this Note.

        This representation will have the form "A#", where A, and #
        are string literals, respectively, the position and
        perspective components of this Note.

        Returns:
            str: the string representation.
        """
        new_list = [a for a in PITCHES[self.position]]
        val0 = new_list[0]
        val1 = new_list[1]
        if (len(new_list) == 2):
            if (self.perspective == '#'):
                return f"{val0}"
            if (self.perspective == None):
                return f"{new_list[0]}/{new_list[1]}"
            if (self.perspective == 'b'):
                return f"{val1}"
        elif (self.position == 0):
            return f"A"
        else:
            return f"{PITCHES[self.position]}{self.perspective}"