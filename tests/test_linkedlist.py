#!/usr/bin/env python3

import sys, os
sys.path.append(os.pardir)
from algorithms import LinkedList
import pytest

class Test_LinkedList:

    #--------------------------------------------------------------------------
    def test_init(self) -> None:
        lnklst = LinkedList()
        assert lnklst._len == 0
        assert lnklst._head is None
        assert lnklst._tail is None

    #--------------------------------------------------------------------------
    def test_len(self) -> None:
        lnklst = LinkedList()
        assert len(lnklst) == 0

        lnklst.append(1)
        assert len(lnklst) == 1

        lnklst.remove(0)
        assert len(lnklst) == 0

    #--------------------------------------------------------------------------
    def test_append(self) -> None:
        lnklst = LinkedList()
        assert lnklst.to_list() == []

        lnklst.append(1)
        assert lnklst.to_list() == [1]

        lnklst.append(2)
        assert lnklst.to_list() == [1, 2]

    #--------------------------------------------------------------------------
    def test_element_at(self) -> None:
        lnklst = LinkedList()
        with pytest.raises(IndexError):
            lnklst._element_at(0)

        lnklst = LinkedList.from_iter([1, 2])
        with pytest.raises(IndexError):
            lnklst._element_at(-1)

        assert lnklst._element_at(0).value == 1

        assert lnklst._element_at(1).value == 2

        with pytest.raises(IndexError):
            lnklst._element_at(2)

    #--------------------------------------------------------------------------
    def test_insert(self) -> None:
        lnklst = LinkedList()
        with pytest.raises(IndexError):
            lnklst.insert(1, 0)

        lnklst = LinkedList.from_iter([3])
        with pytest.raises(IndexError):
            lnklst.insert(1, -1)

        lnklst.insert(1, 0)
        assert lnklst.to_list() == [1, 3]

        lnklst.insert(2, 1)
        assert lnklst.to_list() == [1, 2, 3]

        with pytest.raises(IndexError):
            lnklst.insert(4, 3)

    #--------------------------------------------------------------------------
    def test_remove(self) -> None:
        lnklst = LinkedList()
        with pytest.raises(IndexError):
            lnklst.remove(0)

        lnklst = LinkedList.from_iter([1, 2, 3, 4])
        with pytest.raises(IndexError):
            lnklst.remove(4)

        lnklst.remove(1)
        assert lnklst.to_list() == [1, 3, 4]

        lnklst.remove(2)
        assert lnklst.to_list() == [1, 3]

        lnklst.remove(0)
        assert lnklst.to_list() == [3]

        lnklst.remove(0)
        assert lnklst.to_list() == []

        with pytest.raises(IndexError):
            lnklst.remove(-1)

    #--------------------------------------------------------------------------
    def test_getitem(self) -> None:
        lnklst = LinkedList()
        with pytest.raises(IndexError):
            lnklst[0]

        lnklst = LinkedList.from_iter([1, 2])
        with pytest.raises(IndexError):
            lnklst[-1]

        assert lnklst[0] == 1

        assert lnklst[1] == 2

        with pytest.raises(IndexError):
            lnklst[2]

    #--------------------------------------------------------------------------
    def test_setitem(self) -> None:
        lnklst = LinkedList()
        with pytest.raises(IndexError):
            lnklst[0] = 1

        lnklst = LinkedList.from_iter([1, 2])
        with pytest.raises(IndexError):
            lnklst[-1] = 1

        lnklst[0] = 3
        assert lnklst.to_list() == [3, 2]

        lnklst[1] = 4
        assert lnklst.to_list() == [3, 4]

        with pytest.raises(IndexError):
            lnklst[2] = 5

    #--------------------------------------------------------------------------
    def test_clear(self) -> None:
        lnklst = LinkedList.from_iter([1, 2])
        assert lnklst.to_list() == [1, 2]

        lnklst.clear()
        assert lnklst.to_list() == []

    #--------------------------------------------------------------------------
    def test_from_iter(self) -> None:
        lnklst = LinkedList.from_iter([])
        assert lnklst.to_list() == []

        lnklst = LinkedList.from_iter([1, 2])
        assert lnklst.to_list() == [1, 2]

        lnklst = LinkedList.from_iter('hello')
        assert lnklst.to_list() == ['h', 'e', 'l', 'l', 'o']

        with pytest.raises(TypeError):
            LinkedList.from_iter(100)

    #--------------------------------------------------------------------------
    def test_to_list(self) -> None:
        lnklst = LinkedList()
        assert lnklst.to_list() == []

        lnklst = LinkedList.from_iter([1, 2])
        assert lnklst.to_list() == [1, 2]

        lnklst = LinkedList.from_iter('hello')
        assert lnklst.to_list() == ['h', 'e', 'l', 'l', 'o']

    #--------------------------------------------------------------------------
    def test_clone(self) -> None:
        lnklst = LinkedList()
        clone = lnklst.clone()
        assert clone is not lnklst
        assert clone.to_list() == lnklst.to_list()

        lnklst = LinkedList.from_iter([1, 2])
        clone = lnklst.clone()
        assert clone is not lnklst
        assert clone.to_list() == lnklst.to_list()

        lnklst = LinkedList.from_iter('hello')
        clone = lnklst.clone()
        assert clone is not lnklst
        assert clone.to_list() == lnklst.to_list()

    #--------------------------------------------------------------------------
    def test_str(self) -> None:
        lnklst = LinkedList()
        assert str(lnklst) == "LinkedList([])"

        lnklst = LinkedList.from_iter([1, 2])
        assert str(lnklst) == "LinkedList([1, 2])"

        lnklst = LinkedList.from_iter('hello')
        assert str(lnklst) == "LinkedList(['h', 'e', 'l', 'l', 'o'])"
