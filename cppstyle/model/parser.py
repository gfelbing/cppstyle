import re

import clang.cindex as ci

from cppstyle import utils
from cppstyle.model import *


def parse(file):
    index = ci.Index.create()
    source = index.parse(file)
    return to_node(source.cursor)


def to_node(clang_node):
    file = str(clang_node.location.file)
    position = get_location(clang_node)
    access = get_access(clang_node)
    children = get_children(clang_node)
    kind = get_kind(clang_node)
    comments = get_comments(clang_node)

    if kind == ci.CursorKind.CLASS_DECL:
        return Class(file, position, access, comments, clang_node.spelling, children)
    elif kind == ci.CursorKind.CXX_ACCESS_SPEC_DECL:
        return AccessSpecifier(file, position, access, comments, children)
    elif kind == ci.CursorKind.VAR_DECL:
        return Variable(file, position, access, comments, clang_node.spelling, children)
    elif kind == ci.CursorKind.FUNCTION_DECL:
        return Function(file, position, access, comments, clang_node.spelling, children)
    elif kind == ci.CursorKind.CXX_METHOD:
        return Method(file, position, access, comments, clang_node.spelling, children)
    elif kind == ci.CursorKind.FIELD_DECL:
        return Field(file, position, access, comments, clang_node.spelling, children)
    elif kind == ci.CursorKind.COMPOUND_STMT:
        return Scope(file, position, access, comments, children)
    elif kind == ci.CursorKind.STRUCT_DECL:
        return Struct(file, position, access, comments, clang_node.spelling, children)
    elif kind == ci.CursorKind.PARM_DECL:
        return Parameter(file, position, access, comments, clang_node.spelling, children)
    else:
        return Node(file, position, access, comments, children)


def get_location(clang_node):
    if hasattr(clang_node, 'location'):
        return Position(clang_node.extent.start.line, clang_node.extent.start.column - 1)
    else:
        return Position(0, 0)


def get_access(clang_node):
    if hasattr(clang_node, 'access_specifier'):
        if clang_node.access_specifier == ci.AccessSpecifier.PRIVATE:
            return Access.PRIVATE
        elif clang_node.access_specifier == ci.AccessSpecifier.PROTECTED:
            return Access.PROTECTED
        elif clang_node.access_specifier == ci.AccessSpecifier.PUBLIC:
            return Access.PUBLIC
    else:
        return Access.NONE


def get_children(clang_node):
    children = []
    if hasattr(clang_node, 'get_children'):
        for c in clang_node.get_children():
            node = to_node(c)
            children.append(node)
    return tuple(children)


def get_kind(clang_node):
    if hasattr(clang_node, 'kind'):
        return clang_node.kind
    else:
        return {}


def get_comments(clang_node):
    if clang_node.raw_comment:
        lines = clang_node.raw_comment.splitlines()
        stripped = map(lambda line: re.match("(?:[/*\s]*)(.*)", line).group(1), lines)
        splitted = utils.split(
            stripped,
            lambda l: not l or len(l) == 0 or l.startswith("@"),
            lambda l: l and len(l) > 0
        )
        return list(map(to_comment, splitted))
    else:
        return []


def to_comment(comment_lines):
    type = "default"
    firstline, *remaining = list(comment_lines)
    if firstline.startswith("@"):
        matcher = re.match("(@\w+)(?:\s*)(.*)", comment_lines[0])
        type = matcher.group(1)
        firstline = matcher.group(2)
    content = "\n".join([firstline] + remaining)
    return Comment(type, content)
