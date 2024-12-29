import pygame
import sys
from z3 import Real, Solver, sat

# Initialize Pygame
pygame.init()

# Define screen dimensions
screen_width = 990
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("The Inference Mystery")

# Define colors
WHITE = (255, 255, 255)
LIGHT_PINK = (255, 228, 225)  # Soft light pink for the background
TEXT_COLOR = (255, 20, 147)  # Deep pink for the text
HOVER_COLOR = (255, 105, 180)  # Hover color for the button

# Define fonts
font = pygame.font.SysFont("Comic Sans MS", 24)
heading_font = pygame.font.SysFont("Comic Sans MS", 50, bold=True)
answer_font = pygame.font.SysFont("Comic Sans MS", 20, bold=False)
input_font = pygame.font.SysFont("Comic Sans MS", 28)

# A general function to solve the riddles
def solve_riddle(constraints, variables):
    solver = Solver()
    for constraint in constraints:
        solver.add(constraint)

    if solver.check() == sat:
        solution = solver.model()
        return {str(var): solution[var].as_decimal(2) for var in variables}
    else:
        return None

# Function to solve the birthday riddle
def solve_birthday_riddle():
    # Define variables
    x = Real('x')  # Oldest child's age
    y = Real('y')  # Second child's age
    z = Real('z')  # Youngest child's age

    # Constraints based on the riddle
    constraints = [
        x + y + z == 18,  # The sum of the ages is 18
        x == z + 6,  # The oldest is 6 years older than the youngest
        y == z + 3  # The second is 3 years older than the youngest
    ]
    # Solve the riddle
    result = solve_riddle(constraints, [x, y, z])
    return result


# Function to solve the Fruit Basket Riddle
def solve_fruit_basket_riddle():
    # Let a, b, c be the number of apples, bananas, and oranges
    a = Real('a')
    b = Real('b')
    c = Real('c')
    # Constraints based on the riddle
    constraints = [
        a + b + c == 24,
        a == b + 4,
        c == 2 * a
    ]
    # Solve the riddle
    result = solve_riddle(constraints, [a, b, c])
    return result

# Function to solve the book Riddle
def book_puzzle():
    f = Real('f')
    s = Real('s')
    h = Real('h')
    # Constraints based on the riddle
    constraints = [
        s == 3 * f,
        h == f + 20,
        f + s + h == 120
    ]
    # Solve the riddle
    result = solve_riddle(constraints, [f, s, h])
    return result

# Function to solve the garden Riddle
def garden_riddle():
    # Create Z3 variables as real numbers
    tomatoes = Real('tomatoes')
    cucumbers = Real('cucumbers')
    lettuce = Real('lettuce')
    # Constraints based on the riddle
    constraints = [
        tomatoes + cucumbers + lettuce == 120,  # Total area of the garden
        tomatoes == 2 * lettuce,  # Tomatoes area is twice the lettuce area
        cucumbers == lettuce + 30  # Cucumbers area is 30 more than lettuce area
    ]
    # Solve the riddle
    result = solve_riddle(constraints, [tomatoes, cucumbers, lettuce])
    return result

# Function to solve the stamps Riddle
def stamps_riddle():
    # Create Z3 variables as real numbers
    ten_cent = Real('ten_cent')
    five_cent = Real('five_cent ')
    twenty_five_cent = Real('twenty_five_cent')
    # Constraints based on the riddle
    constraints = [
        ten_cent + five_cent + twenty_five_cent == 50,
        ten_cent == 2 * five_cent,
        twenty_five_cent == five_cent + 10
    ]
    # Solve the riddle
    result = solve_riddle(constraints, [ten_cent, five_cent, twenty_five_cent])
    return result

# Function to solve the library Riddle
def library_riddle():
    # Create Z3 variables as real numbers
    first_shelf = Real('fisrt_shelf')
    second_shelf = Real('second_shelf ')
    third_shelf = Real('third_shelf')
    # Constraints based on the riddle
    constraints = [
        first_shelf + second_shelf + third_shelf == 90,
        second_shelf == first_shelf + 10,
        third_shelf == 2 * first_shelf
    ]
    # Solve the riddle
    result = solve_riddle(constraints, [first_shelf, second_shelf, third_shelf])
    return result

