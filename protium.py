#!/usr/bin/env python

# protium - a web browser & renderer written in Python
# code written by danceitbreakit on github
# feel free to do whatever with this code
# ps. dont expect comments in this code lol figure it out yourself, im not taking my time to write comments like a loser

import requests as rq
import tkinter as tk
import tkinter.font as tkfont
from bs4 import BeautifulSoup as bs
#from PIL import ImageTk, Image

# https://iamwillwang.com/every-html-element/
# test website ^^^ 
# use i.string for text value, alt i.get_text()

def loadpage():
	for widget in frame.winfo_children():
		widget.destroy()
	global scr
	src = url.get()
	try:
		if "https://" in src or "http://" in src or 'file://' in src:
			rqstr = rq.get(src)
		else:
			rqstr = rq.get(f"{urlprefix.get()}{src}")
	except rq.exceptions.InvalidURL:
		popup = tk.Tk()
		popup.overrideredirect(True)
		popup['bg'] = "red"
		tk.Label(popup, text = "Invalid URL!").pack(padx = 30, pady = 30)
		popup.attributes('-topmost', True)
		popup.after(1000, popup.destroy())
		popup.mainloop()
		return None
	render(rqstr.text, src)

def redirect(src):
	try:
		if "https://" in src or "http://" in src:
			rqstr = rq.get(src)
		else:
			rqstr = rq.get(f"https://{src}")
	except rq.exceptions.InvalidURL:
		popup = tk.Tk()
		popup.overrideredirect(True)
		popup['bg'] = "red"
		tk.Label(popup, text = "Invalid URL!").pack(padx = 30, pady = 30)
		popup.attributes('-topmost', True)
		popup.after(1000, popup.destroy())
		popup.mainloop()
		return None
	for widget in frame.winfo_children():
		widget.destroy()
	render(rqstr.text, src)

