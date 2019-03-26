from tkinter import *
from tkinter import messagebox

answers = list(range(1,10))  # Возможные ходы
counter = 0  # Для определения кто ходит (0 или х)
start = True
master = Tk()
master.title("Крестики-нолики")
master.geometry("300x300")
c = Canvas(master, width=600, height=600)
c.pack()
Label(master, text="Press Enter to restart").place(x=100,y=10)
# Чертим поле для игры:
c.create_line(50,120,250,120,fill = "black")
c.create_line(50,180,250,180,fill = "black")
c.create_line(120,50,120,250,fill = "black")
c.create_line(180,50,180,250,fill = "black")


def draw_xo(posx, posy, pos):
	'''Рисует 0 или х
	pos - позиция хода
	'''
	global counter
	if pos not in answers:  # Проверяем свободна ли ячейка для хода
		messagebox.showerror(f'Ячека {pos} уже заня')  # Если нет ты выводим сообщение
	else: # Если свободна, рисуем Х или 0, взависимости от хода
		if counter%2 == 0: # Рисует круг в координатах posx, posy
			answers.insert(answers.index(pos), 'O')
			c.create_oval(posx-20, posy-20, posx+20, posy+20)
		else: # Рисует крест в координатах posx, posy
			answers.insert(answers.index(pos), 'X')
			c.create_line(posx-20, posy-20, posx+20, posy+20)
			c.create_line(posx-20, posy+20, posx+20, posy-20)
		counter += 1
		answers.remove(pos)

def check_win(answers):
	'''Определяет не победил ли какая нибудь комбинация'''
	win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
	# проходится по списку с победными комбинациями, сравнвая с ходами игроков
	for each in win_coord:
		if answers[each[0]] == answers[each[1]] == answers[each[2]]:
			return answers[each[0]]
	return False

def restart_game(event): # Перезапускает игру по нажатию Enter
	'''Очищает поле и список, а затем рисует все заново'''
	global start, counter, answers
	start = True
	counter = 0
	c.delete('all')
	Label(master, text="Press Enter to restart").place(x=100,y=10)
	c.create_line(50,120,250,120,fill = "black")
	c.create_line(50,180,250,180,fill = "black")
	c.create_line(120,50,120,250,fill = "black")
	c.create_line(180,50,180,250,fill = "black")
	answers.clear()
	answers = list(range(1,10))


def play(event):
	'''Рисует фигуры на поле, в зависимости от того куда тыкнет игрок'''
	global start
	global counter
	x = event.x
	y = event.y
	pos = 0
	posx = 0
	posy = 0

	if 50<x<120 and 50<y<120:
		pos=1
		posx=75
		posy=75
	elif 120<x<180 and 50<y<120:
		pos=2
		posx=145
		posy=75
	elif 180<x<250 and 50<y<120:
		pos=3
		posx=205
		posy=75
	elif 50<x<120 and 120<y<180:
		pos=4
		posx=75
		posy=145
	elif 120<x<180 and 120<y<180:
		pos=5
		posx=145
		posy=145
	elif 180<x<250 and 120<y<180:
		pos=6
		posx=205
		posy=145
	elif 50<x<120 and 180<y<250:
		pos=7
		posx=75
		posy=205
	elif 120<x<180 and 180<y<250:
		pos=8
		posx=145
		posy=205
	elif 180<x<250 and 180<y<250:
		pos=9
		posx=205
		posy=205	

	if start == True:
		draw_xo(posx, posy, pos)

	if counter > 4:
		tmp = check_win(answers)
		if tmp:
			messagebox.showinfo(f'The end {tmp} win!')
			start = False
		elif counter == 9:
			messagebox.showinfo('The end, draw')
			start = False

def main():
	c.bind_all("<Button-1>", play)
	c.bind_all("<Return>", restart_game)
	master.mainloop()

if __name__ == '__main__':
	main()

