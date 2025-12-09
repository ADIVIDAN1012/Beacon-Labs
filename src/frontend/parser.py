# parser.py

from symbol_table import SymbolTable
from lexer import Token
from beacon_ast import (ProgramNode, NumberNode, BinaryOpNode, UnaryOpNode, VarAccessNode, VarAssignNode, ConstantDeclNode, ShowStatementNode, NickDeclNode, FunctionDeclNode, ReturnStatementNode, FunctionCallNode, StringNode, ExpressionStatementNode, DocstringNode, CheckStatementNode, TraverseNode, UntilNode, AttemptTrapConcludeNode, BlueprintNode, AttributeAccessNode, SpawnNode, DenNode, ConvertNode, ToolkitNode, PlugNode, BridgeNode, InletNode, LinkNode, InterpolatedStringNode, HaltNode, ProceedNode, WaitNode, TriggerNode, BlameNode, TypeNode, KindNode, NickNode, HiddenNode, ShieldedNode, InternalNode, EmbedNode, ParalNode, HoldNode, SignalNode, ListenNode, ConstructorNode, AskNode, AuthenNode, TransformNode, CondenseNode, PackNode, UnpackNode, BooleanNode, NilNode)

class Parser:
    def __init__(self, tokens: list[Token]):
        self.tokens = tokens
        self.position = 0
        self.current_token = self.tokens[self.position] if self.tokens else None
        self.symbol_table = SymbolTable()

    def advance(self):
        self.position += 1
        self.current_token = self.tokens[self.position] if self.position < len(self.tokens) else None

    def eat(self, token_type):
        if self.current_token and self.current_token.type == token_type:
            self.advance()
        else:
            raise Exception(f"Expected {token_type}, got {self.current_token.type if self.current_token else 'EOF'}")

    def parse(self):
        return self.program()

    def program(self):
        statements = []
        while self.current_token.type != 'EOF':
            statements.append(self.statement())
        return ProgramNode(statements)

    def statement(self):
        if self.current_token.type == 'FIRM':
            return self.parse_constant_declaration()

        elif self.current_token.type == 'NOTE':
            self.eat('NOTE')
            if self.current_token.type == 'STRING':
                docstring_value = self.current_token.value
                self.eat('STRING')
                return DocstringNode(docstring_value)
            else:
                raise Exception("Expected STRING after NOTE for docstring")
        elif self.current_token.type == 'SPEC' or self.current_token.type == 'PREP': # Changed from KEYWORD and value == 'spec'
            return self.parse_function_declaration()
        elif self.current_token.type == 'FORWARD': # Changed from KEYWORD and value == 'forward'
            self.eat('FORWARD') # Consume 'forward'
            expression = self.expression()
            return ReturnStatementNode(expression)
        elif self.current_token.type == 'SHOW':
            return self.parse_show_statement()
        elif self.current_token.type == 'CHECK':
            return self.parse_check_statement()
        elif self.current_token.type == 'TRAVERSE':
            return self.parse_traverse_statement()
        elif self.current_token.type == 'UNTIL':
            return self.parse_until_statement()
        elif self.current_token.type == 'ATTEMPT':
            return self.parse_attempt_trap_conclude_statement()
        elif self.current_token.type == 'BLUEPRINT':
            return self.parse_blueprint_declaration()
        elif self.current_token.type == 'TOOLKIT':
            return self.parse_toolkit_declaration()
        elif self.current_token.type == 'PLUG':
            return self.parse_plug_statement()
        elif self.current_token.type == 'BRIDGE':
            return self.parse_bridge_declaration()
        elif self.current_token.type == 'INLET':
            return self.parse_inlet_block()
        elif self.current_token.type == 'LINK':
            return self.parse_link_statement()
        elif self.current_token.type == 'EXPOSE':
            return self.parse_expose_statement()
        elif self.current_token.type == 'SHARE':
            return self.parse_share_statement()
        elif self.current_token.type == 'HALT':
            return self.parse_halt_statement()
        elif self.current_token.type == 'PROCEED':
            return self.parse_proceed_statement()
        elif self.current_token.type == 'WAIT':
            return self.parse_wait_statement()
        elif self.current_token.type == 'TRIGGER':
            return self.parse_trigger_statement()
        elif self.current_token.type == 'BLAME':
            return self.parse_blame_statement()
        elif self.current_token.type == 'TYPE':
            return self.parse_type_statement()
        elif self.current_token.type == 'KIND':
            return self.parse_kind_statement()
        elif self.current_token.type == 'NICK':
            return self.parse_nick_statement()
        elif self.current_token.type == 'HIDDEN':
            return self.parse_hidden_statement()
        elif self.current_token.type == 'SHIELDED':
            return self.parse_shielded_statement()
        elif self.current_token.type == 'INTERNAL':
            return self.parse_internal_statement()
        elif self.current_token.type == 'EMBED':
            return self.parse_embed_statement()
        elif self.current_token.type == 'PARAL':
            return self.parse_paral_statement()
        elif self.current_token.type == 'HOLD':
            return self.parse_hold_statement()
        elif self.current_token.type == 'SIGNAL':
            return self.parse_signal_statement()
        elif self.current_token.type == 'LISTEN':
            return self.parse_listen_statement()
        elif self.current_token.type == 'ASK':
            return self.parse_ask_statement()
        elif self.current_token.type == 'AUTHEN':
            return self.parse_authen_statement()
        elif self.current_token.type == 'TRANSFORM':
            return self.parse_transform_statement()
        elif self.current_token.type == 'CONDENSE':
            return self.parse_condense_statement()
        elif self.current_token.type == 'PACK':
            return self.parse_pack_statement()
        elif self.current_token.type == 'UNPACK':
            return self.parse_unpack_statement()
        elif self.current_token.type == 'FUNCALL':
            return self.parse_function_call_statement()
        elif self.current_token.type == 'WORD' and self.current_token.value == 'funcall':
            self.eat('WORD')
            expr = self.expression()
            if isinstance(expr, VarAccessNode):
                expr = FunctionCallNode(expr.var_name, [])
            if not isinstance(expr, FunctionCallNode):
                raise Exception(f"Expected a function call after 'funcall', but got {type(expr)}")
            return ExpressionStatementNode(expr)
        else:
            left = self.expression()
            if self.current_token and self.current_token.type == 'ASSIGN':
                self.eat('ASSIGN')
                right = self.expression()
                if not isinstance(left, (VarAccessNode, AttributeAccessNode)):
                    raise Exception("Invalid assignment target.")
                return VarAssignNode(target=left, value=right)
            return ExpressionStatementNode(left)

    def parse_function_call_statement(self):
        self.eat('FUNCALL')
        expr = self.expression()
        if isinstance(expr, VarAccessNode):
            expr = FunctionCallNode(expr.var_name, [])
        
        if not isinstance(expr, FunctionCallNode):
            raise Exception(f"Expected a function call after 'funcall', but got {type(expr)}")

        return ExpressionStatementNode(expr)

    def parse_function_declaration(self, exposed=False, shared=False):
        func_type = self.current_token.type
        if func_type not in ['SPEC', 'PREP']:
            raise Exception(f"Expected SPEC or PREP, got {func_type}")
        self.eat(func_type) # Consume 'spec' or 'prep'
        if self.current_token.type == 'WORD':
            function_name = self.current_token.value
            self.eat('WORD') # Consume function name
        else:
            function_name = None
        self.eat('LPAREN') # Consume '('
        params = []
        if self.current_token.type == 'WORD' or self.current_token.type == 'OWN':
            params.append(self.current_token.value)
            self.eat(self.current_token.type)
            while self.current_token.type == 'COMMA':
                self.eat('COMMA')
                params.append(self.current_token.value)
                self.eat(self.current_token.type)
        self.eat('RPAREN')

        docstring = None
        if self.current_token.type == 'NOTE':
            self.eat('NOTE')
            if self.current_token.type == 'STRING':
                docstring = self.current_token.value
                self.eat('STRING')
            else:
                raise Exception("Expected STRING after NOTE")

        body = []
        if not exposed:
            self.eat('LBRACE')
            while self.current_token.type != 'RBRACE':
                body.append(self.statement())
            self.eat('RBRACE') # Consume '}'
        
        return FunctionDeclNode(function_name, params, body, func_type.lower(), exposed, shared, docstring=docstring)

    def parse_show_statement(self):
        self.eat('SHOW')
        self.eat('LPAREN')
        expressions = []
        while self.current_token and self.current_token.type != 'RPAREN':
            if self.current_token.type == 'COMMA':
                self.eat('COMMA')
                continue
