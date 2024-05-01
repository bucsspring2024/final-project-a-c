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