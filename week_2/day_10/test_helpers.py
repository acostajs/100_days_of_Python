# Test helper functions from helpers.py

import pytest

from helpers import calc

def test_calc():
    assert calc("+", 2, 2) == 4
    assert calc("-", 2, 2) == 0
    assert calc("*", 2, 2) == 4
    assert calc("/", 2, 2) == 1
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc("/", 2, 0)

