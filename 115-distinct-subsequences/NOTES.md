* target中每一个letter出现时 该letter对应在dp里的位置里（显示target可能被找到的次数） = 该letter前一次字母出现次数 + 本letter出现次数
​
* example2: string = “babgbag” target = “bag”
​
* for string 中每一个字母：
iterate target from end to front：
如果string中字母和target中字母相同： 则意味着target中字母被找到“一次”（最开始为0时： target字母对应位置所显示的target已出现次数 则完全取决于前置位letter已出现次数； 若不为0: 则需将前置位和本位相加
* target之所以要由end -> front： 因为前值为出现次数增加，若后置位此后并没有出现，则无法将前置位后来出现的次数 计入 target出现总数