# Function to solve the icecream Riddle
def ice_cream_riddle():
    # Create Z3 variables as real numbers
    vanilla = Real('vanilla')
    chocolate = Real('chocolate ')
    strawberry = Real('strawberry')
    # Constraints based on the riddle
    constraints = [
        vanilla + chocolate + strawberry == 120,
        vanilla == 2 * chocolate,
        strawberry == vanilla + 10
    ]
    # Solve the riddle
    result = solve_riddle(constraints, [vanilla, chocolate, strawberry])
    return result

# Function to solve the pile of stones Riddle
def pile_of_stones_riddle():
    # Create Z3 variables as real numbers
    pile1 = Real('pile1')
    pile2 = Real('pile2')
    pile3 = Real('pile3')

    # Constraints based on the riddle
    constraints = [
        pile1 + pile2 + pile3 == 45,
        pile2 == pile1 + 5,
        pile3 == 2 * pile1
    ]
    # Solve the riddle
    result = solve_riddle(constraints, [pile1, pile2, pile3])
    return result

# Function to solve the train station Riddle
def train_station_riddle():
    # Create Z3 variables as real numbers
    platform1 = Real('platform1')
    platform2 = Real('platform2 ')
    platform3 = Real('platform3')
    # Constraints based on the riddle
    constraints = [
        platform1 + platform2 + platform3 == 240,
        platform2 == platform1 + 50,
        platform3 == 2 * platform1
    ]
    # Solve the riddle
    result = solve_riddle(constraints, [platform1, platform2, platform3])
    return result

# Function to solve the pool Riddle
def pool_riddle():
    # Create Z3 variables as real numbers
    pool1 = Real('pool1')
    pool2 = Real('pool2')
    pool3 = Real('pool3')
    # Constraints based on the riddle
    constraints = [
        pool1 + pool2 + pool3 == 60,
        pool1 == pool2 + 10,
        pool2 == pool3 + 5
    ]
    # Solve the riddle
    result = solve_riddle(constraints, [pool1, pool2, pool3])
    return result

# Function to solve the bottle Riddle
def bottle_riddle():
    # Create Z3 variables as real numbers
    bottle1 = Real('bottle1')
    bottle2 = Real('bottle2')
    bottle3 = Real('bottle3')
    # Constraints based on the riddle
    constraints = [
        bottle1 + bottle2 + bottle3 == 75,
        bottle1 == bottle2 + 10,
        bottle2 == bottle3 + 5
    ]
    # Solve the riddle
    result = solve_riddle(constraints, [bottle1, bottle2, bottle3])
    return result

# Function to solve theater Riddle
def movie_theater_riddle():
    # Create Z3 variables as real numbers
    row1 = Real('row1')
    row2 = Real('row2 ')
    row3 = Real('row3')

    # Constraints based on the riddle
    constraints = [
        row1 + row2 + row3 == 150,
        row1 == row2 + 10,
        row2 == row3 + 5
    ]
    # Solve the riddle
    result = solve_riddle(constraints, [row1, row2, row3])
    return result

# Function to solve the building Riddle
def building_riddle():
    # Create Z3 variables as real numbers
    building1 = Real('building1')
    building2 = Real('building2 ')
    building3 = Real('building3')

    # Constraints based on the riddle
    constraints = [
        building1 + building2 + building3 == 3000,
        building2 == building1 + 500,
        building3 == building1 + 1000
    ]
    # Solve the riddle
    result = solve_riddle(constraints, [building1, building2, building3])
    return result

# Function to solve the share money Riddle
def share_riddle():
    # Create Z3 variables as real numbers
    child1 = Real('child1')
    child2 = Real('child2 ')
    child3 = Real('child3')

    # Constraints based on the riddle
    constraints = [
        child1 + child2 + child3 == 100,
        child1 == 2 * child2,
        child3 == child2 + 10
    ]
    # Solve the riddle
    result = solve_riddle(constraints, [child1, child2, child3])
    return result

