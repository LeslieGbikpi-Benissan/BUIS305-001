class ToDoTask:
    def __init__(self, description):
        self.description = description
        self.completed = False

class ChoresToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f'Chore "{task.description}" added to the to-do list.')

    def mark_as_completed(self, task_description):
        for task in self.tasks:
            if task.description == task_description:
                task.completed = True
                print(f'Chore "{task_description}" marked as completed.')
                return
        print(f'Chore "{task_description}" not found.')

    def display_tasks(self):
        if not self.tasks:
            print('No chores in the to-do list.')
        else:
            print('Chores To-Do List:')
            for task in self.tasks:
                status = 'Completed' if task.completed else 'Not Completed'
                print(f'{task.description} - {status}')
                
chores_list = ChoresToDoList()
chores_list.add_task(ToDoTask('Do BUIS 305 Homework'))
chores_list.add_task(ToDoTask('Post Lab Reflections to Slack'))
chores_list.add_task(ToDoTask('Complete all Labs Before 15 December 23'))
chores_list.add_task(ToDoTask('Ace the Presentation for This Project in Class!'))

while True:
    print("\nOptions:")
    print("1. Display Chores")
    print("2. Mark Chore as Completed")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == '1':
        chores_list.display_tasks()
    elif choice == '2':
        task_description = input("Enter the chore description to mark as completed: ")
        chores_list.mark_as_completed(task_description)
    elif choice == '3':
        print("YOU COMPLETED ALL YOUR TASKS! :) Good Job!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 3.")
