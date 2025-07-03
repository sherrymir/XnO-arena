
# ❌⭕ Tic-Tac-Toe: Python Terminal Game with Basic AI

A simple terminal-based **Tic-Tac-Toe** game where you play as **X** against a basic AI playing as **O**.  
The AI can block your winning move and tries to win when it gets a chance!

---

## 🎮 Features

- 3×3 grid with position labels (e.g., `TopL`, `MidC`, `BotR`)
- Input validation and board rendering
- Win detection for both players
- Basic AI with:
  - Win detection
  - Block opponent’s winning move
  - Random fallback move

---

## 🧠 How the AI Works

The AI (`O`) tries to:
1. **Win if it can** by completing any winning triplet.
2. **Block the player (`X`)** if the player is about to win.
3. **Otherwise** make a random valid move.

---

## 🕹️ How to Play

1. Clone the repository:
   ```bash
   git clone https://github.com/sherrymir/tic-tac-toe-ai.git
   cd tic-tac-toe-ai
   ```

2. Run the game:
   ```bash
   python game.py
   ```

3. Enter your move when prompted using position keys like `TopL`, `MidC`, `BotR`, etc.

---

## 🗺️ Board Position Guide

```
TopL | TopC | TopR
-----+------+-----
MidL | MidC | MidR
-----+------+-----
BotL | BotC | BotR
```

Example input:
```
Where do you wanna put X e.g(TopL,MidC,BotR): MidC
```

---

## 🧩 File Structure

```
tic-tac-toe-ai/
└── game.py         # Main game logic with AI
```

---

## 📌 Coming Soon

- Smarter minimax-based AI
- GUI version with Pygame or Tkinter
- Two-player local mode
- Score tracking

---

