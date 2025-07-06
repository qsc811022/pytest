import pytest
from prime import is_prime

def test_is_prime_negative():
    with pytest.raises(ValueError):
        is_prime(-2)
