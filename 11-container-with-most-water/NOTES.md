# declare a variable: res
# two pointers: leftmost and rightmost
# find area
# res = max(area, res)
​
# approach to find a greater area -> move the shorter endpoint
# if left H < right H: keep right pointer, move left pointer to next
# if left H >= right H, keep left pointer, move right pointer to next
# repeat line5 and 6 to update res