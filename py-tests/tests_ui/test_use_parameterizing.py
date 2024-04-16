import pytest


# to run this use this command pytest -m parametrize -s -v
@pytest.mark.parametrize("log1, log2", [("What", "up?"), ("Nothing", "much")])
def test_logging(log1, log2):
    print(log1, log2)

