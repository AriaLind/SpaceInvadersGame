# Example file showing a circle moving on screen
import pygame
import random
import music_manager
import utils
import enemy_manager
import ui_manager
import player_manager

# pygame setup
pygame.init()
pygame.mixer.init()

screen_x = 1280
screen_y = 720

screen = pygame.display.set_mode((screen_x, screen_y))
clock = pygame.time.Clock()
running = True
dt = 0

pygame.mixer.music.load('./resources/audio/boss_music.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(music_manager.music_volume)

first_time_setup_complete = False

color = (255,0,0)

player_x = screen.get_width() / 2
player_y = screen.get_height() - 75

score = 0

player_pos = pygame.Vector2(player_x, player_y)



mute_icon = pygame.image.load("./resources/img/mute.png")
unmute_icon = pygame.image.load("./resources/img/unmute.png")

mute_icon_width = 10
mute_icon_height = 10

score = 0

def first_time_setup():
    player_manager.bullet_sound.set_volume(0.1)

 
    
def reset_game():
    print("Game Reset!")  # Placeholder for the reset functionality    
    
utils.buttons.append({"text": "Mute/Unmute", "color": "blue", "pos": (400, 0), "size": (150, 50), "action": music_manager.toggle_mute, "logo": "./resources/img/mute.png"})
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

    pygame.draw.rect(screen, "red", pygame.Rect(player_x, player_y, player_manager.player_height, player_manager.player_width))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and player_x > 0:
        player_x -= player_manager.player_move_speed * dt
    if keys[pygame.K_d] and player_x < screen_x - player_manager.player_width:
        player_x += player_manager.player_move_speed * dt
    if keys[pygame.K_SPACE] and player_manager.cooldown_timer <= 0:
        player_manager.spawn_bullet(player_x, player_y)
        player_manager.cooldown_timer = player_manager.fire_rate  # Reset the cooldown timer after spawning a bullet
    
    if player_manager.cooldown_timer > 0:
        player_manager.cooldown_timer -= dt * 1000
        
    for enemy in enemy_manager.enemies:
        pygame.draw.rect(screen, "red", enemy)
            
    ui_manager.show_health(screen, player_manager.current_health, player_manager.max_health)        
    
    # Spawn a wave of enemies if there are none left
    if len(enemy_manager.enemies) < 1:
        enemy_manager.spawn_wave(10, screen_x, 50)  # Spawn 10 enemies with size 50
    
    # Move enemies down the screen
    enemy_manager.move_enemies()  # Adjust the speed as necessary

    # Draw enemies in each frame
    enemy_manager.draw_enemies(screen)

    score = player_manager.check_bullet_collision(enemy_manager, score)
    player_manager.animate_bullets(screen)

    if (enemy_manager.reached_bottom_of_screen(screen_y)):
        print("An enemy has reached the bottom of the screen!")
        player_manager.damage_player(1)
    
    # Draw buttons here
    for button in utils.buttons:
        utils.draw_button(screen, button["color"], button["text"], button["pos"][0], button["pos"][1], button["size"][1], button["size"][0])

    ui_manager.show_score(screen, score)
    ui_manager.show_player_position(screen, player_x, player_y)
    ui_manager.show_cooldown_timer(screen, player_manager.cooldown_timer)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    dt = clock.tick(60) / 1000

pygame.quit()