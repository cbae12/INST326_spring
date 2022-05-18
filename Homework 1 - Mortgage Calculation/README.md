# Homework: Mortgage Calculator
<hr/>

## Table of Contents
[Instructions](#instructions)<br/>
&emsp;[get_min_payment()](#getminpayment)<br/>
&emsp;[interest_due()](#interestdue)<br/>
&emsp;[remaining_payments()](#remainingpayments)<br/>
&emsp;[main()](#main)<br/>
[Running your program](#running-your-program)<br/>
[Testing](#testing)<br/>
<hr/>

## Instructions
For this homework you will write a script to do some useful calculations for fixed-rate mortgages. Use the provided template (*mortgage.py*) and make sure your file is called *mortgage.py* (if you end up downloading the template more than once, take extra care that the file you submit is not named, for example, mortgage (1).py). At a minimum, your script should contain the functions *get_min_payment()*, *interest_due()*, *remaining_payments()*, and *main()*, each of which is described below. Be sure to include a docstring in each function.
<hr/>

### get_min_payment()
**Parameters**

- The total amount of the mortgage (called the *principal*; you can assume this is a positive number)

- The annual interest rate (you can assume this is a float between 0 and 1; for example, an interest rate of 3.5% would be expressed as 0.035)

- The term of the mortgage in years (you can assume this is a positive integer; assign this parameter a default value of 30)

- The number of payments per year (you can assume this is a positive integer; assign this parameter a default value of 12)

**Functionality**

1. Compute the minimum mortgage payment A using the formula **A=[Pr(1+r)^n)]/[(1+r)^n−1]** where

    * **P** is the principal amount

    * **r** is the interest rate per payment (the annual interest rate divided by the number of payments per year)

    * **n** is the total number of payments (the term of the mortgage in years × the number of payments per year)

Use *math.ceil()* to raise the minimum payment you calculated in step 1 to the next highest integer; return this integer.

You will need to import math in order to do this. *import* statements belong at the top of your script, right after your script docstring.

**NOTE**<hr/>
This function takes into account only principal and interest, which are typically the two largest components in a mortgage payment. In the real world, mortgage payments often also cover other expenses like property taxes, home insurance, and private mortgage insurance.<hr/>

### interest_due()
**Parameters**

- The balance of the mortgage (the part of the principal that has not been paid back yet; you can assume this is a positive number)

- The annual interest rate (you can assume this is a float between 0 and 1; for example, an interest rate of 3.5% would be expressed as 0.035)

- The number of payments per year (you can assume this is a positive integer; assign this parameter a default value of 12)

**Functionality**

- Compute and return *i*, the amount of interest due in the next payment according to the formula **i=br**, where

    * **b** is the the balance of the mortgage

    * **r** is the interest rate per payment (the annual interest rate divided by the number of payments per year)

### remaining_payments()
**Parameters**

- The balance of the mortgage (the part of the principal that has not been paid back yet; you can assume this is a positive number)

- The annual interest rate (you can assume this is a float between 0 and 1; for example, an interest rate of 3.5% would be expressed as 0.035)

- The target payment (the amount the user wants to pay per payment; you can assume this is a positive number)

- The number of payments per year (you can assume this is a positive integer; assign this parameter a default value of 12)

**Functionality**

Compute and return the number of payments required to pay off the mortgage. We will do this by simulating payments one at a time until the balance of the mortgage reaches zero, assuming fixed payments (in other words, assume that each payment is the same amount of money as the previous one).

**NOTE**<hr/>
A mortgage payment is broken down into two parts: an interest payment, and a part that pays down the balance of the mortgage. The interest payment is calculated as described under *interest_due()*; the rest of the payment goes toward the balance of the mortgage. The percentage of the payment that goes toward interest decreases with every payment because it depends on the balance of the mortgage, which also decreases with every payment.
<hr/>
Here is an algorithm for simulating payments until the mortgage is paid off:

- Initialize a counter with a value of zero; this counter represents the number of payments to be made.

- As long as the balance of the mortgage is positive, do the following:

    * Use the interest_due() function to determine what portion of the next payment will be interest. The total payment minus interest due is the amount that will go toward paying the balance of the principal. Remember, these amounts will change with every payment.

    * Reduce the balance by the part of the payment that goes toward paying the balance.

    * Increase the counter.

- When the balance of the mortgage is no longer positive, the value of the counter is the number of payments required. Return this value.
<hr/>

### main()
**Parameters**

- The total amount of the mortgage (called the principal; you can assume this is a positive number)

- The annual interest rate (you can assume this is a float between 0 and 1; for example, an interest rate of 3.5% would be expressed as 0.035)

- The term of the mortgage in years (you can assume this is a positive integer; assign this parameter a default value of 30)

- The number of payments per year (you can assume this is a positive integer; assign this parameter a default value of 12)

- The user’s target payment (the amount the user wishes to pay per payment; you can assume this is a positive number or None; assign this parameter a default value of None)

    * A value of None indicates that the user wishes to use the minimum payment

**Functionality**

- Compute the minimum payment using the *get_min_payment()* function

- Display the minimum payment to the user

- If the user’s target payment is *None*, set the target payment to the minimum payment

- If the user’s target payment is less than the minimum payment, print a message to the user (e.g., "Your target payment is less than the minimum payment for this mortgage"); otherwise:

    * Use *remaining_payments()* to figure out the total number of payments required (hint: at the beginning of a mortgage, the balance is equal to the total mortgage amount)

    * Display this number to the user (e.g., "If you make payments of $*< target payment >*, you will pay off the mortgage in *< total payments >* payments."; replace the angle brackets with the appropriate values)
<hr/>

## Running your program
Your program is designed to run from the terminal. To run it, open a terminal and ensure you are in the directory where your script is saved.

The program takes two required command-line arguments: a mortgage amount and an interest rate (expressed as a float between 0 and 1). It also allows the following optional arguments: *-y* (the term of the mortgage in years), *-n* (the number of annual payments), and *-p* (the target payment). Below are some examples of how to use the program. The examples assume you are using macOS and your program is called *mortgage.py*. If you are using Windows, replace *python3* with *python*.

**Basic usage**<br/>
&emsp;*python3 mortgage.py 300000 0.03*<br/>
**With one optional parameter**<br/>
&emsp;*python3 mortgage.py 300000 0.03 -y 15*<br/>
**With multiple optional parameters**<br/>
&emsp;*python3 mortgage.py 300000 0.03 -y 15 -p 4000*<br/>
<hr/>

## Testing
You can use the script *test_mortgage.py* to test your solution. Make sure you have Pytest installed (see https://docs.pytest.org/en/latest/getting-started.html#install-pytest) and that your script and *test_mortgage.py* are in the same directory on your computer. Edit line 4 of *test_mortgage.py* so that it contains the name of your script (withou the .py ending).

To use the test script, open a terminal and navigate to the directory containing your script and *test_mortgage.py*. Then type the following at the command prompt:

&emsp;*pytest test_mortgage.py*