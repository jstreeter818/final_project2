import pygame
import pygame_gui

pygame.init()

pygame.display.set_caption('Connect 4!')
window_surface = pygame.display.set_mode((800, 600))

background = pygame.Surface((800, 600))
background.fill(pygame.Color('#8abab6'))

manager = pygame_gui.UIManager((800, 600))

start_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((340, 275), (120, 50)), text='Start Game', manager=manager)

clock = pygame.time.Clock()
is_running = True

while is_running:
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == start_button:
                print('Hello World!')

        manager.process_events(event)

    manager.update(time_delta)

    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)

    pygame.display.update()