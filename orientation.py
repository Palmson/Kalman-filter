
import pygame

import pandas as pd


def rotate_image(image, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect().center)
    return rotated_image, new_rect

def main():

    pygame.init()


    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 600
    ARROW_IMAGE_PATH = "./public/arrow.png"
    CSV_FILE_PATH = "./public/data1.csv"


    gps_data = pd.read_csv('./public/data1.csv')
    
    bearing_data = gps_data[' Bearing']


    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Arrow Rotation Demo")


    arrow_image = pygame.image.load(ARROW_IMAGE_PATH)
    arrow_rect = arrow_image.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))


    running = True
    index = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        angle = -bearing_data[index]  
        rotated_arrow, rotated_rect = rotate_image(arrow_image, angle)
        rotated_rect.center = arrow_rect.center


        screen.fill((255, 255, 255)) 
        screen.blit(rotated_arrow, rotated_rect)
        pygame.display.flip()

        index = (index + 1) % len(bearing_data)

        pygame.time.delay(10)

    pygame.quit()

if __name__ == "__main__":
    main()
