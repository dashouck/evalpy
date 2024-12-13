# 
import os
import readline

import log as l
import env as e

HISTORY_FILE = os.path.expanduser("~/.custom_repl_history")
global_env = e.init_global_env()

def parse(program):
    "read expression from a string"
    return read_tokens(tokenize(program))


def tokenize(s):
    "convert string into a list of tokens"
    return s.replace('(',' ( ').replace(')',' ) ').split()


def read_tokens(tokens):
    "read expressions from a list of tokens"
    if (len(tokens) == 0):
        l.error("zero tokens")
        return None
    token = tokens.pop(0)
    if token == '(':
        sub_list = []
        while tokens[0] != ')':
            sub_list.append(read_tokens(tokens))
        tokens.pop(0)
        return sub_list
    elif token == ')':
        l.error("unexpected )")
        return None
    else:
        return atom(token)
    

def is_int_or_float(string):
    try:
        value = float(string)
        if value.is_integer():
            return "int"
        else:
            return "float"
    except ValueError:
        return "nan"
    

def atom(token):
    "numbers stay numbers and everything else is a symbol"
    if is_int_or_float(token) == "int":
        return int(token)
    elif is_int_or_float(token) == "float":
        return float(token)
    else:
        return str(token)


def eval(x):
    # l.info(f"eval({x}), {type(x)}")

    if isinstance(x, str): # variable 
        # l.info(f"looking for var {x}: {global_env.find(x)}")
        return global_env.find(x)
    elif not isinstance(x, list): # literal
        # l.info("yep, literal")
        return x
    elif x[0] == 'def': # (def var exp)
        (_, var, exp) = x
        global_env[var] = eval(exp)
        # print(global_env)
    else:
        proc = eval(x[0])
        args = [eval(exp) for exp in x[1:]]

        return proc(*args)


def repl():
    "infinite loop for repl"

    if os.path.exists(HISTORY_FILE):
        readline.read_history_file(HISTORY_FILE)

    try:
        print("Type 'exit or 'quit' to exit.")
        while True:
            prompt = "\033[1;32m>>> \033[0m"
            program = input(prompt)
            if program in {'exit', 'quit', 'q'}:
                l.info("Exiting...")
                break
            try:
                program = parse(program)
                l.info(f"parsed program: {program}")
                result = eval(program)
                if result is not None:
                    print(result)
            except Exception as e:
                l.error(f"Error: {e}")
    except KeyboardInterrupt:
        # ctrl c
        l.error("\nKeyboard interrupt detected. Exiting...")
    except EOFError:
        # ctrl d
        l.error("\nEnd of input detected. Exiting...")
    finally:
        readline.write_history_file(HISTORY_FILE)


if __name__=="__main__":
    print(global_env)
    repl()
