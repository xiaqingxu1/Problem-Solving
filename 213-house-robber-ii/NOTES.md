* helper func为House Robber I的答案， 用2个variable 来track 至 curr - 2， curr -1 的总和，若curr - 2 + 当前值 > curr - 1 的值，即代表值应该被rob， 前一个被跳过
​
* House RobberII 的解法为： 将 nums分成2个， 1个没有头，一个没有尾， 则变成了了2个house robberI的问题， 取两者之间更大值即可
​
* 唯一的edge case就是当nums只有一个数字时， 去头和去尾都为0，但并不正确，最大值应为nums[0]
​
​