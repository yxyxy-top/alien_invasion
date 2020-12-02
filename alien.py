import pygame
from pygame.sprite import Sprite


class Alien:
    """表示单个外星人的类"""

    def __init__(self, ai_settings, screen):
        """初始化外星人并设置起始位置"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载外星人图像，并设置其rect属性
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # 每个外星人
