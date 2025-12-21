"""
Beacon Language CLI - Cross Platform Entry Point
"""

import sys
import os

# Add root directory to path to allow imports from src
ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT_PATH)

try:
    from src.frontend.lexer import Lexer
    from src.frontend.parser import Parser
    from src.frontend.interpreter import Interpreter
    from src.frontend.frontend import generate_ast_json
except ImportError as e:
    print(f"Critical Error: Could not import Beacon frontend modules: {e}")
    sys.exit(1)


def print_usage():
    """Print usage information"""
    print("""Beacon Programming Language (Cross-Platform)

Usage:
    beacon run <file.bpl>       Run Beacon file with interpreter
    beacon <file.bpl>           Run Beacon file (default mode)
    beacon --help               Show this help message

Examples:
    beacon run hello.bpl        # Interpret and run
    beacon hello.bpl            # Same as 'beacon run hello.bpl'
""")


def run_file(file_path: str):
    """Run a Beacon file using the interpreter"""
    try:
        with open(file_path, 'r') as f:
            source_code = f.read()
    except FileNotFoundError:
        print(f"Error: File not found: {file_path}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}", file=sys.stderr)
        sys.exit(1)
    
    try:
        # Lexing
        lexer = Lexer(source_code)
        tokens = lexer.tokenize()
        
        # Parsing
        parser = Parser(tokens)
        ast = parser.parse()
        
        # Interpreting
        interpreter = Interpreter()
        interpreter.interpret(ast)
        
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


def main():
    """Main CLI entry point"""
    if len(sys.argv) < 2:
        print_usage()
        sys.exit(1)
    
    # Parse command
    first_arg = sys.argv[1]
    
    if first_arg in ['--help', '-h', 'help']:
        print_usage()
        sys.exit(0)
    
    # Determine mode and file
    if first_arg == 'run':
        if len(sys.argv) < 3:
            print("Error: No input file specified", file=sys.stderr)
            print_usage()
            sys.exit(1)
        mode = 'run'
        file_path = sys.argv[2]
    elif first_arg == 'compile':
        print("Error: Compilation to C is not supported in this cross-platform build. Use 'run' mode.", file=sys.stderr)
        sys.exit(1)
    else:
        mode = 'run'
        file_path = first_arg
    
    # Execute based on mode
    if mode == 'run':
        run_file(file_path)


if __name__ == "__main__":
    main()
