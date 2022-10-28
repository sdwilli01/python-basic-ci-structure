from conversions.list_string_conversions import list_to_string, string_to_list
import pytest


@pytest.mark.parametrize("test_string_input,expected_list", [
    ('', []),
    ('cat', ['c', 'a', 't']),
])
def test_string_to_list_conversions(test_string_input, expected_list):
    actual = string_to_list(test_string_input)
    assert actual == expected_list


@pytest.mark.parametrize("test_list_input,expected_string", [
    ([], ''),
    (['c', 'a', 't'], 'cat'),
])
def test_list_to_string_conversions(test_list_input, expected_string):
    actual = list_to_string(test_list_input)
    assert actual == expected_string


@pytest.mark.skip(reason="Have not implemented int to string yet")
def test_int_to_string_conversions():
    assert int_to_string(567) == '567'


# This is how you annotate expected/known failures
# but that you don't want to break the build.
@pytest.mark.xfail
def test_divide_by_zero():
    assert 1 / 0 == 1


# This is how you check for expected exceptions
def test_invalid_type_input():
    with pytest.raises(TypeError):
        string_to_list(500)
