# INSERTION SORT #

Sort a given list of numbers either in ascending or descending order.

## Input ##

A list either sorted or unsorted i.e [5, 1, 9, 8, 2]

## Output ##

Sorted list i.e [1, 2, 5, 8, 9]

## PSeudocode ##

1.Set key to 0
2. While True
    2.1 Loop through numbers in the list from key to end of  list.
        i. Find the smallest value in list.
    2.2.a If smallest found
            swap smallest value and  value at numbers[key]
            increment key
    2.2.b if smallest not found.
            numbers is sorted, break out of outer loop
4. Repeat 2
