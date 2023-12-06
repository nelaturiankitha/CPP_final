import ast
import sys
import os
import argparse

class CallGraphVisitor(ast.NodeVisitor):
    def __init__(self):
        self.graph = {}

    def visit_Call(self, node):
        caller = getattr(node.func, 'id', str(node.func))
        if isinstance(node.func, ast.Name):
            callee = node.func.id
            self.graph.setdefault(caller, []).append(callee)
        self.generic_visit(node)

def generate_call_graph(file_path):
    with open(file_path, 'r') as file:
        source_code = file.read()

    try:
        tree = ast.parse(source_code)
    except SyntaxError:
        raise

    visitor = CallGraphVisitor()
    visitor.visit(tree)
    return visitor.graph

def save_call_graph(call_graph, file_path):
    with open(file_path, 'w') as file:
        for caller, callees in call_graph.items():
            file.write(f"{caller} calls:\n")
            for callee in callees:
                file.write(f"    {callee}\n")

def check_python_files(python_files: list[str]) -> str:
    for python_file in python_files:
        if not os.path.isfile(python_file):
            raise FileNotFoundError(f"{python_file} does not exist.")
    return python_files[0]

def print_call_graph(call_graph):
    for caller, callees in call_graph.items():
        print(f"{caller} calls:")
        for callee in callees:
            print(f"    {callee}")

def main():
    parser = argparse.ArgumentParser(description="Generate call graph for a Python file.")
    parser.add_argument('python_file', help="The Python file to analyze.")
    args = parser.parse_args()

    python_file = args.python_file
    try:
        python_file = check_python_files([python_file])
        call_graph = generate_call_graph(python_file)
        print_call_graph(call_graph)
    except FileNotFoundError as e:
        print(e)
        sys.exit(1)
    except SyntaxError as e:
        print(f"Error: {python_file} contains a syntax error.")
        sys.exit(1)

if __name__ == "__main__":
    main()