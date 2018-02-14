# EvernoteEasyGuids
在命令行中交互的一个按名称查找笔记(note)的guid的小程序。

针对确定的笔记操作时，只知笔记的guid足够，所以没有设计笔记本guid的输出

支持筛选方式：
1.指定标题的笔记本中，所有笔记的guid
2.指定标题的笔记的guid——可给定或不给其所在笔记本名称

支持输出方式：
将笔记本名称,guid
1.print输出
2.保存为txt文件 （文件名固定为 ‘guids_output.txt’，需在源码中修改）

特色
支持中文笔记本名、笔记名的输入输出

写作版本
python 2.7
3以上请注意Evernote SDK版本、中文编码处理、print 语句

使用方法
1.下载 EasyGuids.py
2.将自己的devToken填入源码
3.同目录命令行中运行 python EasyGuids.py 
4.按提示分别选择筛选方式、输出方式

How to Use
1.Have Evernote SDK for python2 installed
2.Get yourself a Evernote Developer Token 
3.Download EasyGuids.py
4.Fill your Developer Token in EasyGuids.py
5.Run it EasyGuids.py with Python2.7
6..Select Filter mode and if save or print on screen based on prompts
7.Get guids on screen or in .txt file

