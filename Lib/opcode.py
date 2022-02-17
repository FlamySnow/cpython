
"""
opcode module - potentially shared between dis and other modules which
operate on bytecodes (e.g. peephole optimizers).
"""

__all__ = ["cmp_op", "hasconst", "hasname", "hasjrel", "hasjabs",
           "haslocal", "hascompare", "hasfree", "opname", "opmap",
           "HAVE_ARGUMENT", "EXTENDED_ARG", "hasnargs"]

# It's a chicken-and-egg I'm afraid:
# We're imported before _opcode's made.
# With exception unheeded
# (stack_effect is not needed)
# Both our chickens and eggs are allayed.
#     --Larry Hastings, 2013/11/23

import random

cmp_op = ('<', '<=', '==', '!=', '>', '>=')

hasconst = []
hasname = []
hasjrel = []
hasjabs = []
haslocal = []
hascompare = []
hasfree = []
hasnargs = [] # unused

opmap = {}
opname = ['<%r>' % (op,) for op in range(256)]

busy_opcodes = []


def gen_opcode(a, b):
    opcode = random.randint(a, b)
    while opcode in busy_opcodes:
        opcode = random.randint(a, b)
    busy_opcodes.append(opcode)
    return opcode

def def_op(name, op):
    opname[op] = name
    opmap[name] = op

def name_op(name, op):
    def_op(name, op)
    hasname.append(op)

def jrel_op(name, op):
    def_op(name, op)
    hasjrel.append(op)

def jabs_op(name, op):
    def_op(name, op)
    hasjabs.append(op)

# Instruction opcodes for compiled code
# Blank lines correspond to available opcodes

def_op('POP_TOP', gen_opcode(0, 89))

def_op('NOP', gen_opcode(0, 89))
def_op('UNARY_POSITIVE', gen_opcode(0, 89))
def_op('UNARY_NEGATIVE', gen_opcode(0, 89))
def_op('UNARY_NOT', gen_opcode(0, 89))

def_op('UNARY_INVERT', gen_opcode(0, 89))

def_op('BINARY_SUBSCR', gen_opcode(0, 89))

def_op('GET_LEN', gen_opcode(0, 89))
def_op('MATCH_MAPPING', gen_opcode(0, 89))
def_op('MATCH_SEQUENCE', gen_opcode(0, 89))
def_op('MATCH_KEYS', gen_opcode(0, 89))

def_op('PUSH_EXC_INFO', gen_opcode(0, 89))

def_op('WITH_EXCEPT_START', gen_opcode(0, 89))
def_op('GET_AITER', gen_opcode(0, 89))
def_op('GET_ANEXT', gen_opcode(0, 89))
def_op('BEFORE_ASYNC_WITH', gen_opcode(0, 89))
def_op('BEFORE_WITH', gen_opcode(0, 89))
def_op('END_ASYNC_FOR', gen_opcode(0, 89))

def_op('STORE_SUBSCR', gen_opcode(0, 89))
def_op('DELETE_SUBSCR', gen_opcode(0, 89))

def_op('GET_ITER', gen_opcode(0, 89))
def_op('GET_YIELD_FROM_ITER', gen_opcode(0, 89))
def_op('PRINT_EXPR', gen_opcode(0, 89))
def_op('LOAD_BUILD_CLASS', gen_opcode(0, 89))

def_op('GET_AWAITABLE', gen_opcode(0, 89))
def_op('LOAD_ASSERTION_ERROR', gen_opcode(0, 89))
def_op('RETURN_GENERATOR', gen_opcode(0, 89))

def_op('LIST_TO_TUPLE', gen_opcode(0, 89))
def_op('RETURN_VALUE', gen_opcode(0, 89))
def_op('IMPORT_STAR', gen_opcode(0, 89))
def_op('SETUP_ANNOTATIONS', gen_opcode(0, 89))
def_op('YIELD_VALUE', gen_opcode(0, 89))
def_op('ASYNC_GEN_WRAP', gen_opcode(0, 89))
def_op('PREP_RERAISE_STAR', gen_opcode(0, 89))
def_op('POP_EXCEPT', gen_opcode(0, 89))

HAVE_ARGUMENT = 90              # Opcodes from here have an argument:

