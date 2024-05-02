import Lab2


def test_find_min_max():
    test_arr = [15, 18, 22, 26]
    expected_result = [15, 26]

    result = Lab2.calc_min_max(test_arr)
    assert (result == expected_result)


def test_calc_average():
    test_arr = [15, 18, 22, 26]
    expected_result = 20.25

    result = Lab2.calc_average(test_arr)
    assert (result == expected_result)

def test_calc_median_temperature():
    test_arr = [15, 18, 22, 26]
    expected_result = 20

    result = Lab2.calc_median_temperature(test_arr)
    assert (result == expected_result)
