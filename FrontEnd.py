from Make import *
import BackEnd


# ==================================== Setting ==================================== #
mainWindow = Tk()
mainWindow.title('Book Store')

JK = make(mainWindow, None)

JK.backLabel(mainWindow, 'Title', **{'row': 0, 'column': 0})
JK.backLabel(mainWindow, 'Author', **{'row': 0, 'column': 2})
JK.backLabel(mainWindow, 'Year', **{'row': 1, 'column': 0})
JK.backLabel(mainWindow, 'ISBN', **{'row': 1, 'column': 2})


# ==================================== Entries ==================================== #
title_text = StringVar()
JK.backEntry(mainWindow, title_text, **{'row': 0, 'column': 1})

author_text = StringVar()
JK.backEntry(mainWindow, author_text, **{'row': 0, 'column': 3})

year_text = StringVar()
JK.backEntry(mainWindow, year_text, **{'row': 1, 'column': 1})

isbn_text = StringVar()
JK.backEntry(mainWindow, isbn_text, **{'row': 1, 'column': 3})


# ==================================== Listbox ==================================== #
list = Listbox(mainWindow, width=35, height=8)
list.grid(row=2, column=0, rowspan=6, columnspan=2)
sb = Scrollbar(mainWindow)
sb.grid(row=3, column=2, rowspan=4, sticky='ns')
list.configure(yscrollcommand=sb.set)
sb.configure(command=list.yview)

def get_selected_row(event):
    global selected_book
    index = list.curselection()[0]
    selected_book = list.get(index)
    title_text.set(selected_book[1])
    author_text.set(selected_book[2])
    year_text.set(selected_book[3])
    isbn_text.set(selected_book[4])

list.bind('<<ListboxSelect>>', get_selected_row)


# ==================================== Functions ==================================== #
def clearEntry():
    title_text.set('')
    author_text.set('')
    year_text.set('')
    isbn_text.set('')

def printData(books):
    for book in books:
        list.insert(END, book)

def clearList():
    list.delete(0,END)

def viewAll():
    clearList()
    books = BackEnd.view()
    printData(books)

def searchEntry():
    clearList()
    books = BackEnd.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    printData(books)

def addEntry():
    BackEnd.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    print(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    clearEntry()
    viewAll()

def deleteSelected():
    BackEnd.delete(selected_book[0])
    clearEntry()
    viewAll()

def updateSelected():
    BackEnd.update(selected_book[0],title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    viewAll()

# ==================================== Buttons ==================================== #
JK.backButton(mainWindow, 'View All', viewAll, **{'row': 2, 'column': 3})
JK.backButton(mainWindow, 'Search Entry', searchEntry, **{'row': 3, 'column': 3})
JK.backButton(mainWindow, 'Add Entry', addEntry, **{'row': 4, 'column': 3})
JK.backButton(mainWindow, 'Update Selected', updateSelected, **{'row': 5, 'column': 3})
JK.backButton(mainWindow, 'Delete Selected', deleteSelected, **{'row': 6, 'column': 3})
JK.backButton(mainWindow, 'Close', mainWindow.destroy, **{'row': 7, 'column': 3})


# ==================================== Main Loop ==================================== #
def close(event):
    mainWindow.withdraw()  # if you want to bring it back
    exit()  # if you want to exit the entire thing


mainWindow.bind('<Escape>', close)
mainWindow.bind('<Control-Key-w>', close)

viewAll()
mainWindow.mainloop()
