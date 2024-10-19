import pygame

print("utils module loaded")

buttons = []

def draw_button(screen, color: str, text: str, start_x: float, start_y: float, height: float, width: float, logo: str = None) -> pygame.Rect:
    # Create the button rectangle
    button_rect = pygame.Rect(start_x, start_y, width, height)
    pygame.draw.rect(screen, color, button_rect)  # Draw the button rectangle
    
    # Draw text
    font = pygame.font.Font(None, 36)  # Use default font and size 36
    text_surface = font.render(text, True, "white")  # Render text with anti-aliasing
    text_rect = text_surface.get_rect(center=button_rect.center)  # Center the text in the button
    screen.blit(text_surface, text_rect)  # Draw the text on the button

    # Draw logo if provided
    if logo:
        logo_image = pygame.image.load(logo)  # Load the logo image
        logo_rect = logo_image.get_rect(center=(start_x + width / 2, start_y + height / 2))  # Center the logo in the button
        # Scale the logo if needed
        logo_image = pygame.transform.scale(logo_image, (int(height * 0.6), int(height * 0.6)))  # Scale logo to fit button
        screen.blit(logo_image, logo_rect)  # Draw the logo on the button

    return button_rect  # Return the button rectangle for collision detection

  
def handle_button_clicks(event, screen):
    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_x, mouse_y = event.pos
        for button in buttons:
            # Create the button rectangle for collision detection
            button_rect = pygame.Rect(button["pos"][0], button["pos"][1], button["size"][0], button["size"][1])
            if button_rect.collidepoint((mouse_x, mouse_y)):
                button["action"]()  # Call the associated action if clicked