def render(source, url):
	frame.configure(width = 3000, height = 50000)
	canvas.configure(scrollregion = (0,0,3000,50000))
	urlhtml = bs(source, 'html.parser').find_all(True)
	#print(urlhtml)
	for i in urlhtml:
		if i.name == 'body':
			if i.get('background-color') != None:
				frame.configure(bg = i.get('background-color'))
		# <p> or <data> or <time> or <span> or <header> or <footer> or <aside> or <search> or <nav>
		if i.name == 'p' or i.name == "#text" or i.name == 'data' or i.name == 'nav' or i.name == 'time' or i.name == 'span' or i.name == 'header' or i.name == 'footer' or i.name == 'aside' or i.name == 'search':
			currenttk = tk.Label(frame,
				text = i.string,
				bg = "snow", #i.get('background-color'),
				fg = i.get('color'),
				font = ("Times New Roman", 12),
				justify = "left",
				)
			currenttk.pack(anchor = "w")
		# <a>
		if i.name == 'a':
			src = ""
			try:
				src = i.get('href')
			except Exception:
				src = "<Invalid URL>"
			currenttk = tk.Button(frame,
				text = f"\"{i.text}\" ({src})", # i.text,
				bg = "snow", #i.get('background-color'),
				fg = "RoyalBlue1",
				relief = "flat",
				highlightthickness = 0,
				height = -1,
				width = -1,
				font = ("Times New Roman", 12, "underline"),
				justify = "left",
				#font = ("Comic Sans MS", i.get('font-size')),
				)
			currenttk.configure(command = lambda src = src: redirect(src))
			currenttk.pack(anchor = "w", padx = 0, pady = 0) #place(x = i['x'], y = i['y'])
		# <h1>
		if i.name == 'h1':
			currenttk = tk.Label(frame,
				text = i.string,
				bg = "snow", #i.get('background-color'),
				fg = i.get('color'),
				font = ("Times New Roman", 24, "bold"),
				justify = "left",
				#font = ("Comic Sans MS", i.get('font-size')),
				).pack(anchor = "w") #place(x = i['x'], y = i['y'])
		# <h2>
		if i.name == 'h2':
			currenttk = tk.Label(frame,
				text = i.string,
				bg = "snow", #i.get('background-color'),
				fg = i.get('color'),
				font = ("Times New Roman", 20, "bold"),
				justify = "left",
				#font = ("Comic Sans MS", i.get('font-size')),
				).pack(anchor = "w") #place(x = i['x'], y = i['y'])
		# <h3>
		if i.name == 'h3':
			currenttk = tk.Label(frame,
				text = i.string,
				bg = "snow", #i.get('background-color'),
				fg = i.get('color'),
				font = ("Times New Roman", 16, "bold"),
				justify = "left",
				#font = ("Comic Sans MS", i.get('font-size')),
				).pack(anchor = "w") #place(x = i['x'], y = i['y'])
		# <h4>
		if i.name == 'h4':
			currenttk = tk.Label(frame,
				text = i.string,
				bg = "snow", #i.get('background-color'),
				fg = i.get('color'),
				font = ("Times New Roman", 12, "bold"),
				justify = "left",
				#font = ("Comic Sans MS", i.get('font-size')),
				).pack(anchor = "w") #place(x = i['x'], y = i['y'])
		# <h5>
		if i.name == 'h5':
			currenttk = tk.Label(frame,
				text = i.string,
				bg = "snow", #i.get('background-color'),
				fg = i.get('color'),
				font = ("Times New Roman", 9, "bold"),
				justify = "left",
				#font = ("Comic Sans MS", i.get('font-size')),
				).pack(anchor = "w") #place(x = i['x'], y = i['y'])
		# <h6>
		if i.name == 'h6':
			currenttk = tk.Label(frame,
				text = i.string,
				bg = "snow", #i.get('background-color'),
				fg = i.get('color'),
				font = ("Times New Roman", 8, "bold"),
				justify = "left",
				#font = ("Comic Sans MS", i.get('font-size')),
				).pack(anchor = "w") #place(x = i['x'], y = i['y'])
		# <li> or <menu> or <blockquote>
		if i.name == 'li' or i.name == 'menu' or i.name == "blockquote":
			currenttk = tk.Label(frame,
				text = f"\t•  {i.string}",
				bg = "snow", #i.get('background-color'),
				fg = i.get('color'),
				font = ("Times New Roman", 12),
				justify = "left",
				)
			if i.name == "blockquote":
				currenttk.configure(text = i.string, bg = "grey80")
				currenttk.pack(anchor = "w", padx = 45)
			else:
				currenttk.pack(anchor = "w") #place(x = i['x'], y = i['y'])
		# <b> or <strong>
		if i.name == 'b' or i.name == 'strong':
			currenttk = tk.Label(frame,
				text = i.string,
				bg = "snow", #i.get('background-color'),
				fg = i.get('color'),
				font = ("Times New Roman", 12, "bold"),
				justify = "left",
				)
			currenttk.pack(anchor = "w")
		# <i> or <em> or <cite> or <dfn> or <var> or <address>
		if i.name == 'i' or i.name == 'em' or i.name == 'cite' or i.name == 'dfn' or i.name == 'var' or i.name == 'address':
			currenttk = tk.Label(frame,
				text = i.string,
				bg = "snow", #i.get('background-color'),
				fg = i.get('color'),
				font = ("Times New Roman", 12, "italic"),
				justify = "left",
				)
			currenttk.pack(anchor = "w")
		# <u> or <ins>
		if i.name == 'u' or i.name == 'ins':
			currenttk = tk.Label(frame,
				text = i.string,
				bg = "snow", #i.get('background-color'),
				fg = i.get('color'),
				font = ("Times New Roman", 12, "underline"),
				justify = "left",
				)
			currenttk.pack(anchor = "w")
		# <mark>
		if i.name == 'mark':
			currenttk = tk.Label(frame,
				text = i.string,
				bg = "yellow",
				fg = i.get('color'),
				font = ("Times New Roman", 12),
				justify = "left",
				)
			currenttk.pack(anchor = "w")
		# <s> or <del>
		if i.name == 's' or i.name == 'del':
			currenttk = tk.Label(frame,
				text = i.string,
				bg = "snow",
				fg = i.get('color'),
				font = ("Times New Roman", 12, "overstrike"),
				justify = "left",
				)
			currenttk.pack(anchor = "w")
		# <small>
		if i.name == 'small':
			currenttk = tk.Label(frame,
				text = i.string,
				bg = "snow", #i.get('background-color'),
				fg = i.get('color'),
				font = ("Times New Roman", 6),
				justify = "left",
				)
			currenttk.pack(anchor = "w")
		# <sub>
		if i.name == 'sub':
			currenttk = tk.Label(frame,
				text = i.string,
				bg = "snow", #i.get('background-color'),
				fg = i.get('color'),
				font = ("Times New Roman", 7),
				justify = "left",
				)
			currenttk.pack(anchor = "sw")
		# <sup>
		if i.name == 'sup':
			currenttk = tk.Label(frame,
				text = i.string,
				bg = "snow", #i.get('background-color'),
				fg = i.get('color'),
				font = ("Times New Roman", 7),
				justify = "left",
				)
			currenttk.pack(anchor = "nw")
		# <br>
		if i.name == 'br':
			currenttk = tk.Label(frame,
				text = "",
				bg = "snow", #i.get('background-color'),
				fg = i.get('color'),
				font = ("Times New Roman", 12),
				justify = "left",
				)
			currenttk.pack(anchor = "w", padx = 0, pady = 0)
		# <code>
		if i.name == 'code':
			currenttk = tk.Label(frame,
				text = i.string,
				bg = "grey80", #i.get('background-color'),
				relief = "sunken",
				fg = i.get('color'),
				font = ("Consolas", 10),
				justify = "left",
				)
			currenttk.pack(anchor = "w")
		# <abbr>
		if i.name == 'abbr':
			currenttk = tk.Label(frame,
				text = i.string,
				bg = "snow", #i.get('background-color'),
				fg = "orange4",
				font = ("Consolas", 12),
				justify = "left",
				)
			currenttk.pack(anchor = "w")
		# <kbd> or <samp>
		if i.name == 'kbd' or i.name == 'samp':
			currenttk = tk.Label(frame,
				text = i.string,
				bg = "snow", #i.get('background-color'),
				fg = i.get('color'),
				font = ("Consolas", 10),
				justify = "left",
				)
			if i.name == 'samp':
				currenttk.configure(font = ("Consolas", 8))
			currenttk.pack(anchor = "w")
		# <hr>
		#if i.name == 'hr':
		# <button>
		if i.name == 'button':
			currenttk = tk.Button(frame,
				text = i.string,
				bg = "grey70", #i.get('background-color'),
				fg = i.get('color'),
				font = ("Times New Roman", 10),
				justify = "left",
				)
			currenttk.pack(anchor = "w")
		# <ruby> or <math> or <dl>
		if i.name == 'ruby' or i.name == 'math' or i.name == 'dl':
			currenttk = tk.Label(frame,
				text = i.get_text(),
				bg = "snow", #i.get('background-color'),
				fg = i.get('color'),
				font = ("Times New Roman", 12),
				justify = "left",
				)
			currenttk.pack(anchor = "w")
		# <q>
		if i.name == 'q':
			currenttk = tk.Label(frame,
				text = f"\"{i.get_text()}\"",
				bg = "snow", #i.get('background-color'),
				fg = i.get('color'),
				font = ("Times New Roman", 12),
				justify = "left",
				)
			currenttk.pack(anchor = "w")

	tk.Label(frame).pack(anchor = "w")

	global urldisplay
	urldisplay.configure(text = url)

