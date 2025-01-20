# Snake, Water, Gun Game Using a Matrix

This project is a Python implementation of the classic **Snake, Water, Gun** game using a matrix to determine the outcomes. The program allows users to play against the computer, with the winner decided based on predefined rules.

---

## Features
- Implements the game logic using a 3x3 matrix.
- Allows continuous play until the user decides to exit.
- Randomized computer choices to ensure fairness.
- Simple input validation to ensure correct gameplay.

---

## How to Use
1. Clone the repository:
   ```bash
   git clone https://github.com/Vishal-shamdasani/PyPocketProjects/blob/main/snake%20water%20gun/snake_water_gun.py
   ```
2. Navigate to the project directory:
   ```bash
   cd snake\ water\ gun
   ```
3. Run the Python script:
   ```bash
   python snake_water_gun.py
   ```
4. Follow the prompts to play the game:
   - Enter `S` for snake, `W` for water, and `G` for gun.
   - Enter `1` to play or `0` to exit.

---

## Code Explanation
### Input Validation
- The function `input_check()` ensures that the user inputs are valid (`S`, `W`, or `G`).
- Invalid inputs prompt the user to try again.

### Game Logic
- A 3x3 matrix defines the outcomes:
  - `D` for Draw
  - `W` for Win
  - `L` for Lose
- The program generates a random choice for the computer.
- Outcomes are determined by comparing the user's choice with the computer's choice.

### Continuous Play
- The game loop allows users to play multiple rounds until they choose to exit by entering `0`.

---

## Example Usage
```
enter 1 to play the game and 0 exit: 1
Enter s for snake, w for water and g for gun: s
computer chose water
Win

enter 1 to play the game and 0 exit: 0
thanks for playing the game
```

---

## Improvements
This program can be enhanced by:
- Keeping track of the user's score across multiple rounds.
- Adding a GUI for a more interactive experience.
- Including sound effects or animations to make the game more engaging.

---

## License
This project is licensed under the MIT License. Feel free to use and modify it.

---

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests to enhance this project.

---

## Repository Link
[Snake, Water, Gun Game on GitHub](https://github.com/Vishal-shamdasani/PyPocketProjects/blob/main/snake%20water%20gun/snake_water_gun.py)

