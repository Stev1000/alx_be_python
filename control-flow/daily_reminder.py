# Prompt for task description
task = input("Enter your task: ")

# Prompt for whether the task is time-bound
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Prompt for task priority
priority = input("Priority (high/medium/low): ").lower()

# Determine priority message using match-case
match priority:
    case 'high':
        priority_message = f"'{task}' is a high priority task"
    case 'medium':
        priority_message = f"'{task}' is a medium priority task"
    case 'low':
        priority_message = f"'{task}' is a low priority task"
    case _:
        priority_message = f"'{task}' has an unknown priority"

# Modify the reminder based on whether the task is time-bound
if time_bound == 'yes':
    reminder_message = "that requires immediate attention today!"
else:
    reminder_message = "that does not require immediate attention."

# Print the customized reminder
print(f"Reminder: {priority_message} {reminder_message}")