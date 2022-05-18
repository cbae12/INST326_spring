import rpn as r

from math import isclose

def test_evaluate_edge_cases():
    assert r.evaluate(int(9)) == 9
    assert isclose(r.evaluate(float(1/3)), 0.33333333333)
    assert r.evaluate(int(-1)) == -1
    assert r.evaluate(int(30)) == 30
def test_evaluate_happy_path():
    assert r.evaluate("6 5 +") == 11
    assert r.evaluate("5 6 -") == -1
    assert r.evaluate("10 3 *") == 30
    assert isclose(r.evaluate("5 6 /"), 0.833333333333)
    assert r.evaluate("6 5 3 + *") == 33
    assert r.evaluate("0 1 + 11 *") == 11