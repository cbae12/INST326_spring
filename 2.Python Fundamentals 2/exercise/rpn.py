from argparse import ArgumentParser
import sys

def evaluate(post_e):
    """ Evaluate a given postfix expression and returns the result of the 
        expression.

        Expect one mandatory argument (a given postfix expression as a string)

        Args:
            post_e(str): string argument given from a line in the file 
            postfix_expressions.txt
        
        Returns:
            ans(float): a float type value that is the result found 
            from the given postfix expression.
    """
    new = list()
    num = list()
    res = list()
    ans = 0
    if isinstance(post_e, int):
        new.append(str(post_e))
        return post_e
    elif isinstance(post_e, float):
        new.append(str(post_e))
        return post_e
    else:
        new_var = post_e.strip()
        new = new_var.split(" ")
        for exp in new:
            if exp.isnumeric():
                num.append(float(exp))
            if not exp.isnumeric() and num != []:
                first = num.pop(0)
                second = num.pop(0)
                if exp == "+":
                    ans =+ first + second
                if exp == "-":
                    ans =+ first - second
                if exp == "*":
                    ans =+ first * second
                if exp == "/":
                    ans =+ first / second
                num.insert(0, ans)
    return ans

def main(file_name):
    """ Defines main function where a given file will be redefined to evalute
        postfix expressions in each line.

        Expect one mandatory argument (a file containing postfix expressions)

        Args:
            file_name(list of str): arguments that contain postfix expressions
            that need to be separated into each expression and to be evaluted,
            using evaluate(post_e).
        
        Returns:
            list of str: arguments that are printed in the format of "postfix
            expression" = "ans" in a single line as a string per expression,
            discovered using evaluate(post_e) function.
    """
    folder = open(file_name, "r")
    for line in folder:
        new_line = line.strip()
        ans = evaluate(new_line)
        print(f"{new_line} = {ans}")
        folder.close
    
def parse_args(arglist):
    """ Process command line arguments.
    
    Expect one mandatory argument (a file containing postfix expressions).
    
    Args:
        arglist (list of str): arguments from the command line.
    
    Returns:
        namespace: the parsed arguments, as a namespace.
    """
    parser = ArgumentParser()
    parser.add_argument("file", help="file containing reverse polish notation")
    args = parser.parse_args(arglist)
    return args


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.file)