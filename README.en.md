# ff-ou

[日本語](README.md) | [English](README.en.md)

An ASCII-graphics RPG that runs in the terminal.
It is a personal project written in Python with [asciimatics](https://github.com/peterbrittain/asciimatics), and it is still in development.

```text
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:#............###########.#      :quests                          :
:......##########.........#      :(X) first                       :
:########..........########      :( ) back                        :
:.........................#      :                                :
:..................T......#      :                                :
:.........................#      :                                :
:.........................#      :                                :
:.........................#      :                                :
:................$........#      :                                :
:.........................#      :                                :
:.........................#      :                                :
:.........................#      :                                :
:.........................#      :                                :
:.........................#      :                                :
:.........................#      :                                :
:.........................#      :           < 1 / 5 >            :
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
```

The map is on the left (`$` is the hero, `#` is a wall). The side menu is on the right.

## Features

- **A map that scrolls with the hero**: the map is loaded from a text file (`mapLight.txt`), and only the 32×16 tiles around the hero are drawn.
- **Collision**: the hero can't walk through walls (`#`) or other blocked tiles.
- **Reusable menu UI**: the selectable list is a `FatherList` class. The `SideScreen` subclass adds page switching and a close action. The cursor skips heading rows on its own.
- **Side menu with 5 pages**: quests / equipment / items / skills / stats. The pages are placeholders for now.
- **Battle system prototype** (`fight.py`): attack, skill, item and run. Damage is random.

## Tech stack

| Technology | Used for |
|---|---|
| Python 3 | Language (tested on 3.14) |
| [asciimatics](https://github.com/peterbrittain/asciimatics) | Drawing to the terminal and reading keyboard input |
| [cutie](https://github.com/kamik423/cutie) | Selection menus in the battle prototype (`fight.py`) |

## Getting started

```bash
git clone https://github.com/gerahertzjpn/ff-ou.git
cd ff-ou

python -m venv .venv
.venv\Scripts\activate          # Windows
# source .venv/bin/activate     # macOS / Linux

pip install -r requirements.txt
python game.py
```

- Run it **from the repository root**, because the map and text files are loaded by relative path.
- A terminal of at least 80×24 characters is recommended (the game screen is 67×18).
- The battle prototype runs on its own: `python fight.py`

## Controls

| Screen | Key | Action |
|---|---|---|
| Main menu | ↑ / ↓ | Select an item |
| | Enter | Confirm |
| Map | ← ↑ ↓ → | Move |
| | E | Open the side menu |
| | Esc | Quit the game |
| Side menu | ↑ / ↓ | Select an item |
| | ← / → | Switch pages (1–5) |
| | Q | Close the menu and return to the map |

## Project structure

| File | Contents |
|---|---|
| `game.py` | Entry point: setup, main loop, hero movement |
| `map.py` | Map loading and drawing, the side screen, menu UI (`FatherList` / `SideScreen`) |
| `mainmenu.py` | Main menu (play / settings / exit) |
| `fight.py` | Battle system prototype (runs on its own) |
| `mapLight.txt` | The map used by the game |
| `map.txt` | A large maze map (not used yet) |
| `secondscreen.txt` | Text for the side screen |
| `settings.py` / `sidescreen.py` | Old versions and experiments (commented out) |

## How it evolved

1. It started as a simple text menu. Map display and movement were then built with `curses` and `cutie`.
2. A large refactor moved all drawing and input handling to `asciimatics`.
3. The selectable list was rewritten from a function into a class, and the side screen got an interactive menu.

## Roadmap

- Connect the battle system to enemies on the map
- Fill in the side menu pages (quests, equipment, items, skills, stats)
- Settings screen
- WASD movement

## Notes for development

- All in-game text is English (ASCII). Full-width characters, such as Japanese, take two cells in a terminal and would break the tile-based layout.
- The side screen fits at most 32 characters per line. Wrap longer text by hand.
- The map view and the side screen are both fixed at 32×16 tiles.

## Author

[gerahertzjpn](https://github.com/gerahertzjpn)
