class Environment:
    def __init__(self, enclosing):
        self.values = {}
        self.enclosing = enclosing

    def define(self, name, value):
        self.values[name] = value

    def assign(self, name, value):
        if name in self.values:
            self.values[name] = value
        elif self.enclosing is not None:
            self.enclosing.assign(name, value)
        else:
            raise Exception("Undefined variable: {}".format(name))

    def get(self, name):
        if name in self.values:
            return self.values[name]
        elif self.enclosing is not None:
            return self.enclosing.get(name)
        else:
            raise Exception("Undefined variable: {}".format(name))