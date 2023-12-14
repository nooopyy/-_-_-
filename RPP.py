import pygame
import random
import sys
import ctypes
import tkinter
from tkinter import PhotoImage
import time 
from tkinter import messagebox
from datetime import datetime, timedelta

# pygame 초기화
pygame.init()
pygame.mixer.pre_init(44100, -16, 2, 1024)
pygame.mixer.init()

# 화면 크기 설정
screen_width, screen_height = 1210, 907
screen = pygame.display.set_mode((screen_width, screen_height))

# 배경 이미지 로드
background_image = pygame.image.load("bgimg.png")
help_image = pygame.image.load("bgimg.png")

# 버튼에 대한 위치와 크기 설정
start_button = pygame.Rect(screen_width / 2.2 - 100, screen_height / 2 - -30, 300, 70)
help_button = pygame.Rect(screen_width / 2.2 - 100, screen_height / 2 - -110, 300, 70)
back_button = pygame.Rect(20, 20, 80, 30)

# 폰트 설정
font = pygame.font.Font("HelpFont.otf", 32)

# 변수
p1 = 0
p2 = 0
coin1 = 0
coin2 = 0
star1 = 0
star2 = 0
click_count1 = 0
click_count2 = 0
current_screen = 0
WIDTH, HEIGHT = 1200, 900
BUTTON_WIDTH, BUTTON_HEIGHT = 100, 80
FPS = 60
stop_flag=False
stop_flag1=False
current_image_index = 0
current_image_index1 = 0 
current_time = datetime.now()
specific_action_time = 0

#보드게임판
start = (112,740)
board1 = (265,725)  #+5코인
board2 = (427,712)
board3 = (587,694)
board4 = (756,671)
board5 = (877,609)  #-3코인
board6 = (746,556)
board7 = (617,523)  #미니게임
board8 = (492,479)  #+5코인
board9 = (360,433)
board10 = (248,380) #+5코인
board11 = (379,310) #+5코인
board12 = (527,265) #-3코인
board13 = (651,193) #미니게임
board14 = (746,131)
board15 = (661,69)  #+5코인

board = [start, board1, board2, board3, board4, board5, board6, board7, board8, board9, board10, board11, board12, board13, board14, board15]

def update_action_time():
    global specific_action_time
    # 현재 시간을 새로운 action_time.txt에 저장
    specific_action_time = datetime.now()
    with open("action_time.txt", "w") as file:
        file.write(str(specific_action_time))

def check_elapsed_time():
    global specific_action_time
    # 파일에서 시간 읽어오기
    try:
        with open("action_time.txt", "r") as file:
            stored_time_str = file.read()
            specific_action_time = datetime.strptime(stored_time_str, "%Y-%m-%d %H:%M:%S.%f")
    except FileNotFoundError:
        # 파일이 없는 경우, 초기 시간을 설정
        specific_action_time = datetime.now()
        with open("action_time.txt", "w") as file:
            file.write(str(specific_action_time))

#스크린 blit
def main_blit():
    global current_screen
    current_screen = 0
    screen.blit(main_screen, (0,0))
    #코인1
    font_coin1 = pygame.font.Font(None, 84)
    text_coin1 = "%d" %coin1
    coin1_render = font_coin1.render(text_coin1, True, (255, 255, 255))
    coin1_rect = coin1_render.get_rect()
    coin1_rect.topleft = (221,96)
    screen.blit(coin1_render, coin1_rect)
    #스타1
    font_star1 = pygame.font.Font(None, 84)
    text_star1 = "%d" %star1
    star1_render = font_star1.render(text_star1, True, (255, 255, 255))
    star1_rect = star1_render.get_rect()
    star1_rect.topleft = (221,25)
    screen.blit(star1_render, star1_rect)
    #코인2
    font_coin2 = pygame.font.Font(None, 84)
    text_coin2 = "%d" %coin2
    coin2_render = font_coin2.render(text_coin2, True, (255, 255, 255))
    coin2_rect = coin2_render.get_rect()
    coin2_rect.topleft = (1116,96)
    screen.blit(coin2_render, coin2_rect)
    #스타2
    font_star2 = pygame.font.Font(None, 84)
    text_star2 = "%d" %star2
    star2_render = font_star2.render(text_star2, True, (255, 255, 255))
    star2_rect = star2_render.get_rect()
    star2_rect.topleft = (1116,25)
    screen.blit(star2_render, star2_rect)

