    task = input("Enter your task: ").strip()
    priority = input("Priority (high/medium/low): ").strip().lower()
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

    print()  # Blank line for readability
    match priority:
        case "high":
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
            else:
                print(f"Reminder: '{task}' is a high priority task. Try to complete it soon.")
        case "medium":
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a medium priority task that should be completed today.")
            else:
                print(f"Reminder: '{task}' is a medium priority task. Aim to finish it this week.")
        case "low":
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a low priority task, but it is time-bound. Try to finish it today.")
            else:
                print(f"Note: '{task}' is a low priority task. Consider doing it when you have spare time.")
        case _:
            print("Invalid priority. Please enter high, medium, or low.")
