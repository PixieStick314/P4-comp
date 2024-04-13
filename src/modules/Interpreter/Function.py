from modules.Interpreter.Environment import Environment


class Function:
    def __init__(self, params, body):
        self.params = [params]
        self.body = body
