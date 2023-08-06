import webbrowser
from tkinter import *
from tkinter import ttk
from googlesearch import search


def googlesearch(query):
	print("Here is the top search result for ",query)
	for i in search(query, tld="co.in", num=1, stop=1, pause=2):
		print(i)
		webbrowser.open(i)


win = Tk()
win.geometry("1000x500")


def get_value():
	e_text = inputsearch.get()
	Label(win, text=e_text, font=('Times 15 bold')).pack(pady=20)
	googlesearch(e_text)
	win.destroy()


# Create an Entry Widget
inputsearch = ttk.Entry(win, font=('Times 12'),width=40)
inputsearch.pack(pady=50)

# Create a button to display the text of entry widget
button = ttk.Button(win, text="Search Google", command=get_value)
button.pack()
win.mainloop()



