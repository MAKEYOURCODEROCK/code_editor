import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox





class Menubar:

    def __init__(self, parent, textarea):
        font_specs = ("ubuntu", 14)

        menubar = tk.Menu(parent.master, font=font_specs)
        parent.master.config(menu=menubar)

        

        file_dropdown = tk.Menu(menubar, font=font_specs, tearoff=0)
        file_dropdown.add_command(label="New File",
                                  accelerator="Cmd+N",
                                  command=parent.new_file)
        file_dropdown.add_command(label="Open File",
                                  accelerator="Cmd+O",
                                  command=parent.open_file)
        file_dropdown.add_command(label="Save",
                                  accelerator="Cmd+S",
                                  command=parent.save)
        file_dropdown.add_command(label="Save As",
                                  accelerator="Cmd+Shift+S",
                                  command=parent.save_as)
        file_dropdown.add_command(label="Undo",
                                  accelerator="Cmd+Z",
                                  command=textarea.edit_undo),
        file_dropdown.add_separator()
        file_dropdown.add_command(label="Exit",
                                  command=parent.master.destroy)

        view_dropdown = tk.Menu(menubar, font=font_specs, tearoff=0)
        view_dropdown.add_command(label="Open Music Player",
                                   command=parent.master.destroy)
        

        about_dropdown = tk.Menu(menubar, font=font_specs, tearoff=0)
        about_dropdown.add_command(label="Release Notes",
                                   command=self.show_release_notes)
        about_dropdown.add_separator()
        about_dropdown.add_command(label="About",
                                   command=self.show_about_message)

        menubar.add_cascade(label="File", menu=file_dropdown)
        menubar.add_cascade(label="Music", menu=about_dropdown)
        menubar.add_cascade(label="About", menu=about_dropdown)

    def show_about_message(self):
        box_title = "Welcome to Blu Text"
        box_message = "Version 0.0.1"
        messagebox.showinfo(box_title, box_message)

    def show_release_notes(self):
        box_title = "Release Notes"
        box_message = "Version 0.01"
        messagebox.showinfo(box_title, box_message)





class PyText:

    def __init__(self, master):
        master.title("Untitled")
        #master.config(bg = "red")
        master.geometry("1200x700")
        font_specs = ("ubuntu", 12)

        self.master = master
        self.filename = None
        self.textarea = tk.Text(master, width="4000",  insertwidth="6", insertbackground="white", font=(font_specs), background="black", fg="white", bd="0")
        self.scroll = tk.Scrollbar(master, command=self.textarea.yview)
        self.textarea.configure(yscrollcommand=self.scroll.set)
        self.textarea.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        self.scroll.pack(side=tk.RIGHT, fill=tk.Y)

        self.textarea.bind("<Key>", key_pressed)


        self.menubar = Menubar(self, self.textarea)
        #self.statusbar = Statusbar(self)
        self.bind_shortcuts()

    def set_window_title(self, name=None):
        if name:
            self.master.title(name)
        else:
            self.master.title("Untitled")

    def new_file(self, *args):
        self.textarea.delete(1.0, tk.END)
        self.filename = None
        self.set_window_title()

    def open_file(self, *args):
        self.filename = filedialog.askopenfilename(
            defaultextension=".txt",
            filetypes=[("All Files", "*.*"),
                       ("Text Files", "*.txt"),
                        ("Python Scripts", "*.py"),
                        ("Markdown Documents", "*.md"),
                        ("JavaScript Files", "*.js"),
                        ("HTML Documents", "*.html"),
                        ("CSS Documents", "*.css"),
                        ("Swift", "*.swift"),
                        ("mocha", "*.mocha"),
                        ("C++", "*.cc"),
                        ("C", "*.c"),
                        ("BATCHFILE", "*.bat"),
                        ("My-SQL", "*.sql"),
                        ("JSON", "*.json"),
                        ("PHP", "*.php")])
        if self.filename:
            self.textarea.delete(1.0, tk.END)
            with open(self.filename, "r") as f:
                self.textarea.insert(1.0, f.read())
            self.set_window_title(self.filename)
    
    def save(self, *args):
        if self.filename:
            try:
                textarea_content = self.textarea.get(1.0, tk.END)
                with open(self.filename, "w") as f:
                    f.write(textarea_content)
                #self.statusbar.update_status(True)
            except Exception as e:
                print(e)
        else:
            self.save_as()

    def save_as(self, *args):
        try:
            new_file = filedialog.asksaveasfilename(
                initialfile="Untitled.txt",
                defaultextension=".txt",
                filetypes=[("All Files", "*.*"),
                        ("Text Files", "*.txt"),
                        ("Python Scripts", "*.py"),
                        ("Markdown Documents", "*.md"),
                        ("JavaScript Files", "*.js"),
                        ("HTML Documents", "*.html"),
                        ("CSS Documents", "*.css"),
                        ("Swift", "*.swift"),
                        ("mocha", "*.mocha"),
                        ("C++", "*.cc"),
                        ("C", "*.c"),
                        ("BATCHFILE", "*.bat"),
                        ("My-SQL", "*.sql"),
                        ("JSON", "*.json"),
                        ("PHP", "*.php")])
            textarea_content = self.textarea.get(1.0, tk.END)
            with open(new_file, "w") as f:
                f.write(textarea_content)
            self.filename = new_file
            self.set_window_title(self.filename)
            #self.statusbar.update_status(True)
        except Exception as e:
            print(e)

    def bind_shortcuts(self):
        self.textarea.bind('<Control-n>', self.new_file)
        self.textarea.bind('<Control-o>', self.open_file)
        self.textarea.bind('<Command-n>', self.new_file)
        self.textarea.bind('<Command-o>', self.open_file)
        self.textarea.bind('<Control-s>', self.save)
        self.textarea.bind('<Command-s>', self.save)
        self.textarea.bind('<Command-s>', self.save_as)
        self.textarea.bind('<Control-S>', self.save_as)
        #self.textarea.bind('<Key>', self.statusbar.update_status)



def key_pressed(key):
    #print(key.char)
    print(key.char)
    
    #print(self.textarea)

def music():
    print("Hello world")
    

        


if __name__ == "__main__":
    master = tk.Tk()
    #master.bind("<Key>", key_pressed)
    master.config(bg="black")
    pt = PyText(master)
    master.mainloop()
