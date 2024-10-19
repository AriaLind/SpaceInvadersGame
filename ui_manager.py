import pygame

print("ui_manager module loaded")

# Define position as a tuple (x, y)
health_bar_position = (20, 100)  # x=20, y=60 for example
# Define size as a tuple (width, height)
health_bar_size = (200, 40)  # 200px wide, 20px tall

def show_player_position(screen, player_x: float, player_y: float):
    font = pygame.font.Font(None, 36)
    text = font.render(f"Player X: {int(player_x)} Player Y: {int(player_y)}", True, "white")
    screen.blit(text, (0, 40))

def show_cooldown_timer(screen, cooldown_timer: float):
    font = pygame.font.Font(None, 36)
    text = font.render(f"Weapon cooldown: {cooldown_timer}", True, "white")
    screen.blit(text, (0, 60))

def show_score(screen, score: int):
    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score}", True, "white")
    screen.blit(text, (0, 20))
    
def show_wave_info(screen, wave: int, wave_speed: float, enemy_count: int, enemy_size: int):
    font = pygame.font.Font(None, 36)
    text = font.render(f"Wave: {wave} Enemy Speed: {wave_speed} Enemy Count: {enemy_count} Enemy Size: {enemy_size}", True, "white")
    screen.blit(text, (0, 0))
    
def wave_defeated_screen(screen, wave_number, countdown_time=3):
    # Set up fonts
    font = pygame.font.Font(None, 74)  # Large font for the message
    countdown_font = pygame.font.Font(None, 48)  # Smaller font for countdown

    # Create the wave defeated message
    wave_defeated_text = font.render(f"Wave {wave_number} Defeated!", True, "green")
    
    # Get the rect for positioning the text
    wave_defeated_rect = wave_defeated_text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2 - 20))

    # Fill the screen with black
    screen.fill("black")

    # Blit the wave defeated text to the screen
    screen.blit(wave_defeated_text, wave_defeated_rect)

    # Start the countdown timer
    for remaining_time in range(countdown_time, 0, -1):
        # Create the countdown text
        countdown_text = countdown_font.render(f"Next wave in: {remaining_time}", True, "white")
        countdown_rect = countdown_text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2 + 40))
        
        # Update the display
        screen.fill("black")  # Clear the screen
        screen.blit(wave_defeated_text, wave_defeated_rect)  # Re-blit the wave defeated text
        screen.blit(countdown_text, countdown_rect)  # Blit countdown text
        pygame.display.flip()
        
        # Wait for a short time, ensuring the game remains responsive
        for _ in range(10):  # Wait for approximately 1 second
            pygame.time.delay(100)  # Delay for 100 milliseconds
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()  # Exit the game if the window is closed

    # Clear the screen for the next wave to start
    screen.fill("black")
    pygame.display.flip()



def show_health(screen, current_health: int, max_health: int):
    """
    Draws a health bar on the screen and displays the current health as a fraction.
    
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

    # Prepare the health text
    health_text = f"{current_health}/{max_health}"
    font = pygame.font.Font(None, 36)  # Font size for the health text
    text_surface = font.render(health_text, True, (255, 255, 255))  # White text
    text_rect = text_surface.get_rect(center=(x + width // 2, y + height // 2))  # Center the text

    # Blit the health text on the screen
    screen.blit(text_surface, text_rect)

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