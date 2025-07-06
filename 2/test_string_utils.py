import pytest
from string_utils import reverse_string

@pytest.mark.parametrize("test_input, expected", [
    ("abc", "cba"),
    ("", ""),
    ("12345", "54321"),
])
def test_reverse_string_normal(test_input, expected):
    assert reverse_string(test_input) == expected

def test_reverse_string_invalid():
    with pytest.raises(ValueError):
        reverse_string(123)
    with pytest.raises(ValueError):
        reverse_string(None)
