# symbol_table.py

class SymbolTable:
    def __init__(self):
        self.symbols = {}

    def define(self, name, symbol_type):
        self.symbols[name] = {'type': symbol_type}

    def is_constant(self, name):
        return self.symbols.get(name, {}).get('type') == 'FIRM'