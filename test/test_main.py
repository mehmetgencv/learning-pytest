import main


def test_add():
    assert main.add(1, 2) == 3
    assert main.add(1, -2) == -1
    assert main.add(-1, -2) == -3


def test_sub():
    assert main.sub(1, 2) == -1
    assert main.sub(1, -2) == 3
    assert main.sub(-1, -2) == 1


def test_to_sentence():
    assert main.to_sentence('hello') == 'Hello.'
    assert main.to_sentence('hello world') == 'Hello world.'
    assert main.to_sentence('Hello world.') == 'Hello world.'
