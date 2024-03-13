import json
import os
from pathlib import Path
import tkinter as tk
import webbrowser

# Paths
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets" / "frame0"
DATA_DIR = Path(os.getenv("APPDATA")).joinpath("ClickerCrazeIdleFortune")
DATA_FILE = DATA_DIR / "game_data.json"

# Load images
def load_image(asset_path: str) -> tk.PhotoImage:
    return tk.PhotoImage(file=ASSETS_PATH.joinpath(asset_path))

# Load data or initialize with default values
def load_data() -> dict:
    data = {
        "money_count": 0,
        "gem_count": 0,
        "upgrade_cost": 1,
        "money_per_click": 1,
        "gem_upgrade_cost": 1,
        "gems_per_click": 1,
        "gem_click_upgrades": 0,
        "money_click_upgrades": 0,
    }

    if DATA_FILE.exists():
        with open(DATA_FILE, "r") as file:
            data = json.load(file)

    return data

# Save data
def save_data():
    with open(DATA_FILE, "w") as file:
        json.dump(data, file)

# Create game window
window = tk.Tk()
window.title("Clicker Craze: Idle Fortune")
window.geometry("1000x500")
window.configure(bg="#FFFFFF")

# Game data
data = load_data()
money_count = data["money_count"]
gem_count = data["gem_count"]
upgrade_cost = data["upgrade_cost"]
money_per_click = data["money_per_click"]
gem_upgrade_cost = data["gem_upgrade_cost"]
gems_per_click = data["gems_per_click"]
gem_click_upgrades = data["gem_click_upgrades"]
money_click_upgrades = data["money_click_upgrades"]

def update_counters():
    money_text.set(f"Money: {money_count}")
    gem_text.set(f"Gems: {gem_count}")

def upgrade_money_per_click():
    global money_per_click, money_count, upgrade_cost, money_click_upgrades
    if money_count >= upgrade_cost:
        money_count -= upgrade_cost
        money_click_upgrades += 1
        money_per_click += money_click_upgrades
        upgrade_cost += 10
        update_counters()
        save_data()

def upgrade_gems_per_click():
    global gem_count, gem_upgrade_cost, gem_click_upgrades, gems_per_click
    if gem_count >= gem_upgrade_cost:
        gem_count -= gem_upgrade_cost
        gem_click_upgrades += 1
        gems_per_click += gem_click_upgrades
        gem_upgrade_cost += 10
        update_counters()
        save_data()

def increment_money():
    global money_count
    money_count += money_per_click
    update_counters()
    save_data()

def increment_gems():
    global gem_count
    gem_count += gems_per_click
    update_counters()
    save_data()

def add_money():
    global money_count
    money_count += money_per_click
    update_counters()
    button_1.config(state="disabled")
    window.after(1000, add_money)

def add_gem():
    global gem_count
    gem_count += gems_per_click
    update_counters()
    button_3.config(state="disabled")
    window.after(1000, add_gem)

def open_google():
    url = "https://discord.gg/jvTkSgYzWj"
    webbrowser.open(url)

# Canvas and counters
canvas = tk.Canvas(
    window,
    bg="#FFFFFF",
    height=500,
    width=1000,
    bd=0,
    highlightthickness=0,
    relief="ridge",
)
canvas.pack()

money_text = tk.StringVar()
gem_text = tk.StringVar()

update_counters()

money_label = tk.Label(canvas, textvariable=money_text, font=("Inter", 12))
money_label.place(x=0, y=8)

gem_label = tk.Label(canvas, textvariable=gem_text, font=("Inter", 12))
gem_label.place(x=505, y=11)

# Buttons
button_1_img = load_image("button_1.png")
button_1 = tk.Button(
    image=button_1_img,
    borderwidth=0,
    highlightthickness=0,
    command=add_money,
    relief="flat",
)
button_1.place(x=131, y=92, width=263, height=20)

# ... Add other buttons here, following the same pattern as button_1

# Save game button
save_button_img = load_image("button_5.png")
save_button =
