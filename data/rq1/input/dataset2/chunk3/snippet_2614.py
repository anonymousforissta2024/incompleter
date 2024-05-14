#Source: https://stackoverflow.com/questions/76041886/filenotfounderror-errno-2-no-such-file-or-directory-file-name-py
########################################
#TREE
########################################
file_tree = Frame(root)
file_tree.pack(side='left', fill=Y, expand=NO)
def open_dir():
    for i in tree.get_children():
        tree.delete(i)
    path = askdirectory()
    abspath = os.path.abspath(path)
    root_node = tree.insert('', 'end', text=abspath, open=True)
    process_directory(root_node,abspath)

def process_directory( parent, path):

        for p in os.listdir(path):
            abspath = os.path.join(path, p)
            isdir = os.path.isdir(abspath)
            oid = tree.insert(parent, 'end', text=p, open=False)
            if isdir:
                process_directory(oid, abspath)

def Open_file_from_list_box(value):
    global file
    item_id = tree.selection()
    file = tree.item(item_id, 'text') # get the filename from 'text' option
    filepath = os.path.join(value,file)     
    editArea.delete(1.0,END)
    with open(filepath,"r") as f:
        editArea.insert(1.0,f.read())

tree = ttk.Treeview(file_tree)
tree.pack(expand=YES,fill=BOTH)
path = '.'
tree.heading('#0', text=path, anchor='w')
abspath = os.path.abspath(path)
root_node = tree.insert('', 'end', text=abspath, open=True)
process_directory(root_node, abspath)

tree.bind("<<TreeviewSelect>>",lambda event=None:Open_file_from_list_box(path))