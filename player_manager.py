import pygame

pygame.mixer.init()

print("player_manager module loaded")

player_width = 40
player_height = 60 
player_move_speed = 500

max_health = 5
current_health = 5

bullet_width, bullet_height = 5, 10
bullet_speed = 10
bullet_color = "white"
bullet_sound = pygame.mixer.Sound("./resources/audio/laser_sound.mp3")
fire_rate = 200
cooldown_timer = 0
bullets = []

def spawn_bullet(player_x: float, player_y: float):
    bullet_x = player_x + player_width / 2 - bullet_width / 2
    bullet_y = player_y - bullet_height
    bullets.append(pygame.Rect(bullet_x, bullet_y, bullet_width, bullet_height))
    bullet_sound.play()
        
def animate_bullets(screen):
    for bullet in bullets[:]:  # Iterate over a copy of the bullets list
        bullet.y -= bullet_speed  # Move the bullet upwards
        if bullet.y < 0:
            bullets.remove(bullet)  # Remove the bullet if it goes off-screen
        pygame.draw.rect(screen, bullet_color, bullet)
    
def check_bullet_collision(enemy_manager, score):
    for bullet in bullets[:]:  # Use a copy of the bullets list
        for enemyLocation in enemy_manager.enemies[:]:  # Use a copy of the enemies list
            if bullet.colliderect(enemyLocation):  # Check for collision
                bullets.remove(bullet)  # Remove the bullet
                enemy_manager.enemies.remove(enemyLocation)  # Remove the enemy
                
                print(f"Enemy removed at: {enemyLocation}")
            
                score += 1
            
    return score
            
def set_player_health(amount: int):
    current_health = amount
    
def damage_player(amount: int):
    global current_health
    current_health -= amount
    print(f"Player took {amount} damage! Current hp: {current_health}")