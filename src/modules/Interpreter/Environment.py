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
            if len(index) == 1:
                value = self.values[name]
                return value[index[0]]
            else:
                value = self.values[name]
                for i in index:
                    value = value[i]
                return value
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

    def minus_equals(self, name, value):
        if name in self.values:
            self.values[name].remove(value)
        elif self.enclosing is not None:
            self.enclosing.minus_equals(name, value)
        else:
            raise Exception("Undefined variable: {}".format(name))