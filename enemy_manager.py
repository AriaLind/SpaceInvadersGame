import pygame
import random

print("enemy_manager module loaded")

move_speed = 5
enemies = []

def spawn_enemy(pos_x: float, pos_y: float, height: float, width: float):
    new_enemy = pygame.Rect(pos_x, pos_y, width, height)
    
    # Check for overlap with existing enemies
    for enemy in enemies:
        if new_enemy.colliderect(enemy):
            print(f"Couldn't spawn enemy at x: {pos_x} y: {pos_y}")
            return False  # Abort spawning this enemy if it overlaps
    
    # If no overlaps, add the new enemy to the list
    print(f"Enemy spawned at x: {pos_x} y: {pos_y}")
    enemies.append(new_enemy)
    return True

def spawn_wave(amount: int, screen_width: int, enemy_size: int):
    spawned = 0
    attempts = 0
    max_attempts = 100  # Limit attempts to avoid an infinite loop
    
    while spawned < amount and attempts < max_attempts:
        attempts += 1
        pos_x = random.randint(0, screen_width - enemy_size)  # Random X position within screen width
        pos_y = random.randint(-200, -50)  # Spawn enemies off-screen initially
        
        if spawn_enemy(pos_x, pos_y, enemy_size, enemy_size):
            spawned += 1

def move_enemies():
    # Move each enemy downwards by a certain speed
    for enemy in enemies:
        enemy.y += move_speed

def draw_enemies(screen):
    # Draw each enemy on the screen
    for enemy in enemies:
        pygame.draw.rect(screen, "red", enemy)

# def damage_player(player_rect, damage_amount: int, player_health: int) -> int:
#     """
#     Checks if any enemies collide with the player and applies damage.
    
#     :param player_rect: The player's pygame.Rect object for collision detection.
#     :param damage_amount: The amount of damage to apply if a collision occurs.
#     :param player_health: The player's current health.
#     :return: The updated health of the player.
#     """
#     for enemy in enemies:
#         if player_rect.colliderect(enemy):
#             print("Player hit by enemy!")
#             player_health -= damage_amount
#             # Optionally, you can remove the enemy upon collision if desired
#             enemies.remove(enemy)
    
#     # Ensure the player's health doesn't go below zero
#     player_health = max(player_health, 0)
    
#     return player_health

def reached_bottom_of_screen(screen_height):
    for enemy in enemies:
        # Check if any enemy has reached the bottom of the screen
        if enemy.y >= screen_height:
            enemies.remove(enemy)
            return True
    return False
