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


    """
    {
        "count": 3,
        "entries": [
            {
            "API": "7Timer!",
            "Description": "Weather, especially for Astroweather",
            "Auth": "",
            "HTTPS": false,
            "Cors": "unknown",
            "Link": "http://www.7timer.info/doc.php?lang=en",
            "Category": "Weather"
            },
            {
            "API": "AccuWeather",
            "Description": "Weather and forecast data",
            "Auth": "apiKey",
            "HTTPS": false,
            "Cors": "unknown",
            "Link": "https://developer.accuweather.com/apis",
            "Category": "Weather"
            },
            {
            "API": "ODWeather",
            "Description": "Weather and weather webcams",
            "Auth": "",
            "HTTPS": false,
            "Cors": "unknown",
            "Link": "http://api.oceandrivers.com/static/docs.html",
            "Category": "Weather"
            }
        ]
    }
    """