*  use an array to hold product result
*  res = [1] * len(nums) // array to present
* 从前往后走计算一遍不包含本字母在内左边所有数字的product
* prefix = 1
* iterate over the nums, for each i, num
*        assgin prefix value to res[i]
*        update prefix by mutiplyin num (to be used in next round)
* 再从后往前走一遍， 计算右边数字的总和
*    postfix = 1
*    iterate over the nums[::-1], for each i, num
*        assign res[i] = postfix * res[i]
*        update postfix by multiplying current num
​
*    return res
​