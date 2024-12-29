import pygame
import sys

# Initialize Pygame
pygame.init()

# Define screen dimensions
screen_width = 990
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Riddles")

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

# Function to apply resolution on two clauses
def resolve(c1, c2):
    """
    Resolves two clauses c1 and c2. If they can be resolved, returns the resolved clause.
    If no resolution is possible, returns None.
    """
    for literal in c1:
        if f"~{literal}" in c2:
            resolved_clause = (set(c1) | set(c2)) - {literal, f"~{literal}"}
            return resolved_clause
    return None

# Function to check if the clauses can lead to a contradiction (empty clause)
def resolution_algorithm(clauses):
    new_clauses = set(clauses)  # Start with the original clauses
    while True:
        pairs = list(new_clauses)  # Convert the set to a list to pair up clauses
        resolvents = set()  # To store newly resolved clauses
        
        for i in range(len(pairs)):
            for j in range(i + 1, len(pairs)):
                resolved = resolve(pairs[i], pairs[j])
                if resolved:
                    resolvents.add(frozenset(resolved))
        
        # If no new clauses are found, stop
        if not resolvents:
            return True, new_clauses  # No contradiction found, satisfiable
        
        # Add new clauses to the list of clauses
        new_clauses.update(resolvents)
        
        # Check for empty clause (contradiction)
        if frozenset() in new_clauses:
            return False, new_clauses  # Contradiction found, unsatisfiable

# def solve_treasure_location_riddle():
#     clauses = [
#         frozenset(["A", "B", "C"]),  # Treasure is in one of the locations
#         frozenset(["~A", "~B"]),      # Either 1 or 2 is false
#         frozenset(["~C"]),             # Location 3 is false
#     ]

#     result, final_clauses = resolution_algorithm(clauses)
#     if result:
#         is_in_location_1 = frozenset({"A"}) in final_clauses
#         is_in_location_2= frozenset({"B"}) in final_clauses
       
#         return {
#             "Treasure":"Location 1." if is_in_location_1 else "Treasure is in location 1",
#             "Treasure":"Location 2" if is_in_location_2 else "Treasure is in Location 2"
#         }
#     else:
#         return "No valid location for treasure."

def solve_hat_riddle():
# A = Person 1 sees a red hat
# B = Person 2 sees a red hat
# C = Person 3 sees a red hat
    clauses = [
        frozenset(["A", "B", "C"]),  # At least one sees a red hat
        frozenset(["~B", "~C"]),     # Person 1 doesn't see both others' hats red
        frozenset(["~A", "~C"]),     # Person 2 doesn't see both others' hats red
        frozenset(["C"]),             # Person 3 sees a red hat
    ]

    result, final_clauses = resolution_algorithm(clauses)
    if result:
        if frozenset({"C"}) in final_clauses:
            return "Person 3 sees a red hat."
    else:
        return "No consistent hat colors found."

def solve_crime_riddle():
    # A = Alice committed the crime
    # B = Bob committed the crime
    # C = Charlie committed the crime
    clauses = [
        frozenset(["A", "B", "C"]),  
        frozenset(["~A", "~C"]),      
        frozenset(["B"]),          
    ]

    result, final_clauses = resolution_algorithm(clauses)
    if result:
        if frozenset({"B"}) in final_clauses:
            return("Bob is the criminal.")
    else:
        return("No criminal identified.") 


def solve_truth_teller_riddle():
    # Clauses representing the problem
    clauses = [
        frozenset(["~A", "~B"]),  # Alice: "Bob is a liar" => ~A ∨ ~B
        frozenset(["~B", "C"]),  # Bob: "Charlie is a truth-teller" => ~B ∨ C
        frozenset(["~C", "~A"]),  # Charlie: "Alice is lying" => ~C ∨ ~A
        frozenset(["A", "B", "C"]),  # At least one is a truth-teller: A ∨ B ∨ C
    ]

    result, final_clauses = resolution_algorithm(clauses)

    if result:
        # Determine the truthfulness of each individual
        is_alice_truthful = frozenset({"A"}) in final_clauses
        is_bob_truthful = frozenset({"B"}) in final_clauses
        is_charlie_truthful = frozenset({"C"}) in final_clauses

        return {
            "Alice": "Truth-teller" if is_alice_truthful else "Liar",
            "Bob": "Truth-teller" if is_bob_truthful else "Liar",
            "Charlie": "Truth-teller" if is_charlie_truthful else "Liar",
        }
    else:
        return "No consistent solution found."
    
