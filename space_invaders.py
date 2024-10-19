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

# def draw_mute_button():
#     if is_muted:
#         screen.blit(mute_icon, (mute_icon_width, mute_icon_height))  # Position for the mute icon
#     else:
#         screen.blit(unmute_icon, (mute_icon_width, mute_icon_height))  # Position for the unmute icon

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
    
    
    
while running:
    if (first_time_setup_complete == False):
        first_time_setup()
        first_time_setup_complete = True
    
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos

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
    
    if (cooldown_timer > 0):
        cooldown_timer -= dt * 1000
        
    for enemy in enemies:
        pygame.draw.rect(screen, "red", enemy)
        
    if len(enemies) < 1:
        spawn_enemy(random.randint(0, int(screen_x)), random.randint(0, int(screen_y - 300)), 50, 50)
        
    for bullet in bullets[:]:  # Use a copy of the bullets list
        for enemyLocation in enemies[:]:  # Use a copy of the enemies list
            if bullet.colliderect(enemyLocation):  # Check for collision
                bullets.remove(bullet)  # Remove the bullet
                enemies.remove(enemyLocation)  # Remove the enemy
                score += 1
                break  # Exit the inner loop since the bullet is already removed

    
    animate_bullets()

    utils.draw_button(screen, "red", "Button", 100, 100, 50, 100, toggle_mute())
    show_score()
    show_player_position()
    show_cooldown_timer()

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()