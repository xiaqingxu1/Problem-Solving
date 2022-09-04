用stack 来储存nodes
用curr来指代root node
​
while loop 当stack 或者 curr存在时：
while loop 当curr存在时：
将curr node 存入stack， 并curr = curr.left（向左分叉下移）
exit while loop时即代表curr不存在了， 即最左边的branch已traverse完毕
对stack 进行while loop：
从stack中pop出最有一个node， 即左下角（值最小的node）， 此时 k 减一
若当前k = 0， 则代表现在这个node即为所寻找的kth node
弱当前k不为0， 则继续从stack中pop出node来，重复上述过程
将curr指向curr的右侧， curr = curr.right