def result_blit():
    global current_screen
    current_screen = 1

    pygame.mixer.music.stop()
    finish_sound.play()

    screen.blit(result_screen, (0,0))
    #코인1
    font_coin1 = pygame.font.Font(None, 84)
    text_coin1 = "%d" %coin1
    coin1_render = font_coin1.render(text_coin1, True, (255, 255, 255))
    coin1_rect = coin1_render.get_rect()
    coin1_rect.topleft = (290,25)
    screen.blit(coin1_render, coin1_rect)
    #스타1
    font_star1 = pygame.font.Font(None, 84)
    text_star1 = "%d" %star1
    star1_render = font_star1.render(text_star1, True, (255, 255, 255))
    star1_rect = star1_render.get_rect()
    star1_rect.topleft = (125,25)
    screen.blit(star1_render, star1_rect)
    #코인2
    font_coin2 = pygame.font.Font(None, 84)
    text_coin2 = "%d" %coin2
    coin2_render = font_coin2.render(text_coin2, True, (255, 255, 255))
    coin2_rect = coin2_render.get_rect()
    coin2_rect.topleft = (1115,25)
    screen.blit(coin2_render, coin2_rect)
    #스타2
    font_star2 = pygame.font.Font(None, 84)
    text_star2 = "%d" %star2
    star2_render = font_star2.render(text_star2, True, (255, 255, 255))
    star2_rect = star2_render.get_rect()
    star2_rect.topleft = (950,25)
    screen.blit(star2_render, star2_rect)

#버튼 움직이게 하는 코드
def mmb(button):
    global WIDTH, HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT, FPS
    delay = 0.9 #버튼 속도
    if pygame.time.get_ticks() - button.last_move_time > delay * 1000:
        x = random.randint(0, WIDTH - BUTTON_WIDTH)
        y = random.randint(0, HEIGHT - BUTTON_HEIGHT)
        button.rect.topleft = (x, y)
        button.last_move_time = pygame.time.get_ticks()

#미니게임
def minigame1_blit():
    global current_screen, WIDTH, HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT, FPS
    current_screen = 2

    WHITE = (255, 255, 255)

    #겜 시작할 때 나오는 노래
    pygame.mixer.music.load("minigame1-1.mp3")
    pygame.mixer.music.play(-1)

    # 폰 트 설정
    mini1font = pygame.font.Font(None, 36)

