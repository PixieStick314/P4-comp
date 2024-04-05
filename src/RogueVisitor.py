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
        return "hii"

    def visitVarDecl(self, ctx):
        name = ctx.ID().getText()
        value = ctx.expr().getText()
        self.output_buffer += self.strategy.variable_declaration(name, value)

    def visitDataType(self, ctx):
        pass
 
    def visitIfStat(self, ctx):
        if_condition = self.visit(ctx.expr())
        if_block = ctx.ifBlock()
        if_body = ""
        for stat in if_block.stat():
            if_body += stat.getText() + "\n"
        self.output_buffer += self.strategy.if_statement(if_condition, if_body)


        if ctx.ELIF():
            for i in range(len(ctx.elifExpr())):
                elif_condition = self.visit(ctx.elifExpr(i))
                elif_block_stats = ctx.elifBlock(i).stat()
                elif_block = ""
                for stat in elif_block_stats:
                    elif_block += stat.getText() + "\n"
                self.output_buffer += self.strategy.elif_statement(elif_condition, elif_block)

        if ctx.ELSE():
            else_block_stats = ctx.elseBlock().stat()
            else_body = ""
            for stat in else_block_stats:
                else_body += stat.getText() + "\n"
            self.output_buffer += self.strategy.else_statement(else_body)
    
    def visitIfBlock(self, ctx):
        return self.visit(ctx.stat())

    def visitElifExpr(self, ctx):
        return self.visit(ctx.expr())
    
    def visitStat(self, ctx):
        if ctx.printStat():
            return self.visit(ctx.printStat())
        elif ctx.varDecl():
            return self.visit(ctx.varDecl())
        elif ctx.ifStat():
            return self.visit(ctx.ifStat())
        elif ctx.forLoop():
            return self.visit(ctx.forLoop())
        elif ctx.whileLoop():
            return self.visit(ctx.whileLoop())
        elif ctx.functionDecl():
            return self.visit(ctx.functionDecl())
        elif ctx.functionCall():
            return self.visit(ctx.functionCall())
        elif ctx.arrayInit():
            return self.visit(ctx.arrayInit())
        elif ctx.enumDecl():
            return self.visit(ctx.enumDecl())
        elif ctx.expr():
            return self.visit(ctx.expr())

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
        while_condition = ctx.expr().getText()
        while_body = ""
        for stat in ctx.stat():
            while_body += stat.getText() + "\n"
        self.output_buffer += self.strategy.while_loop(while_condition, while_body)

    def visitFunctionDecl(self, ctx):
        func_name = ctx.ID().getText()
        func_params = ctx.params().getText()
        function_body = ""
        
        for stat in ctx.stat():
            function_body += stat.getText() + "\n"

        self.functions[func_name] = {"params": func_params, "body": ctx.stat()}
        self.output_buffer += self.strategy.function_definition(func_name, func_params, function_body)

    def visitFunctionCall(self, ctx):
        name = ctx.ID().getText()
        args = ctx.args().getText()

        if name in self.functions:
            self.output_buffer += self.strategy.function_call(name, args)
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
                return "not " + left
            
        elif ctx.AND() or ctx.OR():
            if ctx.expr(0) and ctx.expr(1) is not None:
                left = ctx.expr(0).getText()
                right = ctx.expr(1).getText()
                if ctx.op is not None:
                    if ctx.op.type == RogueLangParser.AND: 
                        return left + " and " + right + "\n" 
                    elif ctx.op.type == RogueLangParser.OR:
                        return left + " or " + right + "\n" 
                    
    
           
        
        #handling comparison operators
        elif ctx.GT() or ctx.GTE() or ctx.LT() or ctx.LTE() or ctx.EQ() or ctx.NEQ() :
            if ctx.expr(0) and ctx.expr(1) is not None:
                left = ctx.expr(0).getText()
                right = ctx.expr(1).getText()
                if ctx.op is not None:
                    if ctx.op.type == RogueLangParser.GT: 
                        return left + " > " + right + "\n" 
                    elif ctx.op.type == RogueLangParser.GTE:
                        return left + " >= " + right + "\n" 
                    elif ctx.op.type == RogueLangParser.LT:
                        return left + " < " + right + "\n" 
                    elif ctx.op.type == RogueLangParser.LTE:
                        return left + " <= " + right + "\n" 
                    elif ctx.op.type == RogueLangParser.EQ:
                        return left + " == " + right + "\n" 
                    elif ctx.op.type == RogueLangParser.NEQ:
                        return left + " != " + right + "\n" 
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
                        return left + " + " + right + "\n" 

                    elif ctx.op.type == RogueLangParser.MINUS:
                        return left + " - " + right + "\n"

                    elif ctx.op.type == RogueLangParser.MULT:
                        return left + " * " + right + "\n"

                    elif ctx.op.type == RogueLangParser.MOD:
                        return left + " % " + right + "\n"

                    elif ctx.op.type == RogueLangParser.DIV:
                        if right != 0:
                            return left + " / " + right + "\n"
                        else:
                            raise Exception("Division by 0")
            else:
                # Handle cases where the expression doesn't lead to a binary operation
                # This might involve handling unary operations or simply returning the result of a single child expression
                # Example:
                if ctx.expr(0) is not None:
                    return self.visit(ctx.expr(0))
                # Add more cases here as needed based on your grammar and possible expression structures
