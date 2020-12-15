import numpy as np
import pandas as pd
from tkinter import *
from tkinter import messagebox
import os
import random

board = pd.DataFrame({'0' : np.array(['--','--','--','--','--','--','--','--','--','--']),
						'1' : np.array(['--','--','--','--','--','--','--','--','--','--']),
						'2' : np.array(['--','--','--','--','--','--','--','--','--','--']),
						'3' : np.array(['--','--','--','--','--','--','--','--','--','--']),
						'4' : np.array(['--','--','--','--','--','--','--','--','--','--']),
						'5' : np.array(['--','--','--','--','--','--','--','--','--','--']),
						'6' : np.array(['--','--','--','--','--','--','--','--','--','--']),
						'7' : np.array(['--','--','--','--','--','--','--','--','--','--']),
						'8' : np.array(['--','--','--','--','--','--','--','--','--','--']),
						'9' : np.array(['--','--','--','--','--','--','--','--','--','--'])},
						index = [0,1,2,3,4,5,6,7,8,9])

ct=0

position = {}

position['currx'] = random.randint(1,9)
position['curry'] = random.randint(4,9)

position['prevx'] = 0
position['prevy'] = 0

position['currow'] = 0
position['curcol'] = 0

position['prevrow'] = 0
position['prevcol'] = 0

board.iloc[position['currow']][position['curcol']] = '#'
board.iloc[position['curry']][position['currx']] = '$'

def right(position):
	if position['curcol']==9:
		pass
	else:
		position['prevrow'] = position['currow']
		position['prevcol'] = position['curcol']
		position['curcol'] = position['curcol']+1
		board.iloc[position['currow']][position['curcol']] = '#'
		board.iloc[position['prevrow']][position['prevcol']] = '--'
	movement(position)
	
def left(position):
	if position['curcol']==0:
		pass
	else:
		position['prevrow'] = position['currow']
		position['prevcol'] = position['curcol']
		position['curcol'] = position['curcol']-1
		board.iloc[position['currow']][position['curcol']] = '#'
		board.iloc[position['prevrow']][position['prevcol']] = '--'
	movement(position)
	
def up(position):
	if position['currow']==0:
		pass
	else:
		position['prevrow'] = position['currow']
		position['prevcol'] = position['curcol']
		position['currow'] = position['currow']-1
		board.iloc[position['currow']][position['curcol']] = '#'
		board.iloc[position['prevrow']][position['prevcol']] = '--'
	movement(position)
	
def down(position):
	if position['currow']==9:
		pass
	else:
		position['prevrow'] = position['currow']
		position['prevcol'] = position['curcol']
		position['currow'] = position['currow']+1
		board.iloc[position['currow']][position['curcol']] = '#'
		board.iloc[position['prevrow']][position['prevcol']] = '--'
	movement(position)
	
def movement(position):
	global ct
	ct+=1
	chancevert = random.randint(1,2)
	chancehorz = random.randint(1,2)
	position['prevx'] = position['currx']
	position['prevy'] = position['curry']
	if chancevert == 1:
		if chancehorz==1:
			if position['curry'] == 0:
				position['curry'] = position['curry']+1
			else:
				position['curry'] = position['curry']-1
		elif chancehorz==2:
			if position['curry'] == 9:
				position['curry'] = position['curry']-1
			else:
				position['curry'] = position['curry']+1
	elif chancevert == 2:
		if chancehorz==1:
			if position['currx'] == 0:
				position['currx'] = position['currx']+1
			else:
				position['currx'] = position['currx']-1
		elif chancehorz==2:
			if position['currx'] == 9:
				position['currx'] = position['currx']-1
			else:
				position['currx'] = position['currx']+1
	board.iloc[position['curry']][position['currx']] = '$'
	board.iloc[position['prevy']][position['prevx']] = '--'
	if position['prevx'] == position['curcol'] and position['prevy'] == position['currow']:
		board.iloc[position['currow']][position['curcol']] = '#'
	os.system("cls")
	print("Catch the dollar\n\n{}\n\nYour position: {},{}\nDollar position: {},{}\nMoves: {}".format(board,position['currow'],position['curcol'],position['curry'],position['currx'],ct))
	if position['currx'] == position['curcol'] and position['curry'] == position['currow']:
		board.iloc[position['curry']][position['currx']] = '#'
		os.system("cls")
		print("Catch the dollar\n\n{}\n\nYour position: {},{}\nDollar position: {},{}\nMoves: {}".format(board,position['currow'],position['curcol'],position['curry'],position['currx'],ct))
		messagebox.showinfo("You win","Congratulations! You caught the dollar!")
		root.destroy()
		quit()

os.system("cls")
print("Catch the dollar\n\n{}\n\nYour position: {},{}\nDollar position: {},{}\nMoves: {}".format(board,position['currow'],position['curcol'],position['curry'],position['currx'],ct))

root = Tk()
root.geometry("235x100+500+200")
root.title("Controls")

UP = Button(root,text="UP",width=10,command = lambda : up(position))
UP.grid(row=0,column=1)

DOWN = Button(root,text="DOWN",width=10,command = lambda : down(position))
DOWN.grid(row=1,column=1)

LEFT = Button(root,text="LEFT",width=10,command = lambda : left(position))
LEFT.grid(row=1,column=0)

RIGHT = Button(root,text="RIGHT",width=10,command = lambda : right(position))
RIGHT.grid(row=1,column=2)

root.mainloop()
