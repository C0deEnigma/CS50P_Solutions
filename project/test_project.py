import pytest
from unittest.mock import patch, MagicMock
from project import date, time, get_city, weather


def test_date():
    with patch('project.datetime') as mock_datetime:
        mock_datetime.now.return_value = MagicMock(
            year=2024,
            month=12,
            day=8,
            strftime=MagicMock(side_effect=['December', 'Friday'])
        )
        assert date() == "Today is Sunday, Eighth of December, Two Thousand And Twenty-Fourth"


def test_time():
    with patch('project.now') as mock_now:
        mock_now.hour = 14
        mock_now.minute = 5
        assert time() == "Time is 02:05 PM"


@patch('project.requests.get')
def test_get_city(mock_get):
    mock_get.return_value.json.return_value = {'city': 'London'}
    result = get_city()
    assert result == 'London'