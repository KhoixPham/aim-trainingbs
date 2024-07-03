# Aim Trainer Game

import pygame as pg
import random

pg.init()

def draw_score():
    global hit_shots, total_shots, miss
    score_text = score_font.render(f'Score: {score}', True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    percentage = (hit_shots / total_shots) * 100
    percentage = round(percentage)
    percentage_text = percentage_font.render(f'Hit: {percentage}' + '%', True, (255, 255, 255))
    screen.blit(percentage_text, (10, 30))

    miss_text = miss_font.render(f'Misses: {miss}', True, (255, 255, 255))
    screen.blit(miss_text, (10, 50))


def detect_hit():
    global hit_target, score, miss, hit_shots, total_shots
    (mouse_x, mouse_y) = pg.mouse.get_pos()
    if hit_target.collidepoint(mouse_x, mouse_y):
        random_width = random.randint(10, 1080)
        random_height = random.randint(10,720)
        hit_target.center = (random_width, random_height)
        score += 100
        hit_shots += 1
        total_shots += 1
    else:
        score -= 300
        miss += 1
        total_shots += 1

screen_width = 1080
screen_height = 720
random_width = random.randint(2,1080)
random_height = random.randint(2,720)

screen = pg.display.set_mode((screen_width,screen_height))
pg.display.set_caption("Aim Training")

clock = pg.time.Clock()

hit_target = pg.Rect(0,0,100,100)
hit_target.center = (random_width, random_height)

score = 0
hit_shots = 1
total_shots = 1
miss = 0

score_font = pg.font.Font(None, 25)
percentage_font = pg.font.Font(None, 25)
miss_font = pg.font.Font(None, 25)
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
        if event.type == pg.MOUSEBUTTONDOWN:
            detect_hit()
    
    screen.fill((0, 0, 0))  # Clear the screen
    draw_score()
    pg.draw.ellipse(screen, 'red', hit_target)
    pg.display.update()
    clock.tick(144)