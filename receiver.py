import sys


def get_temerature_list(temperature):
    temperature = temperature.strip()
    temperature_string, temperature = temperature.split(':')
    temperature = temperature.split(' ')
    temperature = list(map(int, temperature))
    return temperature


def get_state_of_charge_list(state_of_charge):
    state_of_charge = state_of_charge.strip()
    state_of_charge_string, state_of_charge = state_of_charge.split(':')
    state_of_charge= state_of_charge.split(' ')
    state_of_charge = list(map(int, state_of_charge))
    return state_of_charge


def print_maximum_and_minimum_stream_values(temperature_list, state_of_charge_list):
    print(f'Temp[MIN, MAX] : {min(temperature_list)},{max(temperature_list)} '
          f'Charge[MIN,MAX] : {min(state_of_charge_list)},{max(state_of_charge_list)}')



def get_simple_moving_average_of_stream(stream, window_size):
    moving_average = []
    index = 0
    while index < len(stream) - window_size + 1:
        window = stream[index:index + window_size]
        windowAverage = round((sum(window) / window_size), 2)
        moving_average.append(windowAverage)
        index = index + 1
    return moving_average


def print_simple_moving_average_of_streams(temperature_list, state_of_charge_list, window_size):
    simple_moving_average_temp = get_simple_moving_average_of_stream(temperature_list, window_size)
    simple_moving_average_charge = get_simple_moving_average_of_stream(state_of_charge_list, window_size)
    print(f'Simple moving average of Temperature: {simple_moving_average_temp}')
    print(f'Simple moving average of state of charge: {simple_moving_average_charge}')


if __name__ == "__main__":
    console_input = sys.stdin.readlines()
    temperature, state_of_charge = console_input[0], console_input[1]
    temperature_list = get_temerature_list(temperature)
    state_of_charge_list = get_state_of_charge_list(state_of_charge)
    print_maximum_and_minimum_stream_values(temperature_list, state_of_charge_list)
    print_simple_moving_average_of_streams(temperature_list, state_of_charge_list, 5)
