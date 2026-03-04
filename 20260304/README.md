# Perfect Cube Count
Given two integers, determine how many perfect cubes exist in the range between and including the two numbers.

The lower number is not garanteed to be the first argument.
A number is a perfect cube if there exists an integer (n) where n * n * n = number. For example, 27 is a perfect cube because 3 * 3 * 3 = 27.

The key to the challenge is that when calculating cubicroot, Python messes up with float numbers. Like cubicroot of 64 would result in 3.99999999996 rather than 4.
