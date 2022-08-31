Ex. 7 8 9 1 2 3 4 5
7 8 9 10 1 2 3 4
* declare left and right pointer
* while loop: left <= right
* mid = (left + right)//2
* if mid value = target -> return mid
* if left portion is sorted(left <= mid):  左侧为顺序排列
*  若target < left 或者 target > mid  -> left = mid + 1
* else: right = mid
* if 右侧为顺序排列， 即mid < right:
* 若target < mid 或target >  right -> right = mid
* else: left = mid + 1