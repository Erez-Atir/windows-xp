#-----------------------Imports-----------------------
import pygame


#-----------------------Globals-----------------------
screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
#screen = pygame.display.set_mode((1920, 1080))
x = None
y = None
position = None
new = True

#----------------------Functions----------------------
pygame.init()
pygame.mixer.init()


#-------------------------Main-------------------------
def main():
    finish = False
    screen.blit(pygame.transform.scale(pygame.image.load("desktop.jpg"), (1980, 1080)), (0, 0))  # load background
    x = -1000
    y = -1000
    off = (0, 0)
    drag = None
    prev = [(-1000, -1000)]
    while not finish:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    finish = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                if pygame.mouse.get_pressed()[0]:
                    new = True
                    for cx, cy in prev:
                        global new
                        if cx <= position[0] <= cx+250 and cy <= position[1] <= cy+165:
                            if position[1] < cy+40:
                                drag = True
                                off = (position[0] - cx, position[1] - cy)
                            new = False
                    if new:
                        pygame.mixer.music.load("error.mp3")
                        pygame.mixer.music.play(1)
                        x = position[0] - 250/2
                        y = position[1] - 125/2
                        prev.append((x, y))
            if event.type == pygame.MOUSEBUTTONUP:
                drag = False
                prev.append((x, y))
        if drag:
            x, y = tuple([x[0]-x[1] for x in zip(pygame.mouse.get_pos(), off)])
        img = pygame.image.load("error.png")
        img.set_colorkey((251, 247, 252))
        screen.blit(pygame.transform.scale(img, (250, 165)), (x, y))
        pygame.display.flip()


if __name__ == '__main__':
    main()