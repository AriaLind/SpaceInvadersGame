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
    
    # Draw logo if provided
    if logo:
        logo_image = pygame.image.load(logo)  # Load the logo image
        # Scale the logo to fit within the button height
        scaled_logo_height = int(height * 0.6)
        scaled_logo_width = int(height * 0.6)  # Keep it square for simplicity, but you can adjust this as needed
        logo_image = pygame.transform.scale(logo_image, (scaled_logo_width, scaled_logo_height))  
        
        # Calculate the position for the logo to appear next to the text
        logo_rect = logo_image.get_rect(midleft=(button_rect.left + 10, button_rect.centery))  # Adjust `midleft` for positioning
        
        # Adjust the text position slightly to the right of the logo
        text_rect = text_surface.get_rect(midleft=(logo_rect.right + 10, button_rect.centery))

        # Draw the logo on the button
        screen.blit(logo_image, logo_rect)

    # Draw the text on the button
    screen.blit(text_surface, text_rect)

    return button_rect  # Return the button rectangle for collision detection


def handle_button_clicks(event, screen):
    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_x, mouse_y = event.pos
        for button in buttons:
            # Create the button rectangle for collision detection
            button_rect = pygame.Rect(button["pos"][0], button["pos"][1], button["size"][0], button["size"][1])
            if button_rect.collidepoint((mouse_x, mouse_y)):
                button["action"]()  # Call the associated action if clicked
