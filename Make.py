from tkinter import *


class make:
    def __init__(self, root, color):
        self.root = root
        self.color = color

    def backFrame(self):
        frame = Frame(self.root, width=400, height=50, bg=self.color)
        frame.pack(side=TOP)

        return frame

    def backButton(self, frame, text, func, **kwargs):
        btn = Button(frame, text=text, width=12,
                     highlightbackground=self.color, command=func)
        btn.grid(row=kwargs['row'], column=kwargs['column'])

        return btn

    def backLabel(self, frame, txt, **kwargs):
        label = Label(frame, text=txt, bg=self.color)
        label.grid(row=kwargs['row'], column=kwargs['column'])

        return label

    def backEntry(self, frame, value, **kwargs):
        entry = Entry(frame, highlightbackground=self.color,
                      textvariable=value)
        entry.grid(row=kwargs['row'], column=kwargs['column'])

        return entry

    def backListBox(self, frame, **kwargs):
        list = Listbox(frame, width=35, height=6)
        list.grid(row=kwargs['row'], column=kwargs['column'], rowspan=6, columnspan=2)

        return list
