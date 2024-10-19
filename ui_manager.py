import pygame

print("ui_manager module loaded")

# Define position as a tuple (x, y)
health_bar_position = (20, 60)  # x=20, y=60 for example
# Define size as a tuple (width, height)
health_bar_size = (200, 20)  # 200px wide, 20px tall

def show_player_position(screen, player_x: float, player_y: float):
    font = pygame.font.Font(None, 36)
    text = font.render(f"Player X: {int(player_x)} Player Y: {int(player_y)}", True, "white")
    screen.blit(text, (0, 20))

def show_cooldown_timer(screen, cooldown_timer: float):
    font = pygame.font.Font(None, 36)
    text = font.render(f"Weapon cooldown: {cooldown_timer}", True, "white")
    screen.blit(text, (0, 40))

def show_score(screen, score: int):
    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score}", True, "white")
    screen.blit(text, (0, 0))

def show_health(screen, current_health: int, max_health: int):
    """
    Draws a health bar on the screen.
    
    :param screen: The Pygame screen to draw on.
    :param current_health: The current health value.
    :param max_health: The maximum health value.
    """
    x, y = health_bar_position
    width, height = health_bar_size

    # Calculate the health percentage
    health_percentage = current_health / max_health
    health_bar_width = int(width * health_percentage)

    # Draw the background (depleted health)
    pygame.draw.rect(screen, (150, 0, 0), (x, y, width, height))  # Dark red background for the total bar

    # Draw the foreground (current health)
    pygame.draw.rect(screen, (0, 200, 0), (x, y, health_bar_width, height))  # Green bar for current health

    # Optional: Draw a border around the health bar for better visual separation
    pygame.draw.rect(screen, (255, 255, 255), (x, y, width, height), 2)  # White border with thickness 2
