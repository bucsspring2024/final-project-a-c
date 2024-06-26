import pygame
from src.game import Character
from src.game import Tower
from src.game import Witch
#from src.game import Apple
from src.game import StartButton
from src.game import Rapunzel
from src.game import Apple
from src.game import Cloud
from src.game import Highscore

#from src.game import RetryButton


class Controller:
    def __init__(self):
        pygame.init()
        self.start_button = StartButton(300, 150, .60, 'assets/startgame.png')
        self.retry_button = StartButton(400, 400, .60, 'assets/retry.png')  # Add retry button THIS IS NEW, DELETE IF DONT WORK
        self.start_button_visible = True
        self.clock = pygame.time.Clock()
        self.game_over = False


        self.you_win_image = pygame.image.load('assets/youwin.png')
        self.you_win_rect = self.you_win_image.get_rect()
        self.you_win_rect.center = (400, 300)

        self.game_over_image = pygame.image.load('assets/gameover.png')
        self.game_over_rect = self.game_over_image.get_rect()
        self.game_over_rect.center = (400, 300)

        self.retry_image = pygame.image.load('assets/retry.png')
        self.retry_rect = self.retry_image.get_rect()
        self.retry_rect.center = (400, 300)

   
    def reset_game(self):


        

        self.cloud = Cloud(50, 150 , .90, 'assets/clouds.png')
        self.prince = Character(100, 400, .25, 'assets/prince.png')
        self.tower = Tower(300, 50 , .55, 'assets/tower.png')
        self.witch = Witch(100, 20, .02,'assets/witch.png', )
        self.apple = Apple(100, 50, .005,  'assets/apple.png')
        self.rapunzel = Rapunzel (350, 150 , .30, 'assets/rapunzel.png')
        self.score = 0


        self.charactergroup= pygame.sprite.Group(self.prince)
        self.witchgroup= pygame.sprite.Group(self.witch)
        self.towergroup= pygame.sprite.Group(self.tower)
        #self.startbuttongroup = pygame.sprite.Group(self.start_button)
        self.rapunzelgroup = pygame.sprite.Group(self.rapunzel)
        self.apple_group = pygame.sprite.Group(self.apple)
        self.cloud_group = pygame.sprite.Group(self.cloud)

        



    def mainloop(self):

        screen = pygame.display.set_mode((800, 600))
        clock = pygame.time.Clock()
        self.reset_game()
        #CONSTANTS
        INTRO=0
        GAME=1
        RETRY=2


        cloud = Cloud(50, 150 , .90, 'assets/clouds.png')
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
        cloud_group = pygame.sprite.Group(cloud)
        
       
        

        
        running = True
        start_game = INTRO
        game_over= False
        score = 0

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:

                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN and  start_game == INTRO:
                    if self.start_button.is_clicked(event.pos):
                  #if self.start_button.rect.collidepoint(event.pos):
                        start_game = GAME
                        score = 0
                        #self.startbuttongroup.empty()


                elif event.type == pygame.MOUSEBUTTONDOWN and game_over:
                    #if self.retry_button.rect.collidepoint(event.pos):
                    if self.retry_button.is_clicked(event.pos):  # Check for retry button click NEW STUFFY
                        print(self.score)
                        self.reset_game()
                        game_over = False
                        start_game= GAME
                    
                

            if start_game == GAME:
                key=pygame.key.get_pressed()
                if key[pygame.K_LEFT]:
                    self.prince.move_left()
                if key[pygame.K_RIGHT]:
                    self.prince.move_right()
                if key[pygame.K_UP]:
                    self.prince.move_up()
                if key[pygame.K_DOWN]:
                    self.prince.move_down()
                if key[pygame.K_1]:
                    self.witch.move_left()
                if key[pygame.K_2]:
                    self.witch.move_right()
                if key[pygame.K_1]:
                    self.apple.move_left()
                if key[pygame.K_2]:
                    self.apple.move_right()
                if key[pygame.K_3]:
                    self.apple.move_up()
                    self.witch.move_up()
                if key[pygame.K_4]:
                    self.apple.move_down()
                    self.witch.move_down()

                
                
                
                
            #prince.move_up()  # Example movement, adjust as needed
            #apple.move()  # Example apple movement, adjust as needed

            # Check collisions
            #if tower.check_collision(prince):
                # Handle collision logic
                pass
                
            
                self.charactergroup.update()
                self.witchgroup.update()
                self.towergroup.update()
                #self.startbuttongroup.update()
                self.rapunzelgroup.update()
                self.apple_group.update()
                self.cloud_group.update()
                # Draw everything
                screen.fill((" sky blue"))  # White background
                # Draw characters, tower, apples, etc.
                self.cloud_group.draw(screen)
                self.towergroup.draw(screen)
                self.charactergroup.draw(screen)
                self.witchgroup.draw(screen)
                self.rapunzelgroup.draw(screen)
                self.apple_group.draw(screen)



                if pygame.sprite.collide_rect(self.prince, self.apple):
                    screen.blit(self.game_over_image, self.game_over_rect)
                    pygame.display.flip()
                    pygame.time.delay(3000)  # Display for 3 seconds before quitting
                    start_game = RETRY
                    game_over= True
                    self.score=score

                if pygame.sprite.collide_rect(self.prince, self.rapunzel):
                    screen.blit(self.you_win_image, self.you_win_rect)
                    pygame.display.flip()
                    pygame.time.delay(3000)  # Display for 3 seconds before quitting
                    start_game = RETRY
                    game_over=True
                    self.score=score


            #THIS IS NEW STUFF     
                if pygame.sprite.collide_rect(self.prince, self.apple) or pygame.sprite.collide_rect(self.prince, self.rapunzel):
                    #screen.blit(self.retry_image, self.retry_rect)
                    self.retry_button.draw(screen)
                    pygame.display.flip()
                    pygame.time.delay(3000)  # Display for 3 seconds before quitting
                    start_game = RETRY
                    game_over= True
                    self.score=score



                    


            #if pygame.sprite.spritecollide(prince, apple_group, True):
                #self.game_over = True
                #print("Prince hit by apple! Witch wins.")

            elif start_game == INTRO:
                screen.fill("sky blue")
                #self.startbuttongroup.draw(screen)
                self.start_button.draw(screen)


            #else:
                    
                #screen.fill("sky blue")
                #startbuttongroup.draw(screen)
            
            pygame.display.flip()
            score += clock.tick(60)
        
        pygame.quit()

if __name__ == "__main__":
    controller = Controller()
    controller.mainloop()
