import statistics

print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")

def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32):")


def get_user_input():
        user_input = input()
        number_strings = user_input.split(',')
        numbers = [float(num.strip()) for num in number_strings]
        return numbers


def calc_average(temperature):
    average = sum(temperature) / len(temperature)
    return average


def calc_min_max(temperature):
    min_temp = min(temperature)
    max_temp = max(temperature)
    return [min_temp, max_temp]


def sort_temperature(temperature):
    sorted_temperature = sorted(temperature)
    return sorted_temperature


#def calc_median_temperature(numlist):
    print("Median temperature: " + str(statistics.median(numlist)))


def main():
    display_main_menu()
    temperature = get_user_input()
    print("Average temperature:", calc_average(temperature))
    min_max = calc_min_max(temperature)
    print("Minimum temperature:", min_max[0])
    print("Maximum temperature:", min_max[1])
    print("Sorted temperature:", sort_temperature(temperature))
    #calc_median_temperature(temperature)


if __name__ == "__main__":
    main()
