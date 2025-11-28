# ast.py

from dataclasses import dataclass

class ASTNode:
    def to_dict(self):
        raise NotImplementedError

class NumberNode(ASTNode):
    def __init__(self, value):
        self.value = value

    def to_dict(self):
        return {"type": "NumberNode", "value": self.value}

class BooleanNode(ASTNode):
    def __init__(self, value):
        self.value = value

    def to_dict(self):
        return {"type": "BooleanNode", "value": self.value}

class NilNode(ASTNode):
    def to_dict(self):
        return {"type": "NilNode"}

class BinaryOpNode(ASTNode):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

    def to_dict(self):
        return {
            "type": "BinaryOpNode",
            "left": self.left.to_dict(),
            "op": {"type": self.op.type, "value": self.op.value},
            "right": self.right.to_dict(),
        }

class UnaryOpNode(ASTNode):
    def __init__(self, op, right):
        self.op = op
        self.right = right

    def to_dict(self):
        return {
            "type": "UnaryOpNode",
            "op": {"type": self.op.type, "value": self.op.value},
            "right": self.right.to_dict(),
        }

class VarAccessNode(ASTNode):
    def __init__(self, var_name):
        self.var_name = var_name

    def to_dict(self):
        return {"type": "VarAccessNode", "var_name": self.var_name}

class VarAssignNode(ASTNode):
    def __init__(self, target, value):
        self.target = target
        self.value = value

    def to_dict(self):
        return {
            'type': 'VarAssignNode',
            'target': self.target.to_dict(),
            'value': self.value.to_dict() if self.value else None,
        }

class ConstantDeclNode(ASTNode):
    def __init__(self, const_name, value):
        self.const_name = const_name
        self.value = value

    def to_dict(self):
        return {'type': 'ConstantDeclNode', 'const_name': self.const_name, 'value': self.value.to_dict()}

class ShowStatementNode(ASTNode):
    def __init__(self, expressions):
        self.expressions = expressions

    def to_dict(self):
        return {
            "type": "ShowStatementNode",
            "expressions": [expr.to_dict() for expr in self.expressions]
        }

class NickDeclNode(ASTNode):
    def __init__(self, original_type, alias):
        self.original_type = original_type
        self.alias = alias

    def to_dict(self):
        return {
            "type": "NickDeclNode",
            "original_type": self.original_type,
            "alias": self.alias
        }

@dataclass
class FunctionDeclNode(ASTNode):
    name: str
    params: list[str]
    body: list[ASTNode]
    func_type: str
    exposed: bool = False
    shared: bool = False
    docstring: str | None = None

    def to_dict(self):
        return {
            "type": "FunctionDeclNode",
            "name": self.name,
            "params": self.params,
            "body": [stmt.to_dict() for stmt in self.body],
            "func_type": self.func_type,
            "exposed": self.exposed,
            "shared": self.shared,
            "docstring": self.docstring
        }

@dataclass
class ReturnStatementNode(ASTNode):
    expression: ASTNode

    def to_dict(self):
        return {
            "type": "ReturnStatementNode",
            "expression": self.expression.to_dict()
        }

@dataclass
class FunctionCallNode(ASTNode):
    function_name: str
    arguments: list[ASTNode]

    def to_dict(self):
        return {
            "type": "FunctionCallNode",
            "function_name": self.function_name,
            "arguments": [arg.to_dict() for arg in self.arguments]
        }

class StringNode(ASTNode):
    def __init__(self, value):
        self.value = value

    def to_dict(self):
        return {'type': 'StringNode', 'value': self.value}

@dataclass
class DocstringNode(ASTNode):
    value: str

    def to_dict(self):
        return {"type": "DocstringNode", "value": self.value}

class ProgramNode(ASTNode):
    def __init__(self, statements):
        self.statements = statements

    def to_dict(self):
        return {
            "type": "ProgramNode",
            "statements": [s.to_dict() for s in self.statements],
        }

class StatementNode(ASTNode):
    pass



class ExpressionStatementNode(StatementNode):
    def __init__(self, expression):
        self.expression = expression

    def to_dict(self):
        return {"type": "ExpressionStatementNode", "expression": self.expression.to_dict()}

class CheckStatementNode(ASTNode):
    def __init__(self, condition, body, alter_clauses=None, altern_clause=None):
        self.condition = condition
        self.body = body
        self.alter_clauses = alter_clauses if alter_clauses is not None else []
        self.altern_clause = altern_clause

    def to_dict(self):
        return {
            "type": "CheckStatementNode",
            "condition": self.condition.to_dict(),
            "body": [stmt.to_dict() for stmt in self.body],
            "alter_clauses": [
                {
                    "condition": cond.to_dict(),
                    "body": [stmt.to_dict() for stmt in body]
                } for cond, body in self.alter_clauses
            ],
            "altern_clause": [stmt.to_dict() for stmt in self.altern_clause] if self.altern_clause else None
        }

