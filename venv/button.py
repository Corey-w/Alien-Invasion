import pygame.font


class Button():

    def __init__(self, ai_settings, screen, msg):
        """Initialise button attributes"""
        self.screen = screen
        self.screen_rect = screen.get_rect()


        # Buttons properties
        self.width, self.height = 200, 50
        self.button_color = (69, 201, 249)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Build buttons object and center it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Button prep messsage
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """Turns message into an image and centers the text"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # Draw blank button plus message
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
