#   PythonVisitor.py
from grammar_files.generated.RogueLangParser import RogueLangParser
from grammar_files.generated.RogueLangVisitor import RogueLangVisitor

class PythonVisitor(RogueLangVisitor):
    def __init__(self):
        self.output_buffer = ""

    def add_indentation(self, lines, level=1):
        indentation = '    ' * level
        indented_lines = [indentation + line if line.strip() != '' else line for line in lines.split('\n')]
        return '\n'.join(indented_lines)

    def visitProg(self, ctx:RogueLangParser.ProgContext):
        for stat in ctx.stat():
            self.output_buffer += self.visit(stat) + '\n'
        return self.output_buffer


    def visitPrintStat(self, ctx:RogueLangParser.PrintStatContext):
        return f'print({self.visit(ctx.expr())})'

    def visitVarDecl(self, ctx:RogueLangParser.VarDeclContext):
        varName = ctx.ID().getText()
        expr = self.visit(ctx.expr()) if ctx.expr() else 'None'
        return f'{varName} = {expr}'

    def visitStatBlock(self, ctx):
        statements = [self.visit(statement) for statement in ctx.stat()]
        return '\n'.join(filter(None, statements))

    def visitIfStat(self, ctx:RogueLangParser.IfStatContext):
        # Initialize output with the 'if' condition and block.
        output = "if " + self.visit(ctx.expr(0)) + ":\n" + self.add_indentation(self.visit(ctx.statBlock(0)))
        
        elif_count = len(ctx.ELIF())
        for i in range(elif_count):
            output += "\nelif " + self.visit(ctx.expr(i + 1)) + ":\n" + self.add_indentation(self.visit(ctx.statBlock(i + 1)))
        
        # To determine if there's an else block, check if the number of statBlocks is greater than the number of conditions.
        total_conditions = 1 + elif_count  # 1 for 'if' and others for 'elif'
        if len(ctx.statBlock()) > total_conditions:  # This implies there's an 'else' block.
            output += "\nelse:\n" + self.add_indentation(self.visit(ctx.statBlock(total_conditions)))
        
        return output

    def visitForLoop(self, ctx):
        loop_var = ctx.varDecl().ID().getText()
        iterable = self.visit(ctx.expr(0))
        body_statements = '\n'.join([self.visit(stat) for stat in ctx.stat()])
        body = self.add_indentation(body_statements)
        return f'for {loop_var} in {iterable}:\n{body}'

    
    def visitWhileLoop(self, ctx):
        while_condition = self.visit(ctx.expr())
        body_statements = '\n'.join(self.visit(stat) for stat in ctx.stat())
        body = self.add_indentation(body_statements)
        return f'while {while_condition}:\n{body}'

    def visitFunctionDecl(self, ctx:RogueLangParser.FunctionDeclContext):
        func_name = ctx.ID().getText()  # Assuming the function name is an ID token
        # Handling parameters, if present
        params = [param.getText() for param in ctx.params().param()] if ctx.params() else []
        params_str = ", ".join(params)  # Convert parameters list to a comma-separated string
        
        # Handling the function body: iterate over each statement and visit
        body_statements = [self.visit(stat) for stat in ctx.stat()]
        # Join the visited statements with newlines and add indentation
        body_indented = self.add_indentation('\n'.join(body_statements))
        
        return f"def {func_name}({params_str}):\n{body_indented}\n"


    def visitFunctionCall(self, ctx:RogueLangParser.FunctionCallContext):
        func_name = ctx.ID().getText()
        args = [self.visit(arg) for arg in ctx.args().expr()] if ctx.args() else []
        
        args_str = ", ".join(args)  # Convert arguments list to a comma-separated string
        return f"{func_name}({args_str})"

    def visitArrayInit(self, ctx):
        elements = [self.visit(expr) for expr in ctx.expr()]
        return f'[{", ".join(elements)}]'

    def defaultResult(self):
        # Returns a placeholder for unhandled cases
        return "''"


    def visitExpr(self, ctx):
        if ctx.ID():
            return ctx.ID().getText()
        elif ctx.STRING():
            return ctx.STRING().getText()
        elif ctx.TRUE() or ctx.getText().lower() == 'true':
            return 'True'
        elif ctx.FALSE() or ctx.getText().lower() == 'false':
            return 'False'
        elif ctx.NUMBER():
            return ctx.NUMBER().getText()
        
        elif ctx.getChildCount() == 3:
            left = self.visit(ctx.expr(0)) if ctx.expr(0) else ''
            right = self.visit(ctx.expr(1)) if ctx.expr(1) else ''
            op = ctx.getChild(1).getText()
            if op == '[':
                return f'{left}[{right}]'
            else:
                return f'{left} {op} {right}'

        elif ctx.op:
            left = self.visit(ctx.expr(0))
            right = self.visit(ctx.expr(1)) if ctx.expr(1) else ''
            operator = {'+': '+', '-': '-', '*': '*', '/': '/', '%': '%',
                        '>': '>', '>=': '>=', '<': '<', '<=': '<=',
                        '==': '==', '!=': '!=', 'and': 'and', 'or': 'or', 'not': 'not'}.get(ctx.op.text, ctx.op.text)
            if ctx.NOT():
                return f'not {left}'
            elif right:  # Binary operation
                return f'{left} {operator} {right}'
            else:  # Unary operation
                return left
        else:
            return self.defaultResult()