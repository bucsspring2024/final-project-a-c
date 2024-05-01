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
    def __init__(self, x, y, scale, img_file, apple_group):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.img_file = img_file
        self.image= pygame.image.load(img_file)
        self.image=pygame.transform.scale_by(self.image, scale)
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.apple_group = apple_group

    def throw_apple(self):
        apple = Apple(self.rect.x + self.rect.width // 2, self.rect.y + self.rect.height, 'assets/apple.png')
        self.apple_group.add(apple)


    def update(self):
        self.rect.x=self.x
        self.rect.y=self.y
        pass
     
    def move_left(self):
        self.x -= 1

    def move_right(self):
        self.x += 1


class Apple(pygame.sprite.Sprite):
    def __init__(self, x, y, img_file):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.img_file = img_file
        self.image = pygame.image.load(img_file)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def move(self):
        self.y += 1

class StartButton(pygame.sprite.Sprite):
    def __init__(self, x, y, scale, img_file):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.img_file = img_file
        self.image = pygame.image.load(img_file)
        self.image = pygame.transform.scale_by(self.image, scale)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)
    
class Rapunzel(pygame.sprite.Sprite):
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
    
    def check_collision(self, character):
        if (character.x >= self.x and character.x <= self.x + 100) and \
            (character.y >= self.y and character.y <= self.y + 200):
            return True
        return False
