# CS2006 W07 Practical - Classes and Iterators in Python

## Description:
### This project is an implementation of a unique operation of mathematical expressions. The intricate Integer class has been represented in this implementation. Defining new integers, printing those integers as well as multiplying Intricate Integers has been implemented. There is also a new type of Intricate Integer, which only requires a z range value and alpha. Then using an iterator, the program is able to start at a default value of zero and increase the next Intricate Integer with respect to the previous.

## Instructions:
##### Run via Python Interpreter:
1. Open the terminal and cd into the src of the project directory
2. Type 'python3' into the command line
3. Type 'from IntricateInteger import *' into the python interpreter to load all the functions
4. Type 'from Testing import *' into the pyhton interpreter to load all the testing functions
5. Begin working with Intricate Integers (See Examples Below for Suggestions)

##### Run Automated Tests via Command Line
1. Open the terminal and cd into the src of the project directory
2. Type 'python3 Testing.py'
3. Watch as all the automated testing for the implementation run

## Examples to Copy & Paste:
**1. From the Specification**<br>
&nbsp;&nbsp;&nbsp;&nbsp;>> x=IntricateInteger(3,7,2)<br>
&nbsp;&nbsp;&nbsp;&nbsp;>> y=IntricateInteger(5,7,2)<br>
&nbsp;&nbsp;&nbsp;&nbsp;>> print(x)<br>
&nbsp;&nbsp;&nbsp;&nbsp;>> print(y)<br>
&nbsp;&nbsp;&nbsp;&nbsp;>> print(x*x)<br>
&nbsp;&nbsp;&nbsp;&nbsp;>> print(x*y)

**2. Unit Tests to Run**<br>
&nbsp;&nbsp;&nbsp;&nbsp;>> peculiar_test()<br>
&nbsp;&nbsp;&nbsp;&nbsp;>> peculiar_iterative_test()<br>
&nbsp;&nbsp;&nbsp;&nbsp;>> roots_test()<br>
&nbsp;&nbsp;&nbsp;&nbsp;>> minimum_roots_test()

## How to Run Coverage Test Check:
1. Open the terminal and cd into the src of the project directory
2. Type 'python3 -m pip install coverage' to install coverage
3. Type 'python3 -m coverage run -m unittest Testing.py' to generate a report
4. Type 'coverage report -m' to view what percentage of the code is covered with tests
5. **Output for this coverage is below:**<br>
&nbsp;&nbsp;&nbsp;&nbsp;Name&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Stmts&nbsp;&nbsp;&nbsp;Miss&nbsp;&nbsp;Cover&nbsp;&nbsp;&nbsp;Missing<br>
&nbsp;&nbsp;&nbsp;&nbsp;---------------------------------------------------------------<br>
&nbsp;&nbsp;&nbsp;&nbsp;IntricateInteger.py&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;66&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3&nbsp;&nbsp;&nbsp;&nbsp;95%&nbsp;&nbsp;&nbsp;45,&nbsp;96,&nbsp;101<br>
&nbsp;&nbsp;&nbsp;&nbsp;IntricateIntegers.py&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;20&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1&nbsp;&nbsp;&nbsp;&nbsp;95%&nbsp;&nbsp;&nbsp;18<br>
&nbsp;&nbsp;&nbsp;&nbsp;Testing.py&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;126&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;6&nbsp;&nbsp;&nbsp;&nbsp;95%&nbsp;&nbsp;&nbsp;20,&nbsp;35-37, 39,&nbsp;213<br>
&nbsp;&nbsp;&nbsp;&nbsp;---------------------------------------------------------------<br>
&nbsp;&nbsp;&nbsp;&nbsp;TOTAL&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;212&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;10&nbsp;&nbsp;&nbsp;&nbsp;95%<br>