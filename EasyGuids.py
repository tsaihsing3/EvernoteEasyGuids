# -*- coding: utf-8 -*-
"""
Created on Sun Apr 02 19:41:52 2017

@author: tsaihsing
"""
# for python 2.7
import sys
reload(sys) 
sys.setdefaultencoding( "utf-8" ) 

from evernote.api.client import EvernoteClient
devToken = [Enter you developer token as string here] 
client = EvernoteClient(token = devToken,sandbox=False)
note_store = client.get_note_store()
user_store = client.get_user_store()
from evernote.edam.notestore import NoteStore 

def printcn(raw):
    return raw.decode('utf-8').encode(sys.getfilesystemencoding())
def getcn(raw):
    return raw.decode(sys.getfilesystemencoding().encode('utf-8'))

Mode=None
while  Mode not in ('1','y','n'): 
    Mode=raw_input('(1)Output guids of all notes in a notebook or (2)Output guid of one singe note?:')
    if Mode == '2':
        Mode=raw_input('Is Noetbook\'s name already Known \n (y) or (n):')
        

SaveMode=None
while SaveMode not in ('txt','print'):
    SaveMode_0=raw_input('(1) Save guids into a .txt file or (2) print it:')
    if SaveMode_0 == '1': SaveMode='txt'
    if SaveMode_0 == '2': SaveMode='print'
 
need_notebook_title_Bool=(Mode in ('1','y')) #Bool Type
need_note_title_Bool=(Mode in ('y','n'))  #Bool Type



if need_notebook_title_Bool:
    given_notebook_title=getcn(raw_input('Enter the Notebook\'s Name:'))#here enter the name of the notebooks you need

if need_note_title_Bool:
    given_note_title=getcn(raw_input('Enter the Note\'s Name:'))

#save all notebooks' guid 
notebook_guid_list=[]
for notebook in note_store.listNotebooks():
    #print 'notebook.name=',printcn(notebook.name)
    if need_notebook_title_Bool:
        if notebook.name != given_notebook_title  :
            continue
        else:
            print 'Notebook Found:'
    #print 'Fit:',printcn(notebook.name)
    #notebookGuid = notebook.guid
    notebookt=(notebook.name,notebook.guid)
    notebook_guid_list.append(notebookt)

if Mode == 'n':print 'Searching through all notes in all notebooks...'
note_guid_list=[]
for onebook in notebook_guid_list: 
    f = NoteStore.NoteFilter()
    #one=(notebook.name,notebook.guid)   
    f.notebookGuid=onebook[1]
    #spec
    spec = NoteStore.NotesMetadataResultSpec()
    spec.includeTitle = True
       
    #get notes' titleXguid
    ourNoteList=note_store.findNotesMetadata(devToken,f,0,100,spec)
        
    for  notemeta in ourNoteList.notes:
        notet=notemeta.title
        noteg=notemeta.guid
        
        if need_note_title_Bool:
            if notet != given_note_title: 
                continue
            else:
                print 'Note Found'
        note_guidt=(notet,noteg)
        note_guid_list.append(note_guidt)

#save txt or print
allnotes_output=[]
for one in note_guid_list:
    notestr='\t'.join(one)
    allnotes_output.append(notestr)
allnotesstr_output='\n'.join(allnotes_output)

#Output
if SaveMode == 'txt':
    fhands=open('guids_output.txt','w') #here save notes' guids
    fhands.write(allnotesstr_output)
    fhands.close()
    print 'See: guids_output.txt'
if SaveMode == 'print':
    print printcn(allnotesstr_output)
    

