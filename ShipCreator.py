# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()

screen_x = 1280
screen_y = 720

screen = pygame.display.set_mode((screen_x, screen_y))
clock = pygame.time.Clock()
running = True
dt = 0

color = (255,0,0)

player_x = screen.get_width() / 2
player_y = screen.get_height() - 75
player_width = 40
player_height = 60 

player_pos = pygame.Vector2(player_x, player_y)

def draw_grid(grid_size: int, grid_square_size: int, grid_gap: int, square_color: str, border_thickness: int, border_color: str, line_thickness: int, line_color: str):
    start_x = (screen_x - grid_square_size * grid_size) // 2
    start_y = (screen_y - grid_square_size * grid_size) // 2
    
    for i in range(grid_size):
        for j in range(grid_size):
            rect_x = start_x + i * (grid_square_size + grid_gap)
            rect_y = start_y + j * (grid_square_size + grid_gap)
            
            pygame.draw.rect(screen, square_color, pygame.Rect(rect_x, rect_y, grid_square_size, grid_square_size))
            
            if (border_thickness > 0):
                pygame.draw.rect(screen, border_color, pygame.Rect(rect_x, rect_y, grid_square_size, grid_square_size), border_thickness)
                
    for j in range(grid_size + 1):  # +1 to draw the bottom line
        line_y = start_y + j * (grid_square_size + grid_gap)
        pygame.draw.rect(screen, line_color, pygame.Rect(start_x - grid_gap, line_y - grid_gap, (grid_square_size + grid_gap) * grid_size + grid_gap + line_thickness, line_thickness + grid_gap))

    # Draw vertical lines
    for i in range(grid_size + 1):  # +1 to draw the right line
        line_x = start_x + i * (grid_square_size + grid_gap)
        pygame.draw.rect(screen, line_color, pygame.Rect(line_x - grid_gap, start_y - grid_gap, line_thickness + grid_gap, (grid_square_size + grid_gap) * grid_size + grid_gap + line_thickness))


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")
        
    draw_grid(11, 30, 1, "white", 1, "red", 1, "green")
        
    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()