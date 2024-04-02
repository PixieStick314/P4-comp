#   RogueVisitor.py
from tokenize import Double
from grammar_files.generated.RogueLangParser import RogueLangParser
from grammar_files.generated.RogueLangVisitor import RogueLangVisitor

from modules.Algorithms.bsp_algorithm import bsp_partition

class RogueVisitor(RogueLangVisitor):
    def __init__(self, strategy):
        super().__init__()
        self.strategy = strategy
        self.output_buffer = "" # for storing the shit to print
        self.variables = {}  # For storing variables
        self.functions = {}  # For storing functions

    def visitProg(self, ctx):
        result = self.visitChildren(ctx)
        return result

    def visitPrintStat(self, ctx):
        expr_code = ctx.expr().getText()
        self.output_buffer += self.strategy.function_call("print", [expr_code])  
        

    def visitVarDecl(self, ctx):
        name = ctx.ID().getText()
        value = ctx.expr().getText()
        var_decl_code = self.strategy.variable_declaration(name, value)
        self.output_buffer += var_decl_code
    
    def visitDataType(self, ctx):
        pass
 
    def visitIfStat(self, ctx):
        if_expr_code = "if" + "(" + ctx.ifExpr().getText() + ")" + ":" + "\n"
        if_block = ctx.ifBlock()
        for stat in if_block.stat():
            if_expr_code += "   " + stat.getText() + "\n"

        if ctx.ELIF():
            if_expr_code += "elif" + "(" + ctx.ifExpr().getText() + ")" + ":" + "\n"
            if_block = ctx.ifBlock()
            for stat in if_block.stat():
                if_expr_code += "   " + stat.getText() + "\n"
        
        if ctx.ELSE():
            if_expr_code += "else" + ":" + "\n"
            else_block = ctx.elseBlock()
            for stat in else_block.stat():
                if_expr_code += "   " + stat.getText() + "\n"
        #self.output_buffer += if_expr_code
        self.output_buffer += if_expr_code 


    def visitForLoop(self, ctx):
        self.visit(ctx.varDecl())
        while self.visit(ctx.expr(0)):
            self.visit(ctx.stat())
            self.visit(ctx.expr(1))

    def visitForeachLoop(self, ctx):
        name = ctx.varDecl().ID().getText()
        array = self.visit(ctx.expr())
        originalVal = self.variables.get(name, None)
        for item in array:
            self.variables[name] = item
            for stat in ctx.stat():
                self.visit(stat)
        if originalVal is not None:
            self.variables[name] = originalVal
        else:
            del self.variables[name]


    def visitWhileLoop(self, ctx):
        while(self.visit(ctx.expr())):
            stats = ctx.stat()
            for stat in stats:
                self.visit(stat)

    def visitFunctionDecl(self, ctx):
        name = ctx.ID().getText()
        params = [param.ID().getText() for param in ctx.params().param()]
        body_code = self.visit(ctx.body())
        func_decl_code = self.strategy.function_definition(name, params, body_code)
        self.output_buffer += func_decl_code + "\n"


    def visitFunctionCall(self, ctx):
        name = ctx.ID().getText()
        if name in self.functions:
            # Retrieve function definition
            function = self.functions[name]
            params = function["params"]
            body = function["body"]
            
            # Evaluate arguments
            args = [self.visit(arg) for arg in ctx.args().expr()]
            
            # Backup current variables state
            variables_backup = self.variables.copy()
            
            # Map arguments to parameters
            for param_name, arg_value in zip(params, args):
                self.variables[param_name] = arg_value
                
            # Execute the function body
            result = None
            for statement in body:
                if self.visit(statement) == ctx.RETURN():
                    print(ctx.RETURN)
                result = self.visit(statement)
            
            # Restore the previous variables state
            self.variables = variables_backup
            
            return result
        else:
            raise Exception(f"Function '{name}' is not defined.")
        

    def visitArrayInit(self,ctx):
        return[self.visit(expr) for expr in ctx.expr()]
        

    def visitExpr(self, ctx):
        # Part of visitExpr method for handling ID tokens
        if ctx.ID():
            var_name = ctx.ID().getText()
            if var_name in self.variables:
                return self.variables[var_name]
            else:
                # Handle undefined variable error or return a default value
                print(f"Variable '{var_name}' is not defined.")
                return None

        #base case for string literals
        elif ctx.STRING():
            return ctx.STRING().getText()[1:-1]
        elif ctx.TRUE() or ctx.getText() == 'true':
            return True
        elif ctx.FALSE() or ctx.getText() == 'false':
            return False
        elif ctx.NUMBER():
            return float(ctx.NUMBER().getText())
        
        #base case for array element literals
        elif ctx.getChildCount() == 3 and ctx.getChild(1).getText() == '[':
            arrayName = self.visit(ctx.getChild(0))
            index = self.visit(ctx.getChild(2))
            return self.variables[arrayName][index]

        #handling function calls within expressions
        elif isinstance(ctx,RogueLangParser.FunctionCallContext):
            if ctx.ID().getText() == "length":
                array = self.visit(ctx.args().expr(0))
                return len(array)
            else:
                return self.visitFunctionCall(ctx)
            
        #handling logical operators
        elif ctx.NOT():
            if ctx.expr(0) is not None:
                left = ctx.expr(0).getText()
                self.output_buffer += "not " + left + "\n"

        elif ctx.AND() or ctx.OR():
            if ctx.expr(0) and ctx.expr(1) is not None:
                left = ctx.expr(0).getText()
                right = ctx.expr(1).getText()
                if ctx.op is not None:
                    if ctx.op.type == RogueLangParser.AND: 
                        self.output_buffer += left + " and " + right + "\n" 
                    elif ctx.op.type == RogueLangParser.OR:
                        self.output_buffer += left + " or " + right + "\n" 
                    
    
           
        
        #handling comparison operators
        elif ctx.GT() or ctx.GTE() or ctx.LT() or ctx.LTE() or ctx.EQ() or ctx.NEQ() :
            if ctx.expr(0) and ctx.expr(1) is not None:
                left = ctx.expr(0).getText()
                right = ctx.expr(1).getText()
                if ctx.op is not None:
                    if ctx.op.type == RogueLangParser.GT: 
                        self.output_buffer += left + " > " + right + "\n" 
                    elif ctx.op.type == RogueLangParser.GTE:
                        self.output_buffer += left + " >= " + right + "\n" 
                    elif ctx.op.type == RogueLangParser.LT:
                        self.output_buffer += left + " < " + right + "\n" 
                    elif ctx.op.type == RogueLangParser.LTE:
                        self.output_buffer += left + " <= " + right + "\n" 
                    elif ctx.op.type == RogueLangParser.EQ:
                        self.output_buffer += left + " == " + right + "\n" 
                    elif ctx.op.type == RogueLangParser.NEQ:
                        self.output_buffer += left + " != " + right + "\n" 
            else:
                # Handle cases where the expression doesn't lead to a binary operation
                # This might involve handling unary operations or simply returning the result of a single child expression
                # Example:
                if ctx.expr(0) is not None:
                    return self.visit(ctx.expr(0))

        
        # arithmetic expression handlers:
        else:
            if ctx.expr(0) is not None and ctx.expr(1) is not None:
                left = ctx.expr(0).getText()
                right = ctx.expr(1).getText()
                if ctx.op is not None:
                    if ctx.op.type == RogueLangParser.PLUS:  
                        self.output_buffer += left + " + " + right + "\n" 

                    elif ctx.op.type == RogueLangParser.MINUS:
                        self.output_buffer += left + " - " + right + "\n"

                    elif ctx.op.type == RogueLangParser.MULT:
                        self.output_buffer += left + " * " + right + "\n"

                    elif ctx.op.type == RogueLangParser.MOD:
                        self.output_buffer += left + " % " + right + "\n"

                    elif ctx.op.type == RogueLangParser.DIV:
                        if right != 0:
                            self.output_buffer += left + " / " + right + "\n"
                        else:
                            raise Exception("Division by 0")
            else:
                # Handle cases where the expression doesn't lead to a binary operation
                # This might involve handling unary operations or simply returning the result of a single child expression
                # Example:
                if ctx.expr(0) is not None:
                    return self.visit(ctx.expr(0))
                # Add more cases here as needed based on your grammar and possible expression structures
