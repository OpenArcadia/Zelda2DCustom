import pygame

class Weapon(pygame.sprite.Sprite):
    def __init__(self, player, groups):
        super().__init__(groups)
        self.sprite_type = 'weapon'
        direcion = player.status.split('_')[0]

        # graphic
        full_path = f'../graphics/weapons/{player.weapon}/{direcion}.png'
        self.image = pygame.image.load(full_path).convert_alpha()

        # placement
        if direcion == 'up':
            self.rect = self.image.get_rect(midbottom = player.rect.midtop + pygame.math.Vector2(-10,16))
        elif direcion == 'down':
            self.rect = self.image.get_rect(midtop = player.rect.midbottom + pygame.math.Vector2(-10,0))
        elif direcion == 'left':
            self.rect = self.image.get_rect(midright = player.rect.midleft + pygame.math.Vector2(0,16))
        elif direcion == 'right':
            self.rect = self.image.get_rect(midleft = player.rect.midright + pygame.math.Vector2(0,16))
        else:
            self.rect = self.image.get_rect(center = player.rect.center)