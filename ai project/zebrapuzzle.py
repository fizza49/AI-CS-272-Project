import pygame  #for gui
from z3 import * #for solving propositional logic
import os  # For launching the main.py

# Initialize PyGame
pygame.init()

# Screen dimensions and setup
WIDTH, HEIGHT = 990, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Einstein Riddle")

# Colors
BLACK = (0, 0, 0)
LIGHT_PINK = (255, 228, 225)
WHITE = (255, 255, 255)
HEADER_COLOR = (200, 200, 255)
LINE_COLOR = (0, 0, 0)
TEXT_COLOR = (255, 20, 147)

# Font setup
FONT_SIZE = 30
FONT = pygame.font.Font(None, FONT_SIZE)

# Solver and Z3 setup
houses = 5
nationalities = ['English', 'Spaniard', 'Ukrainian', 'Japanese', 'Norwegian']
colors = ['Red', 'Green', 'Yellow', 'Blue', 'Ivory']
drinks = ['Tea', 'Coffee', 'Milk', 'OrangeJuice', 'Water']
pets = ['Dog', 'Snails', 'Fox', 'Horse', 'Zebra']
cigarettes = ['Kools', 'Chesterfields', 'Parliaments', 'LuckyStrike', 'OldGold']

nationality_vars = {name: Int(name) for name in nationalities}
color_vars = {color: Int(color) for color in colors}
drink_vars = {drink: Int(drink) for drink in drinks}
pet_vars = {pet: Int(pet) for pet in pets}
cigarette_vars = {cigarette: Int(cigarette) for cigarette in cigarettes}

solver = Solver()

# Add constraints based on the clues
for var in list(nationality_vars.values()) + list(color_vars.values()) + list(drink_vars.values()) + list(
        pet_vars.values()) + list(cigarette_vars.values()):
    solver.add(var >= 1, var <= houses)

solver.add(nationality_vars['English'] == color_vars['Red'])
solver.add(nationality_vars['Spaniard'] == pet_vars['Dog'])
solver.add(drink_vars['Coffee'] == color_vars['Green'])
solver.add(nationality_vars['Ukrainian'] == drink_vars['Tea'])
solver.add(color_vars['Green'] == color_vars['Ivory'] + 1)
solver.add(cigarette_vars['OldGold'] == pet_vars['Snails'])
solver.add(cigarette_vars['Kools'] == color_vars['Yellow'])
solver.add(drink_vars['Milk'] == 3)
solver.add(nationality_vars['Norwegian'] == 1)
solver.add(Or(cigarette_vars['Chesterfields'] == pet_vars['Fox'] - 1, cigarette_vars['Chesterfields'] == pet_vars['Fox'] + 1))
solver.add(Or(cigarette_vars['Kools'] == pet_vars['Horse'] - 1, cigarette_vars['Kools'] == pet_vars['Horse'] + 1))
solver.add(cigarette_vars['LuckyStrike'] == drink_vars['OrangeJuice'])
solver.add(nationality_vars['Japanese'] == cigarette_vars['Parliaments'])
solver.add(Or(nationality_vars['Norwegian'] == color_vars['Blue'] + 1,nationality_vars['Norwegian'] == color_vars['Blue'] - 1))

solver.add(Distinct(list(nationality_vars.values())))
solver.add(Distinct(list(color_vars.values())))
solver.add(Distinct(list(drink_vars.values())))
solver.add(Distinct(list(pet_vars.values())))
solver.add(Distinct(list(cigarette_vars.values())))

# Solve the puzzle
if solver.check() == sat:
    model = solver.model()

    table = [[] for _ in range(houses)]
    for key, var_dict in [("Nationality", nationality_vars),
                          ("Color", color_vars),
                          ("Drink", drink_vars),
                          ("Pet", pet_vars),
                          ("Cigarette", cigarette_vars)]:
        for item, var in var_dict.items():
            house = model[var].as_long() - 1
            table[house].append((key, item))


# Screens
def draw_gradient_background():
    # Function to create a vertical gradient from light pink to white
    for i in range(HEIGHT):
        # Interpolate between LIGHT_PINK and WHITE
        r = LIGHT_PINK[0] + (WHITE[0] - LIGHT_PINK[0]) * i // HEIGHT
        g = LIGHT_PINK[1] + (WHITE[1] - LIGHT_PINK[1]) * i // HEIGHT
        b = LIGHT_PINK[2] + (WHITE[2] - LIGHT_PINK[2]) * i // HEIGHT
        pygame.draw.line(screen, (r, g, b), (0, i), (WIDTH, i))


