# if nums[mid] <= nums[right], we know the numbers continued increasing to
# the right of mid, so they never reached the pivot and wrapped around.
# therefore, we know the pivot must be at index <= mid.
​
# we know that nums[mid] <= nums[right].
# therefore, we know it is possible for the mid index to store a smaller
# value than at least one other index in the list (at right), so we do
# not discard it by doing right = mid - 1. it still might have the minimum value.
right = mid
# at this point, left and right converge to a single index (for minimum value) since
# our if/else forces the bounds of left/right to shrink each iteration:
​
# when left bound increases, it does not disqualify a value
# that could be smaller than something else (we know nums[mid] > nums[right],
# so nums[right] wins and we ignore mid and everything to the left of mid).
​
# when right bound decreases, it also does not disqualify a
# value that could be smaller than something else (we know nums[mid] <= nums[right],
# so nums[mid] wins and we keep it for now).
​
# so we shrink the left/right bounds to one value,
# without ever disqualifying a possible minimum
return nums[left]