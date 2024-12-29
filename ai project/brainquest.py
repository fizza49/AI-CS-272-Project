import pygame
from itertools import permutations
import sys

# Initialize Pygame
pygame.init()

# Define screen dimensions
screen_width = 990
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("The Brain Quest")

# Define colors
WHITE = (255, 255, 255)
LIGHT_PINK = (255, 228, 225)  # Soft light pink for the background
TEXT_COLOR = (255, 20, 147)  # Deep pink for the text
HOVER_COLOR = (255, 105, 180)  # Hover color for the button

# Define fonts
font = pygame.font.SysFont("Comic Sans MS", 24)
heading_font = pygame.font.SysFont("Comic Sans MS", 50, bold=True)  # Larger font for the heading
answer_font = pygame.font.SysFont("Comic Sans MS", 20, bold=False)  # Smaller font for the answer heading
input_font = pygame.font.SysFont("Comic Sans MS", 28)


# Function to draw text on screen
def draw_text(text, font, color, x, y, max_width=780):
    words = text.split(' ')
    lines = []
    current_line = ""
    for word in words:
        if font.size(current_line + word)[0] <= max_width:
            current_line += word + ' '
        else:
            lines.append(current_line)
            current_line = word + ' '
    lines.append(current_line)

    for idx, line in enumerate(lines):
        label = font.render(line, True, color)
        screen.blit(label, (x, y + idx * 40))


# RiddleSolver class
class RiddleSolver:
    def __init__(self, entities, positions):
        self.entities = entities
        self.positions = positions
        self.constraints = []
        self.translations = []

    def add_constraint(self, constraint_func, description):
        #Add a constraint function with its symbolic logic description.
        self.constraints.append(constraint_func)
        self.translations.append(description)

    def show_translations(self):
        return self.translations

    def solve(self):
        possible_arrangements = permutations(self.entities)
        valid_arrangements = []

        for arrangement in possible_arrangements:
            if all(constraint(arrangement) for constraint in self.constraints):
                valid_arrangements.append(arrangement)

        return valid_arrangements


# Constraint functions for the riddles
def not_next_to(entity1, entity2):
 #first object is not next to the second object
    def constraint(arrangement):
        idx1 = arrangement.index(entity1)
        idx2 = arrangement.index(entity2)
        return abs(idx1 - idx2) != 1

    return constraint

def left_of(entity1, entity2):
   #first object is to the left of second object
    def constraint(arrangement):
        idx1 = arrangement.index(entity1)
        idx2 = arrangement.index(entity2)
        return idx1 < idx2

    return constraint

def is_in_position(entity, position):

    def constraint(arrangement):
        return arrangement[position - 1] == entity

    return constraint


# Order of the Books Riddle
def solve_order_of_books_riddle():
    entities = ["Math", "Science", "History"]
    positions = [1, 2, 3]

    solver = RiddleSolver(entities, positions)

    # adding constraints 
    solver.add_constraint(
        left_of("Math", "Science"),
        "Math book is not on the far left => (Pos(Math) ≠ 1)"
    )

    solver.add_constraint(
        not_next_to("Math", "History"),
        "History book is not next to the Math book => ¬(NextTo(Math, History))"
    )

    solver.add_constraint(
        is_in_position("Science", 2),
        "Science book is in the middle => (Pos(Science) = 2)"
    )

    translations = solver.show_translations()
    solutions = solver.solve()

    return translations, solutions


# Who is in the Middle Riddle
def solve_who_is_in_the_middle_riddle():
    entities = ["Alice", "Bob", "Carol"]  
    positions = [1, 2, 3]  

    solver = RiddleSolver(entities, positions)

    #  adding constraints
    solver.add_constraint(
        not_next_to("Alice", "Bob"),
        "¬(NextTo(Alice, Bob)) => ¬(|Pos(Alice) - Pos(Bob)| = 1)"
    )

    solver.add_constraint(
        left_of("Bob", "Carol"),
        "Pos(Bob) < Pos(Carol)"
    )

    solver.add_constraint(
        is_in_position("Carol", 2),
        "Pos(Carol) = 2"
    )

    translations = solver.show_translations()
    solutions = solver.solve()

    return translations, solutions


