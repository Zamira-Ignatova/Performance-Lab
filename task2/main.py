import sys
import math


def read_data(file_path):
    with open(file_path, 'r') as file:
        x, y = map(float, file.readline().split())
        radius = float(file.readline())
    return x, y, radius

def read_coordinates(path):
    with open(path, 'r') as file:
        points = [tuple(map(float, line.split())) for line in file]
    return points

def position_detection(circle, point):
    cx, cy, radius = circle
    px, py = point
    distance_from_a_pont_to_the_center = math.sqrt((px - cx) ** 2 + (py - cy) ** 2)

    if math.isclose(distance_from_a_pont_to_the_center, radius, rel_tol=1e-9):
        return 0  # in case the point is ON the circle
    elif distance_from_a_pont_to_the_center < radius:
        return 1  # in case the point is INSIDE the circle
    else:
        return 2  # # in case the point is OUTSIDE  the circle

def main():
    #checking that all the required argument are being entered
    if len(sys.argv) != 2:
        print("Please enter the arguments in the following order: python <script_name>.py <circle> <points>")
        return

    circle_file = sys.argv[1]
    circle_data = read_data(circle_file)

    points_file = sys.argv[2]
    points = read_coordinates(points_file)

    for point in points:
        position = position_detection(circle_data, point)
        print(position)


if __name__ == "__main__":
    main()
