from datetime import datetime

import random


class Environment:
    def __init__(self, enclosing):
        self.values = {}
        self.seed = None
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

    def assign_to_list_element(self, variable, indices, value):
        if len(indices) > 1:
            i = indices.pop(0)
            sublist = variable[i]
            variable[i] = self.assign_to_list_element(sublist, indices, value)
            return variable
        else:
            variable[indices[0]] = value
            return variable

    def get_struct_field(self, name, fields, indices):
        if name in self.values:
            struct = self.values[name]
            if len(fields) == 1:
                if indices[0] is None:
                    return struct.get_field(fields[0])
                else:
                    struct = struct.get_field(fields[0])
                    for index_list in indices:
                        for index in index_list:
                            struct = struct[index]
                    return struct
            else:
                for i in range(len(fields)):
                    struct = struct.get_field(fields[i])
                    if indices[i] is not None:
                        for index in indices[i]:
                            struct = struct[index]
                return struct
        elif self.enclosing is not None:
            return self.enclosing.get_struct_field(name, fields)
        else:
            raise Exception("Undefined field: {}".format(name))

    def assign_to_struct_field(self, struct, fields, value, indices):
        if len(fields) > 1:
            field = fields.pop(0)
            index_list = indices.pop(0)
            nested_struct = struct.fields[field]
            if index_list is not None:
                for index in index_list:
                    nested_struct = nested_struct[index]
            struct.fields[field] = self.assign_to_struct_field(nested_struct, fields, value)
            return struct
        else:
            if indices[0] is None:
                struct.fields[fields[0]] = value
            else:
                struct.fields[fields[0]] = self.assign_to_list_element(struct.fields[fields[0]], indices[0], value)
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

    def check_seed(self):
        if self.seed is not None:
            pass
        elif self.enclosing is not None:
            self.enclosing.check_seed()
        else:
            self.seed = str(datetime.now())
            random.seed(self.seed)
            print(f"No seed set, using {self.seed}")
