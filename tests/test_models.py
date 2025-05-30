"""Tests for statistics functions within the Model layer."""

import numpy as np
import numpy.testing as npt
import pytest

from inflammation.models import daily_mean, daily_max, daily_min


@pytest.mark.parametrize(
        "test, expected",
        [
            ([ [0,0], [0,0], [0,0] ], [0,0]),
            ([ [1,2], [3,4], [5,6] ], [3,4]),
        ]
)
def test_daily_mean(test, expected):
    """Test mean function works for array of zeroes and positive integers."""
    npt.assert_array_equal(daily_mean(np.array(test)), np.array(expected))


def test_daily_max():
    """Test that max function works for an array of positive integers."""

    test_input = np.array([[4, 2, 5],
                           [1, 6, 2],
                           [4, 1, 9]])
    test_result = np.array([4, 6, 9])
    npt.assert_array_equal(daily_max(test_input), test_result)


def test_daily_min():
    """Test that min function works for an array of positive and negative integers."""

    test_input = np.array([[ 4, -2, 5],
                           [ 1, -6, 2],
                           [-4, -1, 9]])
    test_result = np.array([-4, -6, 2])
    npt.assert_array_equal(daily_min(test_input), test_result)


def test_daily_min_string():
    """Test for TypeError when passing strings"""

    with pytest.raises(TypeError):
        error_expected = daily_min([['Hello', 'there'], ['General', 'Kenobi']])