name_op('STORE_NAME', gen_opcode(90, 143))       # Index in name list
name_op('DELETE_NAME', gen_opcode(90, 143))      # ""
def_op('UNPACK_SEQUENCE', gen_opcode(90, 143))   # Number of tuple items
jrel_op('FOR_ITER', gen_opcode(90, 143))
def_op('UNPACK_EX', gen_opcode(90, 143))
name_op('STORE_ATTR', gen_opcode(90, 143))       # Index in name list
name_op('DELETE_ATTR', gen_opcode(90, 143))      # ""
name_op('STORE_GLOBAL', gen_opcode(90, 143))     # ""
name_op('DELETE_GLOBAL', gen_opcode(90, 143))    # ""
def_op('SWAP', gen_opcode(90, 143))
_load_const = gen_opcode(90, 143)
def_op('LOAD_CONST', _load_const)       # Index in const list
hasconst.append(_load_const)
name_op('LOAD_NAME', gen_opcode(90, 143))       # Index in name list
def_op('BUILD_TUPLE', gen_opcode(90, 143))      # Number of tuple items
def_op('BUILD_LIST', gen_opcode(90, 143))       # Number of list items
def_op('BUILD_SET', gen_opcode(90, 143))        # Number of set items
def_op('BUILD_MAP', gen_opcode(90, 143))        # Number of dict entries
name_op('LOAD_ATTR', gen_opcode(90, 143))       # Index in name list
_comp_op = gen_opcode(90, 143)
def_op('COMPARE_OP', _comp_op)       # Comparison operator
hascompare.append(_comp_op)
name_op('IMPORT_NAME', gen_opcode(90, 143))     # Index in name list
name_op('IMPORT_FROM', gen_opcode(90, 143))     # Index in name list
jrel_op('JUMP_FORWARD', gen_opcode(90, 143))    # Number of bytes to skip
jabs_op('JUMP_IF_FALSE_OR_POP', gen_opcode(90, 143)) # Target byte offset from beginning of code
jabs_op('JUMP_IF_TRUE_OR_POP', gen_opcode(90, 143))  # ""
jabs_op('JUMP_ABSOLUTE', gen_opcode(90, 143))        # ""
jabs_op('POP_JUMP_IF_FALSE', gen_opcode(90, 143))    # ""
jabs_op('POP_JUMP_IF_TRUE', gen_opcode(90, 143))     # ""
name_op('LOAD_GLOBAL', gen_opcode(90, 143))     # Index in name list
def_op('IS_OP', gen_opcode(90, 143))
def_op('CONTAINS_OP', gen_opcode(90, 143))
def_op('RERAISE', gen_opcode(90, 143))
def_op('COPY', gen_opcode(90, 143))
jabs_op('JUMP_IF_NOT_EXC_MATCH', gen_opcode(90, 143))
def_op('BINARY_OP', gen_opcode(90, 143))
jrel_op('SEND', gen_opcode(90, 143)) # Number of bytes to skip
_lf = gen_opcode(90, 143)
def_op('LOAD_FAST', _lf)        # Local variable number
haslocal.append(_lf)
_st_f = gen_opcode(90, 143)
def_op('STORE_FAST', _st_f)       # Local variable number
haslocal.append(_st_f)
del_fast = gen_opcode(90, 143)
def_op('DELETE_FAST', del_fast)      # Local variable number
haslocal.append(del_fast)
jabs_op('JUMP_IF_NOT_EG_MATCH', gen_opcode(90, 143))
jabs_op('POP_JUMP_IF_NOT_NONE', gen_opcode(90, 143))
jabs_op('POP_JUMP_IF_NONE', gen_opcode(90, 143))
def_op('RAISE_VARARGS', gen_opcode(90, 143))    # Number of raise arguments (1, 2, or 3)

def_op('MAKE_FUNCTION', gen_opcode(90, 143))    # Flags
def_op('BUILD_SLICE', gen_opcode(90, 143))      # Number of items
jabs_op('JUMP_NO_INTERRUPT', gen_opcode(90, 143)) # Target byte offset from beginning of code
make_cell = gen_opcode(90, 143)
def_op('MAKE_CELL', make_cell)
hasfree.append(make_cell)
load_closure = gen_opcode(90, 143)
def_op('LOAD_CLOSURE', load_closure)
hasfree.append(load_closure)
load_deref = gen_opcode(90, 143)
def_op('LOAD_DEREF', load_deref)
hasfree.append(load_deref)
tmp = gen_opcode(90, 143)
def_op('STORE_DEREF', tmp)
hasfree.append(tmp)
tmp = gen_opcode(90, 143)
def_op('DELETE_DEREF', tmp)
hasfree.append(tmp)

def_op('CALL_FUNCTION_EX', gen_opcode(90, 143))  # Flags

def_op('EXTENDED_ARG', 144)
EXTENDED_ARG = 144
def_op('LIST_APPEND', gen_opcode(145, 180))
def_op('SET_ADD', gen_opcode(145, 180))
def_op('MAP_ADD', gen_opcode(145, 180))
tmp = gen_opcode(145, 180)
def_op('LOAD_CLASSDEREF', tmp)
hasfree.append(tmp)
def_op('COPY_FREE_VARS', gen_opcode(145, 180))

def_op('RESUME', gen_opcode(145, 180))
def_op('MATCH_CLASS', gen_opcode(145, 180))

def_op('FORMAT_VALUE', gen_opcode(145, 180))
def_op('BUILD_CONST_KEY_MAP', gen_opcode(145, 180))
def_op('BUILD_STRING', gen_opcode(145, 180))

name_op('LOAD_METHOD', gen_opcode(145, 180))

def_op('LIST_EXTEND', gen_opcode(145, 180))
def_op('SET_UPDATE', gen_opcode(145, 180))
def_op('DICT_MERGE', gen_opcode(145, 180))
def_op('DICT_UPDATE', gen_opcode(145, 180))

def_op('PRECALL_FUNCTION', gen_opcode(145, 180))
def_op('PRECALL_METHOD', gen_opcode(145, 180))

