

def add(a: int, b: int):
    return a + b


def test_add():
    assert add(4, 18) == 22
    assert add(5, 26) == 31
    assert add(3, 34) != 3
    assert add(3, 34) != 3

