#Source: https://stackoverflow.com/questions/39702882/glsl-parser-using-pyparsing-giving-attributeerrors
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) 2014, Nicolas P. Rougier
# Distributed under the (new) BSD License. See LICENSE.txt for more info.
# -----------------------------------------------------------------------------
import pyparsing

keywords = ("attribute const uniform varying break continue do for while"
            "if else"
            "in out inout"
            "float int void bool true false"
            "lowp mediump highp precision invariant"
            "discard return"
            "mat2 mat3 mat4"
            "vec2 vec3 vec4 ivec2 ivec3 ivec4 bvec2 bvec3 bvec4 sampler2D samplerCube"
            "struct")
reserved = ("asm"
            "class union enum typedef template this packed"
            "goto switch default"
            "inline noinline volatile public static extern external"
            "interface flat long short double half fixed unsigned superp"
            "input output"
            "hvec2 hvec3 hvec4 dvec2 dvec3 dvec4 fvec2 fvec3 fvec4 sampler1D sampler3D"
            "sampler1DShadow sampler2DShadow"
            "sampler2DRect sampler3DRect sampler2DRectShadow"
            "sizeof cast"
            "namespace using")
precision = "lowp mediump high"
storage = "const uniform attribute varying"


# Tokens
# ----------------------------------
LPAREN = pyparsing.Literal("(").suppress()
RPAREN = pyparsing.Literal(")").suppress()
LBRACK = pyparsing.Literal("[").suppress()
RBRACK = pyparsing.Literal("]").suppress()
LBRACE = pyparsing.Literal("{").suppress()
RBRACE = pyparsing.Literal("}").suppress()
IDENTIFIER = pyparsing.Word(pyparsing.alphas + '_', pyparsing.alphanums + '_')
TYPE = pyparsing.Word(pyparsing.alphas + '_', pyparsing.alphanums + "_")
END = pyparsing.Literal(";").suppress()
INT = pyparsing.Word(pyparsing.nums)
FLOAT = pyparsing.Regex(
    '[+-]?(((\d+\.\d*)|(\d*\.\d+))([eE][-+]?\d+)?)|(\d*[eE][+-]?\d+)')
STORAGE = pyparsing.Regex('|'.join(storage.split(' ')))
PRECISION = pyparsing.Regex('|'.join(precision.split(' ')))
STRUCT = pyparsing.Literal("struct").suppress()


# ------------------------
def get_prototypes(code):
    """
    Get all function declarations

    Code example
    ------------

    mediump vec3 function_1(vec4);
    vec3 function_2(float a, float b);
    """

    PARAMETER = pyparsing.Group(pyparsing.Optional(PRECISION).setResultsName("precision") +
                                TYPE.setResultsName("type") +
                                pyparsing.Optional(IDENTIFIER).setResultsName("name"))
    PARAMETERS = pyparsing.delimitedList(PARAMETER).setResultsName(
        "arg", listAllMatches=True)
    PROTOTYPE = (pyparsing.Optional(PRECISION).setResultsName("precision") +
                 TYPE.setResultsName("type") +
                 IDENTIFIER.setResultsName("name") +
                 LPAREN + pyparsing.Optional(PARAMETERS).setResultsName("args") + RPAREN +
                 END)
    PROTOTYPE.ignore(pyparsing.cStyleComment)

    for (token, start, end) in PROTOTYPE.scanString(code):
        print(token.precision, token.type, token.name, '(',)
        for arg in token.args:
            print(arg.precision, arg.type, arg.name, ',',)
        print(')')


# ------------------------
def get_functions(code):
    """
    Get all function definitions

    Code example
    ------------

    mediump vec3 compute_normal(vec4);
    """

    PARAMETER = pyparsing.Group(pyparsing.Optional(PRECISION).setResultsName("precision") +
                                TYPE.setResultsName("type") +
                                pyparsing.Optional(IDENTIFIER).setResultsName("name"))
    PARAMETERS = pyparsing.delimitedList(PARAMETER).setResultsName(
        "arg", listAllMatches=True)
    FUNCTION = (pyparsing.Optional(PRECISION).setResultsName("precision") +
                TYPE.setResultsName("type") +
                IDENTIFIER.setResultsName("name") +
                LPAREN + pyparsing.Optional(PARAMETERS).setResultsName("args") + RPAREN +
                pyparsing.nestedExpr("{", "}").setParseAction(pyparsing.originalTextFor).setResultsName("code"))
    FUNCTION.ignore(pyparsing.cStyleComment)

    for (token, start, end) in FUNCTION.scanString(code):
        print(token.precision, token.type, token.name, '(',)
        for arg in token.args:
            print(arg.precision, arg.type, arg.name, ',',)
        print(') { ... }')

        # print token.code
        # print code[start:end]


# ------------------------
def get_version(code):
    """
    Get shader version (if specified)

    Code example
    ------------

    #version 120
    """

    VERSION = (
        pyparsing.Literal("#") + pyparsing.Keyword("version")).suppress() + INT
    for (token, start, end) in VERSION.scanString(code):
        version = token[0]
        # print code[start:end]
    return version

# ------------------------


