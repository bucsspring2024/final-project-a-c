import pygame

class Character(pygame.sprite.Sprite):
    def __init__(self, x, y, scale, img_file):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.img_file = img_file
        self.image= pygame.image.load(img_file)
        self.image=pygame.transform.scale_by(self.image, scale)
        self.rect=self.image.get_rect()

    def update(self):
        self.rect.x=self.x
        self.rect.y=self.y

    def move_up(self):
        self.y -= 1

    def move_down(self):
        self.y += 1

    def move_left(self):
        self.x -= 1

    def move_right(self):
        self.x += 1

    def jump(self):
        self.y -= 10 

class Tower(pygame.sprite.Sprite):
    def __init__(self, x, y, scale, img_file):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.img_file = img_file
        self.image= pygame.image.load(img_file)
        self.image=pygame.transform.scale_by(self.image, scale)
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
    
    def update(self):
        self.rect.x=self.x
        self.rect.y=self.y
        pass


   # def check_collision(self, character):
        #if (character.x >= self.x and character.x <= self.x + 100) and \
           #(character.y >= self.y and character.y <= self.y + 200):
            #return True
       #return False
pass

class Witch(pygame.sprite.Sprite): 
    def __init__(self, x, y, scale, img_file):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.img_file = img_file
        self.image= pygame.image.load(img_file)
        self.image=pygame.transform.scale_by(self.image, scale)
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y


    def throw_apple(self):
        # Logic to throw apple at the character
        pass
    def update(self):
        self.rect.x=self.x
        self.rect.y=self.y
        pass
     
    def move_left(self):
        self.x -= 1

    def move_right(self):
        self.x += 1
class Apple:
    def __init__(self, x, y, img_file):
        self.x = x
        self.y = y
        self.img_file = img_file
        self.rect.x=x
        self.rect.y=y

    def move(self):
        self.y += 1

class StartMenu:
    def __init__(self, screen, image_path):
        self.screen = screen
        self.image = pygame.image.load(image_path)
        self.image_rect = self.image.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
        self.rect.x=x
        self.rect.y=y
        

    def display_menu(self):
        self.screen.blit(self.image, self.image_rect)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                return True  

    def run(self):
        while True:
            self.screen.fill((0, 0, 0))
            self.display_menu()
            pygame.display.flip()

            start_game = self.handle_events()
            if start_game:
                break