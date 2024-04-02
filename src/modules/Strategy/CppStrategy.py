#   CppStrategy.py
from modules.Strategy.LanguageStrategy import LanguageStrategy

class CppStrategy(LanguageStrategy):
    def function_definition(self, name, params, body):
        params_str = ", ".join(f"{param_type} {param_name}" for param_name, param_type in params)
        return f"void {name}({params_str}) {{\n{body}\n}}\n"
