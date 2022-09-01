declare curr = []
declare count = 0
iterate over the string, for each character:
iterate over curr， 将curr中每一项都加上c，再将当前char加入curr
更新 count += curr中palindrome
​
return curr