from typing import Tuple, List

import keyboard
import pyautogui

# Enter your mouse locations and corresponding shortcuts to this list
# ((x, y), shortcut)
ls: List[Tuple[Tuple[int, int], str]] = [
    ((-500, 500), 'ctrl+left windows+alt+page up'),
    ((960, 540), 'ctrl+left windows+alt+page down'),
    ((1500, 500), 'ctrl+Shift+left windows+alt+page up')
]


def set_mouse_pos(pos: Tuple) -> None:
    pyautogui.dragTo(pos[0], pos[1])


for (x, y), h_name in ls:
    keyboard.add_hotkey(h_name, pyautogui.dragTo, args=(x, y))

keyboard.wait()