# Function to solve the apples in the baskets Riddle
def apples_in_basket_riddle():
    # Create Z3 variables as real numbers
    basket1 = Real('basket1')
    basket2 = Real('basket2')
    basket3 = Real('basket3')

    # Constraints based on the riddle
    constraints = [
        basket1 + basket2 + basket3 == 60,  # Total apples constraint
        basket2 == basket1 + 10,  # Second basket relation
        basket3 == basket2 + 5  # Third basket relation
    ]
    # Solve the riddle
    result = solve_riddle(constraints, [basket1, basket2, basket3])
    return result


# Function to solve the age of daughters Riddle
def age_puzzle_riddle():
    # Create Z3 variables as real numbers
    daughter1 = Real('daughter1')
    daughter2 = Real('daughter2 ')
    daughter3 = Real('daughter3')
    # Constraints based on the riddle
    constraints = [
        daughter1 + daughter2 + daughter3 == 40,
        daughter2 == daughter1 + 5,
        daughter3 == daughter2 + 10
    ]
    # Solve the riddle
    result = solve_riddle(constraints, [daughter1, daughter2, daughter3])
    return result

# Function to solve the chocolate box Riddle
def chocolate_box_riddle():
    # Create Z3 variables as real numbers
    x1 = Real('x1')
    x2 = Real('x2 ')
    x3 = Real('x3')
    # Constraints based on the riddle
    constraints = [
        x1 == x2 + 5,
        x2 == x3 + 3,
        x1 + x2 + x3 == 45
    ]
    # Solve the riddle
    result = solve_riddle(constraints, [x1, x2, x3])
    return result

# Function to solve the penny Riddle
def penny_puzzle():
    # Create Z3 variables as real numbers
    p1 = Real('p1')
    p2 = Real('p2 ')
    p3 = Real('p3')
    # Constraints based on the riddle
    constraints = [
        p1 == p2 + 0.10,
        p2 == p3 + 0.20,
        p1 + p2 + p3 == 2.00
    ]
    # Solve the riddle
    result = solve_riddle(constraints, [p1, p2, p3])
    return result


# Define the solutions to each riddle
riddle_solvers = {
    0: solve_birthday_riddle,
    1: solve_fruit_basket_riddle,
    2: book_puzzle,
    3: garden_riddle,
    4: stamps_riddle,
    5: library_riddle,
    6: ice_cream_riddle,
    7: pile_of_stones_riddle,
    8: train_station_riddle,
    9: pool_riddle,
    10: bottle_riddle,
    11: movie_theater_riddle,
    12: building_riddle,
    13: share_riddle,
    14: apples_in_basket_riddle,
    15: age_puzzle_riddle,
    16: chocolate_box_riddle,
    17: penny_puzzle
}


# Load riddles and answers from a file
def load_riddles(filename):
    riddles = []
    try:
        with open(filename, 'r') as file:
            content = file.read().split("\n\n")  # Split each riddle by blank lines
            for riddle in content:
                parts = riddle.split("\n")
                if len(parts) >= 2:
                    title = parts[0].strip()  # First line as title
                    question = ' '.join(parts[1:]).strip()  # Rest as the question
                    riddles.append((title, question))
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
    return riddles


# Wrap text for multi-line display
def wrap_text(text, font, max_width):
    wrapped_lines = []
    words = text.split(" ")
    current_line = ""

    for word in words:
        test_line = current_line + " " + word if current_line else word
        test_width = font.size(test_line)[0]

        if test_width <= max_width:
            current_line = test_line
        else:
            if current_line:
                wrapped_lines.append(current_line)
            current_line = word

    if current_line:
        wrapped_lines.append(current_line)

    return wrapped_lines

