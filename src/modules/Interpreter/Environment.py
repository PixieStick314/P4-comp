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

    def get_list_element(self, name, index):
        if name in self.values:
            list_values = self.values[name]
            return list_values[index]
        elif self.enclosing is not None:
            return self.enclosing.get_list_element(name, index)
        else:
            raise Exception("Undefined list: {}".format(name))

    def plus_equals(self, name, value):
        if name in self.values:
            self.values[name].append(value)
        elif self.enclosing is not None:
            self.enclosing.plus_equals(name, value)
        else:
            raise Exception("Undefined variable: {}".format(name))

    def list_pop(self, name, index):
        if name in self.values:
            self.values[name].pop(index)
        elif self.enclosing is not None:
            self.enclosing.list_pop(name, index)
        else:
            raise Exception("Undefined list: {}".format(name))
