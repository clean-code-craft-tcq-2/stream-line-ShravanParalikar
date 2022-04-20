from receiver import get_temerature_list, get_state_of_charge_list, print_maximum_and_minimum_stream_values, \
    get_simple_moving_average_of_stream
from unittest import mock


def test_get_temperature_list():
    temp_list = get_temerature_list('TEMPERATURE:15 27 9 29 38 6 3 18 25 42 10 7')
    assert temp_list == [15, 27, 9, 29, 38, 6, 3, 18, 25, 42, 10, 7]
    assert len(temp_list) == 12

    temp_list = get_temerature_list('TEMPERATURE:8 25 42 10 7')
    assert temp_list == [8, 25, 42, 10, 7]
    assert len(temp_list) == 5


def test_get_state_of_charge_list():
    state_of_charge_list = get_state_of_charge_list('STATE_OF_CHARGE:67 28 60 4')
    assert state_of_charge_list == [67, 28, 60, 4]
    assert len(state_of_charge_list) == 4

    state_of_charge_list = get_state_of_charge_list('STATE_OF_CHARGE:8 25 42 10 7')
    assert state_of_charge_list == [8, 25, 42, 10, 7]
    assert len(state_of_charge_list) == 5


@mock.patch('builtins.print')
def test_print_maximum_and_minimum_stream_values(mocked_obj):
    temperature_list, state_of_charge_list = [1, 2, 3, 4], [5, 6, 7, 8]
    print_maximum_and_minimum_stream_values(temperature_list, state_of_charge_list)
    mocked_obj.assert_called_with('Temp[MIN, MAX] : 1,4 Charge[MIN,MAX] : 5,8')


def test_get_simple_moving_average_of_stream():
    stream, window_size = [1, 2, 3, 4], 4
    moving_average = get_simple_moving_average_of_stream(stream, window_size)
    assert moving_average == [2.5]


if __name__ == "__main__":
    test_get_temperature_list()
    test_get_state_of_charge_list()
    test_print_maximum_and_minimum_stream_values()
    test_get_simple_moving_average_of_stream()