def get_declarations(code):
    """
    Get all declarations prefixed with a storage qualifier.

    Code example
    ------------

    uniform lowp vec4 fg_color = vec4(1),
                      bg_color = vec4(vec3(0),1);
    """

    # Callable expression
    EXPRESSION = pyparsing.Forward()
    ARG = pyparsing.Group(EXPRESSION) | IDENTIFIER | FLOAT | INT
    ARGS = pyparsing.delimitedList(ARG)
    EXPRESSION << IDENTIFIER + \
        pyparsing.Group(LPAREN + pyparsing.Optional(ARGS) + RPAREN)

    # Value
    VALUE = (EXPRESSION | pyparsing.Word(pyparsing.alphanums + "_()+-/*")
             ).setParseAction(pyparsing.originalTextFor)

    # Single declaration
    VARIABLE = (IDENTIFIER.setResultsName("name") +
                pyparsing.Optional(LBRACK +
                                   (INT | IDENTIFIER).setResultsName("size")
                                   + RBRACK) +
                pyparsing.Optional(pyparsing.Literal("=").suppress() + VALUE.setResultsName("value")))

    # Several declarations at once
    DECLARATION = (STORAGE.setResultsName("storage") +
                   pyparsing.Optional(PRECISION).setResultsName("precision") +
                   TYPE.setResultsName("type") +
                   pyparsing.delimitedList(VARIABLE.setResultsName("variable", listAllMatches=True)) +
                   END)
    DECLARATION.ignore(pyparsing.cStyleComment)

    for (tokens, start, end) in DECLARATION.scanString(code):
        for token in tokens.variable:
            print(tokens.storage, tokens.precision, tokens.type,)
            print(token.name, token.size)


# ------------------------
def get_definitions(code):
    """
    Get all structure definitions and associated declarations.

    Code example
    ------------

    uniform struct Light {
        vec4 position;
        vec3 color;
    } light0, light1;
    """

    # Single declaration
    DECLARATION = pyparsing.Group(IDENTIFIER.setResultsName("name") +
                                  pyparsing.Optional(LBRACK +
                                                     (INT | IDENTIFIER).setResultsName("size") +
                                                     RBRACK))
    # Several declarations at once
    DECLARATIONS = (pyparsing.Optional(PRECISION) +
                    TYPE +
                    pyparsing.delimitedList(DECLARATION) +
                    END)

    # Definition + declarations
    DEFINITION = (STRUCT +
                  IDENTIFIER.setResultsName("name") +
                  LBRACE + pyparsing.OneOrMore(DECLARATIONS).setResultsName('content') + RBRACE +
                  pyparsing.Optional(pyparsing.delimitedList(DECLARATION.setResultsName("declarations", listAllMatches=True))) +
                  END)
    DEFINITION.ignore(pyparsing.cStyleComment)

    for (tokens, start, end) in DEFINITION.scanString(code):
        for token in tokens.declarations:
            print(tokens.name, token.name)
            # print tokens.content


# ----------------
def resolve(code):
    """
    Expand const and preprocessor definitions in order to get constant values.

    Return the transformed code
    """

    constants = {}

    DEFINITION = (pyparsing.Literal("#") + pyparsing.Literal("define") +
                  IDENTIFIER.setResultsName("name") +
                  pyparsing.restOfLine.setResultsName("value"))

    VALUE = pyparsing.Word(pyparsing.alphanums + "_()+-/*")
    DECLARATION = (pyparsing.Literal("const") +
                   TYPE.setResultsName("type") +
                   IDENTIFIER.setResultsName("name") +
                   pyparsing.Literal("=") +
                   VALUE.setResultsName("value") +
                   pyparsing.Literal(";"))
    REFERENCE = pyparsing.Forward()

    def process_definition(s, l, t):
        value = REFERENCE.transformString(t.value)
        constants[t.name] = value
        REFERENCE << pyparsing.MatchFirst(
            map(pyparsing.Keyword, constants.keys()))
        return "#define " + t.name + " " + value

    def process_declaration(s, l, t):
        value = REFERENCE.transformString(t.value)
        constants[t.name] = value
        REFERENCE << pyparsing.MatchFirst(
            map(pyparsing.Keyword, constants.keys()))
        return "const " + t.type + " " + t.name + "=" + value + ";"

    def process_reference(s, l, t):
        return constants[t[0]]

    REFERENCE.setParseAction(process_reference)
    DEFINITION.setParseAction(process_definition)
    DECLARATION.setParseAction(process_declaration)
    EXPANDER = REFERENCE | DEFINITION | DECLARATION

    code = EXPANDER.transformString(code)
    for key, val in constants.items():
        constants[key] = eval(val)

    return code, constants


# -----------------------------------------------------------------------------
if __name__ == '__main__':

    code = """
#version 120

#define A (1)
const int B=(A+2);
#define C (B+3)
const int D=C+4;

uniform float array[D];

struct Point {
    vec4 position;
    float size;
};

uniform struct Light {
    vec4 position;
    vec3 color;
} light0, light1;

const float PI = 3.14159265358979323846264;
const float SQRT_2 = 1.4142135623730951;

uniform vec4 fg_color = vec4(1),
             bg_color = vec4(vec3(0),1);

mediump vec3 compute_normal(vec4 position, vec3 orientation);
vec3 /* */ compute_light(vec4, vec3, float intensity)
{
   vec3 hello;
   vec3 hello;
}

"""
code, _ = resolve(code)
print("GLSL version: %s\n" % get_version(code))

get_definitions(code)
get_declarations(code)
get_prototypes(code)
get_functions(code)

# code = """
# #if A
# #if B
# #if C
# #endif
# #endif
# #endif
# """

# IF = (pyparsing.Literal('#') + (pyparsing.Keyword('if') | pyparsing.Keyword('ifdef') | pyparsing.Keyword('ifndef')))
# ENDIF = (pyparsing.Literal('#') + pyparsing.Keyword('endif'))
# MACRO = (IF + pyparsing.restOfLine() +
#          SkipTo(ENDIF, include=True)).setParseAction(pyparsing.originalTextFor)
# for (tokens, start, end) in MACRO.scanString(code):
#     print tokens