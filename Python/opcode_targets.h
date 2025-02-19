static void *opcode_targets[256] = {
    &&_unknown_opcode,
    &&TARGET_BINARY_OP_ADAPTIVE,
    &&TARGET_WITH_EXCEPT_START,
    &&TARGET_BINARY_OP_ADD_INT,
    &&TARGET_RETURN_GENERATOR,
    &&TARGET_BINARY_OP_ADD_FLOAT,
    &&TARGET_BINARY_OP_ADD_UNICODE,
    &&TARGET_BINARY_OP_INPLACE_ADD_UNICODE,
    &&TARGET_PREP_RERAISE_STAR,
    &&TARGET_BINARY_OP_MULTIPLY_INT,
    &&TARGET_BINARY_OP_MULTIPLY_FLOAT,
    &&TARGET_BINARY_OP_SUBTRACT_INT,
    &&TARGET_BINARY_OP_SUBTRACT_FLOAT,
    &&TARGET_GET_YIELD_FROM_ITER,
    &&TARGET_IMPORT_STAR,
    &&TARGET_MATCH_KEYS,
    &&TARGET_COMPARE_OP_ADAPTIVE,
    &&TARGET_COMPARE_OP_FLOAT_JUMP,
    &&TARGET_DELETE_SUBSCR,
    &&TARGET_COMPARE_OP_INT_JUMP,
    &&TARGET_COMPARE_OP_STR_JUMP,
    &&TARGET_POP_TOP,
    &&TARGET_BINARY_SUBSCR_ADAPTIVE,
    &&TARGET_BINARY_SUBSCR_GETITEM,
    &&TARGET_GET_AWAITABLE,
    &&TARGET_BINARY_SUBSCR_LIST_INT,
    &&TARGET_UNARY_POSITIVE,
    &&TARGET_BINARY_SUBSCR_TUPLE_INT,
    &&TARGET_BINARY_SUBSCR_DICT,
    &&TARGET_GET_LEN,
    &&TARGET_GET_AITER,
    &&TARGET_MATCH_MAPPING,
    &&TARGET_LIST_TO_TUPLE,
    &&TARGET_STORE_SUBSCR_ADAPTIVE,
    &&TARGET_STORE_SUBSCR_LIST_INT,
    &&TARGET_STORE_SUBSCR_DICT,
    &&TARGET_MATCH_SEQUENCE,
    &&TARGET_CALL_ADAPTIVE,
    &&TARGET_GET_ITER,
    &&TARGET_STORE_SUBSCR,
    &&TARGET_CALL_BUILTIN_CLASS,
    &&TARGET_CALL_NO_KW_BUILTIN_O,
    &&TARGET_CALL_NO_KW_BUILTIN_FAST,
    &&TARGET_CALL_BUILTIN_FAST_WITH_KEYWORDS,
    &&TARGET_CALL_NO_KW_LEN,
    &&TARGET_CALL_NO_KW_ISINSTANCE,
    &&TARGET_CALL_PY_EXACT_ARGS,
    &&TARGET_BEFORE_ASYNC_WITH,
    &&TARGET_POP_EXCEPT,
    &&TARGET_PRINT_EXPR,
    &&TARGET_CALL_PY_WITH_DEFAULTS,
    &&TARGET_UNARY_NEGATIVE,
    &&TARGET_CALL_NO_KW_LIST_APPEND,
    &&TARGET_END_ASYNC_FOR,
    &&TARGET_BEFORE_WITH,
    &&TARGET_CALL_NO_KW_METHOD_DESCRIPTOR_O,
    &&TARGET_CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS,
    &&TARGET_CALL_NO_KW_STR_1,
    &&TARGET_LOAD_BUILD_CLASS,
    &&TARGET_CALL_NO_KW_TUPLE_1,
    &&TARGET_CALL_NO_KW_TYPE_1,
    &&TARGET_CALL_NO_KW_METHOD_DESCRIPTOR_FAST,
    &&TARGET_YIELD_VALUE,
    &&TARGET_JUMP_ABSOLUTE_QUICK,
    &&TARGET_LOAD_ATTR_ADAPTIVE,
    &&TARGET_LOAD_ATTR_INSTANCE_VALUE,
    &&TARGET_ASYNC_GEN_WRAP,
    &&TARGET_SETUP_ANNOTATIONS,
    &&TARGET_UNARY_NOT,
    &&TARGET_LOAD_ATTR_WITH_HINT,
    &&TARGET_LOAD_ATTR_SLOT,
    &&TARGET_LOAD_ATTR_MODULE,
    &&TARGET_GET_ANEXT,
    &&TARGET_LOAD_GLOBAL_ADAPTIVE,
    &&TARGET_LOAD_GLOBAL_MODULE,
    &&TARGET_RETURN_VALUE,
    &&TARGET_BINARY_SUBSCR,
    &&TARGET_LOAD_GLOBAL_BUILTIN,
    &&TARGET_LOAD_METHOD_ADAPTIVE,
    &&TARGET_LOAD_METHOD_CACHED,
    &&TARGET_UNARY_INVERT,
    &&TARGET_LOAD_ASSERTION_ERROR,
    &&TARGET_LOAD_METHOD_CLASS,
    &&TARGET_LOAD_METHOD_MODULE,
    &&TARGET_PUSH_EXC_INFO,
    &&TARGET_LOAD_METHOD_NO_DICT,
    &&TARGET_RESUME_QUICK,
    &&TARGET_STORE_ATTR_ADAPTIVE,
    &&TARGET_STORE_ATTR_INSTANCE_VALUE,
    &&TARGET_NOP,
    &&TARGET_LOAD_FAST,
    &&TARGET_LOAD_GLOBAL,
    &&TARGET_COPY,
    &&TARGET_JUMP_IF_FALSE_OR_POP,
    &&TARGET_LOAD_ATTR,
    &&TARGET_JUMP_NO_INTERRUPT,
    &&TARGET_CONTAINS_OP,
    &&TARGET_BINARY_OP,
    &&TARGET_UNPACK_EX,
    &&TARGET_DELETE_NAME,
    &&TARGET_UNPACK_SEQUENCE,
    &&TARGET_JUMP_FORWARD,
    &&TARGET_STORE_ATTR_SLOT,
    &&TARGET_BUILD_SLICE,
    &&TARGET_SEND,
    &&TARGET_RAISE_VARARGS,
    &&TARGET_BUILD_SET,
    &&TARGET_DELETE_DEREF,
    &&TARGET_STORE_ATTR_WITH_HINT,
    &&TARGET_IMPORT_NAME,
    &&TARGET_SWAP,
    &&TARGET_LOAD_CONST,
    &&TARGET_STORE_DEREF,
    &&TARGET_RERAISE,
    &&TARGET_STORE_FAST,
    &&TARGET_DELETE_FAST,
    &&TARGET_MAKE_CELL,
    &&TARGET_STORE_NAME,
    &&TARGET_CALL_FUNCTION_EX,
    &&TARGET_POP_JUMP_IF_NOT_NONE,
    &&TARGET_JUMP_IF_NOT_EG_MATCH,
    &&TARGET_IMPORT_FROM,
    &&TARGET_POP_JUMP_IF_NONE,
    &&TARGET_DELETE_GLOBAL,
    &&TARGET_DELETE_ATTR,
    &&TARGET_LOAD_NAME,
    &&TARGET_COMPARE_OP,
    &&TARGET_IS_OP,
    &&TARGET_STORE_GLOBAL,
    &&TARGET_POP_JUMP_IF_TRUE,
    &&TARGET_LOAD_DEREF,
    &&TARGET_FOR_ITER,
    &&TARGET_LOAD_FAST__LOAD_FAST,
    &&TARGET_BUILD_TUPLE,
    &&TARGET_JUMP_IF_TRUE_OR_POP,
    &&TARGET_POP_JUMP_IF_FALSE,
    &&TARGET_BUILD_MAP,
    &&TARGET_LOAD_CLOSURE,
    &&TARGET_JUMP_IF_NOT_EXC_MATCH,
    &&TARGET_STORE_FAST__LOAD_FAST,
    &&TARGET_JUMP_ABSOLUTE,
    &&TARGET_MAKE_FUNCTION,
    &&TARGET_STORE_ATTR,
    &&TARGET_BUILD_LIST,
    &&TARGET_EXTENDED_ARG,
    &&TARGET_LOAD_FAST__LOAD_CONST,
    &&TARGET_DICT_UPDATE,
    &&TARGET_FORMAT_VALUE,
    &&TARGET_PRECALL_METHOD,
    &&TARGET_LOAD_CONST__LOAD_FAST,
    &&TARGET_LIST_EXTEND,
    &&TARGET_SET_UPDATE,
    &&TARGET_STORE_FAST__STORE_FAST,
    &&_unknown_opcode,
    &&_unknown_opcode,
    &&TARGET_KW_NAMES,
    &&_unknown_opcode,
    &&_unknown_opcode,
    &&TARGET_CALL,
    &&_unknown_opcode,
    &&TARGET_LOAD_METHOD,
    &&TARGET_BUILD_STRING,
    &&_unknown_opcode,
    &&_unknown_opcode,
    &&TARGET_DICT_MERGE,
    &&TARGET_MAP_ADD,
    &&_unknown_opcode,
    &&TARGET_BUILD_CONST_KEY_MAP,
    &&TARGET_MATCH_CLASS,
    &&_unknown_opcode,
    &&_unknown_opcode,
    &&TARGET_COPY_FREE_VARS,
    &&TARGET_LOAD_CLASSDEREF,
    &&TARGET_SET_ADD,
    &&_unknown_opcode,
    &&_unknown_opcode,
    &&_unknown_opcode,
    &&TARGET_PRECALL_FUNCTION,
    &&_unknown_opcode,
    &&TARGET_LIST_APPEND,
    &&TARGET_RESUME,
    &&_unknown_opcode,
    &&_unknown_opcode,
    &&_unknown_opcode,
    &&_unknown_opcode,
    &&_unknown_opcode,
    &&_unknown_opcode,
    &&_unknown_opcode,
    &&_unknown_opcode,
    &&_unknown_opcode,
    &&_unknown_opcode,
    &&_unknown_opcode,
    &&_unknown_opcode,
    &&_unknown_opcode,
    &&_unknown_opcode,
    &&_unknown_opcode,
    &&_unknown_opcode,
    &&_unknown_opcode,
    &&_unknown_opcode,
    &&_unknown_opcode,
    &&_unknown_opcode,
    &&_unknown_opcode,
    &&_unknown_opcode,
    &&_unknown_opcode,
    &&_unknown_opcode,
    &&_unknown_opcode,
    &&_unknown_opcode,
    &&_unknown_opcode,
    &&_unknown_opcode,
    &&_unknown_opcode,
    &&_unknown_opcode,
    &&_unknown_opcode,
    &&_unknown_opcode,
    &&_unknown_opcode,
    &&_unknown_opcode,
    &&_unknown_opcode,
    &&_unknown_opcode,
    &&_unknown_opcode,
    &&_unknown_opcode,
    &&_unknown_opcode,
    &&_unknown_opcode,
    &&_unknown_opcode,
    &&_unknown_opcode,
    &&_unknown_opcode,
    &&_unknown_opcode,
    &&_unknown_opcode,
    &&_unknown_opcode,
    &&_unknown_opcode,
    &&_unknown_opcode,
    &&_unknown_opcode,
    &&_unknown_opcode,
    &&_unknown_opcode,
    &&_unknown_opcode,
    &&_unknown_opcode,
    &&_unknown_opcode,
    &&_unknown_opcode,
    &&_unknown_opcode,
    &&_unknown_opcode,
    &&_unknown_opcode,
    &&_unknown_opcode,
    &&_unknown_opcode,
    &&_unknown_opcode,
    &&_unknown_opcode,
    &&_unknown_opcode,
    &&_unknown_opcode,
    &&_unknown_opcode,
    &&_unknown_opcode,
    &&_unknown_opcode,
    &&_unknown_opcode,
    &&_unknown_opcode,
    &&_unknown_opcode,
    &&_unknown_opcode,
    &&_unknown_opcode,
    &&_unknown_opcode,
    &&_unknown_opcode,
    &&TARGET_DO_TRACING
};
