## Table of Contents
- [1: Setting up the language ](#step-1-setting-up-the-language)
- [2: Using the language](#step-2-using-the-language)
- [3: Running the interpreter](#step-3-running-the-interpreter)
- [4: Usage documentation](#step-4-usage-documentation)


#   1: Setting up the language
In order for you to use Dungeon, you first need to install the required dependencies.
- [1: Python]
    You need Python to be able to use dungeon. Visit the official Python website at https://python.org. You'll find the latest Python version available for download, with documentation on how to properly install. You will need at least Python 3.10.

- [2: Pip]
    If you installed Python from source, with an installer from python.org, or via Homebrew you should already have pip. If you’re on Linux and installed using your OS package manager, you may have to install pip separately. See, https://packaging.python.org/en/latest/guides/installing-using-linux-tools/

- [3: Requirements]
    To download and install the rest of the dependencies, simply type
        pip install -r requirements.txt
    into your terminal. This is assuming that you have correctly downloaded and installed Python and pip.

#   2: Using the language
Firstly, create a new .dngn file. This file can be created where you want, but you need to be able acces the file path of the file. 

To write and use the language there are 3 steps:
    Map(10, 10) map {
        let x = [3, 2, 1]
        procedure {
            x[0] = 1
        }
    }
- [Step 1: Define the map] (#step-1-Define-the-map)
    First step is to define the map. This is done by creating a map class with and giving the map a name.

    In the example above a Map is created with the ID 'map' and (EXPLAIN PARAMETERS)

- [Step 2: Regenerate Parser and Lexer]
    Second step is to define the data you want outputted in .JSON formatting.

    In the example above 'let x = [3, 2, 1]' is defined. Meaning that if no procedure is done on 'x', the output would be:
        {"map": {"data": {"x": [3, 2, 1]}}}
    Here we can see, that x is defined as a list with the integers: '3, 2, 1', just as we assigned 'x' to be.

- [Step 3: Update the Visitor Class]
    To manipulate the previously assigned datatypes, you use commands inside a 'procedure{}'.

    In the example above, we reassign the first integer in the list to be '1' instead of '3'. This would then output:
        {"map": {"data": {"x": [1, 2, 1]}}}
    Here we can see that that 'x[0]' has been assigned to be '1' instead of '3'

#   3: Running the interpreter
When you have written your program, you then have to run the interpreter from your terminal. Simply type:
    python .\executor.py
This is assuming that you have not changed the location of the executor.py file.
The system will then asks you for the filepath of the .dngn file:
    'Enter the input file path:'
If your code is functional, you should be able to paste your file path and get your output as a string in the terminal.

Example:
//test.dngn
 Map(10, 10) map {
        let x = [3, 2, 1]
        procedure {
            x[0] = 1
        }
    }

USER:
PS C:\Users\Lenovo\Documents\GitHub\P4-comp> python .\executor.py

SYSTEM:
Enter the input file path:

USER:
C:\Users\Lenovo\Documents\GitHub\P4-comp\tests\examples\test.dngn

SYSTEM:
{"map": {"data": {"x": [1, 2, 1]}}}

#   4: Usage documenatation
[Datatypes]
    To define a datatype simply type
        let (YourVariableName) = (YourData)
    Based on what you assign to the variable, it will be defined to that datatype.

    Integers:
        let x = 1

    Floats:
        let x = 1.2
    
    Strings:
        let x = "Hello world!"

    Arrays and matrix:
        let x = [1, 2, 3]
        let x = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
    
    

    
    
