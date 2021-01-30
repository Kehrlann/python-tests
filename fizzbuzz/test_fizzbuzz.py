from fizzbuzz import fizzbuzz


def test_returns_a_list():
    result = fizzbuzz()

    assert type(result) == list


def test_100_items():
    result = fizzbuzz()

    assert len(result) == 100


def test_only_strings():
    result = fizzbuzz()

    assert type(result[0]) == str
    assert type(result[2]) == str
    assert type(result[4]) == str
    assert type(result[14]) == str


def test_numbers():
    result = fizzbuzz()

    assert result[0] == '1'
    assert result[1] == '2'
    assert result[3] == '4'


def test_multiples_of_three():
    result = fizzbuzz()

    assert result[2] == 'fizz'
    assert result[5] == 'fizz'


def test_multiples_of_five():
    result = fizzbuzz()

    assert result[4] == 'buzz'
    assert result[9] == 'buzz'


def test_multiples_of_both_three_and_five():
    result = fizzbuzz()

    assert result[14] == 'fizzbuzz'
    assert result[29] == 'fizzbuzz'