class TraverseNode(ASTNode):
    def __init__(self, var_name, start_val, end_val, step_val, body):
        self.var_name = var_name
        self.start_val = start_val
        self.end_val = end_val
        self.step_val = step_val
        self.body = body

    def to_dict(self):
        return {
            "type": "TraverseNode",
            "var_name": self.var_name,
            "start_val": self.start_val.to_dict(),
            "end_val": self.end_val.to_dict(),
            "step_val": self.step_val.to_dict() if self.step_val else None,
            "body": [stmt.to_dict() for stmt in self.body]
        }

class UntilNode(ASTNode):
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body

    def to_dict(self):
        return {
            "type": "UntilNode",
            "condition": self.condition.to_dict(),
            "body": [stmt.to_dict() for stmt in self.body]
        }

class AttemptTrapConcludeNode(ASTNode):
    def __init__(self, attempt_body, trap_clauses, conclude_clause, peek=False):
        self.attempt_body = attempt_body
        self.trap_clauses = trap_clauses
        self.conclude_clause = conclude_clause
        self.peek = peek

    def to_dict(self):
        return {
            "type": "AttemptTrapConcludeNode",
            "attempt_body": [stmt.to_dict() for stmt in self.attempt_body],
            "trap_clauses": [
                {
                    "error_type": error_type,
                    "body": [stmt.to_dict() for stmt in body]
                } for error_type, body in self.trap_clauses
            ],
            "conclude_clause": [stmt.to_dict() for stmt in self.conclude_clause] if self.conclude_clause else None,
            "peek": self.peek
        }

class BlueprintNode(ASTNode):
    def __init__(self, name, attributes, methods, docstring=None, constructor=None, parent=None):
        self.name = name
        self.attributes = attributes
        self.methods = methods
        self.docstring = docstring
        self.constructor = constructor
        self.parent = parent

    def to_dict(self):
        return {
            "type": "BlueprintNode",
            "name": self.name,
            "attributes": [attr.to_dict() for attr in self.attributes],
            "methods": [method.to_dict() for method in self.methods],
            "docstring": self.docstring,
            "constructor": self.constructor.to_dict() if self.constructor else None,
            "parent": self.parent.to_dict() if hasattr(self.parent, 'to_dict') else self.parent
        }

class AttributeAccessNode(ASTNode):
    def __init__(self, obj, attribute):
        self.obj = obj
        self.attribute = attribute

    def to_dict(self):
        return {
            "type": "AttributeAccessNode",
            "object": self.obj.to_dict(),
            "attribute": self.attribute
        }

class SpawnNode(ASTNode):
    def __init__(self, blueprint_name, arguments):
        self.blueprint_name = blueprint_name
        self.arguments = arguments

    def to_dict(self):
        return {
            "type": "SpawnNode",
            "blueprint_name": self.blueprint_name,
            "arguments": [arg.to_dict() for arg in self.arguments]
        }

@dataclass
class DenNode(ASTNode):
    params: list[str]
    body: ASTNode

    def to_dict(self):
        return {
            "type": "DenNode",
            "params": self.params,
            "body": self.body.to_dict(),
        }

@dataclass
class ConvertNode(ASTNode):
    expression: ASTNode
    target_type: str

    def to_dict(self):
        return {"type": "ConvertNode", "expression": self.expression.to_dict(), "target_type": self.target_type}

class ToolkitNode(ASTNode):
    def __init__(self, name, body):
        self.name = name
        self.body = body

    def to_dict(self):
        return {
            "type": "ToolkitNode",
            "name": self.name,
            "body": [stmt.to_dict() for stmt in self.body]
        }

class PlugNode(ASTNode):
    def __init__(self, toolkit_name, file_path):
        self.toolkit_name = toolkit_name
        self.file_path = file_path

    def to_dict(self):
        return {
            "type": "PlugNode",
            "toolkit_name": self.toolkit_name,
            "file_path": self.file_path
        }

class BridgeNode(ASTNode):
    def __init__(self, name, body):
        self.name = name
        self.body = body

    def to_dict(self):
        return {
            "type": "BridgeNode",
            "name": self.name,
            "body": [stmt.to_dict() for stmt in self.body]
        }

class InletNode(ASTNode):
    def __init__(self, body):
        self.body = body

    def to_dict(self):
        return {
            "type": "InletNode",
            "body": [stmt.to_dict() for stmt in self.body]
        }

class LinkNode(ASTNode):
    def __init__(self, greeter, implementation):
        self.greeter = greeter
        self.implementation = implementation

    def to_dict(self):
        return {
            "type": "LinkNode",
            "greeter": self.greeter.to_dict(),
            "implementation": self.implementation.to_dict()
        }

