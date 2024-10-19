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

def show_game_over_screen(screen, score, delay=5):
    # Set up fonts
    font = pygame.font.Font(None, 74)  # Use a large font for the game over message
    score_font = pygame.font.Font(None, 36)  # Smaller font for the score
    countdown_font = pygame.font.Font(None, 48)  # Font for countdown timer

    # Create surfaces for the game over text
    game_over_text = font.render("Game Over", True, "red")
    score_text = score_font.render(f"Your Score: {score}", True, "white")

    # Get the rect for positioning the text
    game_over_rect = game_over_text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2 - 20))
    score_rect = score_text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2 + 20))

    # Fill the screen with black
    screen.fill("black")

    # Blit the game over text and score to the screen
    screen.blit(game_over_text, game_over_rect)
    screen.blit(score_text, score_rect)

    # Update the display
    pygame.display.flip()

    # Countdown loop
    for remaining_time in range(delay, 0, -1):
        # Fill the screen with black
        screen.fill("black")

        # Blit the game over text and score to the screen
        screen.blit(game_over_text, game_over_rect)
        screen.blit(score_text, score_rect)

        # Create the countdown text
        countdown_text = countdown_font.render(f"Exiting in {remaining_time}...", True, "white")
        countdown_rect = countdown_text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2 + 80))
        
        # Blit the countdown text to the screen
        screen.blit(countdown_text, countdown_rect)

        # Update the display
        pygame.display.flip()

        # Wait for one second
        pygame.time.delay(1000)

    # Optionally, quit the game or implement your restart logic here