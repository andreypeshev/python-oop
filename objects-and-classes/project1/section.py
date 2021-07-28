from project.task import Task


class Section:

    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        if new_task not in self.tasks:
            self.tasks.append(new_task)
            return f"Task {new_task.details()} is added to the section"
        return f"Task is already in the section {self.name}"

    def complete_task(self, task_name: str):
        for task in self.tasks:
            if task.name == task_name:
                self.tasks[self.tasks.index(task_name)].completed = True
                return f"Completed task {task_name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        cleaned_tasks = 0
        for task in self.tasks:
            if task.completed:
                self.tasks.remove(task)
                cleaned_tasks += 1
        return f"Cleared {cleaned_tasks} tasks."

    def view_section(self):
        tasks_details = []
        nl = "\n"
        for task in self.tasks:
            tasks_details.append(task.details())
        return f"Section {self.name}:\n" \
               f"{nl.join(tasks_details)}"


task = Task("Make bed", "27/05/2020")
print(task.change_name("Go to University"))
print(task.change_due_date("28.05.2020"))
task.add_comment("Don't forget laptop")
print(task.edit_comment(0, "Don't forget laptop and notebook"))
print(task.details())
section = Section("Daily tasks")
print(section.add_task(task))
second_task = Task("Make bed", "27/05/2020")
section.add_task(second_task)
print(section.clean_section())
print(section.view_section())