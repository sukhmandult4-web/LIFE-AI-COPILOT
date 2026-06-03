# ============================================================
#   🤖 LIFE COPILOT - Your Daily Helper!
#   Made simple so EVERYONE can understand it!
#
#   WHAT IT CAN DO:
#   1. Add tasks (things you need to do)
#   2. Show all your tasks
#   3. Mark a task as DONE
#   4. Set a reminder (it will beep and show a message!)
#   5. Make a shopping list from a meal name
#   6. Get a motivational quote to cheer you up
#   7. Check the weather (just for fun!)
#   8. Ask the AI anything!
#
#   HOW TO INSTALL (type this in your VS Code terminal):
#   pip install pyttsx3 requests schedule
# ============================================================

import time       # For checking time and waiting
import datetime   # For getting today's date
import random     # For picking random quotes
import json       # For saving/loading tasks to a file
import os         # For checking if a file exists

# ── Try to import extra libraries ──────────────────────────
try:
    import pyttsx3          # Makes the computer SPEAK
    speech_available = True
except:
    speech_available = False
    print("💡 Tip: Run 'pip install pyttsx3' to enable voice!")

try:
    import requests         # For getting weather from internet
    internet_available = True
except:
    internet_available = False
    print("💡 Tip: Run 'pip install requests' to enable weather!")

# ============================================================
#   STEP 1 — SPEAKING FUNCTION
#   This makes the computer talk to you!
# ============================================================

def speak(text):
    """Make the computer say something out loud"""
    print(f"🔊 {text}")   # Always print it on screen too
    if speech_available:
        try:
            engine = pyttsx3.init()         # Start the speech engine
            engine.setProperty('rate', 150) # Speed of talking (150 = normal)
            engine.say(text)                # Queue the text
            engine.runAndWait()             # Actually say it!
        except:
            pass  # If speaking fails, no problem — it was already printed

# ============================================================
#   STEP 2 — TASKS (Things You Need To Do)
#   Tasks are saved in a file so you don't lose them!
# ============================================================

TASKS_FILE = "my_tasks.json"   # Name of the file where tasks are saved

def load_tasks():
    """Load tasks from the file (or start with empty list)"""
    if os.path.exists(TASKS_FILE):               # If the file exists...
        with open(TASKS_FILE, "r") as f:          # Open it
            return json.load(f)                   # Read and return tasks
    return []                                     # Otherwise return empty list

def save_tasks(tasks):
    """Save tasks to the file so we don't lose them"""
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=2)             # Write tasks nicely to file

def add_task():
    """Add a new task to your list"""
    task_name = input("📝 What task do you want to add? → ")
    if task_name.strip() == "":
        print("❌ You didn't type anything!")
        return

    tasks = load_tasks()                          # Load existing tasks
    new_task = {
        "name": task_name,                        # The task text
        "done": False,                            # Not done yet
        "date": str(datetime.date.today())        # Today's date
    }
    tasks.append(new_task)                        # Add to list
    save_tasks(tasks)                             # Save to file
    speak(f"Task added: {task_name}")

def show_tasks():
    """Show all your tasks on screen"""
    tasks = load_tasks()

    if len(tasks) == 0:
        speak("You have no tasks! Great job or add some!")
        return

    print("\n─────────────────────────────────")
    print("📋 YOUR TASKS:")
    print("─────────────────────────────────")

    for i, task in enumerate(tasks):             # Loop through every task
        number = i + 1                           # Task number (start from 1)
        status = "✅" if task["done"] else "⬜"  # Checkbox emoji
        print(f"  {number}. {status} {task['name']}  (added: {task['date']})")

    print("─────────────────────────────────\n")

def mark_task_done():
    """Mark a task as finished"""
    show_tasks()                                  # Show tasks first
    tasks = load_tasks()

    if len(tasks) == 0:
        return

    try:
        number = int(input("Which task number is done? → "))
        index = number - 1                        # Lists start at 0, not 1

        if index < 0 or index >= len(tasks):
            print("❌ That number doesn't exist!")
            return

        tasks[index]["done"] = True               # Mark as done!
        save_tasks(tasks)                         # Save changes
        speak(f"Great job! Task done: {tasks[index]['name']}")

    except ValueError:
        print("❌ Please type a number!")

