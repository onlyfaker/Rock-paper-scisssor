# Rock Paper Scissors Game

An interactive command-line implementation of the classic Rock Paper Scissors game, featuring ASCII art representations and a best-of-three format against the computer.

## Description

This Python-based game lets players compete against the computer in a best-of-three Rock Paper Scissors match. Each move is visualized with ASCII art, making the game more engaging and visually appealing.

## Features

- ASCII art representations of moves
- Best-of-three format
- Random computer moves
- Score tracking
- Tie handling
- Visual round tracking
- Final winner announcement

## Prerequisites

To run this game, you need:
- Python 3.x installed on your system
- `random` module (included in Python standard library)

## Installation

1. Copy the code into a file named `rock_paper_scissors.py`
2. No additional packages need to be installed

## How to Play

1. Open your terminal/command prompt
2. Navigate to the directory containing the game file
3. Run the game:
   ```bash
   python rock_paper_scissors.py
   ```
4. When prompted, enter your choice:
   - 0 for Rock
   - 1 for Paper
   - 2 for Scissors

### Game Rules

- Rock (0) beats Scissors (2)
- Paper (1) beats Rock (0)
- Scissors (2) beats Paper (1)
- Identical choices result in a tie (round is replayed)

## Game Flow

1. Game announces "Best out of 3"
2. For each round:
   - Player makes a choice (0-2)
   - Computer randomly selects its move
   - Both moves are displayed with ASCII art
   - Winner is determined
   - Score is updated
3. Game continues until one player wins 2 rounds
4. Final winner is announced with score

## ASCII Art Display

The game features detailed ASCII art for each move:

### Rock
```
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
```

### Paper
```
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
```

### Scissors
```
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
```

## Scoring System

- Winning a round: +1 point
- Losing a round: 0 points
- Tie: Round is replayed (no points)
- First to 2 points wins the game

## Features in Detail

### Round Management
- Tracks current round number
- Skips counting tied rounds
- Continues until valid winner is determined

### Score Tracking
- Maintains separate scores for player and computer
- Updates after each valid round
- Displays final scores at game end

### Input Validation
- Accepts numbers 0-2
- Clear input instructions
- Easy to understand choice mapping

## Customization Options

You can modify the code to:
- Change the number of rounds
- Add more moves
- Modify the ASCII art
- Add player names
- Include round history
- Implement different scoring systems

## Educational Value

This program demonstrates:
- List usage in Python
- Random number generation
- Conditional logic
- Loop control
- ASCII art implementation
- Score tracking
- Game state management

## Troubleshooting

Common issues and solutions:
1. Invalid Input:
   - Enter only numbers 0, 1, or 2
   - Don't use special characters
2. Display Issues:
   - Ensure terminal supports ASCII characters
   - Check terminal window size

## Future Enhancements

Potential improvements could include:
- Input validation
- Color text
- Sound effects
- Game statistics
- Player name input
- Multiple game modes
- Score history
- Difficulty levels

## Contributing

Feel free to suggest improvements:
- Additional features
- Better ASCII art
- Enhanced user interface
- More game modes
- Bug fixes

## License

Free to use for educational and personal purposes.
