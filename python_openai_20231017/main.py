# import turtle
# import random
#
# def draw_heart():
#     window = turtle.Screen()
#     window.bgcolor("white")
#     love = turtle.Turtle()
#     love.shape("turtle")
#     love.speed(2)  # 设置画笔速度
#
#     def set_color():
#         R = random.random()
#         G = random.random()
#         B = random.random()
#         love.color(R, G, B)
#
#     love.width(3)
#     love.fillcolor("red")
#     love.begin_fill()
#     love.left(140)
#     love.forward(180)
#     love.circle(-90, 200)
#
#     set_color()
#     love.left(120)
#     love.circle(-90, 200)
#
#     set_color()
#     love.forward(180)
#     love.end_fill()
#
#     love.up()
#     love.goto(0, -180)  # 移动画笔位置
#     love.down()
#     love.hideturtle()
#
#     window.mainloop()
#
# draw_heart()


'''

import pygame
import math

# 初始化pygame
pygame.init()

# 设置窗口大小和标题
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("3D Heart Surprise with Rotation and Name")

# 定义颜色
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

angle = 0  # 初始化旋转角度

# 加载字体
font = pygame.font.SysFont(None, 50)

# 主函数
def main():
    global angle
    clock = pygame.time.Clock()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        win.fill(WHITE)
        draw_heart(angle)
        draw_name()
        angle += 0.02  # 更新旋转角度
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

# 绘制3D爱心
def draw_heart(angle):
    for theta in range(0, 360, 2):  # 旋转角度
        for phi in range(0, 360, 2):  # 旋转角度
            theta_rad = math.radians(theta)
            phi_rad = math.radians(phi)

            # 3D爱心方程
            x = 16 * math.sin(theta_rad)**3
            y = 13 * math.cos(theta_rad) - 5 * math.cos(2*theta_rad) - 2 * math.cos(3*theta_rad) - math.cos(4*theta_rad)
            z = phi / 10  # 为了给爱心增加深度效果

            # 旋转矩阵
            x_rot = x * math.cos(angle) - y * math.sin(angle)
            y_rot = x * math.sin(angle) + y * math.cos(angle)

            # 3D到2D的投影
            scale_factor = 400 / (4 + z)
            x_proj = int(x_rot * scale_factor + WIDTH / 2)
            y_proj = int(-y_rot * scale_factor + HEIGHT / 2)

            pygame.draw.circle(win, RED, (x_proj, y_proj), 2)

# 绘制名字
def draw_name():
    text = font.render("YWL", True, BLACK)
    win.blit(text, (WIDTH - 100, HEIGHT - 100))

main()

'''

"""

import pygame
import random

# 初始化pygame
pygame.init()

# 设置窗口大小和标题
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Click the Stars for YWL")

# 定义颜色
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)

# 加载字体
font = pygame.font.SysFont(None, 50)

stars = [(random.randint(0, WIDTH), random.randint(0, HEIGHT)) for _ in range(10)]

def main():
    clicked_stars = []
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                for star in stars:
                    if star not in clicked_stars and abs(star[0] - x) < 10 and abs(star[1] - y) < 10:
                        clicked_stars.append(star)
                        break

        win.fill(WHITE)
        draw_stars(clicked_stars)
        if len(clicked_stars) == len(stars):
            draw_message()
        pygame.display.flip()

    pygame.quit()

def draw_stars(clicked_stars):
    for star in stars:
        if star in clicked_stars:
            pygame.draw.circle(win, BLACK, star, 5)
        else:
            pygame.draw.circle(win, YELLOW, star, 5)

def draw_message():
    text = font.render("YWL, I want you!", True, BLACK)
    win.blit(text, (WIDTH // 4, HEIGHT // 2))

main()

"""


"""

import tkinter as tk
from tkinter import Entry, Label, Button, StringVar
import random

class MagicCrystalBall:
    def __init__(self, root):
        self.root = root
        self.root.title("魔法水晶球")

        self.question_label = Label(root, text="请输入你的问题：")
        self.question_label.pack(pady=20)

        self.entry = Entry(root, width=50)
        self.entry.pack(pady=20)

        self.shake_button = Button(root, text="摇晃水晶球", command=self.shake_ball)
        self.shake_button.pack(pady=20)

        self.answer_var = StringVar()
        self.answer_label = Label(root, textvariable=self.answer_var, font=("Arial", 16))
        self.answer_label.pack(pady=20)

    def shake_ball(self):
        answers = [
            "当然是的！",
            "我不确定。",
            "可能吧。",
            "不太可能。",
            "不，绝对不是。",
            "再问我一次。",
            "集中精力再问。",
            "不要依赖它。",
            "是的，但要小心。",
            "听从内心的声音。",
            "现在不清楚。",
            "我认为是的。"
        ]
        self.answer_var.set(random.choice(answers))

if __name__ == "__main__":
    root = tk.Tk()
    app = MagicCrystalBall(root)
    root.mainloop()

"""

import pygame
import random
import math

# 初始化pygame
pygame.init()

# 设置窗口大小和标题
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Meteor")

# 定义颜色
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# 加载字体
font = pygame.font.SysFont(None, 50)

class Meteor:
    def __init__(self):
        self.x = random.randint(0, WIDTH)
        self.y = 0 - random.randint(20, 30)
        self.speed = random.randint(5, 10)
        self.size = random.randint(10, 30)

    def move(self):
        self.y += self.speed

    def draw(self):
        pygame.draw.circle(win, RED, (self.x, self.y), self.size)

    def is_off_screen(self):
        return self.y > HEIGHT + self.size

    def is_clicked(self, x, y):
        return self.x - self.size < x < self.x + self.size and self.y - self.size < y < self.y + self.size

def draw_heart():
    for theta in range(0, 360, 1):
        t = math.radians(theta)
        x = 16 * math.sin(t)**3
        y = 13 * math.cos(t) - 5 * math.cos(2*t) - 2 * math.cos(3*t) - math.cos(4*t)
        pygame.draw.circle(win, RED, (int(WIDTH/2 + x*20), int(HEIGHT/2 - y*20)), 3)

def main():
    meteors = []
    score = 0
    missed = 0
    clock = pygame.time.Clock()
    run = True
    victory = False
    while run:
        win.fill(WHITE)

        if not victory:
            if random.random() < 0.02:  # 2%的概率生成新的流星
                meteors.append(Meteor())

            for meteor in meteors:
                meteor.move()
                meteor.draw()
                if meteor.is_off_screen():
                    meteors.remove(meteor)
                    missed += 1

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    for meteor in meteors:
                        if meteor.is_clicked(x, y):
                            meteors.remove(meteor)
                            score += 1

            score_text = font.render(f"Scores: {score} / 5", True, BLACK)
            win.blit(score_text, (10, 10))

            if score >= 5:  # 当玩家得分达到10时，显示胜利画面
                victory = True

        else:
            draw_heart()
            love_text = font.render("YWL, I want you", True, BLACK)
            win.blit(love_text, (WIDTH // 4, HEIGHT // 2 + 50))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

main()


