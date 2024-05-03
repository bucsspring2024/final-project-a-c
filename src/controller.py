import pygame
from src.game import Character
from src.game import Tower
from src.game import Witch
#from src.game import Apple
from src.game import StartButton
from src.game import Rapunzel
from src.game import Apple

class Controller:
    def __init__(self):
        pygame.init()
        self.start_button = StartButton(300, 150, .60, 'assets/startgame.png')
        self.start_button_visible = True
        self.clock = pygame.time.Clock()
        #self.apple_timer = pygame.USEREVENT + 1
        #pygame.time.set_timer(self.apple_timer, 1000)  # Timer event every 1000 milliseconds (1 second)
        self.game_over = False

        self.you_win_image = pygame.image.load('assets/youwin.png')
        self.you_win_rect = self.you_win_image.get_rect()
        self.you_win_rect.center = (400, 300)

        self.game_over_image = pygame.image.load('assets/gameover.png')
        self.game_over_rect = self.game_over_image.get_rect()
        self.game_over_rect.center = (400, 300)

        



    def mainloop(self):
        screen = pygame.display.set_mode((800, 600))
        clock = pygame.time.Clock()

        prince = Character(100, 400, .25, 'assets/prince.png')
        tower = Tower(300, 50 , .55, 'assets/tower.png')
        witch = Witch(100, 20, .02,'assets/witch.png', )
        apple = Apple(100, 50, .005,  'assets/apple.png')
        rapunzel = Rapunzel (350, 150 , .30, 'assets/rapunzel.png')

        charactergroup= pygame.sprite.Group(prince)
        witchgroup= pygame.sprite.Group(witch)
        towergroup= pygame.sprite.Group(tower)
        startbuttongroup = pygame.sprite.Group(self.start_button)
        rapunzelgroup = pygame.sprite.Group(rapunzel)
        apple_group = pygame.sprite.Group(apple)
        
       
        
        running = True
        start_game = False
        game_over= False
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:

                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN and not start_game:
                   if self.start_button.rect.collidepoint(event.pos):
                    start_game = True
                    startbuttongroup.empty()
                
                #elif event.type == self.apple_timer and start_game:
                    #new_apple = Apple(100, 50, .005, 'assets/apple.png')  # Create a new apple
                    #apple_group.add(new_apple)
                
                #if event.type == self.apple_timer and start_game:  # Apple falling timer event
                    #apple.move_down()
                

            if start_game :
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
                if key[pygame.K_1]:
                    apple.move_left()
                if key[pygame.K_2]:
                    apple.move_right()
                if key[pygame.K_3]:
                    apple.move_up()
                    witch.move_up()
                if key[pygame.K_4]:
                    apple.move_down()
                    witch.move_down()

                
                
                
                
            #prince.move_up()  # Example movement, adjust as needed
            #apple.move()  # Example apple movement, adjust as needed

            # Check collisions
            #if tower.check_collision(prince):
                # Handle collision logic
                pass
                
            
                charactergroup.update()
                witchgroup.update()
                towergroup.update()
                startbuttongroup.update()
                rapunzelgroup.update()
                apple_group.update()
                # Draw everything
                screen.fill((" sky blue"))  # White background
                # Draw characters, tower, apples, etc.
                towergroup.draw(screen)
                charactergroup.draw(screen)
                witchgroup.draw(screen)
                rapunzelgroup.draw(screen)
                apple_group.draw(screen)

                if pygame.sprite.collide_rect(prince, apple):
                    screen.blit(self.game_over_image, self.game_over_rect)
                    pygame.display.flip()
                    pygame.time.delay(3000)  # Display for 3 seconds before quitting
                    running = False

                if pygame.sprite.collide_rect(prince, rapunzel):
                    screen.blit(self.you_win_image, self.you_win_rect)
                    pygame.display.flip()
                    pygame.time.delay(3000)  # Display for 3 seconds before quitting
                    running = False


            #if pygame.sprite.spritecollide(prince, apple_group, True):
                #self.game_over = True
                #print("Prince hit by apple! Witch wins.")

            elif not start_game:
                screen.fill("sky blue")
                startbuttongroup.draw(screen)


            #else:
                    
                #screen.fill("sky blue")
                #startbuttongroup.draw(screen)
            
            pygame.display.flip()
            clock.tick(60)  
        
        pygame.quit()

if __name__ == "__main__":
    controller = Controller()
    controller.mainloop()
