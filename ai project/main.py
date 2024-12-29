import pygame
import sys
import time
import os

# Initialize Pygame
pygame.init()

# Define screen dimensions
screen_width = 990
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Inference Riddle Solver")

# Define colors
WHITE = (255, 255, 255)
LIGHT_PINK = (255, 228, 225)  # Soft light pink for the background
PALE_PINK = (255, 182, 193)   # Lighter pink for the loading bar
TEXT_COLOR = (255, 20, 147)   # Deep pink for the text

# Define fonts
font = pygame.font.SysFont("Comic Sans MS", 50)  # Slightly smaller text size
input_font = pygame.font.SysFont("Comic Sans MS", 40)

# Define text
title_text = font.render("Inference Based Riddle Solver ", True, TEXT_COLOR)
start_text = font.render("Start", True, WHITE)  # White color for the start text

# Function to draw the title screen with the start button
def draw_title_screen():
    # Fill the screen with a light pink gradient background
    for y in range(screen_height):
        r = (LIGHT_PINK[0] * (screen_height - y) + WHITE[0] * y) // screen_height
        g = (LIGHT_PINK[1] * (screen_height - y) + WHITE[1] * y) // screen_height
        b = (LIGHT_PINK[2] * (screen_height - y) + WHITE[2] * y) // screen_height
        pygame.draw.line(screen, (r, g, b), (0, y), (screen_width, y))

    # Draw the title text in the center of the screen
    title_rect = title_text.get_rect(center=(screen_width // 2, screen_height // 3))
    screen.blit(title_text, title_rect)

    # Draw the start button
    button_width, button_height = start_text.get_size()
    start_button_rect = pygame.Rect(screen_width // 2 - button_width // 2, screen_height // 2 + 100, button_width + 20, button_height + 10)
    pygame.draw.rect(screen, TEXT_COLOR, start_button_rect, border_radius=10)
    screen.blit(start_text, (start_button_rect.centerx - button_width // 2, start_button_rect.centery - button_height // 2))

    return start_button_rect

# Function to draw the loading bar screen
def draw_loading_screen(progress):
    # Fill the screen with a light pink gradient background
    for y in range(screen_height):
        r = (LIGHT_PINK[0] * (screen_height - y) + WHITE[0] * y) // screen_height
        g = (LIGHT_PINK[1] * (screen_height - y) + WHITE[1] * y) // screen_height
        b = (LIGHT_PINK[2] * (screen_height - y) + WHITE[2] * y) // screen_height
        pygame.draw.line(screen, (r, g, b), (0, y), (screen_width, y))

    # Draw the title text in the center of the screen
    title_rect = title_text.get_rect(center=(screen_width // 2, screen_height // 3))
    screen.blit(title_text, title_rect)

    # Draw the loading bar
    bar_width = 600
    bar_height = 40
    bar_x = (screen_width - bar_width) // 2
    bar_y = screen_height // 2 + 100
    pygame.draw.rect(screen, PALE_PINK, (bar_x, bar_y, bar_width, bar_height), 5)  # Border
    pygame.draw.rect(screen, TEXT_COLOR, (bar_x, bar_y, progress * bar_width, bar_height))  # Progress fill

    # Draw progress text
    progress_text = input_font.render(f"{int(progress * 100)}%", True, TEXT_COLOR)
    screen.blit(progress_text, (screen_width // 2 - progress_text.get_width() // 2, bar_y + (bar_height - progress_text.get_height()) // 2))


def draw_game_selection_screen():
    running = True
    while running:
        screen.fill(WHITE)  # Clear the screen
        draw_game_selection_screen_logic()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check which button was clicked
                if game1_button_rect.collidepoint(event.pos):
                    open_file("newsequence.py")  # Open the new game file
                    return  # Exit the function
                elif game2_button_rect.collidepoint(event.pos):
                    open_file("zebrapuzzle.py")
                    return
                elif game3_button_rect.collidepoint(event.pos):
                    open_file("inferencemystery.py")
                    return
                elif game4_button_rect.collidepoint(event.pos):
                    open_file("brainquest.py")
                    return
                elif game5_button_rect.collidepoint(event.pos):
                    open_file("resolution.py")
                    return

        pygame.display.update()  # Update the display

# Function to draw the game selection screen logic
def draw_game_selection_screen_logic():
    # Fill the screen with a light pink gradient background
    for y in range(screen_height):
        r = (LIGHT_PINK[0] * (screen_height - y) + WHITE[0] * y) // screen_height
        g = (LIGHT_PINK[1] * (screen_height - y) + WHITE[1] * y) // screen_height
        b = (LIGHT_PINK[2] * (screen_height - y) + WHITE[2] * y) // screen_height
        pygame.draw.line(screen, (r, g, b), (0, y), (screen_width, y))

    # Draw the title text
    title_text = font.render("Select a Riddle", True, TEXT_COLOR)
    title_rect = title_text.get_rect(center=(screen_width // 2, screen_height // 5))
    screen.blit(title_text, title_rect)

    # Draw Riddle 1 Button
    pygame.draw.rect(screen, TEXT_COLOR, game1_button_rect, border_radius=10)
    game1_text = input_font.render("Sequence Solver", True, WHITE)
    screen.blit(game1_text, game1_text.get_rect(center=game1_button_rect.center))

    # Draw Riddle 2 Button
    pygame.draw.rect(screen, TEXT_COLOR, game2_button_rect, border_radius=10)
    game2_text = input_font.render("Einstein Riddle", True, WHITE)
    screen.blit(game2_text, game2_text.get_rect(center=game2_button_rect.center))

    # Draw Riddle 3 Button
    pygame.draw.rect(screen, TEXT_COLOR, game3_button_rect, border_radius=10)
    game3_text = input_font.render("Inference Mystery", True, WHITE)
    screen.blit(game3_text, game3_text.get_rect(center=game3_button_rect.center))

    # Draw Riddle 4 Button
    pygame.draw.rect(screen, TEXT_COLOR, game4_button_rect, border_radius=10)
    game4_text = input_font.render("Brain Quest", True, WHITE)
    screen.blit(game4_text, game4_text.get_rect(center=game4_button_rect.center))

    # Draw Riddle 5 Button
    pygame.draw.rect(screen, TEXT_COLOR, game5_button_rect, border_radius=10)
    game5_text = input_font.render("Resolution", True, WHITE)
    screen.blit(game5_text, game5_text.get_rect(center=game5_button_rect.center))

# Define button dimensions and positions for the game selection screen
button_width = 400
button_height = 50
button_spacing = 30

game1_button_rect = pygame.Rect((screen_width - button_width) // 2, screen_height // 3, button_width, button_height)
game2_button_rect = pygame.Rect((screen_width - button_width) // 2, screen_height // 3 + button_height + button_spacing, button_width, button_height)
game3_button_rect = pygame.Rect((screen_width - button_width) // 2, screen_height // 3 + 2 * (button_height + button_spacing), button_width, button_height)
game4_button_rect = pygame.Rect((screen_width - button_width) // 2, screen_height // 3 + 3 * (button_height + button_spacing), button_width, button_height)
game5_button_rect = pygame.Rect((screen_width - button_width) // 2, screen_height // 3 + 4 * (button_height + button_spacing), button_width, button_height)


# Main loop for the title screen
def main():
    running = True
    progress = 0  # Progress starts at 0
    loading = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check if the start button is clicked
                if start_button_rect.collidepoint(event.pos):
                    loading = True  # Start loading animation

        screen.fill(WHITE)  # Clear the screen

        if not loading:
            # Draw the title screen with start button
            start_button_rect = draw_title_screen()
        else:
            # Draw the loading bar screen
            draw_loading_screen(progress)
            progress += 0.005  # Increase the progress
            if progress >= 1:
                time.sleep(1)  # Show completed loading status
                loading = False  # Move to game selection page
                draw_game_selection_screen()  # Display game selection screen

        pygame.display.update()  # Update the display
        time.sleep(0.01)  # Small delay for smoother animation

    pygame.quit()
    sys.exit()

def open_file(file_name):
    """Open the specified Python file."""
    try:
        os.system(f"python {file_name}")
    except Exception as e:
        print(f"Error opening {file_name}: {e}")

if __name__ == "__main__":
    main()
