#!/usr/bin/env python3

from __future__ import annotations
from typing import Any, Optional

class Element:

    #--------------------------------------------------------------------------
    def __init__(self, value: Any) -> None:
        self.value = value
        self._parent: Optional[Element] = None
        self._child: Optional[Element] = None

    #--------------------------------------------------------------------------
    @property
    def parent(self) -> Optional[Element]:
        return self._parent

    #--------------------------------------------------------------------------
    @parent.setter
    def parent(self, elem: Optional[Element]) -> None:
        if elem is not None and not isinstance(elem, Element):
            raise TypeError
        self._parent = elem

    #--------------------------------------------------------------------------
    @property
    def child(self) -> Optional[Element]:
        return self._child

    #--------------------------------------------------------------------------
    @child.setter
    def child(self, elem: Optional[Element]) -> None:
        if elem is not None and not isinstance(elem, Element):
            raise TypeError
        self._child = elem

    #--------------------------------------------------------------------------
    def __str__(self) -> str:
        return f"Element({repr(self.value)})"