#버튼 수 세기
def button_clicked(click_count_var,c_b):
    global p1, p2, coin1, coin2, current_time, specific_action_time
    check_elapsed_time()
    current_time = datetime.now()
    
    click_count_var[0] += 1
    minisound1.play() 

    #버튼 5번 클릭하면 게임 종료하고 메세지박스
    if click_count_var[0] == 5:
        click_count_var[0] = 0
        minisound2.play() #성공시 나오는 효과음
        ctypes.windll.user32.MessageBoxW(0, "펭귄을 구했다!", "상대를 물리쳤다!", 1) 
        if p1 == 7:
            coin1 += 10
            main_blit()
            player2_rect.topleft = board[p2]
            screen.blit(player2_image, player2_rect)
            player1_rect.topleft = board[p1]
            screen.blit(player1_image, player1_rect)
            screen.blit(get_coin10_image, get_coin10_rect)
        elif p2 == 7:
            coin2 += 10
            main_blit()
            player1_rect.topleft = board[p1]
            screen.blit(player1_image, player1_rect)
            player2_rect.topleft = board[p2]
            screen.blit(player2_image, player2_rect)
            screen.blit(get_coin10_image, get_coin10_rect)
        pygame.mixer.music.stop()
        pygame.mixer.music.load("board.mp3")
        pygame.mixer.music.play(-1)

    
    elif current_time >= specific_action_time + timedelta(seconds=15):
        click_count_var[0] = 0
        ctypes.windll.user32.MessageBoxW(0, "시간 초과! 실패했습니다.", "실패", 1)
        
                
        if p1 == 7:
            main_blit()
            player2_rect.topleft = board[p2]
            screen.blit(player2_image, player2_rect)
            player1_rect.topleft = board[p1]
            screen.blit(player1_image, player1_rect)
        elif p2 == 7:
            main_blit()                    
            player1_rect.topleft = board[p1]
            screen.blit(player1_image, player1_rect)
            player2_rect.topleft = board[p2]
            screen.blit(player2_image, player2_rect)
        pygame.mixer.music.stop()
        pygame.mixer.music.load("board.mp3")
        pygame.mixer.music.play(-1)

    #3번버튼인 펭귄을 클릭하면 실패
    elif c_b==mbutton3:
        click_count_var[0] = 0
        ctypes.windll.user32.MessageBoxW(0, "내친구를 공격했다 ㅠㅠ!", "실패", 1) 
        if p1 == 7:
            main_blit()
            player2_rect.topleft = board[p2]
            screen.blit(player2_image, player2_rect)
            player1_rect.topleft = board[p1]
            screen.blit(player1_image, player1_rect)
        elif p2 == 7:
            main_blit()
            player1_rect.topleft = board[p1]
            screen.blit(player1_image, player1_rect)
            player2_rect.topleft = board[p2]
            screen.blit(player2_image, player2_rect)

        pygame.mixer.music.stop()
        pygame.mixer.music.load("board.mp3")
        pygame.mixer.music.play(-1)


def draw_button(screen, button, font, text):
    pygame.draw.rect(screen, (255, 255, 255), button)  # 버튼 그리기
    button_text = font.render(text, True, (0, 0, 0))  # 버튼의 텍스트 설정
    text_rect = button_text.get_rect(center=button.center)  # 텍스트의 위치 설정
    screen.blit(button_text, text_rect)  # 텍스트 그리기

def draw_help_screen(): 
    font = pygame.font.Font("HelpFont.otf", 26)
    draw_button(screen, back_button, font, "뒤로가기")  # 뒤로 가기 버튼 그리기
    screen.blit(help_image, (0, 0))

    help_text = ["[게임 도움말]",
                 "① 이 게임은 2명이서 하는 게임입니다.",
                 "② 미니게임을 통해 코인을 획득할 수 있습니다.",
                 "③ 더 많은 별을 차지해 게임에서 승리하세요!"]
    
    for i, line in enumerate(help_text):
        text_surface = font.render(line, True, (255, 255, 255))  # 흰색으로 텍스트 렌더링
        screen.blit(text_surface, (350, 450 + 45 * i))  # 텍스트를 화면에 그리기

