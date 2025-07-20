
task = input("Enter your task: ")
priority = input("priority (high, medium, low): ")
bound = input("Is this task time-bound? (yes or no): ")

reminder_message = f"Reminder: You have a task '{task}' with {priority} priority."

match priority:
    case "high":
        reminder_message += " This task has high priority."
    case "medium":
        reminder_message += " This task has medium priority."
    case "low":
        reminder_message += " This task has low priority."
    case _:
        reminder_message += " Priority level not recognized."

if time_bound == "yes":
    reminder_message += " This requires immediate attention today!"

print(reminder_message)
