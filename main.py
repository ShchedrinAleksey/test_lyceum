import os
import sys

import pygame
import requests


FPS = 50
delta = "0.02"

def terminate():
    pygame.quit()
    sys.exit()

def load_image(delta):
    print(delta)
    api_server = "http://static-maps.yandex.ru/1.x/"
    lon = "37.530887"
    lat = "55.703118"


    params = {
        "ll": ",".join([lon, lat]),
        "spn": ",".join([delta, delta]),
        "l": "map"
    }
    response = requests.get(api_server, params=params)


    if not response:
        print("Ошибка выполнения запроса:")
        print(map_request)
        print("Http статус:", response.status_code, "(", response.reason, ")")
        sys.exit(1)

    # Запишем полученное изображение в файл.
    map_file = "map.png"
    with open(map_file, "wb") as file:
        file.write(response.content)

load_image(delta)
map_file = "map.png"
# Инициализируем pygame
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((600, 450))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_PAGEDOWN:
                delta = str(float(delta) * 1.5)
                if float(delta) > 90:
                    delta = '90'
                os.remove(map_file)
                load_image(delta)
            if event.key == pygame.K_PAGEUP:
                delta = str(float(delta) / 1.5)
                if float(delta) < 0.002:
                    delta = '0.002'
                os.remove(map_file)
                load_image(delta)
            # if event.key == pygame.K_LEFT:
            #     player.rect.x -= STEP
            # if event.key == pygame.K_RIGHT:
            #     player.rect.x += STEP
            # if event.key == pygame.K_UP:
            #     player.rect.y -= STEP
            # if event.key == pygame.K_DOWN:
            #     player.rect.y += STEP

    # camera.update(player)
    #
    # for sprite in all_sprites:
    #     camera.apply(sprite)

    screen.fill(pygame.Color(0, 0, 0))
    # tiles_group.draw(screen)
    # player_group.draw(screen)
    # Рисуем картинку, загружаемую из только что созданного файла.
    screen.blit(pygame.image.load(map_file), (0, 0))
    pygame.display.flip()

    clock.tick(FPS)
terminate()
# Удаляем за собой файл с изображением.
os.remove(map_file)