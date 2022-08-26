* declare a variable to store subsequence
* iterate through the string using a while loop
*    assign left and right pointers
*    if current letter = next letter:
*          move right pointer to next
*    move curr to right pointer + 1 (下一回合，从右指针的下一位开始）
​
​
*   while loop: 若当前左指针未归零，右指针未到最后一位， 且左指针-1位 == 右指针 + 1
*       则把左指针左移， 右指针右移
*   从while loop出来后， 代表m至n为palindrome， 取result 和 s[m:n+1] 两者长度更长者