# ===== PYTHON TO-DO MANAGER =====
# This program teaches you about Python lists and how to work with them
# A list is like a container that holds multiple items in order


# ===== STEP 1: CREATE A LIST OF TASKS =====
# A list is created using square brackets [ ]
# Items in the list are separated by commas

tasks = [
    "Learn Python",
    "Build projects",
    "Get first client",
    "Master functions",
    "Create a portfolio"
]

# When you create a list, Python remembers the order!
# You can access items by their position (starting from 0):
# tasks[0] = "Learn Python"
# tasks[1] = "Build projects"
# etc.


# ===== STEP 2: FUNCTION TO DISPLAY ALL TASKS =====
# This function shows all tasks with numbers

def display_tasks():
    """
    This function displays all tasks with numbers (1, 2, 3...)

    Why use a function? So we can display tasks anytime without rewriting the code!
    """

    print("\n=== YOUR TASKS ===")

    # len(tasks) tells us how many items are in the list
    print(f"You have {len(tasks)} tasks:\n")

    # range(len(tasks)) creates numbers 0, 1, 2, 3, 4
    # We use i to go through each position in the list
    for i in range(len(tasks)):
        # i is the position (0, 1, 2...)
        # i + 1 converts it to display as 1, 2, 3... (humans count from 1, not 0!)
        # tasks[i] gets the task at position i
        print(f"{i + 1}. {tasks[i]}")


# ===== STEP 3: FUNCTION TO ADD A NEW TASK =====
# This function adds a task to the list

def add_task(new_task):
    """
    This function adds a new task to the to-do list.

    Parameter:
    - new_task: The new task to add (a string)

    List method used: append()
    - append() adds an item to the END of a list
    - Example: tasks.append("Learn AI") adds "Learn AI" to the end
    """

    # append() is a list method that adds something to the end
    tasks.append(new_task)

    # Confirm to the user that the task was added
    print(f"✓ Added task: '{new_task}'")


# ===== STEP 4: FUNCTION TO REMOVE A TASK =====
# This function removes a task from the list

def remove_task(task_number):
    """
    This function removes a task by its number (1, 2, 3...)

    Parameter:
    - task_number: The number of the task to remove (1-indexed, not 0-indexed)

    List method used: pop()
    - pop(index) removes an item at a specific position
    - Example: tasks.pop(0) removes the first task
    """

    # We subtract 1 because:
    # - User sees task "1" but Python stores it at position 0
    # - User sees task "2" but Python stores it at position 1
    # - So we convert: task_number 1 → position 0, task_number 2 → position 1
    position = task_number - 1

    # Check if the task number is valid
    if position < 0 or position >= len(tasks):
        print(f"❌ Error: Task #{task_number} doesn't exist!")
        return

    # Get the task name before removing it (so we can tell the user what was removed)
    removed_task = tasks[position]

    # pop() removes and returns the item at the position
    tasks.pop(position)

    # Confirm to the user that the task was removed
    print(f"✓ Removed task: '{removed_task}'")


# ===== TESTING THE PROGRAM =====
# Now let's use all our functions!

print("🎯 PYTHON TO-DO MANAGER")
print("=" * 30)

# Display the original tasks
display_tasks()

# Add a new task
print("\n--- Adding a new task ---")
add_task("Learn data structures")

# Show tasks again
display_tasks()

# Add another task
print("\n--- Adding another task ---")
add_task("Build a web app")

# Show tasks again
display_tasks()

# Remove a task (remove task #2 "Build projects")
print("\n--- Removing a task ---")
remove_task(2)

# Show tasks one more time
display_tasks()

# Try to remove a task that doesn't exist (to show error handling)
print("\n--- Trying to remove a task that doesn't exist ---")
remove_task(100)

# Final display
display_tasks()


# ===== BONUS: LEARNING ABOUT LISTS =====
print("\n\n=== BONUS: LIST INFORMATION ===")
print(f"Total tasks: {len(tasks)}")
print(f"First task: {tasks[0]}")
print(f"Last task: {tasks[-1]}")  # -1 gets the last item!
print(f"All tasks: {tasks}")