def searchquery():
	for widget in frame.winfo_children():
		widget.destroy()
	query = searchengine.get()
	match query:
		case "Wiby":
			src = rq.get(f"https://wiby.org/?q={search.get().replace(" ", "+")}")
			render(src.text, f"https://wiby.org/?q={search.get().replace(" ", "+")}")

root = tk.Tk()
root.title("Protium - a web browser & renderer written in Python")
root['bg'] = "chartreuse4"
root.wm_attributes("-zoomed", True)


tk.Label(root, text = "", bg = "chartreuse4").pack(pady = 8)
url = tk.StringVar()
urlprefix = tk.StringVar()
urlprefix.set("https://")
searchengine = tk.StringVar()
searchengine.set("Wiby")
search = tk.StringVar()

location = tk.OptionMenu(root,
	urlprefix,
	"https://", "http://").place(x = 10, y = 5) # file does not work yet
tk.Entry(root,
	font = ("Comic Sans MS", 10),
	textvariable = url).place(x = 105, y = 10)
tk.Button(root,
	text = "Go!",
	font = ("Comic Sans MS", 10),
	command = lambda: loadpage(),
	).place(x = 275, y = 5)

engine = tk.OptionMenu(root,
	searchengine,
	"Wiby").place(x = 450, y = 5)
tk.Entry(root,
	font = ("Comic Sans MS", 10),
	textvariable = search).place(x = 531, y = 10)
tk.Button(root,
	text = "Search!",
	font = ("Comic Sans MS", 10),
	command = lambda: searchquery()
	).place(x = 701, y = 5)
urldisplay = tk.Label(root, 
	text="",
	bg = "chartreuse4",
	fg = "grey90",
	justify = "right",
	font = ("Comic Sans MS", 12))
urldisplay.place(x = 800, y = 5)

canvas = tk.Canvas(root,
					bg = "snow", #"#000000",
					scrollregion = (0,0,1366,50000))
frame = tk.Frame(canvas,
	bg = "snow",
	width = 5000,
	height = 50000)
verticalscrollbar = tk.Scrollbar(canvas,
	orient = "vertical",
	command = canvas.yview,
	width = 12)
horizontalscrollbar = tk.Scrollbar(canvas,
	orient = "horizontal",
	command = canvas.xview,
	width = 12)
frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)
canvas.configure(yscrollcommand = verticalscrollbar.set, xscrollcommand = horizontalscrollbar.set)
#frame.pack(expand = True, fill = tk.BOTH, side = tk.LEFT)
canvas.create_window((50,50), window=frame, anchor="nw")
canvas.pack(expand = True, side = tk.LEFT, fill = tk.BOTH, padx = 5, pady = 5)
verticalscrollbar.pack(fill = tk.Y, side = tk.RIGHT)
horizontalscrollbar.pack(fill = tk.X, side = tk.BOTTOM)

root.mainloop()