import pygame

pygame.init()
gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('Hello World!')
clock = pygame.time.clock()

closed = False

while not closed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                closed = True

                print (event)

            pygame.display.update()
            clock.tick(60)

pygame.quit()
quit()