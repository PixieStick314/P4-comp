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

    def assign_to_list_element(self, variable, index, value):
        if len(index) > 1:
            i = index.pop(0)
            sublist = variable[i]
            variable[i] = self.assign_to_list_element(sublist, index, value)
            return variable
        else:
            variable[index[0]] = value
            return variable

    def get_struct_field(self, name, fields):
        if name in self.values:
            struct = self.values[name]
            if len(fields) == 1:
                return struct.get_field(fields[0])
            else:
                for field in fields:
                    struct = struct.get_field(field)
                    return struct
        elif self.enclosing is not None:
            return self.enclosing.get_struct_field(name, fields)
        else:
            raise Exception("Undefined field: {}".format(name))

    def assign_to_struct_field(self, struct, fields, value):
        if len(fields) > 1:
            field = fields.pop(0)
            nested_struct = struct[field]
            struct[field] = self.assign_to_struct_field(nested_struct, fields, value)
            return struct
        else:
            struct[fields[0]] = value
            return struct

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