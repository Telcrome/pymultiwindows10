This simple script demonstrates how to set your mouse cursor to a specific location using the keyboard.

When using multiple screen it might happen that you lose your cursor, so I use it to place the cursor back in the middle of my main screen.
Simply bind a mouse button to a keyboard sequence and use this script to bind it to a mouse placement.

### Installation

```bash
pip install keyboard
pip install pyautogui
```

It might be helpful to place a shortcut to the script inside the autostart folder. (Win+R -> shell:startup)
The shortcut should link to something like:

```bash
pythonw path/main.py # pythonw starts your terminal in the background
```

My full shortcut looks like this:

```bash
C:\Users\rapha\AppData\Local\Continuum\anaconda3\envs\mouse_controller/pythonw.exe main.py
```