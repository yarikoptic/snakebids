"""
This type stub file was generated by pyright.
"""

if False: ...

class Node:
    __slots__ = ...
    def __init__(
        self,
        tag: Any,
        value: Any,
        start_mark: Any,
        end_mark: Any,
        comment: Any = ...,
        anchor: Any = ...,
    ) -> None: ...
    @property
    def tag(self) -> Optional[str]: ...
    @tag.setter
    def tag(self, val: Any) -> None: ...
    def __repr__(self) -> Any: ...
    def dump(self, indent: int = ...) -> None: ...

class ScalarNode(Node):
    """
    styles:
      ? -> set() ? key, no value
      - -> suppressable null value in set
      " -> double quoted
      ' -> single quoted
      | -> literal style
      > -> folding style
    """

    __slots__ = ...
    id = ...
    def __init__(
        self,
        tag: Any,
        value: Any,
        start_mark: Any = ...,
        end_mark: Any = ...,
        style: Any = ...,
        comment: Any = ...,
        anchor: Any = ...,
    ) -> None: ...

class CollectionNode(Node):
    __slots__ = ...
    def __init__(
        self,
        tag: Any,
        value: Any,
        start_mark: Any = ...,
        end_mark: Any = ...,
        flow_style: Any = ...,
        comment: Any = ...,
        anchor: Any = ...,
    ) -> None: ...

class SequenceNode(CollectionNode):
    __slots__ = ...
    id = ...

class MappingNode(CollectionNode):
    __slots__ = ...
    id = ...
    def __init__(
        self,
        tag: Any,
        value: Any,
        start_mark: Any = ...,
        end_mark: Any = ...,
        flow_style: Any = ...,
        comment: Any = ...,
        anchor: Any = ...,
    ) -> None: ...
