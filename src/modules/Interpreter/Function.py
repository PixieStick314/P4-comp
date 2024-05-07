from modules.Interpreter.Environment import Environment


class Function:
    def __init__(self, params, body):
        self.params = params
        self.body = body


class NativeFunction:
    def __init__(self, params, body):
        self.params = params
        self.body = body

    def run(self, args):
        if len(args) == len(self.params):
            return self.body(args)
        else:
            raise RuntimeError(f'Expected {len(self.params)} arguments, got {len(args)}')
