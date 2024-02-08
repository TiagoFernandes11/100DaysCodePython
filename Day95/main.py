import pyautogui


# Function to capture the game window screenshot
def capture_game_screenshot():
    # Replace these coordinates and dimensions with the values that match
    # your game window where the enemies will appear right before jumping
    x, y, width, height = 500, 650, 100, 100

    # Capture the game region
    game_window_element = pyautogui.screenshot(region=(x, y, width, height))
    return game_window_element


# Function to check if an obstacle is present
def is_obstacle(game_window_element, x, y):
    # Assuming that grey color represents obstacles in your game
    pixel_color = game_window_element.getpixel((x, y))
    return pixel_color == (83, 83, 83)


# Function to make the dinosaur jump
def jump():
    pyautogui.press('space')


# Main game loop
if __name__ == "__main__":
    while True:
        game_window = capture_game_screenshot()

        # Check for obstacles and jump if detected
        if is_obstacle(game_window, 0, 0):  # Adjust the coordinates as needed
            jump()