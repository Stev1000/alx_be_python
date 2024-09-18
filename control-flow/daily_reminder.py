task = input("Enter the task description: ")

# Prompt for task priority
priority = input("Enter the task priority (high, medium, low): ").lower()

# Prompt for whether the task is time-bound
time_bound = input("Is the task time-bound (yes or no)? ").lower()

# Determine if the task needs immediate attention
if time_bound == 'yes':
    immediate_attention = "requires immediate attention today!"
else:
    immediate_attention = "does not require immediate attention."

# Print the reminder
print(f"Task: {task}")
print(f"Priority: {priority.capitalize()}")
print(f"This task {immediate_attention}")