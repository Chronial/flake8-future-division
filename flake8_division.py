from __future__ import absolute_import, print_function, unicode_literals

import ast


__version__ = '0.1'


CODE = 'FD01'


class CheckDivision(object):
    name = 'future-division'
    version = __version__

    def __init__(self, tree, filename):
        self.tree = tree
        self.filename = filename

    def run(self):
        future_import = False
        message = CODE + ': Division without __future__.division import'
        for node in ast.walk(self.tree):
            if (isinstance(node, ast.ImportFrom) and
                    node.module == '__future__' and
                    any(name.name == "division" for name in node.names)):
                future_import = True
            elif isinstance(node, ast.BinOp) and isinstance(node.op, (ast.Div, ast.FloorDiv)):
                if not future_import:
                    yield node.lineno, node.col_offset, message, CheckDivision