#미니게임2
def minigame2_tkinter():
    global p1, p2, coin1, coin2
    root = tkinter.Tk()
    root.title("MiniGame")
    pygame.mixer.music.load("minigame1-1.mp3")
    pygame.mixer.music.play(-1)
    canvas = tkinter.Canvas(width=1000, height=700, bg="white")
    canvas.pack()

    def center_window(window, width, height):
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()

        x_position = (screen_width - width) // 2
        y_position = (screen_height - height) // 2

        window.geometry(f"{width}x{height}+{x_position}+{y_position}")

    window_width = 1000
    window_height = 700
    center_window(root, window_width, window_height)

    background_image = tkinter.PhotoImage(file="backimage2.png")
    canvas.create_image(0, 0, anchor=tkinter.NW, image=background_image)

    image_paths = ["image1.png", "image3.png", "image5.png", "image7.png", "image9.png",
                "image11.png", "image13.png", "image15.png", "image17.png", "image19.png",
                "image21.png", "image23.png", "image25.png", "image27.png", "image29.png",
                "image31.png", "image33.png", "image35.png", "image37.png", "image39.png",
                "image41.png", "image43.png", "image45.png", "image47.png", "image49.png", "image0.png"]

    current_image_index = 0
    stop_flag = False

    # 이미지를 표시할 레이블 생성
    image_label = tkinter.Label(root)
    image_label.place(x=650, y=100)

    def show_next_image(event):
        global current_image_index, current_image_index1,stop_flag, p1, p2, coin1, coin2

        if not stop_flag:
            current_image_index = (current_image_index + 1) % len(image_paths)
            current_image_path = image_paths[current_image_index]

            image = PhotoImage(file=current_image_path)

            # 이미지 레이블을 갱신
            image_label.configure(image=image)
            image_label.image = image

            if current_image_path == "image0.png":
                current_image_index = 0
                current_image_index1 = 0
                messagebox.showinfo("게임 결과", "player1이 이겼습니다!")
                root.destroy()
                coin1 += 10
                main_blit()
                player2_rect.topleft = board[p2]
                screen.blit(player2_image, player2_rect)
                player1_rect.topleft = board[p1]
                screen.blit(player1_image, player1_rect)
                screen.blit(get_coin10_image, get_coin10_rect)
                pygame.mixer.music.stop()
                pygame.mixer.music.load("board.mp3")
                pygame.mixer.music.play(-1)
    
    root.bind('<Return>', show_next_image)

    initial_image_path = image_paths[current_image_index]
    initial_image = PhotoImage(file=initial_image_path)

    # 초기 이미지 레이블 생성
    image_label.configure(image=initial_image)
    image_label.image = initial_image

    image_paths1 = ["image 101.png", "image 103.png", "image 105.png", "image 107.png", "image 109.png",
                    "image 111.png", "image 113.png", "image 115.png", "image 117.png", "image 119.png",
                    "image 121.png", "image 123.png", "image 125.png", "image 127.png", "image 129.png",
                    "image 131.png", "image 133.png", "image 135.png", "image 137.png", "image 139.png",
                    "image 141.png", "image 143.png", "image 145.png", "image 147.png", "image 149.png", "image 000.png"]

    current_image_index1 = 0
    stop_flag1 = False

    # 이미지를 표시할 레이블 생성
    image_label1 = tkinter.Label(root)
    image_label1.place(x=650, y=400)

    def show_next_image1(event):
        global current_image_index, current_image_index1,stop_flag1, p1, p2, coin1, coin2

        if not stop_flag1:
            current_image_index1 = (current_image_index1 + 1) % len(image_paths1)
            current_image_path1 = image_paths1[current_image_index1]

            image1 = PhotoImage(file=current_image_path1)

            # 이미지 레이블을 갱신
            image_label1.configure(image=image1)
            image_label1.image1 = image1

            if current_image_path1 == "image 000.png":
                current_image_index = 0
                current_image_index1 = 0
                messagebox.showinfo("게임 결과", "player2가 이겼습니다!")
                root.destroy()
                coin2 += 10
                main_blit()
                player1_rect.topleft = board[p1]
                screen.blit(player1_image, player1_rect)
                player2_rect.topleft = board[p2]
                screen.blit(player2_image, player2_rect)
                screen.blit(get_coin10_image, get_coin10_rect)
                pygame.mixer.music.stop()
                pygame.mixer.music.load("board.mp3")
                pygame.mixer.music.play(-1)

    root.bind('<space>', show_next_image1)

    initial_image_path1 = image_paths1[current_image_index1]
    initial_image1 = PhotoImage(file=initial_image_path1)

    # 초기 이미지 레이블 생성
    image_label1.configure(image=initial_image1)
    image_label1.image1 = initial_image1

    label = tkinter.Label(root, text="풍선터뜨리기 게임", font=("Helvetica", 20), bg="grey")
    label.place(x=5, y=5)
    label = tkinter.Label(root, text="player1", font=("Helvetica", 20), bg="white")
    label.place(x=5, y=280)
    label = tkinter.Label(root, text="player2", font=("Helvetica", 20), bg="white")
    label.place(x=5, y=525)

    img_2 = tkinter.PhotoImage(file="player1.png")
    canvas.create_image(100, 200, image=img_2, tag="MYCHR_copy")

    img_1 = tkinter.PhotoImage(file="player2.png")
    canvas.create_image(100, 450, image=img_1, tag="MYCHR")

    mario_image = PhotoImage(file="ricepopparty.png")
    canvas.create_image(400, 5, anchor=tkinter.NW, image=mario_image)

    root.mainloop()


