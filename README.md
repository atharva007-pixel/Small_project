# 🧪 Small Projects — Python Learning Collection

A curated set of **beginner-friendly Python mini-projects** built during my first year of college. Each folder is a standalone CLI script exploring core concepts: loops, conditionals, file I/O, random, OOP basics, and simple algorithms.

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)](https://python.org)
[![Beginner](https://img.shields.io/badge/Level-Beginner-green)](https://github.com/atharva007-pixel/Small_project)
[![Learning](https://img.shields.io/badge/Purpose-Learning-orange)](https://github.com/atharva007-pixel)

---

## 📁 Projects Included

| Project | Folder | Description | Key Concepts |
|---------|--------|-------------|--------------|
| **FLAME Game** | `FLAME_GAME/` | Relationship predictor (Friends/Lovers/Affair/Marriage/Enemies) from two names | Sets, string manipulation, CLI animation |
| **Hangman** | `HangMan/` | Classic word-guessing game with lives & masked word | Classes, random, loops, string masking |
| **Snake-Water-Gun** | `Snake water game/` | Rock-paper-scissors variant (Snake drinks Water, Water drowns Gun, Gun shoots Snake) | Dict mapping, random, conditionals |
| **To-Do List (v1)** | `To do list/My-todo-built.py` | Task manager with file persistence (`Task_record.txt`) | File I/O, dict dispatch, menu loop |
| **To-Do List (v2)** | `To do list/ai_to-do.py` | Cleaner refactor with lambda exit | Dict dispatch, lambda, list ops |
| **To-Do List (ChatGPT)** | `To do list/chatgpt-to_do_list.py` | Alternative implementation from AI assist | Basic CRUD, enumerate, input validation |
| **Number Guessing** | `Perfect_guess/ai_guess..py` | Guess 1-10 with hints (Higher/Lower), attempt tracking | Class, random, while loop |
| **Login System** | `Login/Login_sytem.py` | Name, email, password confirmation, age/gender greeting | Dict storage, validation loops, string parsing |
| **File Organizer (AI)** | `File Organizer/main_Ai.py` | Move all PDFs from Downloads → Desktop/All PDFs | `os`, `shutil`, path expansion, error handling |
| **File Organizer (Manual)** | `File Organizer/main_me.py` | Same task, hardcoded paths | `os`, `shutil`, try/except |
| **Image Renamer** | `File Organizer/img_renamer.py` | Batch rename PNG/JPG in Documents to `name1.ext`, `name2.ext`... | `os.listdir`, `os.rename`, `pathlib` basics |

---

## 🚀 Run Any Project

```bash
git clone https://github.com/atharva007-pixel/Small_project.git
cd Small_project

# Example: run FLAME game
python "FLAME_GAME/flame_final.py"

# Example: run To-Do list
python "To do list/My-todo-built.py"

# Example: organize PDFs
python "File Organizer/main_Ai.py"
```

> **Note:** Folder names have spaces — quote them or use tab completion.

---

## 🗂 Project Structure

```
Small_project/
├── FLAME_GAME/
│   ├── flame_final.py          # Polished version
│   ├── flame_AI_test.py        # Alternate logic
│   └── flame_first draft.py    # First attempt
├── HangMan/
│   ├── main.py                 # Class-based implementation
│   ├── rules                   # Game rules (text)
│   └── test.py                 # Experimental version
├── Snake water game/
│   └── main.py
├── To do list/
│   ├── My-todo-built.py        # File-persistent version
│   ├── ai_to-do.py             # Refactored
│   ├── chatgpt-to_do_list.py   # AI-assisted version
│   └── test task.py            # Scratchpad
├── Perfect_guess/
│   └── ai_guess..py
├── Login/
│   └── Login_sytem.py
└── File Organizer/
    ├── main_Ai.py              # PDF organizer (expanduser)
    ├── main_me.py              # PDF organizer (hardcoded)
    ├── img_renamer.py          # Batch image rename
    └── Bro0/                   # (empty/subfolder)
```

---

## 🎯 Learning Outcomes

Through these projects I practiced:

- **Core syntax**: variables, loops, conditionals, functions
- **Data structures**: lists, sets, dicts, tuples
- **File I/O**: `open`, `read`, `write`, `append`, `os.path`, `pathlib`, `shutil`
- **Standard library**: `random`, `time`, `os`, `sys`
- **OOP basics**: classes, `__init__`, methods, `self`
- **Error handling**: `try/except`, input validation
- **Code organization**: dict dispatch pattern, separation of concerns
- **CLI UX**: menus, animations, colored output, clear screens

---

## 📸 Sample Runs

| FLAME Game | Hangman | Snake-Water-Gun | To-Do List |
|------------|---------|-----------------|------------|
| ![FLAME](https://via.placeholder.com/250x150?text=FLAME+Game) | ![Hangman](https://via.placeholder.com/250x150?text=Hangman) | ![SWG](https://via.placeholder.com/250x150?text=Snake+Water+Gun) | ![Todo](https://via.placeholder.com/250x150?text=To-Do+List) |

---

## 🤝 What's Next

- [ ] Add unit tests (`pytest`) for each game
- [ ] Convert 1-2 projects to Streamlit web apps
- [ ] Build a unified menu launcher (`python main.py` → pick project)
- [ ] Add type hints & docstrings throughout
- [ ] Create a `requirements.txt` (currently stdlib only)

---

## 📄 License

MIT — learning code, free to copy, modify, remix.

---

> Built by [@atharva007-pixel](https://github.com/atharva007-pixel) · First-year B.Tech · "Code every day, even if it's just 20 lines"