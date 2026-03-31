import random
import os
import time
import sys
import json

def enter(): #엔터키 입력받았을 때 clear
    while True:
        print("\n계속하려면 엔터를 눌러주세요...")
        enter = input("")
        if enter == "":
            os.system('cls' if os.name == 'nt' else 'clear')
            break

def input_int(minn, maxx, custom_input, custom_error):
    while True:
        try:
            select = int(input(custom_input))
            if minn <= select <= maxx:
                break
            else:
                print(custom_error)
        except:
            print(custom_error)
    return select

def input_str(custom_input, custom_error, input_list):
    while True:
        try:
            select = input(custom_input)
            if select in input_list:
                break
            else:
                print(custom_error)
        except:
            print(custom_error)
    return select

def input_all(minn, maxx, custom_input, custom_error, input_list):
    input_list = list(input_list)
    while True:
        try:
            select = input(custom_input)
            if select in input_list:
                break
            try:
                select = int(select)
            except:
                select = float(select)
            if minn <= select <= maxx:
                break
            else:
                print(custom_error)
        except:
            print(custom_error)
    return select

def chance(percent: float) -> bool:
    """percent 확률(%)로 True를 반환하는 함수"""
    return random.random() < (percent / 100)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')










def print_scissors():
    print("┌────────────────────┐")
    print("│               ▩▩   │")
    print("│       ▩▩    ▩▩▩▩▩  │")
    print("│     ▩▩▩▩▩  ▩▩▩▩▩▩▩ │")
    print("│   ▩▩▩▩▩▩▩▩▩▩▩▩▩▩   │")
    print("│  ▩▩▩▩▩▩▩▩▩▩▩▩      │")
    print("│  ▩▩▩▩▩▩▩▩▩         │")
    print("│  ▩▩▩▩▩▩▩▩▩▩▩       │")
    print("│  ▩▩▩▩▩▩▩▩▩▩▩▩▩     │")
    print("│  ▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩   │")
    print("│   ▩▩▩▩▩▩▩ ▩▩▩▩▩▩▩  │")
    print("│    ▩▩▩▩▩▩   ▩▩▩▩▩  │")
    print("│      ▩▩▩      ▩▩   │")
    print("└────────────────────┘")

def print_rock():
    print("┌────────────────────┐")
    print("│                    │")
    print("│     ▩▩▩▩▩          │")
    print("│    ▩▩▩▩▩▩▩▩▩       │")
    print("│   ▩▩▩▩▩▩▩▩▩▩▩      │")
    print("│  ▩▩▩▩▩▩▩▩▩▩▩▩      │")
    print("│  ▩▩▩▩▩▩▩▩▩▩▩▩▩     │")
    print("│  ▩▩▩▩▩▩▩▩▩▩▩▩▩     │")
    print("│  ▩▩▩▩▩▩▩▩▩▩▩▩▩     │")
    print("│  ▩▩▩▩▩▩▩▩▩▩▩▩      │")
    print("│   ▩▩▩▩▩▩▩▩▩▩       │")
    print("│    ▩▩▩▩▩▩▩         │")
    print("│                    │")
    print("└────────────────────┘")
    
def print_paper():
    print("┌───────────────────┐")
    print("│                   │")
    print("│     ▩▩▩▩▩         │")
    print("│    ▩▩▩            │")
    print("│   ▩▩▩▩▩▩▩▩▩▩▩▩▩   │")
    print("│  ▩▩▩▩▩▩▩▩▩        │")
    print("│  ▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩  │")
    print("│  ▩▩▩▩▩▩▩▩▩        │")
    print("│  ▩▩▩▩▩▩▩▩▩▩▩▩▩▩   │")
    print("│  ▩▩▩▩▩▩▩▩▩        │")
    print("│   ▩▩▩▩▩▩▩▩▩▩▩     │")
    print("│    ▩▩▩▩▩          │")
    print("│                   │")
    print("└───────────────────┘")

def shut_down():
    time.sleep(1)
    clear()
    print('게임을 종료합니다.')
    time.sleep(0.5)
    print()
    print()
    time.sleep(0.5)
    print("게임을 종료 중...", end='', flush=True)  # flush 추가
    for _ in range(random.randint(5, 10)):
        print(".", end='', flush=True)
        time.sleep(1)
    print()
    os.system('cls' if os.name == 'nt' else 'clear')
    sys.exit()