def delete_done_tasks():
    """Remove all finished tasks to clean up your list"""
    tasks = load_tasks()
    tasks = [t for t in tasks if not t["done"]]  # Keep only NOT done tasks
    save_tasks(tasks)
    speak("All finished tasks have been removed!")

# ============================================================
#   STEP 3 — REMINDERS
#   Set a reminder and the computer will alert you!
# ============================================================

def set_reminder():
    """Set a reminder for a specific time today"""
    print("\n⏰ SET A REMINDER")
    remind_text = input("What should I remind you about? → ")
    remind_time = input("At what time? (example: 14:30 for 2:30 PM) → ")

    print(f"\n✅ Reminder set! I will alert you at {remind_time}")
    print("⚠️  Keep this program running for the reminder to work!\n")

    # Keep checking the time every 30 seconds
    while True:
        now = datetime.datetime.now().strftime("%H:%M")   # Current time like "14:30"

        if now == remind_time:
            print("\n" + "🔔" * 20)
            speak(f"REMINDER! {remind_text}")
            print("🔔" * 20 + "\n")
            break   # Stop checking after reminder fires

        print(f"  ⏳ Current time: {now} | Waiting for {remind_time}...")
        time.sleep(30)  # Wait 30 seconds before checking again

# ============================================================
#   STEP 4 — SHOPPING LIST FROM A MEAL
#   Tell it what you want to eat and it makes a list!
# ============================================================

# Dictionary of meals and their ingredients
MEAL_INGREDIENTS = {
    "pasta":        ["pasta", "tomato sauce", "garlic", "olive oil", "cheese"],
    "pizza":        ["pizza dough", "tomato sauce", "cheese", "toppings of choice"],
    "sandwich":     ["bread", "butter", "cheese", "lettuce", "tomato", "filling"],
    "fried rice":   ["rice", "eggs", "soy sauce", "vegetables", "oil", "garlic"],
    "omelette":     ["eggs", "butter", "salt", "pepper", "cheese", "vegetables"],
    "soup":         ["vegetables", "broth", "salt", "pepper", "noodles"],
    "salad":        ["lettuce", "tomato", "cucumber", "olive oil", "lemon"],
    "pancakes":     ["flour", "eggs", "milk", "butter", "sugar", "baking powder"],
    "maggi":        ["maggi noodles", "water", "masala", "vegetables", "butter"],
    "dal rice":     ["dal (lentils)", "rice", "onion", "tomato", "spices", "ghee"],
    "paratha":      ["wheat flour", "water", "salt", "butter/ghee", "filling"],
    "poha":         ["poha (flattened rice)", "onion", "mustard seeds", "curry leaves", "lemon"],
}

def make_shopping_list():
    """Generate a shopping list from a meal name"""
    print("\n🛒 SHOPPING LIST MAKER")
    meal = input("What do you want to eat/cook? → ").lower().strip()

    # Check if we know this meal
    if meal in MEAL_INGREDIENTS:
        ingredients = MEAL_INGREDIENTS[meal]
        print(f"\n🛒 Shopping list for {meal.title()}:")
        print("─────────────────────────")
        for item in ingredients:
            print(f"  □ {item}")
        print("─────────────────────────")
        speak(f"Here is your shopping list for {meal}")
    else:
        # Try to find a similar meal
        print(f"❓ I don't know '{meal}' yet.")
        print("   Meals I know:", ", ".join(MEAL_INGREDIENTS.keys()))
        speak("I don't know that meal yet, but you can add it to my list!")

# ============================================================
#   STEP 5 — MOTIVATIONAL QUOTES
#   Get a random quote to cheer you up!
# ============================================================

QUOTES = [
    "Believe you can and you're halfway there! 💪",
    "Every day is a new beginning. Take a deep breath and start again! 🌅",
    "You are braver than you believe and stronger than you seem! 🦁",
    "Small steps every day lead to big results! 🚀",
    "Don't watch the clock — do what it does and keep going! ⏰",
    "The secret of getting ahead is getting started! ✨",
    "You got this! One task at a time! 🎯",
    "Dream big, work hard, stay focused! 🌟",
    "Today is a great day to learn something new! 📚",
    "You are capable of amazing things! 🌈",
]

