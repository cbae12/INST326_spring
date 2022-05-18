"""Perform fixed-rate mortgage calculations."""

from argparse import ArgumentParser
import math
import sys


# replace this comment with your implementation of get_min_payment(),
# interest_due(), remaining_payments(), and main()
def get_min_payment(mortgage_amount, annual_interest_rate, y = 30, n = 12):
    """This function calculates minimum payment required for the given parameter
    values.
    
    Args:
        mortgage_amount (float): total amount of a mortgage
        annual_interest_rate (float): the annual interest rate as a value
            between 0 and 1 (e.g., 0.035 == 3.5%)
        -y / --years (int): the term of the mortgage in years (default is 30)
        -n / --num_annual_payments (int): the number of annual payments
            (default is 12)
    
    Returns:
        total (int): minimum mortgage payment
    """
    total_pay = y * n
    interest_rate = annual_interest_rate/n
    minimum_pay = ((mortgage_amount * interest_rate) * 
    ((1 + interest_rate) ** total_pay))/(((1 + interest_rate) ** total_pay) - 1)
    end_min = math.ceil(minimum_pay)
    return end_min

def interest_due(balance, annual_interest_rate, n = 12):
    """This function calculates interest due per payment, based on the given
    parameter values for mortgage_amount, annual_interest_rate, and
    num_annual_payments.
    
    Args:
        balance (float): balance of the mortgage
        annual_interest_rate (float): the annual interest rate as a value
            between 0 and 1 (e.g., 0.035 == 3.5%)
        -n / --num_annual_payments (int): the number of annual payments
            (default is 12)
    
    Returns:
        interest (float): total interest rate for the payment that was made
    """
    interest_rate = annual_interest_rate/n
    interest = balance * interest_rate
    return interest

def remaining_payments(balance, annual_interest_rate, p, n = 12):
    """This function calculates remaining payments from the given parameters,
    so that users can understand how many payments are remaining after
    deducting interest (calculated using interest_due()) from each payment.
    
    Args:
        balance (float): balance of the mortgage
        annual_interest_rate (float): the annual interest rate as a value
            between 0 and 1 (e.g., 0.035 == 3.5%)
        -n / --num_annual_payments (int): the number of annual payments
            (default is 12)
        -p / --target_payment (float): the amount the user wants to pay per
            payment (default is the minimum payment)
    
    Returns:
        count (int): number of payments remaining
    """
    count = 0
    while balance > 0:
        new_pay = p - interest_due(balance, annual_interest_rate, n)
        balance = balance - new_pay
        count += 1
    return count

def main(mortgage_amount, annual_interest_rate, y = 30, n = 12, p = None):
    """Main function first returns minimum payment required using
    get_min_payment() by the given parameter values and print the minimum.
    The function then assigns minimum payment value to be target_payment value
    when it is not assigned and returns a message when it is less than minimum.
    Afterwards, returns how many minimum payments are required to pay off the
    mortgage.
    
    Args:
        mortgage_amount (float): total amount of a mortgage
        annual_interest_rate (float): the annual interest rate as a value
            between 0 and 1 (e.g., 0.035 == 3.5%)
        -y / --years (int): the term of the mortgage in years (default is 30)
        -n / --num_annual_payments (int): the number of annual payments
            (default is 12)
        -p / --target_payment (float): the amount the user wants to pay per
            payment (default is the minimum payment)
    
    Returns:
        Printed messages that display what the minimum payment is, whether or
        not the target_payment meets it or not, and how many payments are left
        until mortgage is paid off in full.
    """
    minimum_pay = get_min_payment(mortgage_amount, annual_interest_rate, 30, 12)
    print(f'Minimum Payment: ${minimum_pay}')
    if p == None:
        p = minimum_pay
    if p < minimum_pay:
        print("Target payment is less than minimum payment for this mortgage")
    remaining = remaining_payments(mortgage_amount, annual_interest_rate, p, n)
    print("HI!")
    print(f"If you make payments of ${p}, you will pay off the mortgage " 
          f"in {remaining} payments.")

def parse_args(arglist):
    """Parse and validate command-line arguments.
    
    This function expects the following required arguments, in this order:
    
        mortgage_amount (float): total amount of a mortgage
        annual_interest_rate (float): the annual interest rate as a value
            between 0 and 1 (e.g., 0.035 == 3.5%)
        
    This function also allows the following optional arguments:
    
        -y / --years (int): the term of the mortgage in years (default is 30)
        -n / --num_annual_payments (int): the number of annual payments
            (default is 12)
        -p / --target_payment (float): the amount the user wants to pay per
            payment (default is the minimum payment)
    
    Args:
        arglist (list of str): list of command-line arguments.
    
    Returns:
        namespace: the parsed arguments (see argparse documentation for
        more information)
    
    Raises:
        ValueError: encountered an invalid argument.
    """
    # set up argument parser
    parser = ArgumentParser()
    parser.add_argument("mortgage_amount", type=float,
                        help="the total amount of the mortgage")
    parser.add_argument("annual_interest_rate", type=float,
                        help="the annual interest rate, as a float"
                             " between 0 and 1")
    parser.add_argument("-y", "--years", type=int, default=30,
                        help="the term of the mortgage in years (default: 30)")
    parser.add_argument("-n", "--num_annual_payments", type=int, default=12,
                        help="the number of payments per year (default: 12)")
    parser.add_argument("-p", "--target_payment", type=float,
                        help="the amount you want to pay per payment"
                        " (default: the minimum payment)")
    # parse and validate arguments
    args = parser.parse_args()
    if args.mortgage_amount < 0:
        raise ValueError("mortgage amount must be positive")
    if not 0 <= args.annual_interest_rate <= 1:
        raise ValueError("annual interest rate must be between 0 and 1")
    if args.years < 1:
        raise ValueError("years must be positive")
    if args.num_annual_payments < 0:
        raise ValueError("number of payments per year must be positive")
    if args.target_payment and args.target_payment < 0:
        raise ValueError("target payment must be positive")
    
    return args


if __name__ == "__main__":
    try:
        args = parse_args(sys.argv[1:])
    except ValueError as e:
        sys.exit(str(e))
    main(args.mortgage_amount, args.annual_interest_rate, args.years,
         args.num_annual_payments, args.target_payment)
