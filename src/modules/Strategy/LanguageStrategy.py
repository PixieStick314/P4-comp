# LanguageStrategy.py
class LanguageStrategy:
    def function_definition(self, name, params, body):
        """
        Generates code for a function definition.
        :param name: Name of the function
        :param params: List of parameter names
        :param body: Function body code as a string
        """
        raise NotImplementedError # This is actually fucking correct. WTF why is it called this???

    def function_call(self, name, args):
        """
        Generates code for a function call.
        :param name: Name of the function
        :param args: List of arguments
        """
        raise NotImplementedError

    def for_loop(self, variable, iterable, body):
        """
        Generates code for a for loop.
        :param variable: Loop variable
        :param iterable: Iterable object
        :param body: Loop body code as a string
        """
        raise NotImplementedError

    def while_loop(self, condition, body):
        """
        Generates code for a while loop.
        :param condition: Loop condition
        :param body: Loop body code as a string
        """
        raise NotImplementedError

    def if_statement(self, condition, body, elif_condition=None, elif_body=None, else_body=None):
        """
        Generates code for an if statement.
        :param condition: If condition
        :param body: If body code as a string
        :param elif_condition: Elif condition (optional)
        :param elif_body: Elif body code as a string (optional)
        :param else_body: Else body code as a string (optional)
        """
        raise NotImplementedError

    def variable_declaration(self, name, value=None):
        """
        Generates code for a variable declaration.
        :param name: Variable name
        :param value: Initial value of the variable (optional)
        """
        raise NotImplementedError

    def return_statement(self, value):
        """
        Generates code for a return statement.
        :param value: Value to return
        """
        raise NotImplementedError

    def array_initialization(self, values):
        """
        Generates code for array initialization.
        :param values: List of values to initialize the array with
        """
        raise NotImplementedError
