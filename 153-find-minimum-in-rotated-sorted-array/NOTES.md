1. binary heap problem
2. declare left pointer and right pointer
3. use while loop: left < right
*     mid = (left + right) // 2
*     if mid value < right: meaning 右侧为sorted， 则将 right pointer 移至mid 位置
*     if left < mid value: 说明左侧为sorted， 则将left pointer移至mid 位置
4. 返回 right value