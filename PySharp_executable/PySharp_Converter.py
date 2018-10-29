import re


# Function to exchange all operators with those evaluated by python.
def replace_operators(expr):
    REPLACEMENTS = {
        'NOT': ' not ',
        'OR': ' or ',
        'AND': ' and ',
        'XOR': ' ^ ',
        'NAND': ' and ',
        'NOR': ' or ',
        'XNOR': ' ^ ',
    }
    return re.sub('|'.join(re.escape(sym) for sym in REPLACEMENTS.keys()),
                  lambda sym: REPLACEMENTS[sym.group(0)],expr).strip()
