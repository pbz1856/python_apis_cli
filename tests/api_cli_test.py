import os, sys
import pytest
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from apis_cli import find_matching_name

@pytest.mark.parametrize("test_categories, name, expected_list, expected_length, is_error", [
    (['Something', 'cat', 'acat'], 'at', ['cat', 'acat'], 2, False),
    (['Something', 'cat', 'acat'], 'acat', ['acat'], 1, False),
    (['Something', 'cat', 'acat'], '', ['Something', 'cat', 'acat'], 3, False),
    (['Something', 'cat', 'acat'], 'som', ['Something'], 1, False),
])
def test_find_matching_name(test_categories, name, expected_list, expected_length, is_error):
    if is_error:
        with pytest.raises(Null):
            result = find_matching_name(test_categories, name)
    else:
        result = find_matching_name(test_categories, name)
        assert result == expected_list
        assert len(result) == expected_length