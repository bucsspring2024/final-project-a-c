import pygame
from src.game import Character
from src.game import Tower
from src.game import Witch
from src.game import Apple
from src.game import StartButton

class Controller:
    def __init__(self):
        pygame.init()
        self.start_button = StartButton(200, 100, .50, 'assets/startgame.png')
        #self.start_button_visible = True

    def mainloop(self):
        screen = pygame.display.set_mode((800, 600))
        clock = pygame.time.Clock()

        prince = Character(100, 400, .25, 'assets/prince.png')
        tower = Tower(300, 50 , .55, 'assets/tower.png')
        witch = Witch(100, 20, .02,'assets/witch.png')
        apple = Apple(350, 180, 'assets/apple.png')
        charactergroup= pygame.sprite.Group(prince)
        witchgroup= pygame.sprite.Group(witch)
        towergroup= pygame.sprite.Group(tower)
        startbuttongroup = pygame.sprite.Group(self.start_button)
       
        
        running = True
        start_game = False
        while running:
            for event in pygame.event.get():
                

                if event.type == pygame.QUIT:

                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN and not start_game:
                   if self.start_button.rect.collidepoint(event.pos):
                    start_game = True
                    startbuttongroup.empty()
                

        if start_game:
            key=pygame.key.get_pressed()
            if key[pygame.K_LEFT]:
                 prince.move_left()
            if key[pygame.K_RIGHT]:
                 prince.move_right()
            if key[pygame.K_UP]:
                prince.move_up()
            if key[pygame.K_DOWN]:
                prince.move_down()
            if key[pygame.K_1]:
                witch.move_left()
            if key[pygame.K_2]:
                witch.move_right()
            
            #prince.move_up()  # Example movement, adjust as needed
            apple.move()  # Example apple movement, adjust as needed

            # Check collisions
            #if tower.check_collision(prince):
                # Handle collision logic
            pass
            
        
            charactergroup.update()
            witchgroup.update()
            towergroup.update()
            # Draw everything
            screen.fill((" sky blue"))  # White background
            # Draw characters, tower, apples, etc.
            towergroup.draw(screen)
            charactergroup.draw(screen)
            witchgroup.draw(screen)
        else:
                
            startbuttongroup.draw(screen)
            
        pygame.display.flip()
        clock.tick(60)  
        
        pygame.quit()

if __name__ == "__main__":
    controller = Controller()
    controller.mainloop()
