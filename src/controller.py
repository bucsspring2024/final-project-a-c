import pygame
from src.game import Character
from src.game import Tower
from src.game import Witch
from src.game import Apple

class Controller:
    def __init__(self):
        pygame.init()
        # Initialize other resources and objects needed for your game

    def mainloop(self):
        screen = pygame.display.set_mode((800, 600))
        clock = pygame.time.Clock()

        prince = Character(100, 400, .25, 'assets/prince.png')
        tower = Tower(300, 200, 'assets/tower.png')
        witch = Witch(350, 150, 'assets/witch.png')
        apple = Apple(350, 180, 'assets/apple.png')
        charactergroup= pygame.sprite.Group(prince)
        witchgroup= pygame.sprite.Group(witch)
        applegroup=pygame.sprite.Group(apple)
        
        running = True
        while running:
            for event in pygame.event.get():
                

                if event.type == pygame.QUIT:

                    running = False

            key=pygame.key.get_pressed()
            if key[pygame.K_LEFT]:
                 prince.move_left()
            if key[pygame.K_RIGHT]:
                 prince.move_right()
            if key[pygame.K_UP]:
                prince.move_up()
            
            
            #prince.move_up()  # Example movement, adjust as needed
            apple.move()  # Example apple movement, adjust as needed

            # Check collisions
            if tower.check_collision(prince):
                # Handle collision logic
                pass
            
            charactergroup.update()

            # Draw everything
            screen.fill((255, 255, 255))  # White background
            # Draw characters, tower, apples, etc.
            charactergroup.draw(screen)
            
            pygame.display.flip()
            clock.tick(60)  # Limit to 60 FPS
        
        pygame.quit()

if __name__ == "__main__":
    controller = Controller()
    controller.mainloop()
