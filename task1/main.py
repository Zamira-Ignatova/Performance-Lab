import sys


def get_circular_path(n, m):
    path = [] # final path
    ongoing_index = 0 # first element in an array
    elements_in_the_list_are_not_finished = True
    circular_array = list(range(1, n + 1)) # Create an array with length from 1 to n

    while elements_in_the_list_are_not_finished:
        path.append(circular_array[ongoing_index]) #append ongoing element  in our path
        ongoing_index = (ongoing_index + m - 1) % n #calculate the following_element and taking into account circuital array
        if ongoing_index == 0:
            break
    return ''.join(map(str, path))


if __name__ == "__main__": # to take arguments from console and display the final result

    if len(sys.argv) == 3:
        n = int(sys.argv[1])
        m = int(sys.argv[2])

        result = get_circular_path(n, m)
        print(result)
    else:
        print("python <script_name>.py <length_of_an_array> <number_of_steps>")
