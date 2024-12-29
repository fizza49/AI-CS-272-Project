import pygame
from fractions import Fraction
import sys

# Function to resolve different sequences
def resolve_sequence(sequence):
    n = len(sequence)

    # Resolve Arithmetic Sequence
    arithmetic_diff = sequence[1] - sequence[0]
    if all(sequence[i] - sequence[i - 1] == arithmetic_diff for i in range(2, n)):
        return "Arithmetic Sequence", sequence[-1] + arithmetic_diff

    # Resolve Geometric Sequence
    if sequence[0] != 0:
        geometric_ratio = sequence[1] / sequence[0]
        if all(sequence[i] / sequence[i - 1] == geometric_ratio for i in range(2, n)):
            return "Geometric Sequence", sequence[-1] * geometric_ratio

    # Resolve Harmonic Sequence
    if 0 not in sequence:  # Ensure no zeroes in the sequence
        reciprocals = [1 / x for x in sequence]
        harmonic_diff = reciprocals[1] - reciprocals[0]
        if all(reciprocals[i] - reciprocals[i - 1] == harmonic_diff for i in range(2, n)):
            next_reciprocal = reciprocals[-1] + harmonic_diff
            return "Harmonic Sequence", 1 / next_reciprocal

    # Resolve Fibonacci Sequence
    if n >= 3 and all(sequence[i] == sequence[i - 1] + sequence[i - 2] for i in range(2, n)):
        return "Fibonacci Sequence", sequence[-1] + sequence[-2]
    

    return None, None


# Function to parse input string with fractions
def parse_input(input_string):
    try:
        return [float(Fraction(item)) for item in input_string.split()]
    except:
        return None


# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 990, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sequence Solver with Resolution Algorithm")

# Colors and Fonts
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_PINK = (255, 228, 225)
TEXT_COLOR = (255, 20, 147)  # Deep pink for the text
FONT = pygame.font.SysFont("Comic Sans MS", 30)
BUTTON_FONT = pygame.font.Font(None, 30)

