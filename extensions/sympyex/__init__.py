from sympy import Expr, Equality, latex
from IPython.display import display, Latex


def expressionEqualityExtension(self: Expr, function):
    return Equality(self, function, evaluate=False)


def latexify(self: Expr, mode='plain'):
    return latex(self, mode=mode)


def latexify_inline(self: Expr):
    return latex(self, mode='inline')


def latexify_equation(self: Expr):
    return latex(self, mode='equation')


def display_latex(latex: str):
    return display(Latex(latex))


Expr.eq = expressionEqualityExtension
Expr.latex = latexify
Expr.latex_inline = latexify_inline
Expr.latex_equation = latexify_equation
del expressionEqualityExtension
del latexify
del latexify_inline
del latexify_equation
