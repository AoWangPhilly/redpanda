import regex as re
from collections import defaultdict

import sympy
from sympy.matrices import Matrix
from sympy.vector import CoordSys3D, matrix_to_vector
from sympy.parsing.sympy_parser import parse_expr

valid_math_functions = [
    # Complexes
    'sign', 'abs', 'arg',
    # Trig Inverse
    'asin', 'acos', 'atan', 'acot', 'asec', 'acsc', 'atan2',
    # Hyperbolic
    'sinh', 'cosh', 'tanh', 'coth', 'sech', 'csch',
    # Trig Functions
    'sin', 'cos', 'tan', 'cot', 'sec', 'csc', 'sinc',
    # Hyperbolic Inverses
    'asinh', 'acosh', 'atanh', 'acoth', 'asech', 'acsch',
    # Exponential
    'log',
]

valid_math_functions_regex = '|'.join(valid_math_functions)


def parse_eq(eq, evaluate=False):
    eq = re.sub('(?<=\\w|\\))(?=\\() | (?<=\\))(?=\\w) | (?<=\\d)(?=\\w)', '*', eq, flags=re.X)
    print(eq)
    eq = re.sub('(?<={})\\* '.format(valid_math_functions_regex), '', eq, flags=re.X)
    eq = eq.replace('^', '**').replace('e', 'E')
    print(eq)
    return parse_expr(eq, evaluate=evaluate)


def parse_pt(pt):
    return sympy.Point(list(map(int, pt.replace('(', '').replace(')', '').split(','))))


def parse_var(var):
    return sympy.symbols(' '.join(list(var)))


def parse_matrix(var):
    var = var.replace('<', '').replace('>', '').split(',')
    return Matrix(list(map(int, var)))


def norm_vector(plane):
    plane = sympy.Poly(parse_eq(plane))
    constants = plane.coeffs()[:3]
    return Matrix(constants)


def convert(vec):
    C = CoordSys3D('')
    return matrix_to_vector(parse_matrix(vec), C)


if __name__ == '__main__':
    pass
