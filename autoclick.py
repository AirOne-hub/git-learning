import pyautogui
import keyboard
import threading
import time
import tkinter as tk
from tkinter import ttk

pyautogui.FAILSAFE = False

running = False
fixed_pos = False
click_button = "left"
delay = 0.1
pos_x, pos_y = 0, 0


def click_loop():
    global running
    while True:
        if running:
            if fixed_pos:
                pyautogui.click(pos_x, pos_y, button=click_button)
            else:
                pyautogui.click(button=click_button)
            time.sleep(delay)
        else:
            time.sleep(0.05)


def toggle():
    global running
    running = not running
    status.set("ON" if running else "OFF")


def set_position():
    global pos_x, pos_y
    pos_x, pos_y = pyautogui.position()
    pos_label.set(f"Position: {pos_x}, {pos_y}")


def update_delay(val):
    global delay
    delay = float(val)


def set_mode(mode):
    global delay
    if mode == "legit":
        delay = 0.12
    elif mode == "turbo":
        delay = 0.005
    speed.set(delay)


def set_button():
    global click_button
    click_button = btn_choice.get()


def toggle_fixed():
    global fixed_pos
    fixed_pos = not fixed_pos


# --- GUI ---
root = tk.Tk()
root.title("Autoclick PRO")
root.geometry("320x380")
root.resizable(False, False)

status = tk.StringVar(value="OFF")
pos_label = tk.StringVar(value="Position: libre")

tk.Label(root, text="Autoclick PRO", font=("Arial", 16, "bold")).pack(pady=5)
tk.Label(root, text="Statut:").pack()
tk.Label(root, textvariable=status, font=("Arial", 12)).pack()

ttk.Button(root, text="Activer / Désactiver (F6)", command=toggle).pack(pady=5)

btn_choice = tk.StringVar(value="left")
tk.Label(root, text="Bouton de clic").pack()
ttk.Radiobutton(root, text="Gauche", variable=btn_choice, value="left", command=set_button).pack()
ttk.Radiobutton(root, text="Droit", variable=btn_choice, value="right", command=set_button).pack()

ttk.Button(root, text="Capturer position souris", command=set_position).pack(pady=5)
tk.Label(root, textvariable=pos_label).pack()
ttk.Checkbutton(root, text="Clic à position fixe", command=toggle_fixed).pack()

tk.Label(root, text="Vitesse (secondes)").pack(pady=5)
speed = tk.DoubleVar(value=delay)
ttk.Scale(root, from_=0.001, to=0.3, variable=speed, command=update_delay).pack(fill="x", padx=20)

tk.Label(root, text="Modes").pack(pady=5)
ttk.Button(root, text="🎮 Legit (FPS / MC)", command=lambda: set_mode("legit")).pack(fill="x", padx=20)
ttk.Button(root, text="⚡ Turbo (Ultra rapide)", command=lambda: set_mode("turbo")).pack(fill="x", padx=20)

tk.Label(root, text="ESC pour quitter").pack(pady=10)

keyboard.add_hotkey("f6", toggle)
keyboard.add_hotkey("esc", lambda: root.destroy())

threading.Thread(target=click_loop, daemon=True).start()
root.mainloop()