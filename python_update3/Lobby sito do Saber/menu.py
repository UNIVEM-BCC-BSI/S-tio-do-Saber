import pygame
import sys
import time

pygame.init()

WIDTH, HEIGHT = 1919, 1079
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sitio do saber")

background_image = pygame.image.load("fundo.png")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
TRANSPARENT = (0, 0, 0, 0)
GREY = (200, 200, 200, 200)

font = pygame.font.Font("TitanOne-Regular.ttf", 36)

class Button:
    def __init__(self, rect, image=None):
        self.rect = rect
        self.image = image
        self.original_image = image

    def draw(self, surface):
        if self.image:
            image_rect = self.image.get_rect(center=self.rect.center)
            surface.blit(self.image, image_rect.topleft)

    def scale_image(self, factor):
        if self.image:
            width = int(self.original_image.get_width() * factor)
            height = int(self.original_image.get_height() * factor)
            self.image = pygame.transform.scale(self.original_image, (width, height))

class SettingsMenu:
    def __init__(self, rect):
        self.rect = rect
        self.visible = False

    def draw(self, surface):
        if self.visible:
            rounded_rect_surface = pygame.Surface((self.rect.width, self.rect.height), pygame.SRCALPHA)
            rounded_rect_surface.fill(TRANSPARENT)
            pygame.draw.rect(rounded_rect_surface, GREY, rounded_rect_surface.get_rect(), border_radius=20)
            pygame.draw.rect(rounded_rect_surface, BLACK, rounded_rect_surface.get_rect(), 2, border_radius=20)
            surface.blit(rounded_rect_surface, self.rect.topleft)

            settings_text = font.render("Configurações", True, BLACK)
            surface.blit(settings_text, (self.rect.x + 20, self.rect.y + 20))

            volume_text = font.render("Volume", True, BLACK)
            surface.blit(volume_text, (self.rect.x + 40, self.rect.y + 80))

            volume_slider.draw(surface)

class VolumeSlider:
    def __init__(self, rect, min_val=0, max_val=100, initial_val=50):
        self.rect = rect
        self.min_val = min_val
        self.max_val = max_val
        self.value = initial_val
        self.knob_rect = pygame.Rect(self.rect.x + (self.value / self.max_val) * self.rect.width - 10, self.rect.y + 70, 20, self.rect.height + 50)

    def draw(self, surface):
        pygame.draw.rect(surface, BLACK, self.rect, 2)
        pygame.draw.rect(surface, BLACK, (self.rect.x, self.rect.y + 70, self.rect.width * (self.value / self.max_val), self.rect.height))
        pygame.draw.ellipse(surface, BLACK, self.knob_rect)

class VolumeSlider:
    def __init__(self, rect, min_val=0, max_val=100, initial_val=50):
        self.rect = rect
        self.min_val = min_val
        self.max_val = max_val
        self.value = initial_val
        self.knob_rect = pygame.Rect(self.rect.x + (self.value / self.max_val) * self.rect.width - 10, self.rect.y - 10, 20, self.rect.height + 20)
        self.dragging = False

    def draw(self, surface):
        pygame.draw.rect(surface, BLACK, self.rect, 2)
        pygame.draw.rect(surface, BLACK, (self.rect.x, self.rect.y, self.rect.width * (self.value / self.max_val), self.rect.height))
        pygame.draw.ellipse(surface, BLACK, self.knob_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.knob_rect.collidepoint(event.pos):
                self.dragging = True
        elif event.type == pygame.MOUSEBUTTONUP:
            self.dragging = False
        elif event.type == pygame.MOUSEMOTION:
            if self.dragging:
                mouse_x, _ = event.pos
                new_value = max(self.min_val, min(self.max_val, ((mouse_x - self.rect.x) / self.rect.width) * self.max_val))
                if new_value != self.value:
                    self.value = new_value
                    self.knob_rect.x = self.rect.x + (self.value / self.max_val) * self.rect.width - 10
                    self.update_volume()

    def update_volume(self):
        volume = self.value / self.max_val
        pygame.mixer.music.set_volume(volume)

def main_game():
    show_loading_screen()
    print("Iniciar o jogo!")

def quit_game():
    pygame.quit()
    sys.exit()

def open_settings():
    settings_menu.visible = not settings_menu.visible

def show_loading_screen():
    screen.blit(background_image, (0, 0))
    
    loading_screen_image = pygame.image.load("Tela_carregamento.png")
    loading_screen_image = pygame.transform.scale(loading_screen_image, (1919, 1079))

    for alpha in range(0, 255, 5):  
        loading_screen_image.set_alpha(alpha)  
        screen.blit(loading_screen_image, (WIDTH // 2 - 959, HEIGHT // 2 - 539))  
        pygame.display.flip()  
        pygame.time.delay(30)  

    time.sleep(3)

button_width = 250
button_height = 80
button_spacing = 150
button_x = WIDTH // 2 - button_width // 2

start_button_rect = pygame.Rect(button_x, HEIGHT // 2 + button_spacing // 2, button_width, button_height)
quit_button_rect = pygame.Rect(button_x, HEIGHT // 2 + button_spacing + button_spacing // 2 + 50, button_width, button_height)

settings_button_image = pygame.image.load("Config._botao.png")
settings_button_image = pygame.transform.scale(settings_button_image, (150, 150))
settings_button_rect = pygame.Rect(10, 10, 150, 150)

start_button_image = pygame.image.load("Botao_Play.png")
start_button_image = pygame.transform.scale(start_button_image, (300, 300))

quit_button_image = pygame.image.load("Botao_Sair2.png")
quit_button_image = pygame.transform.scale(quit_button_image, (300, 300))

logo_image = pygame.image.load("LOGOsem_slogan.png")
logo_image = pygame.transform.scale(logo_image, (800, 800))
logo_rect = logo_image.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 200))

start_button = Button(start_button_rect, start_button_image)
quit_button = Button(quit_button_rect, quit_button_image)
settings_button = Button(settings_button_rect, settings_button_image)
settings_menu_rect = pygame.Rect(10, 170, 500, 200)
settings_menu = SettingsMenu(settings_menu_rect)
volume_slider = VolumeSlider(pygame.Rect(50, 290, 400, 20))

pygame.mixer.music.load("musicaLobby.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(volume_slider.value / 100)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos

            if start_button.rect.collidepoint(mouse_x, mouse_y):
                main_game()
            elif quit_button.rect.collidepoint(mouse_x, mouse_y):
                quit_game()
            elif settings_button.rect.collidepoint(mouse_x, mouse_y):
                open_settings()

            if settings_menu.visible:
                volume_slider.handle_event(event)

        elif event.type == pygame.MOUSEBUTTONUP:
            volume_slider.handle_event(event)
        
        elif event.type == pygame.MOUSEMOTION:
            mouse_x, mouse_y = event.pos

            if start_button.rect.collidepoint(mouse_x, mouse_y):
                start_button.scale_image(1.2)
            else:
                start_button.scale_image(1.0)

            if quit_button.rect.collidepoint(mouse_x, mouse_y):
                quit_button.scale_image(1.2)
            else:
                quit_button.scale_image(1.0)

            if settings_button.rect.collidepoint(mouse_x, mouse_y):
                settings_button.scale_image(1.2)
            else:
                settings_button.scale_image(1.0)

            if settings_menu.visible:
                volume_slider.handle_event(event)

    screen.blit(background_image, (0, 0))

    screen.blit(logo_image, logo_rect.topleft)

    start_button.draw(screen)
    quit_button.draw(screen)
    settings_button.draw(screen)
    
    settings_menu.draw(screen)

    pygame.display.flip()


