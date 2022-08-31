Ex. 7 8 9 1 2 3 4 5
7 8 9 10 1 2 3 4
* declare left and right pointer
* while loop: left < right
* mid = (left + right)//2
* if mid value = target -> return mid
* if conditions:  mid < left and target > mid,  mid > left and target > mid
* move left to mid + 1
* if conditions:  mid < left and target < mid, mid > left and target < mid
* move right to mid