def solve_doortotreasure_riddle():
    # A = Door 1 leads to treasure
    # B = Door 2 leads to treasure
    # C = Door 3 leads to treasure
    clauses = [
        frozenset(["A", "B", "C"]),  # One door leads to treasure
        frozenset(["~A", "~C"]),     # Not both Door 1 and Door 3 lead to treasure
        frozenset(["B"]),             # Door 2 definitely leads to treasure
    ]

    result, final_clauses = resolution_algorithm(clauses)
    if result:
        if frozenset({"B"}) in final_clauses:
            return("Door 2 leads to treasure.")
    else:
        return("No treasure behind any door.")

def artifact_missing_riddle():
    # A = Artifact is in room 1
    # B = Artifact is in room 2
    # C = Artifact is in room 3
    clauses = [
        frozenset(["A", "B", "C"]),  # Artifact is in one of the rooms
        frozenset(["~A", "~B"]),     # Not in both room 1 and room 2
        frozenset(["C"]),             # It is definitely in room 3
    ]

    result, final_clauses = resolution_algorithm(clauses)
    if result:
        if frozenset({"C"}) in final_clauses:
            return("Artifact is in room 3.")
    else:
        return("No valid room for the artifact.")


def key_to_lock_riddle():
    # A = Key is in the top drawer
    # B = Key is in the middle drawer
    # C = Key is in the bottom drawer
    clauses = [
        frozenset(["A", "B", "C"]),  # Key is in one of the drawers
        frozenset(["~B", "~C"]),     # Not in both middle and bottom drawers
        frozenset(["A"]),             # Key is definitely in the top drawer
    ]

    result, final_clauses = resolution_algorithm(clauses)
    if result:
        if frozenset({"A"}) in final_clauses:
            return("Key is in the top drawer.")
    else:
        return("No valid drawer for the key.")

def guilty_twin_riddle():
    # A = Twin 1 is guilty
    # B = Twin 2 is guilty
    # C = Twin 3 is guilty
    clauses = [
        frozenset(["A", "B", "C"]),  # One twin is guilty
        frozenset(["~A", "~C"]),     # Not both Twin 1 and Twin 3 are guilty
        frozenset(["B"]),             # Twin 2 insists on being guilty
    ]

    result, final_clauses = resolution_algorithm(clauses)
    if result:
        if frozenset({"B"}) in final_clauses:
            return("Twin 2 is guilty.")
    else:
        return"No guilty twin identified."

def magicalstone_riddle():
    # A = Stone is in chest 1
    # B = Stone is in chest 2
    # C = Stone is in chest 3
    clauses = [
        frozenset(["A", "B", "C"]),  # Stone is in one of the chests
        frozenset(["~A", "~B"]),     # Not both chest 1 and chest 2 contain the stone
        frozenset(["C"]),            # Stone is definitely in chest 3
    ]

    # Run the resolution algorithm
    result, final_clauses = resolution_algorithm(clauses)

    # Create a result string based on the outcome
    if result:
        if frozenset({"C"}) in final_clauses:
            return "Stone is in chest 3."
        else:
            return "Magical stone riddle is satisfiable but location is unclear."
    else:
        return "No valid chest for the magical stone."

# Define the riddles and their solvers
riddle_solvers = {
    # 0:solve_treasure_location_riddle,
    0:solve_hat_riddle,
    1:solve_crime_riddle,
    2:solve_truth_teller_riddle,
    3:solve_doortotreasure_riddle,
    4:artifact_missing_riddle,
    5:key_to_lock_riddle,
    6:guilty_twin_riddle,
    7:magicalstone_riddle
}

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
        return(f"Error: The file {filename} was not found.")
    return riddles

def main():
    riddles = load_riddles('resolutionriddles.txt')  # Load riddles from the file
    if not riddles:
        pygame.quit()
        sys.exit()
        return("No riddles loaded. Exiting...")  # If no riddles, quit
    
    current_riddle = 0
    is_flipped = False 
    answer = None

    while True:
        screen.fill(WHITE)  # Clear the screen
        title, riddle = riddles[current_riddle]

        if is_flipped and current_riddle in riddle_solvers:
            answer = riddle_solvers[current_riddle]()

        draw_flashcard(title, riddle, is_flipped, screen_width - 240, answer)

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