from argparse import ArgumentParser
import re
import sys


LETTER_TO_NUMBER = {
    'A': '2',
    'B': '2',
    'C': '2',
    'D': '3',
    'E': '3',
    'F': '3',
    'G': '4',
    'H': '4',
    'I': '4',
    'J': '5',
    'K': '5',
    'L': '5',
    'M': '6',
    'N': '6',
    'O': '6',
    'P': '7',
    'Q': '7',
    'R': '7',
    'S': '7',
    'T': '8',
    'U': '8',
    'V': '8',
    'W': '9',
    'X': '9',
    'Y': '9',
    'Z': '9'
}


# Replace this comment with your implementation of the PhoneNumber class and
# the `read_numbers()` function.
class PhoneNumber:
    def __init__(self, line):
        expr = r"""(?xm)
                   ^
                   (?:(?P<ignore0>\+))?
                   (?:(?P<country_code>[1]))?
                   (?:(?P<ignore1>\D?\(?))?
                   (?P<area_code>[0-9]{3})
                   (?:(?P<ignore2>\)?\W?\_?))?
                   (?P<exchange_code>\w(?:\s)?\w(?:(?P<err0>\W))?\w)
                   (?:(?P<ignore3>\W?\_?))?
                   (?P<line_number>\w.(?:(?P<err1>\W))?\w(?:(?P<err2>\W))?\w?)
                   (?:(?P<leftover>\w))?
                   $"""
        match = re.search(expr, line)
        self.area_code = int(match.group("area_code"))
        no_dash = re.sub('-', '',match.group("exchange_code"))
        print(f"THIS IS THE MATCHHHHHHHHHH {no_dash}")
        self.exchange_code = re.sub(no_dash, LETTER_TO_NUMBER[no_dash], match.group("exchange_code"))

        
        # for number in re.finditer(r"[0-9]+", line):
        #     number = int(number)
        # for letter in re.finditer(r"[A-Z]", line):
        #     letter = LETTER_TO_NUMBER(letter)
        #     letter = int(letter)
        try:
            if not (isinstance(line, str) | isinstance(line, int)):
                raise TypeError("Please enter either a string or integer")
            if match.group("area_code")[0] == (0 | 1):
                raise ValueError("Your Area code cannot start as 0 or 1")
            if match.group("exchange_code")[0] == (0 | 1):
                raise ValueError("Your Exchange code cannot start as 0 or 1")
            if match.group("area_code")[-2:] == "11":
                raise ValueError("Your Area code cannot end with 11")
            if match.group("exchange_code")[-2:] == "11":
                raise ValueError("Your Exchange code cannot end with 11")
        except TypeError as t:
            print(t)
        except ValueError as e:
            print(e)
    
    def convert(matchobj):
        if matchobj.group() == '[A-Z]':
            return LETTER_TO_NUMBER
    
    def __str__(self):
        str = f"({self.area_code}) {self.exchange_code}-{self.line_number}"
        return str

    def __repr__(self):
        str = (f"PhoneNumber('{self.area_code}{self.exchange_code}"
              f"{self.line_number}')")
        return str

    def __lt__(self, other):
        if self < other:
            return True

def read_numbers(path):
    all_read = list()
    with open(path, "r", encoding="utf-8") as f:
        phone_numbers = f.read()
        named_numbers = phone_numbers.strip().split("\n")
        for phone in named_numbers:
            name, numbers = phone.split("\t")
            p_numbers = PhoneNumber(numbers)
            if isinstance(name, str):
                all_read.append((name, p_numbers))
                
        # match1 = re.search(r"\t",phone_numbers)
        # match2 = re.search(r"\n",phone_numbers)
        # p_numbers = phone_numbers[match1.end(0):match2.start(0)]
        # digits = PhoneNumber(p_numbers)
        # phone_digit = (f"({digits.area_code}) {digits.exchange_code}-"
        #                 f"{digits.line_number}")
        # print(phone_digit)
    return

def main(path):
    """Read data from path and print results.
    
    Args:
        path (str): path to a text file. Each line in the file should consist of
            a name, a tab character, and a phone number.
    
    Side effects:
        Writes to stdout.
    """
    for name, number in read_numbers(path):
        print(f"{number}\t{name}")


def parse_args(arglist):
    """Parse command-line arguments.
    
    Expects one mandatory command-line argument: a path to a text file where
    each line consists of a name, a tab character, and a phone number.
    
    Args:
        arglist (list of str): a list of command-line arguments to parse.
        
    Returns:
        argparse.Namespace: a namespace object with a file attribute whose value
        is a path to a text file as described above.
    """
    parser = ArgumentParser()
    parser.add_argument("file", help="file of names and numbers")
    return parser.parse_args(arglist)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.file)
