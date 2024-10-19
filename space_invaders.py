# Example file showing a circle moving on screen
import pygame
import random
# import game_music
import utils

# pygame setup
pygame.init()
pygame.mixer.init()

screen_x = 1280
screen_y = 720

screen = pygame.display.set_mode((screen_x, screen_y))
clock = pygame.time.Clock()
running = True
dt = 0

pygame.mixer.music.load('boss_music.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.1)

first_time_setup_complete = False

color = (255,0,0)

player_x = screen.get_width() / 2
player_y = screen.get_height() - 75
player_width = 40
player_height = 60 
player_move_speed = 500

score = 0

player_pos = pygame.Vector2(player_x, player_y)

bullet_width, bullet_height = 5, 10
bullet_speed = 10
bullet_color = "white"
bullet_sound = pygame.mixer.Sound("laser_sound.mp3")
fire_rate = 200
cooldown_timer = 0
bullets = []

enemies = []

mute_icon = pygame.image.load("mute.png")
unmute_icon = pygame.image.load("unmute.png")

is_muted = False
music_volume = 0.1
mute_icon_width = 10
mute_icon_height = 10

def toggle_mute():
    global is_muted  # Declare is_muted as a global variable
    is_muted = not is_muted
    if is_muted:
        pygame.mixer.music.set_volume(0)  # Mute music
    else:
        pygame.mixer.music.set_volume(music_volume)  # Unmute music

def first_time_setup():
    bullet_sound.set_volume(0.1)

def spawn_bullet():
    bullet_x = player_x + player_width / 2 - bullet_width / 2
    bullet_y = player_y - bullet_height
    bullets.append(pygame.Rect(bullet_x, bullet_y, bullet_width, bullet_height))
    bullet_sound.play()
        
def animate_bullets():
    for bullet in bullets[:]:  # Iterate over a copy of the bullets list
        bullet.y -= bullet_speed  # Move the bullet upwards
        if bullet.y < 0:
            bullets.remove(bullet)  # Remove the bullet if it goes off-screen
        pygame.draw.rect(screen, bullet_color, bullet)
        
def show_player_position():
    font = pygame.font.Font(None, 36)  # None means using the default font, 36 is the font size
    text = font.render(f"Player X: {int(player_x)} Player Y: {int(player_y)}", True, "white")  # True for anti-aliasing
    screen.blit(text, (0, 20))  # Blit text at (50, 50)
    
def show_cooldown_timer():
    font = pygame.font.Font(None, 36)  # None means using the default font, 36 is the font size
    text = font.render(f"Weapon cooldown: {cooldown_timer}", True, "white")  # True for anti-aliasing
    screen.blit(text, (0, 40))  # Blit text at (50, 50)
    
def show_score():
    font = pygame.font.Font(None, 36)  # None means using the default font, 36 is the font size
    text = font.render(f"Score: {score}", True, "white")  # True for anti-aliasing
    screen.blit(text, (0, 0))  # Blit text at (50, 50)
    
def spawn_enemy(pos_x: float, pos_y: float, height: float, width: float):
    enemy = pygame.Rect(pygame.Rect(pos_x, pos_y, height, width))
    pygame.draw.rect(screen, "red", enemy)
    enemies.append(enemy)
    
def reset_game():
    print("Game Reset!")  # Placeholder for the reset functionality    
    
utils.buttons.append({"text": "Mute/Unmute", "color": "blue", "pos": (400, 0), "size": (150, 50), "action": toggle_mute})
utils.buttons.append({"text": "Reset", "color": "green", "pos": (600, 0), "size": (150, 50), "action": reset_game})

while running:
    if not first_time_setup_complete:
        first_time_setup()
        first_time_setup_complete = True
    
    # poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            utils.handle_button_clicks(event, screen)  # Check button clicks right after events

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    pygame.draw.rect(screen, "red", pygame.Rect(player_x, player_y, player_height, player_width))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and player_x > 0:
        player_x -= player_move_speed * dt
    if keys[pygame.K_d] and player_x < screen_x - player_width:
        player_x += player_move_speed * dt
    if keys[pygame.K_SPACE] and cooldown_timer <= 0:
        spawn_bullet()
        cooldown_timer = fire_rate  # Reset the cooldown timer after spawning a bullet
    
    if cooldown_timer > 0:
        cooldown_timer -= dt * 1000
        
    for enemy in enemies:
        pygame.draw.rect(screen, "red", enemy)
            
    if len(enemies) < 5:
        spawn_enemy(random.randint(0, int(screen_x - 50)), random.randint(100, int(screen_y - 300)), 50, 50)

        
    for bullet in bullets[:]:  # Use a copy of the bullets list
        for enemyLocation in enemies[:]:  # Use a copy of the enemies list
            if bullet.colliderect(enemyLocation):  # Check for collision
                bullets.remove(bullet)  # Remove the bullet
                enemies.remove(enemyLocation)  # Remove the enemy
                score += 1
                break  # Exit the inner loop since the bullet is already removed

    animate_bullets()

    # Draw buttons here
    for button in utils.buttons:
        utils.draw_button(screen, button["color"], button["text"], button["pos"][0], button["pos"][1], button["size"][1], button["size"][0])

    show_score()
    show_player_position()
    show_cooldown_timer()

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    dt = clock.tick(60) / 1000

pygame.quit()