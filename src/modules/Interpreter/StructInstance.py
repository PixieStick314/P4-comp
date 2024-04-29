class StructInstance:
    def __init__(self, parent, fields):
        self.parent = parent
        self.fields = {}

    def get_field(self, name):
        return self.fields[name]