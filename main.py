import pyscreenshot as ImageGrab
import time
from PIL import Image
from pytesseract import image_to_string
from pyautogui import typewrite, click, press, hotkey


blue_rank_coord = [1150, 380, 1400, 700]
red_rank_coord = [1150, 710, 1400, 1025]
screen_coord = [1260, 95, 1465, 120]
chat_coord = [1670, 950]
bet_amount = 500
bet_success_sleep = 300
bet_fail_sleep = 60
bet_status = False
bet_blue = f'!blue {bet_amount}'
bet_red = f'!red {bet_amount}'
red_bet_count = 0
blue_bet_count = 0
screen_image = 'C:\\Users\\Justin\\Desktop\\screen_area.png'
blue_image = 'C:\\Users\\Justin\\Desktop\\blue_rank.png'
red_image = 'C:\\Users\\Justin\\Desktop\\red_rank.png'
website = 'https://gameinfo.saltyteemo.com/'


def compare():

    click(red_rank_coord[0] / 2, red_rank_coord[1], 1)
    time.sleep(1)
    hotkey('ctrl', 't')
    typewrite(website)
    press('enter')
    time.sleep(5)
    press('down')
    blue_rank_area = ImageGrab.grab(bbox=blue_rank_coord)
    blue_rank_area.save(blue_image)
    red_rank_area = ImageGrab.grab(bbox=red_rank_coord)
    red_rank_area.save(red_image)
    blue_ranks = image_to_string(Image.open(blue_image), config='--psm 6')
    red_ranks = image_to_string(Image.open(red_image), config='--psm 6')
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


if __name__ == '__main__':

    while True:

        bet_status = False
        screen_area = ImageGrab.grab(bbox=screen_coord)
        # screen_area.show()
        screen_area.save(screen_image)
        bet_state = image_to_string(Image.open(screen_image), config='--psm 7')
        # print(bet_state)

        if 'open' in bet_state.lower():

            team = compare()
            if team == 0:
                click(chat_coord[0], chat_coord[1], 1)
                typewrite(bet_blue)
                press('enter')
                bet_status = True
                blue_bet_count = blue_bet_count + 1
                print(f'\nbetting blue. blue bet count {blue_bet_count}')
                print(f'red bet count {red_bet_count}\n')
                time.sleep(bet_success_sleep)

            if team == 1:
                click(chat_coord[0], chat_coord[1], 1)
                typewrite(bet_red)
                press('enter')
                bet_status = True
                red_bet_count = red_bet_count + 1
                print(f'\nblue bet count {blue_bet_count}')
                print(f'betting red. red bet count {red_bet_count}\n')
                time.sleep(bet_success_sleep)

        if not bet_status:
            time.sleep(bet_fail_sleep)
