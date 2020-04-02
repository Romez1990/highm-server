from pathlib import Path
from importlib import import_module
from typing import List


def load_lessons() -> List:
    lessons: List = []
    current_dir = Path(__file__)
    lessons_dir = current_dir.parent / '..' / 'lessons'
    for lesson_dir in lessons_dir.iterdir():
        if lesson_dir.name.startswith('_'):
            continue
        lesson_module = import_module(
            f'lessons.lessons.{lesson_dir.name}.lesson')
        lesson = lesson_module.Lesson
        lesson.tasks = load_tasks(lesson_dir)
        lessons.append(lesson)
    return lessons


def load_tasks(lesson_dir: Path) -> List:
    tasks = []
    tasks_dir = lesson_dir / 'tasks'
    for task_dir in tasks_dir.iterdir():
        if task_dir.name.startswith('_'):
            continue
        task_module = import_module(
            f'lessons.lessons.{lesson_dir.name}.tasks.{task_dir.name}.task')
        task = task_module.Task
        task.steps = load_steps(lesson_dir, task_dir)
        tasks.append(task)
    return tasks


def load_steps(lesson_dir: Path, task_dir: Path) -> List:
    steps = []
    steps_dir = task_dir / 'steps'
    for step_dir in steps_dir.iterdir():
        if step_dir.name.startswith('_'):
            continue
        step_module = \
            import_module(f'lessons.lessons.{lesson_dir.name}.tasks.'
                          f'{task_dir.name}.steps.{step_dir.stem}')
        steps.append(step_module)
    return steps


lessons: List = None


def load() -> None:
    global lessons
    lessons = load_lessons()


def get_lesson(pk: str):
    try:
        index = int(pk) - 1
    except ValueError:
        raise ValueError()
    try:
        lesson_info = lessons[index]
    except IndexError:
        raise ValueError()
    return lesson_info


def get_task(lesson, pk: str):
    try:
        index = int(pk) - 1
    except ValueError:
        raise ValueError()
    try:
        task = lesson.tasks[index]
    except IndexError:
        raise ValueError()
    return task
