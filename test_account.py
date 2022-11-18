import sys
import pytest
from account import *


def test_init():
    test_1 = Account('test1')
    test_2 = Account(1)
    with pytest.raises(TypeError):
        test_3 = Account()


def test_deposit():
    test_1 = Account('test1')
    assert test_1.deposit(1000) is True
    assert test_1.deposit(-1) is False
    assert test_1.deposit(0) is False
    assert test_1.deposit(14341341) is True
    with pytest.raises(TypeError):
        test_1.deposit('1')
    assert test_1.deposit(1.5) is True


def test_withdraw():
    test_1 = Account('test1')
    test_1.deposit(10000)
    assert test_1.withdraw(1000) is True
    assert test_1.withdraw(-1) is False
    assert test_1.withdraw(0) is False
    assert test_1.withdraw(1434) is True
    with pytest.raises(TypeError):
        test_1.withdraw('1')
    assert test_1.withdraw(1.5) is True


if __name__ == '__main__':
    sys.exit(pytest.main())
