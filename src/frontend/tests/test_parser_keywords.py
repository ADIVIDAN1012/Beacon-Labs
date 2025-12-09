from lexer import Lexer
from parser import Parser

def parse_src(src):
    tokens = Lexer(src).tokenize()
    ast = Parser(tokens).parse()
    return ast.to_dict()

def find_nodes_by_type(ast_dict, node_type):
    out = []
    def walk(node):
        if isinstance(node, dict):
            if node.get("type") == node_type:
                out.append(node)
            for v in node.values():
                walk(v)
        elif isinstance(node, list):
            for item in node:
                walk(item)
    walk(ast_dict)
    return out

def test_funcall_produces_function_call_nodes():
    src = """
spec check_greater(val) {
    check (val > 5) {
        show("val is greater than 5")
    } altern {
        show("val is not greater than 5")
    }
}

spec main() {
    firm a = 10
    funcall check_greater(a)
    funcall check_greater(3)
}

funcall main
"""
    ast = parse_src(src)
    calls = find_nodes_by_type(ast, "FunctionCallNode")
    names = [c["function_name"] for c in calls]
    assert "check_greater" in names
    assert "main" in names

def test_string_interpolation_parses():
    src = """
name = "World"
show("Hello, |name|!")
"""
    ast = parse_src(src)
    interps = find_nodes_by_type(ast, "InterpolatedStringNode")
    assert len(interps) == 1

def test_check_altern_structure():
    src = """
check(x > 10) {
    show("gt")
} altern {
    show("le")
}
"""
    ast = parse_src(src)
    checks = find_nodes_by_type(ast, "CheckStatementNode")
    assert len(checks) == 1
    assert checks[0]["altern_clause"] is not None

def test_traverse_parses():
    src = """
traverse i from 1 to 3 {
    show(i)
}
"""
    ast = parse_src(src)
    trav = find_nodes_by_type(ast, "TraverseNode")
    assert len(trav) == 1

def test_until_parses():
    src = """
counter = 0
until counter == 2 {
    counter = counter + 1
}
"""
    ast = parse_src(src)
    nodes = find_nodes_by_type(ast, "UntilNode")
    assert len(nodes) == 1

def test_toolkit_share_expose_parses():
    src = """
toolkit Math {
    share spec add(a, b) {
        forward a + b
    }
}
expose spec noop()
"""
    ast = parse_src(src)
    tk = find_nodes_by_type(ast, "ToolkitNode")
    assert len(tk) == 1
    funcs = find_nodes_by_type(ast, "FunctionDeclNode")
    shared = [f for f in funcs if f.get("shared")]
    assert len(shared) >= 1

def test_blueprint_and_spawn_parses():
    src = """
blueprint Dog {
    shard name
    prep(own, n) {
        own.name = n
    }
}
firm d = spawn Dog("Buddy")
show(d.name)
"""
    ast = parse_src(src)
    bps = find_nodes_by_type(ast, "BlueprintNode")
    assert len(bps) == 1
    spawns = find_nodes_by_type(ast, "SpawnNode")
    assert len(spawns) == 1

def test_attempt_trap_conclude_parses():
    src = """
attempt {
    show("try")
} trap MyError peek {
    show("catch")
} conclude {
    show("finally")
}
"""
    ast = parse_src(src)
    nodes = find_nodes_by_type(ast, "AttemptTrapConcludeNode")
    assert len(nodes) == 1

def test_paral_hold_signal_listen_blocks():
    src = """
paral { show("p") }
hold { show("h") }
signal { show("s") }
listen { show("l") }
"""
    ast = parse_src(src)
    assert len(find_nodes_by_type(ast, "ParalNode")) == 1
    assert len(find_nodes_by_type(ast, "HoldNode")) == 1
    assert len(find_nodes_by_type(ast, "SignalNode")) == 1
    assert len(find_nodes_by_type(ast, "ListenNode")) == 1

def test_transform_condense_pack_unpack_single_expr():
    src = """
transform 1
condense 2
pack 3
unpack 4
"""
    ast = parse_src(src)
    assert len(find_nodes_by_type(ast, "TransformNode")) == 1
    assert len(find_nodes_by_type(ast, "CondenseNode")) == 1
    assert len(find_nodes_by_type(ast, "PackNode")) == 1
    assert len(find_nodes_by_type(ast, "UnpackNode")) == 1
