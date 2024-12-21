def main():
    task = input("Enter your task: ")

    priority = input("Priority (high/medium/low): ").lower()

    time_bound = input("Is it time-bound? (yes/no): ").lower()

    match priority:
        case "high":
            if time_bound == "yes":
                reminder = f"'{task}' is a high priority task that requires immediate attention today!"
            else:
                reminder = f"'{task}' is a high priority task. Consider completing it when you have free time."
        case "medium":
            if time_bound == "yes":
                reminder = f"'{task}' is a medium priority task that requires immediate attention today!"
            else:
                reminder = f"'{task}' is a medium priority task. Consider completing it when you have free time."
        case "low":
            reminder = f"'{task}' is a low priority task. Consider completing it when you have free time."
        case _:
            reminder = "Invalid priority level entered."

    print("Reminder:", reminder)

if __name__ == "__main__":
    main()
