from datetime import datetime

import random

from modules.Interpreter.StructInstance import StructInstance


class Environment:
    def __init__(self, enclosing):
        self.values = {}
        self.seed = None
        self.map = enclosing.map if enclosing else None
        self.enclosing = enclosing

    def define(self, name, value):
        self.values[name] = value

    def assign(self, name, value):
        if name in self.values:
            self.values[name] = value
        elif self.enclosing is not None:
            self.enclosing.assign(name, value)
        else:
            raise RuntimeError("Undefined variable: {}".format(name))

    def get(self, name):
        if name in self.values:
            return self.values[name]
        elif self.enclosing is not None:
            return self.enclosing.get(name)
        else:
            raise RuntimeError("Undefined variable: {}".format(name))

    def check_seed(self):
        if self.seed is not None:
            pass
        elif self.enclosing is not None:
            self.enclosing.check_seed()
        else:
            self.seed = str(datetime.now())
            random.seed(self.seed)
            print(f"No seed set, using {self.seed}")

    def unpack(self, name, index_list):
        variable = self.get(name)
        if isinstance(index_list, tuple):
            for index in index_list:
                variable = self.get_inner(variable, index)
        else:
            variable = self.get_inner(variable, index_list)
        return variable

    def get_inner(self, variable, index):
        if isinstance(variable, list):
            if isinstance(index, int):
                return variable[index]
            elif isinstance(index, list):
                return variable[self.get(index[1])]
        elif isinstance(variable, dict):
            if isinstance(index, list):
                return variable[self.get(index[1])]
            else:
                return variable[index]
        elif isinstance(variable, StructInstance):
            if isinstance(index, list):
                return variable.get_field(index[1])
            else:
                return variable.get_field(index)

    def unpack_and_assign(self, variable, index_list, value):
        if len(index_list) > 1:
            index = index_list[0]
            inner = self.get_inner(variable, index)
            index_list = index_list[(len(index_list) - 1):]
            inner = self.unpack_and_assign(inner, index_list, value)
            return self.assign_inner(variable, index, inner)
        else:
            return self.assign_inner(variable, index_list[0], value)

    def assign_inner(self, variable, index, value):
        if isinstance(variable, list):
            if isinstance(index, int):
                variable[index] = value
            elif isinstance(variable, list):
                variable[self.get(index[1])] = value
        elif isinstance(variable, dict):
            if isinstance(index, str):
                variable[index] = value
            elif isinstance(index, list):
                variable[self.get(index[1])] = value
        elif isinstance(variable, StructInstance):
            variable.fields[index] = value
        return variable
