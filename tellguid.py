import sys
reload(sys) 
sys.setdefaultencoding( "utf-8" ) 

def book_guid(book_guid):
    result=[]
    f = NoteStore.NoteFilter()
    f.notebookGuid=book_guid #core
    spec = NoteStore.NotesMetadataResultSpec()
    spec.includeTitle = False
    ourNoteList=note_store.findNotesMetadata(devToken,f,0,100,spec)
    for  notemeta in ourNoteList.notes:
        result.append(notemeta.guid)
    return result
    

def book_name(book_name):
    for notebook in note_store.listNotebooks():             
        if notebook.name ==book_name:
            return book_guid(notebook.guid)            
               
