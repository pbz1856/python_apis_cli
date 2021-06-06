from apis_cli import find_matching_name

def test_find_matching_name():
    test_categories = ['Something', 'cat', 'acat']
    name = 'at'

    result = find_matching_name(test_categories, name)

    assert len(result) == 2
    assert result == ['cat', 'acat']

    name = 'acat'

    result = find_matching_name(test_categories, name)

    assert len(result) == 1
    assert result == ['acat']

    name = ''

    result = find_matching_name(test_categories, name)

    assert len(result) == 3
    assert result == test_categories 

    name = 'som'

    result = find_matching_name(test_categories, name)

    assert len(result) == 1
    assert result == ['Something']