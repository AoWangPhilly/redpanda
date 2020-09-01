import sympy
from sympy.matrices import Matrix
from sympy.vector import CoordSys3D, matrix_to_vector
from sympy.parsing.sympy_parser import parse_expr


def parse_eq(eq):
    eq = eq.replace('^', '**').replace('e', 'E')
    return parse_expr(eq)


def parse_pt(pt):
    return sympy.Point(list(map(int, pt.replace('(', '').replace(')', '').split(','))))


def parse_var(var):
    return sympy.symbols(' '.join(list(var)))


def parse_matrix(var):
    vec = vec.replace('<', '').replace('>', '').split(',')
    return Matrix(list(map(int, vec)))


def convert(vec):
    C = CoordSys3D('')
    return matrix_to_vector(parse_matrix(vec, C))


if __name__ == '__main__':
    pass