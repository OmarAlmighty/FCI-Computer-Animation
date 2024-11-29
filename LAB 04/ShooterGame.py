import pygame as pg
import random

# Initialize Pygame modules
pg.init()

# Set the window width and height
window_width = 800
window_height = 600
window = pg.display.set_mode((window_width, window_height))

# Offsets from the left and right borders of the window
MARGIN = 20

# Window title
pg.display.set_caption("Shooter Game")

# An object to help to track the time
clock = pg.time.Clock()


# Player class
class Player:
    def __init__(self):
        """Initialize player attributes."""
        # The speed of moving left and right
        self.speed = 5
        # x-y positions on the window
        self.x = window_width // 2
        self.y = window_height - 100
        # Read the image and convert the pixels to alpha format for better performance
        self.img = pg.image.load('player.png').convert_alpha()
        # Get the rectangle object that embodies the image.
        # This is useful for detecting collisions
        self.rect = self.img.get_rect()
        # Set the rectangle's positions
        self.rect.x = self.x
        self.rect.y = self.y
        # A variable to track the left and right positions
        self.x_change = 0

    def update(self):
        """Move the player."""
        self.x += self.x_change
        # Always update the rect, because it's
        # needed for the collision detection.
        self.rect.x = self.x

    def draw(self, window):
        """Draw the player."""
        window.blit(self.img, self.rect)


# Enemy class
class Enemy:
    def __init__(self):
        """Initialize the enemy attributes."""
        # The x position must be random [0, window_width]
        self.x = random.randint(0, window_width - MARGIN-40)
        # Start from -30 so that it gives the feeling that the enemy is coming from up
        self.y = -30
        # Read the image and convert the pixels to alpha format for better performance
        self.img = pg.image.load("enemy.png").convert_alpha()
        # Get the rectangle object that embodies the image.
        # This is useful for detecting collisions
        self.rect = self.img.get_rect()
        # Set the rectangle's positions
        self.rect.x = self.x
        self.rect.y = self.y
        # The speed of the enemy moving downwards.
        self.speed = 2

    def update(self):
        """Move the enemy down."""
        self.y += self.speed
        self.rect.y = self.y

    def draw(self, window):
        """Draw the object."""
        window.blit(self.img, self.rect)



# Bullet class
class Bullet:
    def __init__(self, x, y):
        """Initialize the bullet attributes."""
        self.speed = 7
        self.x = x
        self.y = y
        self.img = pg.image.load("bullet.png").convert_alpha()
        self.rect = self.img.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        """Move the bullet upwards."""
        self.y -= self.speed
        self.rect.y = self.y

    def draw(self, window):
        window.blit(self.img, self.rect)


# The list of enemies
enemy_lst = []
# The list of bullets
bullet_lst = []

# A timer to spawn new enemies
enemy_timer = 0
spawn_enemy_timer = 1000


# Function to detect it the bullet collide with the enemy
def check_collisions(obj1, obj2):
    """Check if two objects collide."""
    return obj1.rect.colliderect(obj2.rect)


# Create a player object
player = Player()

# The game loop
while True:
    # Listen for events
    for event in pg.event.get():
        # If the user closes the window
        if event.type == pg.QUIT:
            pg.quit()  # uninitialize all pygame modules

        # Check if the user is pressing on the space key
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                # Create a new bullet object
                bullet_x = player.rect.centerx  # x = center of the player
                bullet_y = player.rect.top  # y = top part of the player
                bullet_lst.append(Bullet(bullet_x, bullet_y))  # add the bullet to the list

    # Get a dictionary object of the pressed keys
    keys = pg.key.get_pressed()
    # The left button, move the player to the left
    if keys[pg.K_LEFT] and player.rect.left > MARGIN:
        player.x_change = -player.speed
    # The right button, move the player to the right
    elif keys[pg.K_RIGHT] and player.rect.right < window_width - MARGIN:
        player.x_change = player.speed
    # Otherwise, do not change the player position
    else:
        player.x_change = 0

    # Update player when the left or right keys are pressed
    player.update()

    # Update bullets to move them down
    for bullet in bullet_lst:
        bullet.update()


    # Spawn a new enemy according to current time
    current_time = pg.time.get_ticks() # return the time in ms
    if current_time - enemy_timer > spawn_enemy_timer:
        # If a specified amount of time is passed, create a new enemy
        new_enemy = Enemy()
        # Add it to the list
        enemy_lst.append(new_enemy)
        # Update the time
        enemy_timer = current_time

    # Update enemies
    for enemy in enemy_lst:
        enemy.update()

    # Check for bullet-enemy collisions
    for bullet in bullet_lst:
        for enemy in enemy_lst:
            if check_collisions(bullet, enemy):
                bullet_lst.remove(bullet)
                enemy_lst.remove(enemy)
                break

    # Remove enemies that are off the screen
    for enemy in enemy_lst:
        if enemy.rect.top > window_height:
            enemy_lst.remove(enemy)

    # Remove bullets that are off-screen
    bullet_lst = [bullet for bullet in bullet_lst if bullet.rect.bottom > 0]

    # Fill the background with black
    window.fill((0, 0, 0))

    # Draw the player
    player.draw(window)

    # Draw the bullets
    for bullet in bullet_lst:
        bullet.draw(window)

    # Draw the enemies
    for enemy in enemy_lst:
        enemy.draw(window)

    # Update the display
    pg.display.update()

    # Set the FPS
    clock.tick(60)