#플레이어1 위치
def roll1():
    global p1, p2, coin1, star1, coin2, star2, click_count1, current_time
    click_count1 += 1
    if click_count1 <= 15:
        r1 = random.randint(1,6)
        p1 = p1 + r1
        if p1 == 1 or p1 == 8 or p1 == 10 or p1 == 11 or p1 == 15:
            coin1 += 5
            get_coin_sound.play()
            main_blit()
            player2_rect.topleft = board[p2]
            screen.blit(player2_image, player2_rect)
            player1_rect.topleft = board[p1]
            screen.blit(player1_image, player1_rect)
            if click_count1 <= 14:
                screen.blit(get_coin5_image, get_coin5_rect)
        elif p1 == 5 or p1 == 12:
            lose_coin_sound.play()
            coin1 -= 3
            if coin1 < 0:
                coin1 = 0
            main_blit()
            player2_rect.topleft = board[p2]
            screen.blit(player2_image, player2_rect)
            player1_rect.topleft = board[p1]
            screen.blit(player1_image, player1_rect)
            if click_count1 <= 14:
                screen.blit(lose_coin3_image, lose_coin3_rect)
        elif p1 == 7:
            minigame1_blit()
            update_action_time()
        elif p1 == 13:
            minigame2_tkinter()
        elif p1 >= 16:
            get_star_sound.play()
            p1 = 0
            star1 += 1
            main_blit()
            player2_rect.topleft = board[p2]
            screen.blit(player2_image, player2_rect)
            player1_rect.topleft = board[p1]
            screen.blit(player1_image, player1_rect)
            if click_count1 <= 14:
                screen.blit(get_star_image, get_star_rect)
        else:
            coin1 += 1
            main_blit()
            player2_rect.topleft = board[p2]
            screen.blit(player2_image, player2_rect)
            player1_rect.topleft = board[p1]
            screen.blit(player1_image, player1_rect)

#플레이어2 위치
def roll2():
    global p1, p2, coin1, star2, coin2, star2, click_count2, current_time
    click_count2 += 1
    if click_count2 <= 15:
        r2 = random.randint(1,6)
        p2 = p2 + r2
        if p2 == 1 or p2 == 8 or p2 == 10 or p2 == 11 or p2 == 15:
            get_coin_sound.play()
            coin2 += 5
            main_blit()
            player1_rect.topleft = board[p1]
            screen.blit(player1_image, player1_rect)
            player2_rect.topleft = board[p2]
            screen.blit(player2_image, player2_rect)
            if click_count2 <= 11 or click_count2 == 13:
                screen.blit(get_coin5_image, get_coin5_rect)
        elif p2 == 5 or p2 == 12:
            lose_coin_sound.play()
            coin2 -= 3
            if coin2 < 0:
                coin2 = 0
            main_blit()
            player1_rect.topleft = board[p1]
            screen.blit(player1_image, player1_rect)
            player2_rect.topleft = board[p2]
            screen.blit(player2_image, player2_rect)
            if click_count2 <= 11 or click_count2 == 13:
                screen.blit(lose_coin3_image, lose_coin3_rect)
        elif p2 == 7:
            minigame1_blit()
            update_action_time()
        elif p2 == 13:
            minigame2_tkinter()        
        elif p2 >= 16:
            get_star_sound.play()
            p2 = 0
            star2 += 1
            main_blit()
            player1_rect.topleft = board[p1]
            screen.blit(player1_image, player1_rect)
            player2_rect.topleft = board[p2]
            screen.blit(player2_image, player2_rect)
            if click_count2 <= 11 or click_count2 == 13:
                screen.blit(get_star_image, get_star_rect)
        else:
            coin2 += 1
            main_blit()
            player1_rect.topleft = board[p1]
            screen.blit(player1_image, player1_rect)
            player2_rect.topleft = board[p2]
            screen.blit(player2_image, player2_rect)


        if click_count2 == 12:
            font_turn3 = pygame.font.Font(None, 84)
            text_turn3 = "3 TURNS LEFT!"
            turn3_render = font_turn3.render(text_turn3, True, (0, 0, 0))
            turn3_rect = turn3_render.get_rect()
            turn3_rect.center = (600,450)
            screen.blit(turn3_render, turn3_rect)
        elif click_count2 == 14:
            font_turnl = pygame.font.Font(None, 84)
            text_turnl = "LAST TURN!"
            turnl_render = font_turnl.render(text_turnl, True, (0, 0, 0))
            turnl_rect = turnl_render.get_rect()
            turnl_rect.center = (600,450)
            screen.blit(turnl_render, turnl_rect)
        elif click_count2 >= 15:
            finish_image = pygame.image.load("finish.png")
            finish_rect = finish_image.get_rect()
            finish_rect.topleft = (412, 400)
            screen.blit(finish_image, finish_rect)

