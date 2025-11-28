
from lexer import Lexer
from parser import Parser
import json

def main():
    source_code = """
blueprint MyBlueprint {
    shard my_attribute
    solid my_solid_attribute = 123

    prep(arg1, arg2) {
        own.my_attribute = arg1
    }

    spec my_method(arg1) {
        show(arg1)
    }
}

toolkit MyToolkit {
    share spec my_shared_func() {
        "shared function"
    }
}

bridge MyBridge {
    inlet {
        "inlet"
    }
}

link greeter to implementation

blame MyError {
    "error handling"
}

nick MyType as MyAlias

check(x > 10) {
    show("x is greater than 10")
} alter(x < 10) {
    show("x is less than 10")
} altern {
    show("x is 10")
}

traverse i from 0 to 10 by 1 {
    show(i)
}

until i > 10 {
    i = i + 1
}

attempt {
    show("attempting")
} trap MyError peek {
    show("error caught")
} conclude {
    show("concluded")
}

my_var = "hello"
firm my_const = "world"

show("Hello, |my_var| |my_const|!")
"""
    lexer = Lexer(source_code)
    tokens = lexer.tokenize()
    
    parser = Parser(tokens)
    ast = parser.parse()
    
    print(json.dumps(ast.to_dict(), indent=2))

if __name__ == "__main__":
    main()