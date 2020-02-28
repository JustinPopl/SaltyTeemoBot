import pyscreenshot as ImageGrab
import time
# from pymouse import PyMouse
import PIL.Image
from pytesseract import image_to_string
from pyautogui import typewrite, click, press, hotkey
from tkinter import *
from pynput.mouse import Listener
import win32gui

# Initialize variables
blue_rank_coord = [1175, 380, 1400, 700]  # Screen coordinates of blue team ranks
red_rank_coord = [1175, 700, 1400, 1025]  # Screen coordinates of red team ranks
screen_coord = [1420, 145, 1485, 185]  # Screen coordinates of bet status
chat_coord = [1670, 960]  # Screen coordinates within chat box
bet_amount = 5000  # Amount to bet
bet_success_sleep = 300  # Time between successful bets
bet_fail_sleep = 60  # Time between failed bets
bet_status = False
bet_blue = f'!blue {bet_amount}'
bet_red = f'!red {bet_amount}'
red_bet_count = 0
blue_bet_count = 0
screen_image = 'C:\\Users\\Justin\\Desktop\\screen_area.png'
blue_image = 'C:\\Users\\Justin\\Desktop\\blue_rank.png'
red_image = 'C:\\Users\\Justin\\Desktop\\red_rank.png'
website = 'https://gameinfo.saltyteemo.com/'


# Compares the ranks between the two teams, scores them, and returns the team with the highest score
# TODO add higher/lower win rates to comparison
def compare():

    set_window()
    time.sleep(1)
    hotkey('ctrl', 't')
    typewrite(website)
    press('enter')
    time.sleep(5)
    press('down')
    press('down')
    blue_rank_area = ImageGrab.grab(bbox=blue_rank_coord)
    blue_rank_area.save(blue_image)
    new_image_blue = blue_rank_area.resize((500, 500))
    new_image_blue.save(blue_image)
    red_rank_area = ImageGrab.grab(bbox=red_rank_coord)
    red_rank_area.save(red_image)
    new_image_red = red_rank_area.resize((500, 500))
    new_image_red.save(red_image)
    blue_ranks = image_to_string(PIL.Image.open(blue_image), config='--psm 6')
    red_ranks = image_to_string(PIL.Image.open(red_image), config='--psm 6')
    blue_total = 0
    red_total = 0
    hotkey('ctrl', 'w')
    time.sleep(1)
    for x in blue_ranks.splitlines():
        if 'f' in x[:9].lower():
            continue
        elif '11' in x[:9].lower() or 'i1' in x.lower():
            blue_total = blue_total + 4
        elif '12' in x[:9].lower() or 'i2' in x.lower():
            blue_total = blue_total + 3
        elif '13' in x[:9].lower() or 'i3' in x.lower():
            blue_total = blue_total + 2
        elif '14' in x[:9].lower() or 'i4' in x.lower():
            blue_total = blue_total + 1
        elif 'b4' in x[:9].lower() or '84' in x.lower():
            blue_total = blue_total + 5
        elif 'b3' in x[:9].lower() or '83' in x.lower():
            blue_total = blue_total + 6
        elif 'b2' in x[:9].lower() or '82' in x.lower():
            blue_total = blue_total + 7
        elif 'b1' in x[:9].lower() or '81' in x.lower():
            blue_total = blue_total + 8
        elif '$4' in x[:9].lower():
            blue_total = blue_total + 9
        elif '$3' in x[:9].lower():
            blue_total = blue_total + 10
        elif '$2' in x[:9].lower():
            blue_total = blue_total + 11
        elif '$1' in x[:9].lower():
            blue_total = blue_total + 12
    print(blue_ranks)
    print(f'blue ranks score {blue_total}')

    for x in red_ranks.splitlines():
        if 'f' in x[:9].lower():
            continue
        elif '11' in x[:9].lower() or 'i1' in x.lower():
            red_total = red_total + 4
        elif '12' in x[:9].lower() or 'i2' in x.lower():
            red_total = red_total + 3
        elif '13' in x[:9].lower() or 'i3' in x.lower():
            red_total = red_total + 2
        elif '14' in x[:9].lower() or 'i4' in x.lower():
            red_total = red_total + 1
        elif 'b4' in x[:9].lower() or '84' in x.lower():
            red_total = red_total + 5
        elif 'b3' in x[:9].lower() or '83' in x.lower():
            red_total = red_total + 6
        elif 'b2' in x[:9].lower() or '82' in x.lower():
            red_total = red_total + 7
        elif 'b1' in x[:9].lower() or '81' in x.lower():
            red_total = red_total + 8
        elif '$4' in x[:9].lower():
            red_total = red_total + 9
        elif '$3' in x[:9].lower():
            red_total = red_total + 10
        elif '$2' in x[:9].lower():
            red_total = red_total + 11
        elif '$1' in x[:9].lower():
            red_total = red_total + 12
    print(red_ranks)
    print(f'red rank score {red_total}')

    if blue_total >= red_total:
        return 0
    else:
        return 1


def on_click(x, y, button, pressed):
    count = 0
    if pressed == 1:
        screen_coord[0] = x
        screen_coord[1] = y
        count = 1
    if pressed == 0:
        screen_coord[2] = x
        screen_coord[3] = y
        print(screen_coord)
        count = 2
    if count == 2:
        return False


def mouse_click():
    with Listener(on_click=on_click) as listener:
        listener.join()


def window_enumeration_handler(hwnd, top_windows):
    top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))


def set_window():
    top_windows = []
    win32gui.EnumWindows(window_enumeration_handler, top_windows)
    for i in top_windows:
        if "twitch" in i[1].lower():
            win32gui.SetForegroundWindow(i[0])


def gui():
    root = Tk()
    frame = Frame(root, width=100, height=100)
    button1 = Button(root, text='Coordinates', fg='red', command=mouse_click)
    button2 = Button(root, text='Ranks', fg='blue', command=compare)
    button3 = Button(root, text='Start', fg='black', command=root.destroy)
    button1.bind('<Button-1>')
    button2.bind('<Button-1>')
    button3.bind('<Button-1>')
    button1.pack(side=LEFT)
    button2.pack(side=RIGHT)
    button3.pack(side=BOTTOM)
    frame.pack()
    root.mainloop()


if __name__ == '__main__':

    gui()

    time.sleep(1)
    while True:

        bet_status = False
        screen_area = ImageGrab.grab(bbox=screen_coord)
        # screen_area.show()
        screen_area.save(screen_image)
        # new_image = screen_area.resize((400, 400))
        # new_image.save(screen_image)
        bet_state = image_to_string(PIL.Image.open(screen_image), config='--psm 7')
        print(bet_state)

        if 'open' in bet_state.lower():

            # Compares the teams and bets on the team with the highest score
            team = compare()
            if team == 0:  # Bet on blue team
                click(chat_coord[0], chat_coord[1], 1)
                typewrite(bet_blue)
                press('enter')
                bet_status = True
                blue_bet_count = blue_bet_count + 1
                print(f'\nbetting blue. blue bet count {blue_bet_count}')
                print(f'red bet count {red_bet_count}\n')
                time.sleep(bet_success_sleep)

            if team == 1:  # Bet on red team
                click(chat_coord[0], chat_coord[1], 1)
                typewrite(bet_red)
                press('enter')
                bet_status = True
                red_bet_count = red_bet_count + 1
                print(f'\nblue bet count {blue_bet_count}')
                print(f'betting red. red bet count {red_bet_count}\n')
                time.sleep(bet_success_sleep)

        if not bet_status:
            time.sleep(bet_fail_sleep)  # Wait before scanning for bet status
