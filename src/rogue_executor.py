from RogueLangParser import RogueLangParser
from RogueLangVisitor import RogueLangVisitor

class RogueExecutor(RogueLangVisitor):
    def __init__(self):
        super().__init__()
        self.variables = {}  # For storing variables
        self.functions = {}  # For storing functions

    def visitProg(self, ctx):
        return self.visitChildren(ctx)

    # Override methods from RogueLangVisitor as needed
    def visitPrintStat(self, ctx):
        # Handling a print statement
        text = self.visit(ctx.expr())
        print(text)

    def visitVarDecl(self, ctx):
        # Handling variable declaration
        name = ctx.ID().getText()
        if ctx.arrayInit() :
            value = self.visitArrayInit(ctx.arrayInit())
        elif ctx.expr(): 
            value = self.visit(ctx.expr())  # Evaluate the expression on the right-hand side
        else:
            value = None
        self.variables[name] = value
    
    def visitDataType(self, ctx):
        pass
 
    def visitIfStat(self, ctx):
        condition = self.visit(ctx.expr())
        if condition:
            self.visit(ctx.stat(0))
        elif ctx.stat(1):
            self.visit(ctx.stat(1))

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
            self.visit(ctx.stat())
        
    def visitFunctionDecl(self, ctx):
        name = ctx.ID().getText()
        # Collect parameter names
        params = [param.ID().getText() for param in ctx.params().param()]
        # Store the function with its name, parameters, and body for later use
        self.functions[name] = {"params": params, "body": ctx.stat()}

    
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
            result = self.visit(body)
            
            # Restore the previous variables state
            self.variables = variables_backup
            
            return result
        else:
            raise Exception(f"Function '{name}' is not defined.")
        

    def visitArrayInit(self,ctx):
        return[self.visit(expr) for expr in ctx.expr()]

    def visitExpr(self, ctx):
        
        #base case for integer literals
        if ctx.INT():
            return int(ctx.INT().getText())

        # Part of visitExpr method for handling ID tokens
        elif ctx.ID():
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
        
        elif ctx.DOUBLE():
            return float(ctx.DOUBLE().getText())
        
        #base case for date literals
        elif ctx.DATE():
            return ctx.DATE().getText()
        
        #base case for time literals
        elif ctx.TIME():
            return ctx.TIME().getText()
        
        #the remix
        elif ctx.DATETIME():
            return ctx.DATETIME().getText()
        
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
        
        # arithmetic expression handlers:
        else:
            if ctx.expr(0) is not None and ctx.expr(1) is not None:
                left = self.visit(ctx.expr(0))
                right = self.visit(ctx.expr(1))
                if ctx.op is not None:
                    if ctx.op.type == RogueLangParser.PLUS: 
                        return left + right
                    elif ctx.op.type == RogueLangParser.MINUS:
                        return left - right
                    elif ctx.op.type == RogueLangParser.MULT:
                        return left * right
                    elif ctx.op.type == RogueLangParser.DIV:
                        if right != 0:
                            return left / right
                        else:
                            raise Exception("Division by 0")
            else:
                # Handle cases where the expression doesn't lead to a binary operation
                # This might involve handling unary operations or simply returning the result of a single child expression
                # Example:
                if ctx.expr(0) is not None:
                    return self.visit(ctx.expr(0))
                # Add more cases here as needed based on your grammar and possible expression structures