def clues_screen():
    draw_gradient_background()  # Draw the gradient background

    clues = [
        "The clues to the Riddle",
        "                        ",
        "The Englishman lives in the red house.",
        "The Spaniard owns the dog.",
        "Coffee is drunk in the green house.",
        "The Ukrainian drinks tea.",
        "The green house is immediately to the right of the ivory house.",
        "The Old Gold smoker owns snails.",
        "Kools are smoked in the yellow house.",
        "Milk is drunk in the middle house.",
        "The Norwegian lives in the first house.",
        "The man who smokes Chesterfields lives next to the man with the fox.",
        "Kools are smoked in the house next to the house where the horse is kept.",
        "The Lucky Strike smoker drinks orange juice.",
        "The Japanese smokes Parliaments.",
        "The Norwegian lives next to the blue house."
    ]

    for i, clue in enumerate(clues):
        text = FONT.render(clue, True, TEXT_COLOR)
        screen.blit(text, (50, 50 + i * 30))

    solve_button = pygame.Rect(800, 500, 120, 50)
    pygame.draw.rect(screen, TEXT_COLOR, solve_button, border_radius=25)  # Rounded Solve button

    # Center the text in the button
    solve_text = FONT.render("Solve", True, WHITE)
    text_rect = solve_text.get_rect(center=solve_button.center)
    screen.blit(solve_text, text_rect)

    pygame.display.flip()
    return solve_button


# Initialize global variables
solve_button = None
back_button = None
clock = pygame.time.Clock()


# Function to center text in a button
def render_button_with_text(rect, text, font, text_color, button_color):
    pygame.draw.rect(screen, button_color, rect, border_radius=25)
    text_surface = font.render(text, True, text_color)
    text_rect = text_surface.get_rect(center=rect.center)
    screen.blit(text_surface, text_rect)


# Define RGB colors for each house color
COLOR_RGB = {
    'Red': (255, 0, 0),
    'Green': (0, 255, 0),
    'Yellow': (255, 255, 0),
    'Blue': (0, 0, 255),
    'Ivory': (255, 255, 240)
}

# Extract house colors from the Z3 model
house_colors = [None] * houses
for color, var in color_vars.items():
    house_index = model[var].as_long() - 1
    house_colors[house_index] = COLOR_RGB[color]


# Function to render the solution table
def render_table(table, house_colors):
    x_offset = 100
    col_width = 140
    row_height = 40
    headers = ["House 1", "House 2", "House 3", "House 4", "House 5"]
    characteristics = ["Nationality", "Color", "Drink", "Pet", "Cigarette"]

    # Draw headers
    header_y_offset = 50
    pygame.draw.rect(screen, HEADER_COLOR, (x_offset, header_y_offset, col_width * 6, row_height))
    for i, header in enumerate(headers):
        text = FONT.render(header, True, BLACK)
        screen.blit(text, (x_offset + (i + 1) * col_width + 10, header_y_offset + 10))

    # Draw key column
    char_y_offset = header_y_offset + row_height
    for i, char in enumerate(characteristics):
        pygame.draw.rect(screen, HEADER_COLOR, (x_offset, char_y_offset + i * row_height, col_width, row_height))
        text = FONT.render(char, True, BLACK)
        screen.blit(text, (x_offset + 10, char_y_offset + i * row_height + 10))

    # Draw table cells
    for row in range(len(characteristics)):
        for col in range(len(headers)):
            col_color = house_colors[col] if col < len(house_colors) else WHITE
            pygame.draw.rect(screen, col_color, (
            x_offset + (col + 1) * col_width, char_y_offset + row * row_height, col_width, row_height))

            value = table[col][row][1] if len(table[col]) > row else ""
            if value:
                text = FONT.render(value, True, BLACK)
                screen.blit(text, (x_offset + (col + 1) * col_width + 10, char_y_offset + row * row_height + 10))

            pygame.draw.rect(screen, LINE_COLOR, (
            x_offset + (col + 1) * col_width, char_y_offset + row * row_height, col_width, row_height), 1)


def solution_screen():
    draw_gradient_background()  # Draw the gradient background
    render_table(table, house_colors)

    # Draw the Back to Menu button
    global back_button
    back_button = pygame.Rect((WIDTH - 200) // 2, 500, 200, 50)
    render_button_with_text(back_button, "Back to Menu", FONT, WHITE, TEXT_COLOR)

    pygame.display.flip()
    return back_button


# Main loop
running = True
current_screen = "clues"
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if current_screen == "clues":
                if solve_button.collidepoint(event.pos):
                    current_screen = "solution"  # Launch solution on clicking "solve" button
            elif current_screen == "solution":
                if back_button.collidepoint(event.pos):
                    os.system('python main.py')  # Launch main.py on clicking "Back to Menu"

    if current_screen == "clues":
        solve_button = clues_screen()
    elif current_screen == "solution":
        back_button = solution_screen()

pygame.quit()
