from main.utils.snippet import Snippet
from main.actions.action_base_class import ActionBaseClass
from main.actions.defines.define_func import DefineFunc
from typing import Any
import ast

class DefineInteger(ActionBaseClass):
    def __init__(self, snippet: Snippet=None, lineno: int=0, **kwargs: dict) -> None:
        super().__init__(snippet, lineno)

        self.class_name = None
        if 'class_name' in kwargs: 
            self.class_name = kwargs['class_name']

    def __str__(self) -> str:
        desc = super().__str__()
        desc += 'Integer Class name: {}\n'.format(self.class_name)

        return desc

    def check_criteria(self) -> bool:
        class IsIterableOrSubscriptable(ast.NodeVisitor):
            def __init__(self, **kwargs):
                self.class_name = kwargs['class_name']
                self.snippet = kwargs['snippet']
                self.lineno = kwargs['lineno']
                self.is_iterable_or_subscriptable = True

            def visit_ClassDef(self, node):
                if node.name == self.class_name:
                    for child in node.body:
                        if isinstance(child, ast.FunctionDef):
                            if child.name == '__getitem__':
                                self.is_iterable_or_subscriptable = False
                                break
                return node

        tree = ast.parse(self.snippet.get_latest())
        visitor = IsIterableOrSubscriptable(class_name=self.class_name, snippet=self.snippet, lineno=self.lineno)
        visitor.visit(tree)
        
        return visitor.is_iterable_or_subscriptable

    def apply_pattern(self) -> str:
        # subclass 'int' class
        self.__subclass_int()

        return

    def __subclass_int(self) -> None:
        class IntegerSubclasser(ast.NodeTransformer):
            def __init__(self, **kwargs):
                self.class_name = kwargs['class_name']
                self.snippet = kwargs['snippet']
                self.lineno = kwargs['lineno']

            @ActionBaseClass.add_to_history
            def visit_Body(self, node):
                for (idx, child) in enumerate(node.body):
                    node.body[idx] = self.visit(child)                
                return node

            def visit_ClassDef(self, node):
                if node.name == self.class_name:
                    node.bases.append(ast.Name(id='int', ctx=ast.Load()))
                    node.body.insert(0, ast.parse('def __new__(self):\n\treturn 1'))
                return node
        
        tree = ast.parse(self.snippet.get_latest())
        tree = IntegerSubclasser(class_name=self.class_name, snippet=self.snippet, lineno=self.lineno).visit_Body(tree)

        return None