from lexer import Token
from beacon_ast import (ProgramNode, NumberNode, BinaryOpNode, UnaryOpNode, VarAccessNode, VarAssignNode, ConstantDeclNode, ShowStatementNode, NickDeclNode, FunctionDeclNode, ReturnStatementNode, FunctionCallNode, StringNode, ExpressionStatementNode, DocstringNode, CheckStatementNode, TraverseNode, UntilNode, AttemptTrapConcludeNode, BlueprintNode, AttributeAccessNode, SpawnNode, DenNode, ConvertNode, ToolkitNode, PlugNode, BridgeNode, InletNode, LinkNode, InterpolatedStringNode, HaltNode, ProceedNode, WaitNode, TriggerNode, BlameNode, TypeNode, KindNode, NickNode, HiddenNode, ShieldedNode, InternalNode, EmbedNode, ParalNode, HoldNode, SignalNode, ListenNode, ConstructorNode, AskNode, AuthenNode, TransformNode, CondenseNode, PackNode, UnpackNode, BooleanNode, NilNode)

class Parser:
    def __init__(self, tokens: list[Token]):
        self.tokens = tokens
        self.position = 0
        self.current_token = self.tokens[self.position] if self.tokens else None
        self.symbol_table = SymbolTable()

    def advance(self):
        self.position += 1
        self.current_token = self.tokens[self.position] if self.position < len(self.tokens) else None

    def eat(self, token_type):
        if self.current_token and self.current_token.type == token_type:
            self.advance()
        else:
            raise Exception(f"Expected {token_type}, got {self.current_token.type if self.current_token else 'EOF'}")

    def parse(self):
        return self.program()

    def program(self):
        statements = []
        while self.current_token.type != 'EOF':
            statements.append(self.statement())
        return ProgramNode(statements)

    def statement(self):
        if self.current_token.type == 'FIRM':
            return self.parse_constant_declaration()

        elif self.current_token.type == 'NOTE':
            self.eat('NOTE')
            if self.current_token.type == 'STRING':
                docstring_value = self.current_token.value
                self.eat('STRING')
                return DocstringNode(docstring_value)
            else:
                raise Exception("Expected STRING after NOTE for docstring")
        elif self.current_token.type == 'SPEC' or self.current_token.type == 'PREP': # Changed from KEYWORD and value == 'spec'
            return self.parse_function_declaration()
        elif self.current_token.type == 'FORWARD': # Changed from KEYWORD and value == 'forward'
            self.eat('FORWARD') # Consume 'forward'
            expression = self.expression()
            return ReturnStatementNode(expression)
        elif self.current_token.type == 'SHOW':
            return self.parse_show_statement()
        elif self.current_token.type == 'CHECK':
            return self.parse_check_statement()
        elif self.current_token.type == 'TRAVERSE':
            return self.parse_traverse_statement()
        elif self.current_token.type == 'UNTIL':
            return self.parse_until_statement()
        elif self.current_token.type == 'ATTEMPT':
            return self.parse_attempt_trap_conclude_statement()
        elif self.current_token.type == 'BLUEPRINT':
            return self.parse_blueprint_declaration()
        elif self.current_token.type == 'TOOLKIT':
            return self.parse_toolkit_declaration()
        elif self.current_token.type == 'PLUG':
            return self.parse_plug_statement()
        elif self.current_token.type == 'BRIDGE':
            return self.parse_bridge_declaration()
        elif self.current_token.type == 'INLET':
            return self.parse_inlet_block()
        elif self.current_token.type == 'LINK':
            return self.parse_link_statement()
        elif self.current_token.type == 'EXPOSE':
            return self.parse_expose_statement()
        elif self.current_token.type == 'SHARE':
            return self.parse_share_statement()
        elif self.current_token.type == 'HALT':
            return self.parse_halt_statement()
        elif self.current_token.type == 'PROCEED':
            return self.parse_proceed_statement()
        elif self.current_token.type == 'WAIT':
            return self.parse_wait_statement()
        elif self.current_token.type == 'TRIGGER':
            return self.parse_trigger_statement()
        elif self.current_token.type == 'BLAME':
            return self.parse_blame_statement()
        elif self.current_token.type == 'TYPE':
            return self.parse_type_statement()
        elif self.current_token.type == 'KIND':
            return self.parse_kind_statement()
        elif self.current_token.type == 'NICK':
            return self.parse_nick_statement()
        elif self.current_token.type == 'HIDDEN':
            return self.parse_hidden_statement()
        elif self.current_token.type == 'SHIELDED':
            return self.parse_shielded_statement()
        elif self.current_token.type == 'INTERNAL':
            return self.parse_internal_statement()
        elif self.current_token.type == 'EMBED':
            return self.parse_embed_statement()
        elif self.current_token.type == 'PARAL':
            return self.parse_paral_statement()
        elif self.current_token.type == 'HOLD':
            return self.parse_hold_statement()
        elif self.current_token.type == 'SIGNAL':
            return self.parse_signal_statement()
        elif self.current_token.type == 'LISTEN':
            return self.parse_listen_statement()
        elif self.current_token.type == 'ASK':
            return self.parse_ask_statement()
        elif self.current_token.type == 'AUTHEN':
            return self.parse_authen_statement()
        elif self.current_token.type == 'TRANSFORM':
            return self.parse_transform_statement()
        elif self.current_token.type == 'CONDENSE':
            return self.parse_condense_statement()
        elif self.current_token.type == 'PACK':
            return self.parse_pack_statement()
        elif self.current_token.type == 'UNPACK':
            return self.parse_unpack_statement()
        elif self.current_token.type == 'FUNCALL':
            return self.parse_function_call_statement()
        elif self.current_token.type == 'WORD' and self.current_token.value == 'funcall':
            self.eat('WORD')
            expr = self.expression()
            if isinstance(expr, VarAccessNode):
                expr = FunctionCallNode(expr.var_name, [])
            if not isinstance(expr, FunctionCallNode):
                raise Exception(f"Expected a function call after 'funcall', but got {type(expr)}")
            return ExpressionStatementNode(expr)
        else:
            left = self.expression()
            if self.current_token and self.current_token.type == 'ASSIGN':
                self.eat('ASSIGN')
                right = self.expression()
                if not isinstance(left, (VarAccessNode, AttributeAccessNode)):
                    raise Exception("Invalid assignment target.")
                return VarAssignNode(target=left, value=right)
            return ExpressionStatementNode(left)

    def parse_function_call_statement(self):
        self.eat('FUNCALL')
        expr = self.expression()
        if isinstance(expr, VarAccessNode):
            expr = FunctionCallNode(expr.var_name, [])
        
        if not isinstance(expr, FunctionCallNode):
            raise Exception(f"Expected a function call after 'funcall', but got {type(expr)}")

        return ExpressionStatementNode(expr)

    def parse_function_declaration(self, exposed=False, shared=False):
        func_type = self.current_token.type
        if func_type not in ['SPEC', 'PREP']:
            raise Exception(f"Expected SPEC or PREP, got {func_type}")
        self.eat(func_type) # Consume 'spec' or 'prep'
        if self.current_token.type == 'WORD':
            function_name = self.current_token.value
            self.eat('WORD') # Consume function name
        else:
            function_name = None
        self.eat('LPAREN') # Consume '('
        params = []
        if self.current_token.type == 'WORD' or self.current_token.type == 'OWN':
            params.append(self.current_token.value)
            self.eat(self.current_token.type)
            while self.current_token.type == 'COMMA':
                self.eat('COMMA')
                params.append(self.current_token.value)
                self.eat(self.current_token.type)
        self.eat('RPAREN')

        docstring = None
        if self.current_token.type == 'NOTE':
            self.eat('NOTE')
            if self.current_token.type == 'STRING':
                docstring = self.current_token.value
                self.eat('STRING')
            else:
                raise Exception("Expected STRING after NOTE")

        body = []
        if not exposed:
            self.eat('LBRACE')
            while self.current_token.type != 'RBRACE':
                body.append(self.statement())
            self.eat('RBRACE') # Consume '}'
        
        return FunctionDeclNode(function_name, params, body, func_type.lower(), exposed, shared, docstring=docstring)

    def parse_show_statement(self):
        self.eat('SHOW')
        self.eat('LPAREN')
        expressions = []
        while self.current_token and self.current_token.type != 'RPAREN':
            if self.current_token.type == 'COMMA':
                self.eat('COMMA')
                continue
            expressions.append(self.expression())
        self.eat('RPAREN')
        return ShowStatementNode(expressions)

    def parse_check_statement(self):
        self.eat('CHECK')
        self.eat('LPAREN')
        condition = self.expression()
        self.eat('RPAREN')
        self.eat('LBRACE')
        body = []
        while self.current_token.type != 'RBRACE':
            body.append(self.statement())
        self.eat('RBRACE')

        alter_clauses = []
        while self.current_token and self.current_token.type == 'ALTER':
            self.eat('ALTER')
            self.eat('LPAREN')
            alter_condition = self.expression()
            self.eat('RPAREN')
            self.eat('LBRACE')
            alter_body = []
            while self.current_token.type != 'RBRACE':
                alter_body.append(self.statement())
            self.eat('RBRACE')
            alter_clauses.append((alter_condition, alter_body))

        altern_clause = None
        if self.current_token and self.current_token.type == 'ALTERN':
            self.eat('ALTERN')
            self.eat('LBRACE')
            altern_body = []
            while self.current_token.type != 'RBRACE':
                altern_body.append(self.statement())
            self.eat('RBRACE')
            altern_clause = altern_body

        return CheckStatementNode(condition, body, alter_clauses, altern_clause)

    def expression(self):
        return self.comparison()

    def comparison(self):
        node = self.addition()
        while self.current_token and self.current_token.type in ('EQUALS', 'NOT_EQUALS', 'LESS_THAN', 'GREATER_THAN', 'LESS_THAN_EQUAL', 'GREATER_THAN_EQUAL', 'IS', 'IS_NOT'):
            op = self.current_token
            self.eat(op.type)
            right = self.addition()
            node = BinaryOpNode(left=node, op=op, right=right)
        return node

    def addition(self):
        node = self.multiplication()
        while self.current_token and self.current_token.type in ('PLUS', 'MINUS'):
            op = self.current_token
            self.eat(op.type)
            right = self.multiplication()
            node = BinaryOpNode(left=node, op=op, right=right)
        return node

    def multiplication(self):
        node = self.unary()
        while self.current_token and self.current_token.type in ('MULTIPLY', 'DIVIDE'):
            op = self.current_token
            self.eat(op.type)
            right = self.unary()
            node = BinaryOpNode(left=node, op=op, right=right)
        return node

    def unary(self):
        if self.current_token and self.current_token.type == 'NOT':
            op = self.current_token
            self.eat('NOT')
            node = self.unary()
            return UnaryOpNode(op=op, right=node)
        return self.primary()

    def primary(self):
        token = self.current_token

        if token.type == 'NUMBER':
            self.eat('NUMBER')
            return NumberNode(token.value)
        elif token.type == 'STRING':
            if self.position + 1 < len(self.tokens) and self.tokens[self.position + 1].type == 'INTERPOLATION':
                parts = []
                while self.current_token.type in ('STRING', 'INTERPOLATION'):
                    if self.current_token.type == 'STRING':
                        parts.append(StringNode(self.current_token.value))
                        self.eat('STRING')
                    elif self.current_token.type == 'INTERPOLATION':
                        interp_expr = self.current_token.value
                        if interp_expr.strip() == 'peek':
                            parts.append(VarAccessNode('peek'))
                        else:
                            from lexer import Lexer
                            temp_lexer = Lexer(interp_expr)
                            temp_parser = self.__class__(temp_lexer.tokenize())
                            parts.append(temp_parser.expression())
                        self.eat('INTERPOLATION')
                return InterpolatedStringNode(parts)
            else:
                node = StringNode(self.current_token.value)
                self.eat('STRING')
                return node
        elif token.type == 'ON':
            self.eat('ON')
            return BooleanNode(True)
        elif token.type == 'OFF':
            self.eat('OFF')
            return BooleanNode(False)
        elif token.type == 'NIL':
            self.eat('NIL')
            return NilNode()
        elif token.type == 'SPAWN':
            return self.parse_spawn_expression()
        elif token.type == 'DEN':
            return self.parse_den_expression()
        elif token.type == 'CONVERT':
            return self.parse_convert_expression()
        elif token.type == 'KIND':
            return self.parse_kind_statement()

        node = None
        if token.type == 'LPAREN':
            self.eat('LPAREN')
            node = self.expression()
            self.eat('RPAREN')
        elif token.type == 'ASK':
            # Handle ask as a function-like expression
            self.eat('ASK')
            # Check if it's being used as a function call with parentheses
            if self.current_token.type == 'LPAREN':
                self.eat('LPAREN')
                # Parse the prompt argument (optional)
                prompt = None
                if self.current_token.type != 'RPAREN':
                    prompt = self.expression()
                self.eat('RPAREN')
                # Return as AskNode with the prompt as body
                return AskNode([ExpressionStatementNode(prompt)] if prompt else [])
            else:
                # Legacy syntax: ask { ... } or ask "prompt"
                block = []
                if self.current_token.type == 'LBRACE':
                    self.eat('LBRACE')
                    while self.current_token.type != 'RBRACE':
                        block.append(self.statement())
                    self.eat('RBRACE')
                else:
                    expr = self.expression()
                    block.append(ExpressionStatementNode(expr))
                return AskNode(block)
        elif token.type == 'WORD' or token.type == 'OWN':
            if token.type == 'WORD' and self.position + 1 < len(self.tokens) and self.tokens[self.position + 1].type == 'LPAREN':
                node = self.parse_function_call()
            else:
                self.eat(token.type)
                node = VarAccessNode(token.value)
        else:
            raise Exception(f"Expected number, LPAREN, WORD, OWN, or ASK, got {token.type}")

        while self.current_token and self.current_token.type == 'DOT':
            self.eat('DOT')
            attribute = self.current_token.value
            self.eat('WORD')
            node = AttributeAccessNode(node, attribute)

        return node

    def parse_constant_declaration(self):
        self.eat('FIRM') # Consume 'firm'
        const_name = self.current_token.value
        self.eat('WORD') # Consume constant name
        self.eat('ASSIGN') # Consume '='
        value = self.expression()
        self.symbol_table.define(const_name, 'FIRM')
        return ConstantDeclNode(const_name, value)

    def parse_function_call(self):
        function_name = self.current_token.value
        self.eat('WORD') # Consume function name
        self.eat('LPAREN') # Consume '('
        arguments = []
        if self.current_token.type != 'RPAREN':
            arguments.append(self.expression())
            while self.current_token.type == 'COMMA':
                self.eat('COMMA')
                arguments.append(self.expression())
        self.eat('RPAREN') # Consume ')'
        return FunctionCallNode(function_name, arguments)

    def parse_spawn_expression(self):
        self.eat('SPAWN')
        blueprint_name = self.current_token.value
        self.eat('WORD')
        self.eat('LPAREN')
        arguments = []
        if self.current_token.type != 'RPAREN':
            arguments.append(self.expression())
            while self.current_token.type == 'COMMA':
                self.eat('COMMA')
                arguments.append(self.expression())
        self.eat('RPAREN')
        return SpawnNode(blueprint_name, arguments)

    def parse_traverse_statement(self):
        self.eat('TRAVERSE')
        var_name = self.current_token.value
        self.eat('WORD')
        self.eat('FROM') # from
        start_val = self.expression()
        self.eat('TO') # to
        end_val = self.expression()

        step_val = None
        if self.current_token.type == 'BY':
            self.eat('BY')
            step_val = self.expression()

        self.eat('LBRACE')
        body = []
        while self.current_token.type != 'RBRACE':
            body.append(self.statement())
        self.eat('RBRACE')
        return TraverseNode(var_name, start_val, end_val, step_val, body)

    def parse_until_statement(self):
        self.eat('UNTIL')
        condition = self.expression()
        self.eat('LBRACE')
        body = []
        while self.current_token.type != 'RBRACE':
            body.append(self.statement())
        self.eat('RBRACE')
        return UntilNode(condition, body)

    def parse_attempt_trap_conclude_statement(self):
        self.eat('ATTEMPT')
        self.eat('LBRACE')
        attempt_body = []
        while self.current_token.type != 'RBRACE':
            attempt_body.append(self.statement())
        self.eat('RBRACE')

        trap_clauses = []
        peek = False
        while self.current_token and self.current_token.type == 'TRAP':
            self.eat('TRAP')
            error_type = self.current_token.value
            self.eat('WORD')
            if self.current_token.type == 'PEEK':
                self.eat('PEEK')
                peek = True
            self.eat('LBRACE')
            trap_body = []
            while self.current_token.type != 'RBRACE':
                trap_body.append(self.statement())
            self.eat('RBRACE')
            trap_clauses.append((error_type, trap_body))

        conclude_clause = None
        if self.current_token and self.current_token.type == 'CONCLUDE':
            self.eat('CONCLUDE')
            self.eat('LBRACE')
            conclude_body = []
            while self.current_token.type != 'RBRACE':
                conclude_body.append(self.statement())
            self.eat('RBRACE')
            conclude_clause = conclude_body

        return AttemptTrapConcludeNode(attempt_body, trap_clauses, conclude_clause, peek=peek)

    def parse_blueprint_declaration(self):
        self.eat('BLUEPRINT')
        name = self.current_token.value
        self.eat('WORD')

        parent = None
        if self.current_token.type == 'ADOPT':
            self.eat('ADOPT')
            parent = self.current_token.value
            self.eat('WORD')

        docstring = None
        if self.current_token.type == 'NOTE':
            self.eat('NOTE')
            self.eat('COLON')
            if self.current_token.type == 'STRING':
                docstring = self.current_token.value
                self.eat('STRING')
            else:
                raise Exception("Expected STRING after NOTE:")

        self.eat('LBRACE')
        attributes = []
        methods = []
        constructor = None
        while self.current_token.type != 'RBRACE':
            if self.current_token.type == 'SHARD':
                self.eat('SHARD')
                attr_name = self.current_token.value
                self.eat('WORD')
                attributes.append(VarAssignNode(VarAccessNode(attr_name), None))
            elif self.current_token.type == 'SOLID':
                self.eat('SOLID')
                attr_name = self.current_token.value
                self.eat('WORD')
                self.eat('ASSIGN')
                value = self.expression()
                attributes.append(VarAssignNode(VarAccessNode(attr_name), value))
            elif self.current_token.type == 'SPEC':
                methods.append(self.parse_function_declaration())
            elif self.current_token.type == 'PREP':
                constructor = self.parse_function_declaration()
            else:
                raise Exception(f"Unexpected token in blueprint body: {self.current_token.type}")
        self.eat('RBRACE')
        return BlueprintNode(name, attributes, methods, docstring=docstring, constructor=constructor, parent=parent)

    def parse_constructor_declaration(self):
        self.eat('PREP') # Consume 'prep'
        self.eat('LPAREN') # Consume '('
        params = []
        if self.current_token.type == 'WORD' or self.current_token.type == 'OWN':
            params.append(self.current_token.value)
            self.eat(self.current_token.type)
            while self.current_token.type == 'COMMA':
                self.eat('COMMA')
                params.append(self.current_token.value)
                self.eat(self.current_token.type)
        self.eat('RPAREN')

        body = []
        self.eat('LBRACE')
        while self.current_token.type != 'RBRACE':
            body.append(self.statement())
        self.eat('RBRACE') # Consume '}'
        
        return ConstructorNode(params, body)

    def parse_den_expression(self):
        self.eat('DEN')
        params = []
        if self.current_token.type == 'WORD':
            params.append(self.current_token.value)
            self.eat('WORD')
            while self.current_token.type == 'COMMA':
                self.eat('COMMA')
                params.append(self.current_token.value)
                self.eat('WORD')
        self.eat('COLON')
        body = self.expression()
        return DenNode(params, body)

    def parse_convert_expression(self):
        self.eat('CONVERT')
        expression = self.expression()
        self.eat('TO')
        if self.current_token.type in ['WORD', 'NUM', 'TEXT', 'ON', 'OFF', 'NIL']:
            target_type = self.current_token.value if self.current_token.type == 'WORD' else self.current_token.type
            self.eat(self.current_token.type)
        else:
            raise Exception(f"Expected type name, got {self.current_token.type}")
        return ConvertNode(expression, target_type)

    def parse_toolkit_declaration(self):
        self.eat('TOOLKIT')
        name = self.current_token.value
        self.eat('WORD')
        self.eat('LBRACE')
        body = []
        while self.current_token.type != 'RBRACE':
            body.append(self.statement())
        self.eat('RBRACE')
        return ToolkitNode(name, body)

    def parse_plug_statement(self):
        self.eat('PLUG')
        toolkit_name = self.current_token.value
        self.eat('WORD')
        self.eat('FROM')
        file_path = self.expression()
        return PlugNode(toolkit_name, file_path)

    def parse_bridge_declaration(self):
        self.eat('BRIDGE')
        name = self.current_token.value
        self.eat('WORD')
        self.eat('LBRACE')
        body = []
        while self.current_token.type != 'RBRACE':
            body.append(self.statement())
        self.eat('RBRACE')
        return BridgeNode(name, body)

    def parse_inlet_block(self):
        self.eat('INLET')
        self.eat('LBRACE')
        body = []
    def parse_expose_statement(self):
        self.eat('EXPOSE')
        if self.current_token.type == 'SPEC':
            return self.parse_function_declaration(exposed=True)
        else:
            raise Exception("Expected SPEC after EXPOSE")

    def parse_share_statement(self):
        self.eat('SHARE')
        if self.current_token.type == 'SPEC':
            return self.parse_function_declaration(shared=True)
        else:
            raise Exception("Expected SPEC after SHARE")

    def parse_halt_statement(self):
        self.eat('HALT')
        return HaltNode()

    def parse_proceed_statement(self):
        self.eat('PROCEED')
        return ProceedNode()

    def parse_wait_statement(self):
        self.eat('WAIT')
        duration = self.expression()
        return WaitNode(duration)

    def parse_trigger_statement(self):
        self.eat('TRIGGER')
        # error type is a bare identifier string
        error_name = self.current_token.value
        self.eat('WORD')
        self.eat('LPAREN')
        message = self.expression()
        self.eat('RPAREN')
        return TriggerNode(error_name, message)

    def parse_shielded_statement(self):
        self.eat('SHIELDED')
        declaration = self.statement()
        return ShieldedNode(declaration)

    def parse_internal_statement(self):
        self.eat('INTERNAL')
        declaration = self.statement()
        return InternalNode(declaration)

    def parse_embed_statement(self):
        self.eat('EMBED')
        block = []
        if self.current_token.type == 'LBRACE':
            self.eat('LBRACE')
            while self.current_token.type != 'RBRACE':
                block.append(self.statement())
            self.eat('RBRACE')
        else:
            expr = self.expression()
            block.append(ExpressionStatementNode(expr))
        return EmbedNode(block)

    def parse_paral_statement(self):
        self.eat('PARAL')
        block = []
        if self.current_token.type == 'LBRACE':
            self.eat('LBRACE')
            while self.current_token.type != 'RBRACE':
                block.append(self.statement())
            self.eat('RBRACE')
        else:
            expr = self.expression()
            block.append(ExpressionStatementNode(expr))
        return ParalNode(block)

    def parse_hold_statement(self):
        self.eat('HOLD')
        block = []
        if self.current_token.type == 'LBRACE':
            self.eat('LBRACE')
            while self.current_token.type != 'RBRACE':
                block.append(self.statement())
            self.eat('RBRACE')
        else:
            expr = self.expression()
            block.append(ExpressionStatementNode(expr))
        return HoldNode(block)

    def parse_signal_statement(self):
        self.eat('SIGNAL')
        block = []
        # optional event expression
        if self.current_token.type != 'LBRACE':
            expr = self.expression()
            block.append(ExpressionStatementNode(expr))
        if self.current_token and self.current_token.type == 'LBRACE':
            self.eat('LBRACE')
            while self.current_token.type != 'RBRACE':
                block.append(self.statement())
            self.eat('RBRACE')
        return SignalNode(block)

    def parse_listen_statement(self):
        self.eat('LISTEN')
        block = []
        # event expression followed by optional block
        if self.current_token.type != 'LBRACE':
            expr = self.expression()
            block.append(ExpressionStatementNode(expr))
        if self.current_token and self.current_token.type == 'LBRACE':
            self.eat('LBRACE')
            while self.current_token.type != 'RBRACE':
                block.append(self.statement())
            self.eat('RBRACE')
        return ListenNode(block)

    def parse_ask_statement(self):
        self.eat('ASK')
        block = []
        if self.current_token.type == 'LBRACE':
            self.eat('LBRACE')
            while self.current_token.type != 'RBRACE':
                block.append(self.statement())
            self.eat('RBRACE')
        else:
            expr = self.expression()
            block.append(ExpressionStatementNode(expr))
        return AskNode(block)

    def parse_authen_statement(self):
        self.eat('AUTHEN')
        block = []
        if self.current_token.type == 'LBRACE':
            self.eat('LBRACE')
            while self.current_token.type != 'RBRACE':
                block.append(self.statement())
            self.eat('RBRACE')
        else:
            expr = self.expression()
            block.append(ExpressionStatementNode(expr))
        return AuthenNode(block)

    def parse_transform_statement(self):
        self.eat('TRANSFORM')
        block = []
        if self.current_token.type == 'LBRACE':
            self.eat('LBRACE')
            while self.current_token.type != 'RBRACE':
                block.append(self.statement())
            self.eat('RBRACE')
        else:
            expr = self.expression()
            block.append(ExpressionStatementNode(expr))
        return TransformNode(block)

    def parse_condense_statement(self):
        self.eat('CONDENSE')
        block = []
        if self.current_token.type == 'LBRACE':
            self.eat('LBRACE')
            while self.current_token.type != 'RBRACE':
                block.append(self.statement())
            self.eat('RBRACE')
        else:
            expr = self.expression()
            block.append(ExpressionStatementNode(expr))
        return CondenseNode(block)

    def parse_pack_statement(self):
        self.eat('PACK')
        block = []
        if self.current_token.type == 'LBRACE':
            self.eat('LBRACE')
            while self.current_token.type != 'RBRACE':
                block.append(self.statement())
            self.eat('RBRACE')
        else:
            expr = self.expression()
            block.append(ExpressionStatementNode(expr))
        return PackNode(block)

    def parse_unpack_statement(self):
        self.eat('UNPACK')
        block = []
        if self.current_token.type == 'LBRACE':
            self.eat('LBRACE')
            while self.current_token.type != 'RBRACE':
                block.append(self.statement())
            self.eat('RBRACE')
        else:
            expr = self.expression()
            block.append(ExpressionStatementNode(expr))
        return UnpackNode(block)

    def parse_type_statement(self):
        self.eat('TYPE')
        type_name = self.current_token.value
        self.eat('WORD')
        return TypeNode(type_name)

    def parse_kind_statement(self):
        self.eat('KIND')
        self.eat('LPAREN')
        expr = self.expression()
        self.eat('RPAREN')
        return KindNode(expr)

    def parse_nick_statement(self):
        self.eat('NICK')
        alias = self.current_token.value
        self.eat('WORD')
        self.eat('ASSIGN')
        if self.current_token.type in ['WORD', 'NUM', 'TEXT', 'ON', 'OFF', 'NIL']:
            original = self.current_token.value if self.current_token.type == 'WORD' else self.current_token.type
            self.eat(self.current_token.type)
        else:
            raise Exception(f"Expected type name, got {self.current_token.type}")
        return NickNode(original, alias)
