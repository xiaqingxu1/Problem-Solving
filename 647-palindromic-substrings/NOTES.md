The main idea is to **pick a center and then extend towards the bounds** of the input string. With this approach, we count all valid pallindrome substrings which are based on the specified center.
​
There are **two valid cases** of centers for finding pallindrome substrings:
​
If it's an **odd-lengthed** pallindrome string, then our centers will expand from same center and will match the criteria i=j. eg: for string "aba", center is i=j=1.
If it's an **even-lengthed** pallindrome string, then our centers will not expand from same center and will match the criteria i+1=j eg: for string "abba",i=1, j=2.
​