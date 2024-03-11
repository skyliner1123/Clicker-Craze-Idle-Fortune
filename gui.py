import json
import os
from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage, Label
import webbrowser

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\User 1\Downloads\Game\build\assets\frame0")
DATA_DIR = os.path.join(os.getenv('APPDATA'), 'ClickerCrazeIdleFortune')
DATA_FILE = os.path.join(DATA_DIR, 'game_data.json')

# Create the directory if it doesn't exist
os.makedirs(DATA_DIR, exist_ok=True)

# Load data if the file exists, or initialize with default values
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'r') as file:
        data = json.load(file)
    money_count = data.get('money_count', 0)
    gem_count = data.get('gem_count', 0)
    upgrade_cost = data.get('upgrade_cost', 1)
    money_per_click = data.get('money_per_click', 1)
    gem_upgrade_cost = data.get('gem_upgrade_cost', 1)
    gems_per_click = data.get('gems_per_click', 1)
    gem_click_upgrades = data.get('gem_click_upgrades', 0)
    money_click_upgrades = data.get('money_click_upgrades', 0)  # Initialize money_click_upgrades
else:
    money_count = 0
    gem_count = 0
    upgrade_cost = 1
    money_per_click = 1
    gem_upgrade_cost = 1
    gems_per_click = 1
    gem_click_upgrades = 0
    money_click_upgrades = 0  # Default value for money_click_upgrades

def save_data():
    data = {
        'money_count': money_count,
        'gem_count': gem_count,
        'money_per_click': money_per_click,
        'money_click_upgrades': money_click_upgrades,
        'gem_upgrade_cost': gem_upgrade_cost,
        'gems_per_click': gems_per_click,
        'gem_click_upgrades': gem_click_upgrades
    }
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file)


def save_game_popup():
    save_window = Tk()
    save_window.title("Game Saved")
    save_window.geometry("200x100")

    label = Label(save_window, text="Game Saved", font=("Helvetica", 16))
    label.pack(pady=20)

    save_window.after(2000, save_window.destroy)  # Close the window after 2 seconds

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()
window.title("Clicker Craze: Idle Fortune")
window.geometry("1000x500")
window.configure(bg="#FFFFFF")

def update_counters():
    canvas.itemconfig(money_text, text=f"Money: {money_count}")
    canvas.itemconfig(gem_text, text=f"Gems: {gem_count}")

def upgrade_money_per_click():
    global money_per_click, money_count, upgrade_cost, money_click_upgrades
    if money_count >= upgrade_cost:
        money_count -= upgrade_cost
        money_click_upgrades += 1  # Increment money_click_upgrades
        money_per_click += money_click_upgrades  # Increment money_per_click
        upgrade_cost += 10
        canvas.itemconfig(money_text, text=f"Money: {money_count}")
        canvas.itemconfig(upgrade_text, text=f"Upgrade Money Per Click (${upgrade_cost}): +{money_per_click}")
        save_data()

def upgrade_gems_per_click():
    global gem_count, gem_upgrade_cost, gem_click_upgrades, gems_per_click
    if gem_count >= gem_upgrade_cost:
        gem_count -= gem_upgrade_cost
        gem_click_upgrades += 1
        gems_per_click += gem_click_upgrades  # Increment gems_per_click
        gem_upgrade_cost += 10
        canvas.itemconfig(gem_text, text=f"Gems: {gem_count}")
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
    canvas.itemconfig(money_text, text=f"Money: {money_count}")
    button_1.config(state="disabled")  # Disable the button after it's clicked
    window.after(1000, add_money)  # Schedule the function to run again after 1000 milliseconds (1 second)

def add_gem():
    global gem_count
    gem_count += gems_per_click
    canvas.itemconfig(gem_text, text=f"Gems: {gem_count}")
    button_3.config(state="disabled")  # Disable the button after it's clicked
    window.after(1000, add_gem)  # Schedule the function to run again after 1000 milliseconds (1 second)

def open_google():
    url = "https://discord.gg/jvTkSgYzWj"
    webbrowser.open(url)

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=500,
    width=1000,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
canvas.create_rectangle(
    0.0,
    0.0,
    500.0,
    40.0,
    fill="#B0FFAF",
    outline="")

canvas.create_rectangle(
    500.0,
    0.0,
    1000.0,
    40.0,
    fill="#FF7A7A",
    outline="")

money_text = canvas.create_text(
    0.0,
    8.0,
    anchor="nw",
    text=f"Money: {money_count}",
    fill="#000000",
    font=("Inter", 12 * -1)
)

upgrade_text = canvas.create_text(
    131,
    129,
    anchor="nw",
    text=f"Upgrade Money Per Click (${upgrade_cost}): +{money_per_click}",  # Display initial upgrade info
    fill="#000000",
    font=("Inter", 12 * -1)
)

gem_text = canvas.create_text(
    505.0,
    11.0,
    anchor="nw",
    text=f"Gems: {gem_count}",
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_rectangle(
    0.0,
    40.0,
    500.0,
    500.0,
    fill="#D7FFD6",
    outline="")

canvas.create_rectangle(
    500.0,
    40.0,
    1000.0,
    500.0,
    fill="#FFA3A3",
    outline="")

canvas.create_text(
    716.0,
    482.0,
    anchor="nw",
    text="Made My RustyCMD, GUI Made With Figma",
    fill="#000000",
    font=("Inter", 15 * -1)
)

button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=add_money,
    relief="flat"
)
button_1.place(x=131.0, y=92.0, width=263.0, height=20.0)

button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=increment_money,
    relief="flat"
)
button_2.place(x=131.0, y=57.0, width=263.0, height=20.0)

button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=add_gem,
    relief="flat"
)
button_3.place(x=625.0, y=96.0, width=241.0, height=16.0)

button_image_4 = PhotoImage(file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=increment_gems,
    relief="flat"
)
button_4.place(x=625.0, y=59.0, width=241.0, height=18.0)

button_image_5 = PhotoImage(file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: [save_data(), save_game_popup()],  # Trigger the save_data function and show popup
    relief="flat"
)
button_5.place(x=0.0, y=482.0, width=35.0, height=18.0)

button_image_6 = PhotoImage(file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=open_google,  # Call the open_google function
    relief="flat"
)
button_6.place(x=445.0, y=482.0, width=55.0, height=18.0)

button_image_8 = PhotoImage(file=relative_to_assets("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=upgrade_gems_per_click,
    relief="flat"
)
button_8.place(x=625.0, y=135.0, width=241.0, height=18.0)

button_image_7 = PhotoImage(file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=upgrade_money_per_click,
    relief="flat"
)
button_7.place(x=131.0, y=129.0, width=263.0, height=20.0)

# Save data when the window is closed
def on_closing():
    save_data()
    window.destroy()

window.protocol("WM_DELETE_WINDOW", on_closing)

window.resizable(False, False)
window.mainloop()
