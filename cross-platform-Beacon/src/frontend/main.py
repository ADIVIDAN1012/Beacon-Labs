"""
Beacon Language CLI
Main entry point for the Beacon compiler and interpreter
"""

import sys
import os
from lexer import Lexer
from parser import Parser
from interpreter import Interpreter
from frontend import generate_ast_json


def print_usage():
    """Print usage information"""
    print("""Beacon Programming Language

Usage:
    beacon run <file.bpl>       Run Beacon file with interpreter
    beacon compile <file.bpl>   Compile Beacon file to C
    beacon <file.bpl>           Run Beacon file (default mode)
    beacon --help               Show this help message

Examples:
    beacon run hello.bpl        # Interpret and run
    beacon compile hello.bpl    # Compile to C
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


def compile_file(file_path: str):
    """Compile a Beacon file to C"""
    try:
        with open(file_path, 'r') as f:
            source_code = f.read()
    except FileNotFoundError:
        print(f"Error: File not found: {file_path}", file=sys.stderr)
        sys.exit(1)
    
    # Use existing compilation pipeline
    generate_ast_json(source_code)


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
        if len(sys.argv) < 3:
            print("Error: No input file specified", file=sys.stderr)
            print_usage()
            sys.exit(1)
        mode = 'compile'
        file_path = sys.argv[2]
    
    else:
        # Default to compile mode (uses C backend)
        mode = 'compile'
        file_path = first_arg
    
    # Validate file extension
    if not file_path.endswith('.bpl'):
        print(f"Warning: File '{file_path}' does not have .bpl extension", file=sys.stderr)
    
    # Execute based on mode
    if mode == 'run':
        run_file(file_path)
    elif mode == 'compile':
        compile_file(file_path)


if __name__ == "__main__":
    main()
