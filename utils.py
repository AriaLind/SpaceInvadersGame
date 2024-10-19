import pygame

def draw_button(screen, color: str, text: str, start_x: float, start_y: float, height: float, width: float, onclick: callable):
    pygame.draw.rect(screen, color, pygame.Rect(start_x, start_y, width, height))
    
    font = pygame.font.Font(None, 36)  # Use default font and size 36
    text_surface = font.render(text, True, "white")  # Render text with anti-aliasing
    text_rect = text_surface.get_rect(center=(start_x + width / 2, start_y + height / 2))  # Center the text
    screen.blit(text_surface, text_rect)  # Draw the text on the button
    
    for ev in pygame.event.get():
        if ev.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = ev.pos
            
            if start_x <= mouse_x <= start_x + width and start_y <= mouse_y <= start_y + height:
                onclick()
            
        
