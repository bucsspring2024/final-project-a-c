class Character:
    def __init__(self, x, y, img_file):
        self.x = x
        self.y = y
        self.img_file = img_file

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

class Tower:
    def __init__(self, x, y, img_file):
        self.x = x
        self.y = y
        self.img_file = img_file

    def check_collision(self, character):
        if (character.x >= self.x and character.x <= self.x + 100) and \
           (character.y >= self.y and character.y <= self.y + 200):
            return True
        return False

class Witch:
    def __init__(self, x, y, img_file):
        self.x = x
        self.y = y
        self.img_file = img_file

    def throw_apple(self):
        # Logic to throw apple at the character
        pass

class Apple:
    def __init__(self, x, y, img_file):
        self.x = x
        self.y = y
        self.img_file = img_file

    def move(self):
        self.y += 1