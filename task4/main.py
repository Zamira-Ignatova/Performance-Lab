import sys


def min_moves_to_equal_elements(nums):
    nums.sort()
    median = nums[len(nums) // 2]
    moves = sum(abs(num - median) for num in nums)

    return moves


def main():

    if len(sys.argv) != 2:
        print("Please enter the arguments in the following order: python <script_name>.py <numbers>")
        return

    file_path = sys.argv[1]
    with open(file_path, 'r') as file:
        nums = [int(line.strip()) for line in file]

    result = min_moves_to_equal_elements(nums)
    print(result)


if __name__ == "__main__":
    main()
