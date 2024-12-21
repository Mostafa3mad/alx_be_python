def main():
    task = input("Enter your task: ")

    priority = input("Priority (high/medium/low): ").lower()

    time_bound = input("Is it time-bound? (yes/no): ").lower()

    reminder = ""
    match priority:
        case "high":
            reminder = f"'{task}' is a high priority task"
        case "medium":
            reminder = f"'{task}' is a medium priority task"
        case "low":
            reminder = f"'{task}' is a low priority task"
        case _:
            reminder = "Invalid priority level entered."

    if time_bound == "yes" and priority != "low":
        reminder += " that requires immediate attention today!"
    elif time_bound == "no" or priority == "low":
        reminder += ". Consider completing it when you have free time."

    print("\nReminder:", reminder)

if __name__ == "__main__":
    main()