#  Order of Fruits Riddle
def solve_order_of_fruits_riddle():
    entities = ["Apple", "Banana", "Cherry"]
    positions = [1, 2, 3]

    solver = RiddleSolver(entities, positions)

    #adding constarints 
    solver.add_constraint(
        not_next_to("Apple", "Banana"),
        "Apple is not next to Banana => ¬(NextTo(Apple, Banana))"
    )
    solver.add_constraint(
        left_of("Banana", "Cherry"),
        "Banana is to the left of Cherry => (Pos(Banana) < Pos(Cherry))"
    )
    solver.add_constraint(
        is_in_position("Cherry", 2),
        "Cherry is in the middle => (Pos(Cherry) = 2)"
    )
    translations = solver.show_translations()
    solutions = solver.solve()
    return translations, solutions


# Seating Arrangement Riddle
def solve_seating_arrangement_riddle():
    entities = ["Alice", "Bob", "Carol", "Dave"]
    positions = [1, 2, 3, 4]

    solver = RiddleSolver(entities, positions)
    #adidng constarints 
    solver.add_constraint(
        not_next_to("Alice", "Bob"),
        "Alice is not sitting next to Bob => ¬(NextTo(Alice, Bob))"
    )
    solver.add_constraint(
        left_of("Carol", "Bob"),
        "Carol is sitting to the left of Bob => (Pos(Carol) < Pos(Bob))"
    )
    solver.add_constraint(
        is_in_position("Dave", 4),
        "Dave is sitting at the end => (Pos(Dave) = 4)"
    )
    translations = solver.show_translations()
    solutions = solver.solve()
    return translations, solutions


# Classroom Arrangement Riddle
def solve_classroom_arrangement_riddle():
    entities = ["Student A", "Student B", "Student C", "Student D"]
    positions = [1, 2, 3, 4]

    solver = RiddleSolver(entities, positions)
    solver.add_constraint(
        not_next_to("Student A", "Student B"),
        "Student A is not sitting next to Student B => ¬(NextTo(Student A, Student B))"
    )
    solver.add_constraint(
        is_in_position("Student C", 2),
        "Student C is sitting in the middle => (Pos(Student C) = 2)"
    )
    solver.add_constraint(
        is_in_position("Student D", 4),
        "Student D is sitting at the end => (Pos(Student D) = 4)"
    )
    translations = solver.show_translations()
    solutions = solver.solve()
    return translations, solutions


#  Day of the Week Riddle
def solve_day_of_week_riddle():
    entities = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    positions = [1, 2, 3, 4, 5]

    solver = RiddleSolver(entities, positions)
    solver.add_constraint(
        left_of("Monday", "Wednesday"),
        "Monday is to the left of Wednesday => (Pos(Monday) < Pos(Wednesday))"
    )
    solver.add_constraint(
        not_next_to("Wednesday", "Friday"),
        "Wednesday is not next to Friday => ¬(NextTo(Wednesday, Friday))"
    )
    solver.add_constraint(
        is_in_position("Friday", 5),
        "Friday is in the last position => (Pos(Friday) = 5)"
    )
    translations = solver.show_translations()
    solutions = solver.solve()
    return translations, solutions


#  Office Desk Arrangement Riddle
def solve_office_desk_riddle():
    entities = ["Alice", "Bob", "Charlie", "David"]
    positions = [1, 2, 3, 4]

    solver = RiddleSolver(entities, positions)
    solver.add_constraint(
        not_next_to("Alice", "Bob"),
        "Alice is not next to Bob => ¬(NextTo(Alice, Bob))"
    )
    solver.add_constraint(
        left_of("Charlie", "David"),
        "Charlie is sitting to the left of David => (Pos(Charlie) < Pos(David))"
    )
    solver.add_constraint(
        is_in_position("Alice", 1),
        "Alice is sitting at the leftmost desk => (Pos(Alice) = 1)"
    )
    translations = solver.show_translations()
    solutions = solver.solve()
    return translations, solutions


# Party Seating Riddle
def solve_party_seating_riddle():
    entities = ["Emily", "Frank", "Grace", "Hannah"]
    positions = [1, 2, 3, 4]

    solver = RiddleSolver(entities, positions)
    solver.add_constraint(
        not_next_to("Emily", "Grace"),
        "Emily is not sitting next to Grace => ¬(NextTo(Emily, Grace))"
    )
    solver.add_constraint(
        left_of("Frank", "Hannah"),
        "Frank is sitting to the left of Hannah => (Pos(Frank) < Pos(Hannah))"
    )
    solver.add_constraint(
        is_in_position("Grace", 4),
        "Grace is sitting at the rightmost position => (Pos(Grace) = 4)"
    )
    translations = solver.show_translations()
    solutions = solver.solve()
    return translations, solutions


