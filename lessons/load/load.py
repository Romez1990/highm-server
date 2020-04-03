from pathlib import Path
from importlib import import_module
from typing import List, Tuple, Type

from lessons.base import LessonBase, TaskBase, TaskAnswerBase, StepBase


def load_lessons() -> List[LessonBase]:
    lessons: List[LessonBase] = []
    current_dir = Path(__file__)
    lessons_dir = current_dir.parent / '..' / 'lessons'
    for lesson_dir in lessons_dir.iterdir():
        if lesson_dir.name.startswith('_'):
            continue
        lesson_module = import_module(
            f'lessons.lessons.{lesson_dir.name}.lesson')
        lesson = lesson_module.Lesson
        lesson.tasks, lesson.task_answers = \
            load_tasks_and_task_answers(lesson_dir)
        lessons.append(lesson)
    return lessons


def load_tasks_and_task_answers(
    lesson_dir: Path
) -> Tuple[List[TaskBase], List[TaskAnswerBase]]:
    tasks = []
    task_answers = []
    tasks_dir = lesson_dir / 'tasks'
    for task_dir in tasks_dir.iterdir():
        if task_dir.name.startswith('_'):
            continue
        task_module = import_module(
            f'lessons.lessons.{lesson_dir.name}.tasks.{task_dir.name}.task')
        task_answer_module = import_module(
            f'lessons.lessons.{lesson_dir.name}.tasks.{task_dir.name}.'
            f'task_answer')
        task = task_module.Task
        task_answer = task_answer_module.TaskAnswer
        task_answer.steps = load_steps(lesson_dir, task_dir)
        tasks.append(task)
        task_answers.append(task_answer)
    return tasks, task_answers


def load_steps(lesson_dir: Path, task_dir: Path) -> List[StepBase]:
    steps = []
    steps_dir = task_dir / 'steps'
    for step_dir in steps_dir.iterdir():
        if step_dir.name.startswith('_'):
            continue
        step_module = \
            import_module(f'lessons.lessons.{lesson_dir.name}.tasks.'
                          f'{task_dir.name}.steps.{step_dir.stem}')
        step = step_module.Step()
        steps.append(step)
    return steps


global_lessons: List[Type[LessonBase]] = []


def load() -> None:
    global global_lessons
    global_lessons = load_lessons()


def get_lessons() -> List[Type[LessonBase]]:
    return global_lessons


def get_lesson(pk: int) -> Type[LessonBase]:
    index = pk - 1
    try:
        lesson_info = global_lessons[index]
    except IndexError:
        raise ValueError()
    return lesson_info


def get_task(lesson: LessonBase, pk: int) -> Type[TaskBase]:
    index = pk - 1
    try:
        task = lesson.tasks[index]
    except IndexError:
        raise ValueError()
    return task


def get_task_answer(lesson: LessonBase, pk: int) -> Type[TaskAnswerBase]:
    index = pk - 1
    try:
        task_answer = lesson.task_answers[index]
    except IndexError:
        raise ValueError()
    return task_answer
