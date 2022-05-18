from argparse import ArgumentParser
import re
import sys


# replace this comment with your implementation of the Address class
# and read_addresses() function. Uncomment the __repr__() method below
# and include it in your Address class.

    # def __repr__(self):
    #     """Return a formal representation of the Address object."""
    #     return (
    #         f"address:      {self.address}\n"
    #         f"house number: {self.house_number}\n"
    #         f"street:       {self.street}\n"
    #         f"city:         {self.city}\n"
    #         f"state:        {self.state}\n"
    #         f"zip:          {self.zip}"
    #     )

class Address:
    def __init__(self, line):
        self.address = line
        expr = r""""(?xm)
            ^
            (?P<house_number>\S+)
            \s
            (?P<street_name>[^,]+)
            ,\s
            (?:(?P<city>\w+(?:\s\w+([^A-Z]{,2}))?(?:\s\w+\s\w+([^A-Z]{,2}))?)\s)
            (?P<state>\w+)
            \s
            (?P<zip>\d+)
            $"gm"""
        match1 = re.search("house_number", line)
        match2 = re.search("street_name", line)
        match3 = re.search("city", line)
        match4 = re.search("state", line)
        match5 = re.search("zip", line)
        try:
            if match1 == None:
                raise ValueError("Address string could not be parsed")
            else:
                self.house_number = match1
            if match2 == None:
                raise ValueError("Address string could not be parsed")
            else:
                self.street = match2
            if match3 == None:
                raise ValueError("Address string could not be parsed")
            else:
                self.city = match3
            if match4 == None:
                raise ValueError("Address string could not be parsed")
            else:
                self.state = match4
            if match5 == None:
                raise ValueError("Address string could not be parsed")
            else:
                self.zip = match5
        except ValueError as e:
            print(e)

    def __repr__(self):
        """Return a formal representation of the Address object."""

        return (
            f"address:      {self.address}\n"
            f"house number: {self.house_number}\n"
            f"street:       {self.street}\n"
            f"city:         {self.city}\n"
            f"state:        {self.state}\n"
            f"zip:          {self.zip}"
        )
    
def read_addresses(filepath):
    """Extract address information from a address.txt file.
    
    Args:
        filepath (str): path to address file in text format.
        
    Side effects:
        Modify self.address, self.house_number, self.street,
        self.city, self.state, self.zip"""
    addresses = list()
    with open(filepath, "r", encoding="utf-8") as f:
        line = f.read()
        obj = Address(line)
        print(obj)
        addresses.append([print(a) for a in obj])
        
def parse_args(arglist):
    """ Parse command-line arguments.
    
    Expect one mandatory argument, the path to a file of addresses.
    
    Args:
        arglist (list of str): command-line arguments.
    
    Returns:
        namespace: an object with one attribute, file, containing a string.
    """
    parser = ArgumentParser()
    parser.add_argument("file", help="file containing one address per line")
    return parser.parse_args(arglist)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    for address in read_addresses(args.file):
        # the !r tells the f-string to use the __repr__() method to generate
        # a string version of the address object
        print(f"{address!r}\n")
