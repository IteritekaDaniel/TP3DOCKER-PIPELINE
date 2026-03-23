import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../app")))

from tasks import add_task, get_tasks, delete_task

def setup_function():
    from tasks import tasks
    tasks.clear()
    tasks.extend(['task1', 'task2'])

def test_add_task():
    add_task("Learn Docker")
    assert "Learn Docker" in get_tasks()

def test_multiple_tasks():
    add_task("Learn CI")
    add_task("Learn DevOps")
    tasks_list = get_tasks()
    assert "Learn CI" in tasks_list
    assert "Learn DevOps" in tasks_list

def test_delete_task():
    add_task("Learn Docker")
    assert "Learn Docker" in get_tasks()
    result = delete_task("Learn Docker")
    assert result == True
    assert "Learn Docker" not in get_tasks()

def test_delete_nonexistent_task():
    result = delete_task("Nonexistent Task")
    assert result == False