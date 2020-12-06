# A hiker keeps track of every step on a hike.
# A hike starts and ends at sea level (0).
# Every step is either up one unit in elevation, or down one unit in elevation.
# A valley is defined as a sequence of steps that starts from stepping down 
# one unit from sea level. While below sea level, any step may be up or down.
# The valley ends where the last step in that valley is up to level 0.
# The opposite is true of a mountain, starts from sea level going up and ends when
# the last step is down to sea level 0.
# The hiker keeps track of all steps on the hike until returning to the original location.
# Steps are recorded in a string as follows:
# UUDUDDDU... etc
# Assume the string will have a number of characters n where 2 <= n <= 1000000 (million)
# Assume the string will only contain 'U's and 'D's
#
# The hiker needs you to write a function that will count the number of valleys
# traversed during the hike.
#
# example: input steps = UUDD the result should be 0 valleys
# example: input steps = DDUDUU the result should be 1 valley
# example: input steps = UUDDDDUDUU the result should be 1 valley

def count_valleys(steps) -> int:
    count = 0
    level = 0
    for i in range(len(steps)):
        if steps[i] == 'U':
            level += 1
            if level == 0:
                count += 1
        else:
            level -= 1
    return count


if __name__ == '__main__':
    test1 = "UUDDDDUU"
    print("test1 count should be 1, result = {}".format(count_valleys(test1)))
    test2 = "UDUDDUDUUDUUDUUDUDUUUDUUDUDDDUDUUDDUDUDDDUDDUDDUDUDUDUDDUDDDU"
    print("test2 count should be 6, result = {}".format(count_valleys(test2)))

