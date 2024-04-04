# PythonStrategy.py
from modules.Strategy.LanguageStrategy import LanguageStrategy

class PythonStrategy(LanguageStrategy):
    def function_definition(self, name, params, body):
        body_str = "\n    ".join(body.splitlines())
        return f"def {name}({params}):\n    {body_str}\n"

    def function_call(self, name, args):
        arg_code = ", ".join(args)
        return f"{name}({arg_code})\n"
    
    def for_loop(self, variable, iterable, body):
        body_indent = "\n".join(["    " + line for line in body.splitlines()])
        return f"for {variable} in {iterable}:\n{body_indent}\n"
    
    def while_loop(self, condition, body):
        body_indent = "\n".join(["    " + line for line in body.splitlines()])
        return f"while {condition}:\n{body_indent}\n"
    

    def if_statement(self, if_condition, if_body):
        if_body_indent = "\n".join(["    " + line for line in if_body.splitlines()])
        result = f"if {if_condition}:\n{if_body_indent}\n"
        
        return result
    
    def elif_statement(self, elif_condition, elif_body):
        elif_condition_indent = "\n".join([line for line in elif_condition.splitlines()])
        elif_body_indent = "\n".join(["    " + line for line in elif_body.splitlines()])

        return f"elif {elif_condition_indent}:\n{elif_body_indent}\n"

    def else_statement(self, else_body):
        else_body_indent = "\n".join(["    " + line for line in else_body.splitlines()])
        result = f"else:\n{else_body_indent}\n"
        
        return result
                       

    def variable_declaration(self, name, value=None):
        if value is None:
            return f"{name} = None\n"
        else:
            return f"{name} = {value}\n"    

    
    def return_statement(self, value):
        return f"return {value}\n"
    
    def array_initialization(self, values):
        value_code = ", ".join(values)
        return f"[{value_code}]"