#  Box Arrangement Riddle
def solve_box_arrangement_riddle():
    entities = ["Box A", "Box B", "Box C"]
    positions = [1, 2, 3]

    solver = RiddleSolver(entities, positions)
    solver.add_constraint(
        not_next_to("Box A", "Box B"),
        "Box A is not next to Box B => ¬(NextTo(Box A, Box B))"
    )
    solver.add_constraint(
        left_of("Box B", "Box C"),
        "Box B is to the left of Box C => (Pos(Box B) < Pos(Box C))"
    )
    solver.add_constraint(
        is_in_position("Box C", 3),
        "Box C is in the last position => (Pos(Box C) = 3)"
    )
    translations = solver.show_translations()
    solutions = solver.solve()
    return translations, solutions


# Tea or Coffee Riddle
def solve_tea_or_coffee_riddle():
    entities = ["Tea", "Coffee", "Juice"]
    positions = [1, 2, 3]

    solver = RiddleSolver(entities, positions)
    solver.add_constraint(
        left_of("Tea", "Coffee"),
        "Tea is to the left of Coffee => (Pos(Tea) < Pos(Coffee))"
    )
    solver.add_constraint(
        not_next_to("Tea", "Juice"),
        "Tea is not next to Juice => ¬(NextTo(Tea, Juice))"
    )
    solver.add_constraint(
        is_in_position("Juice", 3),
        "Juice is in the last position => (Pos(Juice) = 3)"
    )
    translations = solver.show_translations()
    solutions = solver.solve()
    return translations, solutions


#  Card Suit Riddle
def solve_card_suit_riddle():
    entities = ["Hearts", "Clubs", "Diamonds", "Spades"]
    positions = [1, 2, 3, 4]

    solver = RiddleSolver(entities, positions)
    solver.add_constraint(
        left_of("Clubs", "Spades"),
        "Clubs is to the left of Spades => (Pos(Clubs) < Pos(Spades))"
    )
    solver.add_constraint(
        not_next_to("Diamonds", "Spades"),
        "Diamonds is not next to Spades => ¬(NextTo(Diamonds, Spades))"
    )
    solver.add_constraint(
        is_in_position("Hearts", 1),
        "Hearts is in the first position => (Pos(Hearts) = 1)"
    )
    translations = solver.show_translations()
    solutions = solver.solve()
    return translations, solutions


#  Book Collection Riddle
def solve_book_collection_riddle():
    entities = ["Book 1", "Book 2", "Book 3", "Book 4"]
    positions = [1, 2, 3, 4]

    solver = RiddleSolver(entities, positions)
    solver.add_constraint(
        left_of("Book 2", "Book 3"),
        "Book 2 is to the left of Book 3 => (Pos(Book 2) < Pos(Book 3))"
    )
    solver.add_constraint(
        not_next_to("Book 1", "Book 4"),
        "Book 1 is not next to Book 4 => ¬(NextTo(Book 1, Book 4))"
    )
    solver.add_constraint(
        is_in_position("Book 4", 4),
        "Book 4 is in the last position => (Pos(Book 4) = 4)"
    )
    translations = solver.show_translations()
    solutions = solver.solve()
    return translations, solutions


#  Fruit Salad Riddle
def solve_fruit_salad_riddle():
    entities = ["Apple", "Banana", "Orange"]
    positions = [1, 2, 3]

    solver = RiddleSolver(entities, positions)
    solver.add_constraint(
        left_of("Apple", "Banana"),
        "Apple is to the left of Banana => (Pos(Apple) < Pos(Banana))"
    )
    solver.add_constraint(
        not_next_to("Banana", "Orange"),
        "Banana is not next to Orange => ¬(NextTo(Banana, Orange))"
    )
    solver.add_constraint(
        is_in_position("Orange", 3),
        "Orange is in the last position => (Pos(Orange) = 3)"
    )
    translations = solver.show_translations()
    solutions = solver.solve()
    return translations, solutions