class InterpolatedStringNode(ASTNode):
    def __init__(self, parts):
        self.parts = parts

    def to_dict(self):
        return {"type": "InterpolatedStringNode", "parts": [part.to_dict() for part in self.parts]}



class AskNode(ASTNode):
    def __init__(self, body):
        self.body = body

    def to_dict(self):
        return {"type": "AskNode", "body": [stmt.to_dict() for stmt in self.body]}

class AuthenNode(ASTNode):
    def __init__(self, body):
        self.body = body

    def to_dict(self):
        return {"type": "AuthenNode", "body": [stmt.to_dict() for stmt in self.body]}

class TransformNode(ASTNode):
    def __init__(self, body):
        self.body = body

    def to_dict(self):
        return {"type": "TransformNode", "body": [stmt.to_dict() for stmt in self.body]}

class CondenseNode(ASTNode):
    def __init__(self, body):
        self.body = body

    def to_dict(self):
        return {"type": "CondenseNode", "body": [stmt.to_dict() for stmt in self.body]}

class PackNode(ASTNode):
    def __init__(self, body):
        self.body = body

    def to_dict(self):
        return {"type": "PackNode", "body": [stmt.to_dict() for stmt in self.body]}

class UnpackNode(ASTNode):
    def __init__(self, body):
        self.body = body

    def to_dict(self):
        return {"type": "UnpackNode", "body": [stmt.to_dict() for stmt in self.body]}

@dataclass
class ConstructorNode(ASTNode):
    params: list[str]
    body: list[ASTNode]

    def to_dict(self):
        return {
            "type": "ConstructorNode",
            "params": self.params,
            "body": [stmt.to_dict() for stmt in self.body],
        }

class HaltNode(ASTNode):
    def to_dict(self):
        return {"type": "HaltNode"}

class ProceedNode(ASTNode):
    def to_dict(self):
        return {"type": "ProceedNode"}

class WaitNode(ASTNode):
    def __init__(self, duration):
        self.duration = duration

    def to_dict(self):
        return {"type": "WaitNode", "duration": self.duration.to_dict()}

class TriggerNode(ASTNode):
    def __init__(self, error_name, message):
        self.error_name = error_name
        self.message = message

    def to_dict(self):
        name = self.error_name if isinstance(self.error_name, str) else getattr(self.error_name, 'value', str(self.error_name))
        msg = self.message.value if hasattr(self.message, 'value') else str(self.message)
        return {"type": "TriggerNode", "error_name": name, "message": msg}

class BlameNode(ASTNode):
    def __init__(self, name, body):
        self.name = name
        self.body = body

    def to_dict(self):
        return {"type": "BlameNode", "name": self.name, "body": [stmt.to_dict() for stmt in self.body]}

class TypeNode(ASTNode):
    def __init__(self, type_name):
        self.type_name = type_name

    def to_dict(self):
        return {"type": "TypeNode", "type_name": self.type_name}

class KindNode(ASTNode):
    def __init__(self, expression):
        self.expression = expression

    def to_dict(self):
        return {"type": "KindNode", "expression": self.expression.to_dict()}

class NickNode(ASTNode):
    def __init__(self, original, alias):
        self.original = original
        self.alias = alias

    def to_dict(self):
        return {"type": "NickNode", "original": self.original, "alias": self.alias}

class HiddenNode(ASTNode):
    def __init__(self, declaration):
        self.declaration = declaration

    def to_dict(self):
        return {"type": "HiddenNode", "declaration": self.declaration.to_dict()}

class ShieldedNode(ASTNode):
    def __init__(self, declaration):
        self.declaration = declaration

    def to_dict(self):
        return {"type": "ShieldedNode", "declaration": self.declaration.to_dict()}

class InternalNode(ASTNode):
    def __init__(self, declaration):
        self.declaration = declaration

    def to_dict(self):
        return {"type": "InternalNode", "declaration": self.declaration.to_dict()}

class EmbedNode(ASTNode):
    def __init__(self, body):
        self.body = body

    def to_dict(self):
        return {"type": "EmbedNode", "body": [stmt.to_dict() for stmt in self.body]}

class ParalNode(ASTNode):
    def __init__(self, body):
        self.body = body

    def to_dict(self):
        return {"type": "ParalNode", "body": [stmt.to_dict() for stmt in self.body]}

class HoldNode(ASTNode):
    def __init__(self, body):
        self.body = body

    def to_dict(self):
        return {"type": "HoldNode", "body": [stmt.to_dict() for stmt in self.body]}

class SignalNode(ASTNode):
    def __init__(self, body):
        self.body = body

    def to_dict(self):
        return {"type": "SignalNode", "body": [stmt.to_dict() for stmt in self.body]}

class ListenNode(ASTNode):
    def __init__(self, body):
        self.body = body

    def to_dict(self):
        return {"type": "ListenNode", "body": [stmt.to_dict() for stmt in self.body]}
