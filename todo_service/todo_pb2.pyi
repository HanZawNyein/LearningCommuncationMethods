from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Todo(_message.Message):
    __slots__ = ["id", "title", "description", "done"]
    ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DONE_FIELD_NUMBER: _ClassVar[int]
    id: int
    title: str
    description: str
    done: bool
    def __init__(self, id: _Optional[int] = ..., title: _Optional[str] = ..., description: _Optional[str] = ..., done: bool = ...) -> None: ...

class TodoListResponse(_message.Message):
    __slots__ = ["todos"]
    TODOS_FIELD_NUMBER: _ClassVar[int]
    todos: _containers.RepeatedCompositeFieldContainer[Todo]
    def __init__(self, todos: _Optional[_Iterable[_Union[Todo, _Mapping]]] = ...) -> None: ...

class TodoRequest(_message.Message):
    __slots__ = ["id", "title", "description", "done"]
    ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DONE_FIELD_NUMBER: _ClassVar[int]
    id: int
    title: str
    description: str
    done: bool
    def __init__(self, id: _Optional[int] = ..., title: _Optional[str] = ..., description: _Optional[str] = ..., done: bool = ...) -> None: ...
