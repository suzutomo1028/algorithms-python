#!/usr/bin/env python3

import sys, os
sys.path.append(os.pardir)
from algorithms import Element
import pytest

class Test_Element:

    #--------------------------------------------------------------------------
    def test_init(self) -> None:
        elem = Element(value=100)
        assert elem.value == 100
        assert elem.parent is None
        assert elem.child is None

    #--------------------------------------------------------------------------
    def test_parent(self) -> None:
        elem = Element(value='elem')
        parent = Element(value='parent')
        elem.parent = parent
        assert elem.parent is parent

        elem.parent = None
        assert elem.parent is None

        with pytest.raises(TypeError):
            elem.parent = 100

    #--------------------------------------------------------------------------
    def test_child(self) -> None:
        elem = Element(value='elem')
        child = Element(value='child')
        elem.child = child
        assert elem.child is child

        elem.child = None
        assert elem.child is None

        with pytest.raises(TypeError):
            elem.child = 100

    #--------------------------------------------------------------------------
    def test_str(self) -> None:
        elem = Element(value=100)
        assert str(elem) == "Element(100)"

        elem = Element(value='hello')
        assert str(elem) == "Element('hello')"

        elem = Element(value=None)
        assert str(elem) == "Element(None)"