def_op('CALL', gen_opcode(145, 180))
tmp = gen_opcode(145, 180)
def_op('KW_NAMES', tmp)
hasconst.append(tmp)

del def_op, name_op, jrel_op, jabs_op

_nb_ops = [
    ("NB_ADD", "+"),
    ("NB_AND", "&"),
    ("NB_FLOOR_DIVIDE", "//"),
    ("NB_LSHIFT", "<<"),
    ("NB_MATRIX_MULTIPLY", "@"),
    ("NB_MULTIPLY", "*"),
    ("NB_REMAINDER", "%"),
    ("NB_OR", "|"),
    ("NB_POWER", "**"),
    ("NB_RSHIFT", ">>"),
    ("NB_SUBTRACT", "-"),
    ("NB_TRUE_DIVIDE", "/"),
    ("NB_XOR", "^"),
    ("NB_INPLACE_ADD", "+="),
    ("NB_INPLACE_AND", "&="),
    ("NB_INPLACE_FLOOR_DIVIDE", "//="),
    ("NB_INPLACE_LSHIFT", "<<="),
    ("NB_INPLACE_MATRIX_MULTIPLY", "@="),
    ("NB_INPLACE_MULTIPLY", "*="),
    ("NB_INPLACE_REMAINDER", "%="),
    ("NB_INPLACE_OR", "|="),
    ("NB_INPLACE_POWER", "**="),
    ("NB_INPLACE_RSHIFT", ">>="),
    ("NB_INPLACE_SUBTRACT", "-="),
    ("NB_INPLACE_TRUE_DIVIDE", "/="),
    ("NB_INPLACE_XOR", "^="),
]

_specialized_instructions = [
    "BINARY_OP_ADAPTIVE",
    "BINARY_OP_ADD_INT",
    "BINARY_OP_ADD_FLOAT",
    "BINARY_OP_ADD_UNICODE",
    "BINARY_OP_INPLACE_ADD_UNICODE",
    "BINARY_OP_MULTIPLY_INT",
    "BINARY_OP_MULTIPLY_FLOAT",
    "BINARY_OP_SUBTRACT_INT",
    "BINARY_OP_SUBTRACT_FLOAT",
    "COMPARE_OP_ADAPTIVE",
    "COMPARE_OP_FLOAT_JUMP",
    "COMPARE_OP_INT_JUMP",
    "COMPARE_OP_STR_JUMP",
    "BINARY_SUBSCR_ADAPTIVE",
    "BINARY_SUBSCR_GETITEM",
    "BINARY_SUBSCR_LIST_INT",
    "BINARY_SUBSCR_TUPLE_INT",
    "BINARY_SUBSCR_DICT",
    "STORE_SUBSCR_ADAPTIVE",
    "STORE_SUBSCR_LIST_INT",
    "STORE_SUBSCR_DICT",
    "CALL_ADAPTIVE",
    "CALL_BUILTIN_CLASS",
    "CALL_NO_KW_BUILTIN_O",
    "CALL_NO_KW_BUILTIN_FAST",
    "CALL_BUILTIN_FAST_WITH_KEYWORDS",
    "CALL_NO_KW_LEN",
    "CALL_NO_KW_ISINSTANCE",
    "CALL_PY_EXACT_ARGS",
    "CALL_PY_WITH_DEFAULTS",
    "CALL_NO_KW_LIST_APPEND",
    "CALL_NO_KW_METHOD_DESCRIPTOR_O",
    "CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS",
    "CALL_NO_KW_STR_1",
    "CALL_NO_KW_TUPLE_1",
    "CALL_NO_KW_TYPE_1",
    "CALL_NO_KW_METHOD_DESCRIPTOR_FAST",
    "JUMP_ABSOLUTE_QUICK",
    "LOAD_ATTR_ADAPTIVE",
    "LOAD_ATTR_INSTANCE_VALUE",
    "LOAD_ATTR_WITH_HINT",
    "LOAD_ATTR_SLOT",
    "LOAD_ATTR_MODULE",
    "LOAD_GLOBAL_ADAPTIVE",
    "LOAD_GLOBAL_MODULE",
    "LOAD_GLOBAL_BUILTIN",
    "LOAD_METHOD_ADAPTIVE",
    "LOAD_METHOD_CACHED",
    "LOAD_METHOD_CLASS",
    "LOAD_METHOD_MODULE",
    "LOAD_METHOD_NO_DICT",
    "RESUME_QUICK",
    "STORE_ATTR_ADAPTIVE",
    "STORE_ATTR_INSTANCE_VALUE",
    "STORE_ATTR_SLOT",
    "STORE_ATTR_WITH_HINT",
    # Super instructions
    "LOAD_FAST__LOAD_FAST",
    "STORE_FAST__LOAD_FAST",
    "LOAD_FAST__LOAD_CONST",
    "LOAD_CONST__LOAD_FAST",
    "STORE_FAST__STORE_FAST",
]
_specialization_stats = [
    "success",
    "failure",
    "hit",
    "deferred",
    "miss",
    "deopt",
]
