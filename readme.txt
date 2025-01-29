# Asteroids Game

This project is a simple implementation of the classic Asteroids game using Python and Pygame. The player controls a spaceship that can rotate, move, and shoot bullets to destroy asteroids. The game features:

- A player-controlled spaceship represented as a triangle.
- Asteroids that spawn at the edges of the screen and move in random directions.
- Bullets that the player can shoot to destroy asteroids.
- Asteroids that split into smaller asteroids when hit by bullets.

## How to Run

1. Ensure you have Python and Pygame installed on your system.
2. Clone this repository to your local machine.
3. Navigate to the project directory.
4. Run the `main.py` file using Python.

```sh
python main.py
```

## Controls

- `W`: Move forward
- `A`: Rotate left
- `D`: Rotate right
- `S`: Move backward
- `SPACE`: Shoot bullets

## Game Logic

- The player can shoot bullets, which will destroy asteroids on collision.
- Large asteroids split into two medium asteroids when hit.
- Medium asteroids split into two small asteroids when hit.
- Small asteroids disappear when destroyed.
- The game ends when the player's spaceship collides with an asteroid.

## Files

- `main.py`: The main game loop and initialization code.
- `constants.py`: Contains game constants such as screen dimensions, player speed, and asteroid properties.
- `player.py`: Defines the Player class and its behavior.
- `asteroid.py`: Defines the Asteroid class and its behavior.
- `asteroidfield.py`: Manages the spawning of asteroids.
- `shot.py`: Defines the Shot class for bullets.
- `circleshape.py`: Base class for game objects with circular shapes and collision detection.

Enjoy playing the game!