#  Animal Placement Riddle
def solve_animal_placement_riddle():
    entities = ["Cat", "Dog", "Rabbit"]
    positions = [1, 2, 3]

    solver = RiddleSolver(entities, positions)
    solver.add_constraint(
        left_of("Cat", "Rabbit"),
        "Cat is to the left of Rabbit => (Pos(Cat) < Pos(Rabbit))"
    )
    solver.add_constraint(
        not_next_to("Rabbit", "Dog"),
        "Rabbit is not next to Dog => ¬(NextTo(Rabbit, Dog))"
    )
    solver.add_constraint(
        is_in_position("Dog", 1),
        "Dog is in the first position => (Pos(Dog) = 1)"
    )
    translations = solver.show_translations()
    solutions = solver.solve()
    return translations, solutions


#  Meeting Room Riddle
def solve_meeting_room_riddle():
    entities = ["Room A", "Room B", "Room C", "Room D"]
    positions = [1, 2, 3, 4]

    solver = RiddleSolver(entities, positions)
    solver.add_constraint(
        left_of("Room B", "Room C"),
        "Room B is to the left of Room C => (Pos(Room B) < Pos(Room C))"
    )
    solver.add_constraint(
        not_next_to("Room A", "Room D"),
        "Room A is not next to Room D => ¬(NextTo(Room A, Room D))"
    )
    solver.add_constraint(
        is_in_position("Room A", 1),
        "Room A is in the first position => (Pos(Room A) = 1)"
    )
    translations = solver.show_translations()
    solutions = solver.solve()
    return translations, solutions


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

# function to draw the flash cards
def draw_flashcard(title, text, is_flipped, max_width, answer=None, translations=None):
    screen.fill(LIGHT_PINK)

    # Display the heading 
    heading_surface = heading_font.render(title, True, TEXT_COLOR)
    heading_rect = heading_surface.get_rect(center=(screen_width // 2, 60))
    screen.blit(heading_surface, heading_rect)

    # Draw flashcard background
    pygame.draw.rect(screen, WHITE, (100, 120, screen_width - 200, screen_height - 220), border_radius=10)

    y_offset = 160  # Start the text inside the box

    if is_flipped:
        # Display symbolic logic translations (constraints) when flipped
        if translations:
            for translation in translations:
                # Wrap each constraint to ensure it fits within the card's width
                translation_lines = wrap_text(translation, font, max_width)
                for i, line in enumerate(translation_lines):
                    translation_surface = font.render(line, True, TEXT_COLOR)
                    screen.blit(translation_surface, (120, y_offset + i * 40))
                    y_offset += translation_surface.get_height()  # Move down for the next line

        # Display the answer below the constraints
        if answer:
            answer_heading = "Answer:"
            answer_heading_surface = answer_font.render(answer_heading, True, TEXT_COLOR)
            answer_heading_rect = answer_heading_surface.get_rect(center=(screen_width // 2, y_offset))
            screen.blit(answer_heading_surface, answer_heading_rect)

            # Use wrap_text to split the answer into multiple lines
            max_width = screen_width - 200  # Adjust for padding
            wrapped_lines = wrap_text(str(answer), answer_font, max_width)

            # Render each wrapped line
            line_spacing = 40  # Vertical spacing between lines
            for i, line in enumerate(wrapped_lines):
                line_surface = answer_font.render(line, True, TEXT_COLOR)
                line_rect = line_surface.get_rect(center=(screen_width // 2, y_offset + 60 + i * line_spacing))
                screen.blit(line_surface, line_rect)

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


# Define the solutions to each riddle
riddle_solvers = {
    0: solve_order_of_books_riddle,
    1: solve_who_is_in_the_middle_riddle,
    2: solve_order_of_fruits_riddle,
    3: solve_seating_arrangement_riddle,
    4: solve_classroom_arrangement_riddle,
    6: solve_day_of_week_riddle,
    7: solve_office_desk_riddle,
    8: solve_party_seating_riddle,
    9: solve_box_arrangement_riddle,
    10: solve_tea_or_coffee_riddle,
    11: solve_card_suit_riddle,
    12: solve_book_collection_riddle,
    13: solve_fruit_salad_riddle,
    14: solve_animal_placement_riddle,
    15: solve_meeting_room_riddle
}

# main function
def main():
    riddles = load_riddles('finalriddles.txt')  # Load riddles from the file
    if not riddles:
        print("No riddles loaded. Exiting...")  # if no riddles quit
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

        # Call `draw_navigation_buttons` once and unpack all three values
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