#교환1
def exchange1():
    global p1, p2, coin1, star1, coin2, star2, click_count2
    if coin1 >= 10:
        coin1 -= 10
        star1 += 1
    main_blit()
    player2_rect.topleft = board[p2]
    screen.blit(player2_image, player2_rect)
    player1_rect.topleft = board[p1]
    screen.blit(player1_image, player1_rect)
    if click_count2 >= 15:
        finish_image = pygame.image.load("finish.png")
        finish_rect = finish_image.get_rect()
        finish_rect.topleft = (412, 400)
        screen.blit(finish_image, finish_rect)

#교환2
def exchange2():
    global p1, p2, coin1, star1, coin2, star2, click_count2
    if coin2 >= 10:
        coin2 -= 10
        star2 += 1
    main_blit()
    player1_rect.topleft = board[p1]
    screen.blit(player1_image, player1_rect)
    player2_rect.topleft = board[p2]
    screen.blit(player2_image, player2_rect)
    if click_count2 >= 15:
        finish_image = pygame.image.load("finish.png")
        finish_rect = finish_image.get_rect()
        finish_rect.topleft = (412, 400)
        screen.blit(finish_image, finish_rect)

#끝
def finish():
    global coin1, coin2, star1, star2
    result_blit()
    if star1 > star2:
        result1_image = pygame.image.load("result1.png")
        result1_rect = result1_image.get_rect()
        result1_rect.topleft = (463, 220)
        screen.blit(result1_image, result1_rect)
    elif star1 < star2:
        result2_image = pygame.image.load("result2.png")
        result2_rect = player2_image.get_rect()
        result2_rect.topleft = (463, 220)
        screen.blit(result2_image, result2_rect)       
    elif star1 == star2:
        if coin1 > coin2:
            result1_image = pygame.image.load("result1.png")
            result1_rect = result1_image.get_rect()
            result1_rect.topleft = (463, 220)
            screen.blit(result1_image, result1_rect)
        elif coin1 < coin2:
            result2_image = pygame.image.load("result2.png")
            result2_rect = player2_image.get_rect()
            result2_rect.topleft = (463, 220)
            screen.blit(result2_image, result2_rect)
        elif coin1 == coin2:
            draw_image = pygame.image.load("draw.png")
            draw_rect = draw_image.get_rect()
            draw_rect.topleft = (326, 220)
            screen.blit(draw_image, draw_rect)


#창 크기 설정
screen_width = 1200
screen_hight = 900

#창 설정
screen = pygame.display.set_mode((screen_width, screen_hight))
pygame.display.set_caption("Rice Pop Party")

