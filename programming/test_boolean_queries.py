# DO NOT modify code except "YOUR CODE GOES HERE" blocks

import boolean_engine

ir = boolean_engine.IRSystem(open("wiki-small.txt"))


def test_q_term1_1points():
    results = ir.run_query('auto')
    assert results == [798, 2175, 2898, 4960, 5669]


def test_q_term2_1points():
    results = ir.run_query('mechanic')
    assert results == [3394, 4960]


def test_q_not_3points():
    results = ir.run_query('NOT the')
    # Too many results to list, checking for size only
    assert len(results) == 1028


def test_q_and2_15_points():
    results = ir.run_query('AND mechanic auto')
    assert results == [4960]
    results = ir.run_query('AND auto mechanic')
    assert results == [4960]


def test_q_or2_20_points():
    results = ir.run_query('OR mechanic auto')
    assert results == [798, 2175, 2898, 3394, 4960, 5669]
    results = ir.run_query('OR auto mechanic')
    assert results == [798, 2175, 2898, 3394, 4960, 5669]


def test_multiple_operators1_10_points():
    results = ir.run_query('AND president OR house white')
    assert results == [1325, 2391, 3041, 3618, 3771, 4053, 5409]