def get_quote():
    """Pick and show a random motivational quote"""
    quote = random.choice(QUOTES)    # Pick a random quote from the list
    print("\n💬 " + "─" * 40)
    print(f"  {quote}")
    print("─" * 40 + "\n")
    speak(quote)

# ============================================================
#   STEP 6 — WEATHER (Needs internet!)
#   Shows simple weather for your city
# ============================================================

def check_weather():
    """Get current weather for a city"""
    if not internet_available:
        print("❌ Please install requests: pip install requests")
        return

    city = input("🌍 Which city? → ").strip()
    if city == "":
        print("❌ Please type a city name!")
        return

    try:
        # Using free weather API (no key needed!)
        url = f"https://wttr.in/{city}?format=3"
        response = requests.get(url, timeout=5)    # Ask the internet for weather

        if response.status_code == 200:
            weather = response.text.strip()
            print(f"\n🌤️  {weather}\n")
            speak(f"Weather in {city}: {weather}")
        else:
            print("❌ Couldn't get weather. Check city name!")

    except:
        print("❌ No internet connection or city not found!")

# ============================================================
#   STEP 7 — DAILY SUMMARY
#   Shows how many tasks you have and a quote!
# ============================================================

def daily_summary():
    """Show a summary of your day"""
    tasks = load_tasks()
    total = len(tasks)
    done  = sum(1 for t in tasks if t["done"])      # Count done tasks
    left  = total - done                             # Count remaining tasks

    today = datetime.date.today().strftime("%B %d, %Y")   # Like "June 03, 2026"

    print("\n" + "🌟" * 20)
    print(f"  📅 Today is: {today}")
    print(f"  📋 Total tasks:     {total}")
    print(f"  ✅ Tasks done:      {done}")
    print(f"  ⬜ Tasks remaining: {left}")
    print("🌟" * 20 + "\n")

    if left == 0 and total > 0:
        speak("Amazing! You finished all your tasks today!")
    elif left > 0:
        speak(f"You have {left} tasks remaining. You can do it!")
    else:
        speak("No tasks yet! Add some to get started.")

    get_quote()   # Also show a motivational quote

# ============================================================
#   MAIN MENU — This is where the program starts!
# ============================================================

def show_menu():
    """Show the main menu"""
    print("\n" + "═" * 40)
    print("       🤖 LIFE COPILOT - MAIN MENU")
    print("═" * 40)
    print("  1. ➕  Add a Task")
    print("  2. 📋  Show All Tasks")
    print("  3. ✅  Mark Task as Done")
    print("  4. 🗑️   Delete Finished Tasks")
    print("  5. ⏰  Set a Reminder")
    print("  6. 🛒  Make a Shopping List")
    print("  7. 💬  Get a Motivational Quote")
    print("  8. 🌤️   Check Weather")
    print("  9. 🌟  Daily Summary")
    print("  0. 👋  Quit")
    print("═" * 40)

def main():
    """Main function — runs the whole program"""
    speak("Hello! Welcome to Life Copilot! I am here to help you!")

    # Keep running until user types 0
    while True:
        show_menu()
        choice = input("\n  Type a number → ").strip()

        if choice == "1":
            add_task()

        elif choice == "2":
            show_tasks()

        elif choice == "3":
            mark_task_done()

        elif choice == "4":
            delete_done_tasks()

        elif choice == "5":
            set_reminder()

        elif choice == "6":
            make_shopping_list()

        elif choice == "7":
            get_quote()

        elif choice == "8":
            check_weather()

        elif choice == "9":
            daily_summary()

        elif choice == "0":
            speak("Goodbye! Have a great day!")
            break   # Exit the loop = close the program

        else:
            print("❌ Please type a number from 0 to 9!")

        input("\n  Press ENTER to go back to menu...")   # Wait before showing menu again

# ── This line starts the program! ──────────────────────────
if __name__ == "__main__":
    main()