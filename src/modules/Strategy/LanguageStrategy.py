class LanguageStrategy:
    def function_definition(self, name, params, body):
        raise NotImplementedError # This is actually fucking correct. WTF why is it called this???
    
    def function_call(self, name, args):
        raise NotImplementedError
    
    def for_loop(self, variable, iterable, body):
        raise NotImplementedError
