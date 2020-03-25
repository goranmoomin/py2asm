import compiler
from compiler.ast import *
def isatom(ast):
    atom_types = (Name, Const)
    return isinstance(ast, atom_types)
def isexpr(ast):
    expr_types = (Add, CallFunc, Const, Div, Mul, Sub, UnaryAdd, UnarySub)
    return isinstance(ast, expr_types)
def issimple(expr):
    if not isexpr(expr):
        raise Exception("Error in issimple: node {} is not an expression"
                        .format(expr))
    if isatom(expr):
        return True
    elif isinstance(expr, (Add, Div, Mul, Sub)):
        return any(isatom(node) for node in [ast.left, ast.right])
    elif isinstance(expr, CallFunc):
        return isatom(expr.node)
    elif isinstance(expr, (UnaryAdd, UnarySub)):
        return isatom(expr.expr)
    else:
        raise Exception("Error in issimple: node {} not recognized"
                        .format(expr))