#메인 스크린
main_screen = pygame.image.load("board.png")
pygame.mixer.music.load("board.mp3")
pygame.mixer.music.play(-1)
main_blit()

#결과 스크린
result_screen = pygame.image.load("result.png")

#플레이어2
player2_image = pygame.image.load("player2.png")
player2_rect = player2_image.get_rect()
player2_rect.topleft = board[p2]
screen.blit(player2_image, player2_rect)

#플레이어1
player1_image = pygame.image.load("player1.png")
player1_rect = player1_image.get_rect()
player1_rect.topleft = board[p1]
screen.blit(player1_image, player1_rect)

#코인2
font_coin2 = pygame.font.Font(None, 84)
text_coin2 = "%d" %coin2
coin2_render = font_coin2.render(text_coin2, True, (255, 255, 255))
coin2_rect = coin2_render.get_rect()
coin2_rect.topleft = (1116,96)
screen.blit(coin2_render, coin2_rect)

#스타2
font_star2 = pygame.font.Font(None, 84)
text_star2 = "%d" %star2
star2_render = font_star2.render(text_star2, True, (255, 255, 255))
star2_rect = star2_render.get_rect()
star2_rect.topleft = (1116,25)
screen.blit(star2_render, star2_rect)

#코인 +5
get_coin5_image = pygame.image.load("get_coin5.png")
get_coin5_rect = get_coin5_image.get_rect()
get_coin5_rect.center = [600,450]
screen.blit(get_coin5_image, get_coin5_rect)

#코인 +10
get_coin10_image = pygame.image.load("get_coin10.png")
get_coin10_rect = get_coin10_image.get_rect()
get_coin10_rect.center = [600,450]
screen.blit(get_coin10_image, get_coin10_rect)

#코인 -3
lose_coin3_image = pygame.image.load("lose_coin3.png")
lose_coin3_rect = lose_coin3_image.get_rect()
lose_coin3_rect.center = [600,450]
screen.blit(lose_coin3_image, lose_coin3_rect)

#스타 +1
get_star_image = pygame.image.load("get_star.png")
get_star_rect = get_star_image.get_rect()
get_star_rect.center = [600,450]
screen.blit(get_star_image, get_star_rect)

#시계
mini1clock = pygame.time.Clock()

# 여러 이미지 넣기
background1 = pygame.image.load("miniimg1-5.png")
mini1bti1 = pygame.image.load("miniimg1-1.png")
mini1bti1 = pygame.transform.scale(mini1bti1, (300, 300))
mini1bti2 = pygame.image.load("miniimg1-2.png")
mini1bti2 = pygame.transform.scale(mini1bti2, (550, 500))
mini1bti3 = pygame.image.load("miniimg1-10.png")
mini1bti3 = pygame.transform.scale(mini1bti3, (300, 300))

mini1_image1 = pygame.image.load("miniimg1-6.png")
mini1_image1=pygame.transform.scale(mini1_image1,(150,150))

mini1_image2 = pygame.image.load("miniimg1-7.png")
mini1_image2=pygame.transform.scale(mini1_image2,(400,400))


# 소리 두개 처음꺼는 깨면 나오는거 아래는 버튼 클릭시 나오는거
minisound2 = pygame.mixer.Sound("minigame1-3.mp3")
minisound1 = pygame.mixer.Sound("minigame1-2.mp3")
board_sound = pygame.mixer.Sound("board.mp3")
get_coin_sound = pygame.mixer.Sound("get_coin.mp3")
get_star_sound = pygame.mixer.Sound("get_star.mp3")
lose_coin_sound = pygame.mixer.Sound("lose_coin.mp3")
finish_sound = pygame.mixer.Sound("finish.mp3")




# 버튼 만들기
mbutton1 = pygame.sprite.Sprite()
mbutton1.image = mini1bti1
mbutton1.rect = mbutton1.image.get_rect()
mbutton1.last_move_time = 0

