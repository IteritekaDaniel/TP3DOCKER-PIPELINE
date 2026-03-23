tasks = ['task1', 'task2']

def add_task(task):
    tasks.append(task)
    return task

def get_tasks():
    return tasks

def delete_task(task):
    if task in tasks:
        tasks.remove(task)
        return True
    return False