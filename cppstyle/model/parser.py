import clang.cindex as ci
from .position import Position
from .access import Access
from .node import Node
from .class_node import Class
from .access_specifier import AccessSpecifier
from .variable import Variable
from .method import Method
from .function import Function
from .field import Field

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

    if kind == ci.CursorKind.CLASS_DECL:
        return Class(file, position, access, clang_node.spelling, children)
    elif kind == ci.CursorKind.CXX_ACCESS_SPEC_DECL:
        return AccessSpecifier(file, position, access, children)
    elif kind == ci.CursorKind.VAR_DECL:
        return Variable(file, position, access, clang_node.spelling, children)
    elif kind == ci.CursorKind.FUNCTION_DECL:
        return Function(file, position, access, clang_node.spelling, children)
    elif kind == ci.CursorKind.CXX_METHOD:
        return Method(file, position, access, clang_node.spelling, children)
    elif kind == ci.CursorKind.FIELD_DECL:
        return Field(file, position, access, clang_node.spelling, children)
    else:
        return Node(file, position, access, children)


def get_location(clang_node):
    if hasattr(clang_node, 'location'):
        return Position(clang_node.location.line, clang_node.location.column)
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
