# LIFE AI COPILOT

#A command-line productivity assistant built in Python.

I created this project while learning Python to practice working with functions, file handling, APIs, and external libraries. The application helps manage daily tasks, set reminders, check weather, generate shopping lists, and provide motivational quotes through a simple menu-driven interface.

The project stores tasks locally using JSON and can also read information from the internet for weather updates.

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Platform](https://img.shields.io/badge/Platform-Mac%20%7C%20Windows%20%7C%20Linux-lightgrey?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

---

## Screenshots

###  Main Menu
![Main Menu](screenshots/menu.png)

###  Weather Check
![Weather](screenshots/weather.png)

### Shopping List Code
![Shopping List](screenshots/shopping.png)

### Code Inside VS Code
![Code](screenshots/code1.png)

---

## Features

| # | Feature | Description |
|---|---------|-------------|
| 1 | Add Task | Add things you need to do today |
| 2 | Show Tasks | See all your pending tasks |
| 3 | Mark Done | Mark a task as completed |
| 4 | Clean Up | Delete all finished tasks |
| 5 | Reminder | Set a time-based reminder |
| 6 | Shopping List | Type a meal name → get ingredients |
| 7 | Quote | Get a random motivational quote |
| 8 | Weather | Live weather for any city |
| 9 | Daily Summary | Overview of your day + motivation |

---

## Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/sukhmandult4-web/LIFE-AI-COPILOT.git
cd LIFE-AI-COPILOT
```

### 2. Install libraries
```bash
pip3 install pyttsx3 requests --break-system-packages
```

### 3. Run the program
```bash
python3 main.py
```

---

## Libraries Used

| Library | Purpose | Install |
|---------|---------|---------|
| `pyttsx3` | 🔊 Text to speech (computer voice) | `pip3 install pyttsx3` |
| `requests` | 🌤️ Fetch live weather from internet | `pip3 install requests` |
| `time` | ⏰ Waiting and checking time | Built-in ✅ |
| `datetime` | 📅 Getting today's date | Built-in ✅ |
| `random` | 💬 Random motivational quotes | Built-in ✅ |
| `json` | 💾 Saving tasks to a file | Built-in ✅ |
| `os` | 📂 Checking if file exists | Built-in ✅ |

---
## What I Learned

While building this project, I practiced:

- Writing reusable Python functions
- Working with dictionaries and lists
- Reading and writing JSON files
- Handling user input
- Using APIs with the requests library
- Error handling with try and except
- Organizing a larger Python program into multiple features

## 🛒 Meals Supported for Shopping List

`pasta` `pizza` `sandwich` `fried rice` `omelette` `soup` `salad` `pancakes` `maggi` `dal rice` `paratha` `poha`
 
## Author

Sukhman Singh

First-year B.Tech student interested in Python, AI, and software development.

GitHub: https://github.com/sukhmandult4-web


---

## License

MIT License — free to use, modify and share!

## Future Improvements

- Better reminder system
- More meal options for shopping lists
- AI-powered task suggestions
- GUI version using Tkinter or PyQt
- Voice command support