mbutton2 = pygame.sprite.Sprite()
mbutton2.image = mini1bti2
mbutton2.rect = mbutton2.image.get_rect()
mbutton2.last_move_time = 0

mbutton3 = pygame.sprite.Sprite()
mbutton3.image = mini1bti3
mbutton3.rect = mbutton3.image.get_rect()
mbutton3.last_move_time = 0


# Set initial positions
mbutton1.rect.topleft = (0, 0)
mbutton2.rect.topleft = (0, 0)
mbutton3.rect.topleft = (0, 0)

c_c_buttons = [0]
pygame.time.get_ticks()

# 게임 화면 그리기
def draw_game_screen():
    screen.blit(main_screen, (0, 0))
    draw_button(screen, back_button, font, "뒤로가기")  # 뒤로 가기 버튼 그리기

# 메인 함수
def main():
    global p1, p2, coin1, coin2, current_time, specific_action_time
    game_state = 'menu'
    prev_game_state = None
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                #보드게임 스크린
                if current_screen == 0:
                    if 30 <= x <= 110 and 163 <= y <= 243:
                        roll1()
                    elif 922 <= x <= 1002 and 163 <= y <= 243:
                        roll2()
                    elif 131 <= x <= 221 and 163 <= y <= 243:
                        exchange1()
                    elif 1026 <= x <= 1126 and 163 <= y <= 243:
                        exchange2()
                    if click_count2 >= 15:
                        if 412 <= x <= 786 and 400 <= y <= 528:
                            finish()
                    elif back_button.collidepoint(x, y):  # 뒤로가기 버튼을 클릭하면 'menu' 상태로 돌아갑니다.
                        game_state = 'menu'
                #결과 스크린
                elif current_screen == 1:
                    None
                #미니게임1 스크린
                elif current_screen == 2:
                    if mbutton1.rect.collidepoint(event.pos):button_clicked(c_c_buttons, mbutton1)
                    elif mbutton2.rect.collidepoint(event.pos):button_clicked(c_c_buttons, mbutton2)
                    elif mbutton3.rect.collidepoint(event.pos):button_clicked(c_c_buttons, mbutton3)
                
                if game_state == 'menu':  # 'menu' 상태에서는 메뉴 버튼을 클릭할 수 있게 합니다.
                    if start_button.collidepoint(x, y):
                        game_state = 'game'
                    elif help_button.collidepoint(x, y):
                        game_state = 'help'
                elif game_state == 'help':  # 'help' 상태에서는 돌아가기 버튼을 클릭할 수 있게 합니다.
                    if back_button.collidepoint(x, y):
                        game_state = 'menu'

        # game_state가 변경되었을 때만 배경을 다시 그립니다.
        if game_state != prev_game_state:
            screen.blit(background_image, (0, 0))  # 배경 이미지를 먼저 그려 화면을 초기화합니다.
            if game_state == 'menu':
                draw_button(screen, start_button, font, "게임시작")
                draw_button(screen, help_button, font, "게임 도움말")
            elif game_state == 'game':
                draw_game_screen()
                draw_button(screen, back_button, font, "뒤로가기")
            elif game_state == 'help':
                draw_help_screen()
                draw_button(screen, back_button, font, "뒤로가기")
            prev_game_state = game_state

        if current_screen == 2:
            # 버튼 움직이기
            mmb(mbutton1)
            mmb(mbutton2)
            mmb(mbutton3)

            # 배경 위치
            screen.blit(background1, (-10,-130))
            # 그림들 위치
            screen.blit(mbutton1.image, mbutton1.rect.topleft) #두개는 버튼
            screen.blit(mbutton2.image, mbutton2.rect.topleft)
            screen.blit(mbutton3.image, mbutton3.rect.topleft)
            screen.blit(mini1_image1, (1050, 740)) #펭귄
            screen.blit(mini1_image2,(900,400)) #말풍선

        else:
            None

        mini1clock.tick(FPS)
        pygame.display.update()

    pygame.mixer.music.stop()
    pygame.quit()

if __name__ == "__main__":
    main()