import pygame
import time

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 400
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Car attributes
car_x = 50  # Start position (in pixels)
car_y = HEIGHT // 2  # Keep car centered
speed_kmh = 60  # Speed in km/h
speed_px_per_sec = (speed_kmh * 1000 / 3600)  # Convert to pixels/sec
total_time = 2.5  # Travel time in hours
fps = 60  # Frames per second
dt = 1 / fps  # Time step

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Physics Simulation - Car Motion")
car = pygame.image.load("car.png")  # Load a car image (add a car.png in the same directory)
car = pygame.transform.scale(car, (100, 50))  # Resize car

running = True
start_time = time.time()

# Main simulation loop
while running:
    screen.fill(WHITE)
    
    # Get elapsed time
    elapsed_time = time.time() - start_time
    
    # Update car position
    car_x += speed_px_per_sec * dt
    
    # Stop the simulation after total_time
    if elapsed_time >= total_time * 3600:  # Convert hours to seconds
        running = False
    
    # Draw car
    screen.blit(car, (car_x, car_y))
    
    # Refresh display
    pygame.display.flip()
    pygame.time.delay(int(dt * 1000))  # Convert to milliseconds

# Quit Pygame
pygame.quit()