# Drawing the flashcards
def draw_flashcard(title, text, is_flipped, max_width, answer=None):
    screen.fill(LIGHT_PINK)

    # Display the heading (bold and above the white box)
    heading_surface = heading_font.render(title, True, TEXT_COLOR)
    heading_rect = heading_surface.get_rect(center=(screen_width // 2, 60))
    screen.blit(heading_surface, heading_rect)

    # Draw flashcard background
    pygame.draw.rect(screen, WHITE, (100, 120, screen_width - 200, screen_height - 220), border_radius=10)

    y_offset = 160  # Start the text inside the box

    if is_flipped:
        # Display only the answer heading after flip, using smaller font
        answer_heading = "Answer:"
        answer_heading_surface = answer_font.render(answer_heading, True, TEXT_COLOR)
        answer_heading_rect = answer_heading_surface.get_rect(center=(screen_width // 2, y_offset))
        screen.blit(answer_heading_surface, answer_heading_rect)

        # Display the answer if available
        if answer:
            answer_surface = answer_font.render(str(answer), True, TEXT_COLOR)
            answer_rect = answer_surface.get_rect(center=(screen_width // 2, y_offset + 40))
            screen.blit(answer_surface, answer_rect)
    else:
        # Display the riddle before flipping
        riddle_lines = wrap_text(text, font, max_width)
        for i, line in enumerate(riddle_lines):
            text_surface = font.render(line, True, TEXT_COLOR)
            text_rect = text_surface.get_rect(topleft=(120, y_offset + i * 40))
            screen.blit(text_surface, text_rect)

# function to draw the buttons
def draw_button(screen, rect, text, font, text_color, button_color, border_radius=10):
    # Draw the button rectangle
    pygame.draw.rect(screen, button_color, rect, border_radius=border_radius)
    # Render the text
    text_surface = font.render(text, True, text_color)
    # Center the text on the button
    text_position = (
        rect.centerx - text_surface.get_width() // 2,
        rect.centery - text_surface.get_height() // 2
    )
    screen.blit(text_surface, text_position)

 # Draws the navigation buttons ("Next", "Previous", and "Main Menu") on the screen.
def draw_navigation_buttons():
    # Define button rectangles
    next_button_rect = pygame.Rect(screen_width // 2 + 110, screen_height - 80, 150, 50)
    prev_button_rect = pygame.Rect(screen_width // 2 - 260, screen_height - 80, 150, 50)
    menu_button_rect = pygame.Rect(screen_width // 2 - 75, screen_height - 80, 150, 50)  # Main Menu Button

    # Draw buttons 
    draw_button(screen, next_button_rect, "Next", input_font, WHITE, TEXT_COLOR)
    draw_button(screen, prev_button_rect, "Previous", input_font, WHITE, TEXT_COLOR)
    draw_button(screen, menu_button_rect, "Main Menu", input_font, WHITE, TEXT_COLOR)

    # Return button rectangles for event handling
    return prev_button_rect, next_button_rect, menu_button_rect

# main function
def main():
    riddles = load_riddles('riddles.txt')  # Loading riddles from the file
    if not riddles:
        print("No riddles loaded. Exiting...")  # if riddles not displayed quit
        pygame.quit()
        sys.exit()

    current_riddle = 0
    is_flipped = False  
    answer = None

    while True:
        screen.fill(WHITE)  # Clear the screen
        title, riddle = riddles[current_riddle]

        if is_flipped and current_riddle in riddle_solvers:
            answer = riddle_solvers[current_riddle]()

        draw_flashcard(title, riddle, is_flipped, screen_width - 240, answer)

        # Call draw_navigation_buttons once 
        prev_button_rect, next_button_rect, menu_button_rect = draw_navigation_buttons()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                # Check for Main Menu button click
                if menu_button_rect.collidepoint(mouse_pos):
                    return  # Exit to main menu

                # Check for navigation buttons
                elif next_button_rect.collidepoint(mouse_pos):
                    current_riddle = (current_riddle + 1) % len(riddles)
                    is_flipped = False
                elif prev_button_rect.collidepoint(mouse_pos):
                    current_riddle = (current_riddle - 1) % len(riddles)
                    is_flipped = False
                else:
                    # Flip the card
                    is_flipped = not is_flipped

        pygame.display.flip()


# Run the main game loop
if __name__ == "__main__":
    main()

