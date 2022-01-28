#!/usr/bin/env python3

# Created by: Ina Tolo
# Created on: Jan. 27, 2022
# This program uses a for loop to generate and
# print random numbers in a list, then
# displays the largest value

import constants
import random


# function calculates the max value in the list of elements
def find_max_value(ran_nums):

    max = ran_nums[0]

    # calculate the max value
    for counter in range(len(ran_nums)):
        if max < ran_nums[counter]:
            max = ran_nums[counter]

    return max


def main():
    # initializing  sum and counter
    sum = 0
    counter = 0

    # declaring variable
    ran_nums_user = []

    # display opening message to console
    print("This program generates a list of random "
          "numbers between 0 and 100, then determines the largest number.")
    print("")

    # displays random numbers and calculates average
    for counter in range(constants.MAX_ARRAY_SIZE):
        ran_nums_user.append(random.randint(constants.MIN_NUM,
                                            constants.MAX_NUM))
        sum = sum + ran_nums_user[counter]
        print("{} added to the list at "
              "position {}" .format(ran_nums_user[counter], counter))

    max_user = find_max_value(ran_nums_user)
    print("")
    print("The max value is: {}" .format(max_user))


if __name__ == "__main__":
    main()
