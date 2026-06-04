import pytest


@pytest.mark.skip
def test_skipped1():
    pass

@pytest.mark.skip
def test_skipped2():
    pass

@pytest.mark.skip
def test_skipped3():
    pass


def test_skipped11():
    # какая‑то тестовая логика
    result = some_function()
    assert result is not None  # обязательный assert