# Input box settings
input_box = pygame.Rect((WIDTH - 600) // 2, 250, 600, 60)

# Button settings (aligned horizontally with padding)
button_width = 200
button_height = 60
padding = 20  # Padding between buttons

# Calculate total width of buttons plus padding
total_buttons_width = 3 * button_width + 2 * padding  # 2 gaps for 3 buttons

# Center align buttons considering padding
buttons_x = (WIDTH - total_buttons_width) // 2

submit_button = pygame.Rect(buttons_x, 350, button_width, button_height)
main_menu_button = pygame.Rect(buttons_x + button_width + padding, 350, button_width, button_height)
retry_button = pygame.Rect(buttons_x + 2 * (button_width + padding), 350, button_width, button_height)

text = ''
sequence_result = ''
next_number = ''


def draw_buttons():
    # Draw Submit Button
    pygame.draw.rect(screen, TEXT_COLOR, submit_button, border_radius=10)
    submit_text = BUTTON_FONT.render("Submit", True, WHITE)
    screen.blit(submit_text, (
        submit_button.centerx - submit_text.get_width() // 2,
        submit_button.centery - submit_text.get_height() // 2
    ))

    # Draw Main Menu Button
    pygame.draw.rect(screen, TEXT_COLOR, main_menu_button, border_radius=10)
    menu_text = BUTTON_FONT.render("Main Menu", True, WHITE)
    screen.blit(menu_text, (
        main_menu_button.centerx - menu_text.get_width() // 2,
        main_menu_button.centery - menu_text.get_height() // 2
    ))

    # Draw Retry Button
    pygame.draw.rect(screen, TEXT_COLOR, retry_button, border_radius=10)
    retry_text = BUTTON_FONT.render("Retry", True, WHITE)
    screen.blit(retry_text, (
        retry_button.centerx - retry_text.get_width() // 2,
        retry_button.centery - retry_text.get_height() // 2
    ))

def display_popup_message(message):
    """Display a pop-up message on the screen."""
    popup_width, popup_height = 500, 200
    popup_rect = pygame.Rect(
        (WIDTH - popup_width) // 2, (HEIGHT - popup_height) // 2, popup_width, popup_height
    )

    # Semi-transparent background overlay
    overlay = pygame.Surface((WIDTH, HEIGHT))
    overlay.set_alpha(128)  # Set transparency
    overlay.fill(BLACK)
    screen.blit(overlay, (0, 0))

    # Popup box
    pygame.draw.rect(screen, WHITE, popup_rect, border_radius=10)
    pygame.draw.rect(screen, TEXT_COLOR, popup_rect, 5, border_radius=10)

    # Render message text
    message_lines = message.split("\n")  # Split by lines for multi-line messages
    y_offset = popup_rect.top + 30
    for line in message_lines:
        text_surface = FONT.render(line, True, TEXT_COLOR)
        screen.blit(
            text_surface,
            (popup_rect.centerx - text_surface.get_width() // 2, y_offset)
        )
        y_offset += 40  # Line spacing

    # OK button
    ok_button = pygame.Rect(
        popup_rect.centerx - 50, popup_rect.bottom - 60, 100, 40
    )
    pygame.draw.rect(screen, TEXT_COLOR, ok_button, border_radius=10)
    ok_text = BUTTON_FONT.render("OK", True, WHITE)
    screen.blit(ok_text, ok_text.get_rect(center=ok_button.center))

    pygame.display.flip()

    # Wait for user to acknowledge the popup
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if ok_button.collidepoint(event.pos):
                    return  # Close the popup


def main():
    global text, sequence_result, next_number
    running = True

    while running:
        screen.fill(LIGHT_PINK)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode
            if event.type == pygame.MOUSEBUTTONDOWN:
                if submit_button.collidepoint(event.pos):
                    # Parse and resolve the sequence
                    sequence = parse_input(text)
                    if sequence and len(sequence) >= 3:
                        result, number = resolve_sequence(sequence)
                        if result:
                            sequence_result = f"Type: {result}"
                            next_number = f"Next Number: {number}"
                        else:
                            display_popup_message("No recognizable pattern\nPlease try again.")
                            sequence_result = ''
                            next_number = ''
                    else:
                        display_popup_message("Invalid input or too few numbers...\nEnter at least three numbers.")
                        sequence_result = ''
                        next_number = ''

                elif main_menu_button.collidepoint(event.pos):
                    return  # Exit to the main menu

                elif retry_button.collidepoint(event.pos):
                    # Reset the sequence result and input text
                    text = ''
                    sequence_result = ''
                    next_number = ''

        # Render input box and text
        pygame.draw.rect(screen, WHITE, input_box, border_radius=10)
        pygame.draw.rect(screen, TEXT_COLOR, input_box, 3, border_radius=10)
        txt_surface = FONT.render(text, True, TEXT_COLOR)
        screen.blit(txt_surface, (input_box.x + 10, input_box.y + 15))

        # Render Submit Button
        pygame.draw.rect(screen, TEXT_COLOR, submit_button, border_radius=10)
        submit_text = BUTTON_FONT.render("Submit", True, WHITE)
        screen.blit(submit_text, submit_text.get_rect(center=submit_button.center))

        # Display Results
        result_surface = BUTTON_FONT.render(sequence_result, True, TEXT_COLOR)
        next_surface = BUTTON_FONT.render(next_number, True, TEXT_COLOR)
        screen.blit(result_surface, (WIDTH // 2 - 300, 450))
        screen.blit(next_surface, (WIDTH // 2 - 300, 500))

        # Instructions
        instructions = FONT.render("Enter numbers (fractions allowed) separated by spaces:", True, TEXT_COLOR)
        screen.blit(instructions, ((WIDTH - instructions.get_width()) // 2, 200))
        # Draw buttons
        draw_buttons()

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
