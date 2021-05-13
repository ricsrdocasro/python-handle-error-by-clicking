from graphics import *
import traceback
import time
import sys

def clickMouse():
	win = GraphWin("My Window", 500, 500)
	click = 0

	try:
		raise RuntimeError("Program not responding!")
	
	except:
		traceback.print_exc()

		while click < 317: 
			win.getMouse()
			click += 1
			chars = "/—\|" 
			for char in chars:
				sys.stdout.write('\r'+'loading...'+char)
				time.sleep(0.05)
				sys.stdout.flush()

		print("\rIssue Resolved: 317 clicks has corrected that error")
	
clickMouse()

