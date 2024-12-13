import math
import operator as op

def init_global_env():
    env = Env()
    env.update(vars(math))
    env.update({
        '+':op.add, '-':op.sub,
        '*':op.mul, '/':op.truediv,
        '<':op.lt, '<=':op.le, 
        '>':op.gt, ">=":op.ge,
        '=':op.eq, '!=':op.ne,
        'abs': abs,
        'length': len,
        'round': round,
        'min': min,
        'max': max,
        'not':     op.not_
    })

    return env

class Env(dict):
    def __init__(self, var_names=(), var_vals=()):
        self.update(zip(var_names, var_vals))
    
    def find(self, var):

        return self.get(var)