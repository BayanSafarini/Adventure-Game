# Text-Based Adventure Game
---
A Python text-based adventure game where players encounter various villains and make decisions to progress through the story. The game includes randomization of villains and the option to find a magical sword to aid in defeating them.

## Features

- **Dynamic Gameplay:** Encounter different villains randomly chosen from a list, each requiring strategic decisions to overcome.
- **Decision Making:** Choose between fighting or running away in various scenarios.
- **Interactive Storytelling:** Explore a house and a cave, each with unique outcomes based on player choices.
- **Play Again Option:** After completing the game, players have the option to restart for a new adventure.

## How to Play

1. **Run the Game:** Execute the script in a Python environment (`python adventure_game.py`).
2. **Follow Prompts:** Make choices presented by the game to navigate through different scenarios.
3. **Outcome:** Experience different endings based on your decisions in encounters with villains.

## Game Structure

The game is structured into several functions:
- **`print_sleep(message_to_print)`**: Delays printing messages to simulate pacing.
- **`valid_input(prompt, option_1, option_2)`**: Ensures valid user input for decision-making.
- **`play_again()`**: Allows players to restart the game after completion.
- **`fight(player)`**: Handles combat scenarios based on player decisions and inventory.
- **`intro(player)`**: Introduces the game setting and initial conditions to the player.
- **`house(player)`**: Manages interactions when approaching a house in the game.
- **`cave(player)`**: Manages interactions when exploring a cave in the game.
- **`outside_choices(player)`**: Guides players through choices outside the house and cave.
- **`adventure_game()`**: Initializes and orchestrates the game flow, including random villain selection.

## Installation

Ensure Python 3.x is installed on your machine. No additional libraries are required.

```bash
git clone https://github.com/BayanSafarini/adventure-game.git
cd adventure-game
python adventure_game.py
```
