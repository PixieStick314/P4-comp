## Table of Contents
- [1: Setting up the language ](#step-1-setting-up-the-language)
- [2: Using the language](#step-2-using-the-language)
- [3: Running the interpreter](#step-3-running-the-interpreter)
- [4: Usage documentation](#step-4-usage-documentation)
    - [4.1: Datatypes](#step-4-1-datatypes)
    - [4.2: Basic operations](#step-4-1-datatypes)
    - [4.3: Conditionals](#step-4-1-datatypes)



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

- [Step 2: Define output]
    Second step is to define the data you want outputted in .JSON formatting.

    In the example above 'let x = [3, 2, 1]' is defined. Meaning that if no procedure is done on 'x', the output would be:
        {"map": {"data": {"x": [3, 2, 1]}}}
    Here we can see, that x is defined as a list with the integers: '3, 2, 1', just as we assigned 'x' to be.

- [Step 3: Using procedures]
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
Here you will find all of the tools the language includes. You will also find small examples of the syntax that needs to be used, in order to get a fully optimal output.
##   4.1: Dataypes
    To define a datatype simply type
        let (YourVariableName) = (YourData)
    Based on what you assign to the variable, it will be defined to that datatype.

    Integers:
        let my_int = 1

    Floats:
        let my_float = 1.2

    Booleans:
        let my_bool = True 
        let my_bool = False 
    
    Strings:
        let my_string = "Hello world!"

    Lists:
    2d arrays can also be assigned
        let my_list = [1, 2, 3]
        let my_matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]

        Manipulations:
            Add element:
                my_list += 4 // This will add 4 to the list = [1, 2, 3, 4]
                my_matrix += 10 // This will add 4 to the list = 
                [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9], 10
                ]

            Pop:
                pop(my_list) // This will remove the latest element from the list = [1, 2]
                pop(my_matrix) // This will remove the latest row from the list = 
                [
                [1, 2, 3],
                [4, 5, 6],
                ]

            Length of a list:
                z = len(my_list) // z will be set to 3
                z = len(my_matrix) // z will be set to 3

        The values can then be accessed:
        Arrays:
        my_list[0] == 1, 
        my_list[1] == 2, 
        my_list[2] == 3

        Matrix: 
        my_matrix[0][0] == 1,
        my_matrix[0][1] == 2,
        my_matrix[1][0] == 4
        and so on..
    
    Layers:
        Can only be initialized inside of a map declaration.
        Fixed-size arrays that represent individual layers of a map.

        Map (10, 10) map {
            layer terrain = 0
        }

        This will create a 10x10 2d array, that is filled with 0. You can then use terrain as a standard 2d array.

    Hashmaps:
        let my_hash = {"a": 1, "b": 2}

        Reassign:
        my_hash["a"] = 10

        The values can then be accessed:
        my_hash["a"] == 1
        my_hash["b"] == 2

    Structs:
        let my_struct = Struct{
            my_array = [1, 2, 3]
            my_int = 10
        }

        Reassign:
        my_struct.my_int = 20

        The values can then be accessed:
        my_struct.my_array[0] == 1
        my_struct.my_array[1] == 2
        my_struct.my_array[2] == 3
        my_struct.my_int = 10



##   4.2: Basic operations
    Single line comments:
    //Hello, i am a single line comment

    Arithmetic operations:
    Arithmetic operations work with both integers and floats. 
    The '+' operator works for strings, meaning you can combine to strings into one.

        Plus:
        x = 1 + 1
        or
        x = 1
        x += 1

        Minus:
        x = 1 - 1
        or
        x = 1
        x -= 1
        
        Multiplication:
        x = 1 * 1

        Modulus:
        x = 1 % 1

    Comparison Operators:
    Comparison operations work with both integers and floats.

        Greater than:
        10 > 1

        Greater than or equal to:
        10 >= 1

        Less than:
        10 < 1

        Less than or equal to:
        10 <= 1

        Equal to: 
        10 == 1

        Not equal to:
        10 != 1

    Logic operators:
    Logic operations work with both integers and floats.

        And:
        x < 5 and x < 10
        Returns True if both statements are true 

        Or:
        x < 5 or x < 4
        Returns True if one of the statements is true

        Not:
        not 10 > 1
        Returns False if the result is true
    
    Random:
        my_random = random in 2..5 // A random value between 2 and 5
        or
        x = [1, 2, 3]
        my_random = random in x // A random value between 1 and 3

##   4.3: Conditionals
    If statements:
        if(10 > 1) {
            print("The if statement")
        } elif (10 != 1) {
            print("The elif statement")
        } else {
            print("The else statement")
        }

    For loops:
        for i in 0..10 {
            print("The for loop")
        }

        or

        x =[1, 2, 3, 4, 5]

        for i in x {
            print("The for loop with list")
        }

    While loops:
        while(True) {
            print("The while loop")
        }

##   4.4: Function declaration and calling
    Functions can be defined and return values are also included in the language

    Functions:
        def myFunction(x, y) {
            x += 20
            y += 20
            x = x + y
            return x
        }
        x = myFunction(1, 2) 

##  4.5: Algorithms
    White noise:
        let my_matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        my_matrix = WhiteNoise(my_matrix, 0..1) // This will change all integers in my_matrix to either a '0' or '1'

    bsp:
        Map (64, 64) map {
            layer terrain = 0
                procedure {
                    let tree = bsp(terrain, 4)
                }
        }
        Tree is assigned with the function and 2 parameters are passed.
        The first paramater can either be a layer or a 2d list, and will be the matrix that gets partioned.
        The second parameter is how many ties the space is going to be partitioned. The slice direction is random and can either be vertical or horizontal.
        The output is a struct that functions like a node tree.

    astar: 
        let path = astar(start, goal, matrix)

        astar is used to find the shortest path. It takes three parameters:
            Start: The starting coordinate of the path.
            Ending: The ending coordinate of the ending.
            Matrix: The 2d array that the path is located on.
        astar returns a list of coordinates. The coordinates show the shortest path.










    
    

