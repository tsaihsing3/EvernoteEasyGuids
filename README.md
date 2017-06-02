# EvernoteEasyGuids
from notebookname,notename,etc. return a list of guids.

Evernote API还是很简单的。这里把常用的寻找笔记guid做了封装。也是python模块学习的作业。
Evernote 的filter功能还支持以标签等查找笔记。后续会加上。

使用举例
from evernote.edam.notestore import NoteStore 
import tellguid as tg
tg.note_store=note_store
tg.devToken=devToken
tg.NoteStore=NoteStore
#设置必要的三个参数

for one in tg.book_name('mynotebookname'):
    print one.decode('utf-8').encode(sys.getfilesystemencoding())#保证中文等支持输出

for one in tg.book_guid('mynotebookguid'):
    print one
    
