from pathlib import Path
from importlib import import_module
from typing import List, Tuple, Type, Optional

from lessons.base import LessonBase, TaskBase, AnswerBase, StepBase


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
        lesson.tasks, lesson.answers = \
            load_tasks_and_answers(lesson_dir)
        lessons.append(lesson)
    return lessons


def load_tasks_and_answers(
    lesson_dir: Path
) -> Tuple[List[TaskBase], List[AnswerBase]]:
    tasks = []
    answers = []
    tasks_dir = lesson_dir / 'tasks'
    for task_dir in tasks_dir.iterdir():
        if task_dir.name.startswith('_'):
            continue
        task_module = import_module(
            f'lessons.lessons.{lesson_dir.name}.tasks.{task_dir.name}.task')
        answer_module = import_module(
            f'lessons.lessons.{lesson_dir.name}.tasks.{task_dir.name}.'
            f'answer')
        task = task_module.Task
        answer = answer_module.Answer
        answer.steps = load_steps(lesson_dir, task_dir)
        tasks.append(task)
        answers.append(answer)
    return tasks, answers


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


def get_lesson(pk: int) -> Optional[Type[LessonBase]]:
    index = pk - 1
    if index >= len(global_lessons):
        return None
    lesson_info = global_lessons[index]
    return lesson_info


def get_task(lesson: LessonBase, pk: int) -> Optional[Type[TaskBase]]:
    index = pk - 1
    if index >= len(lesson.tasks):
        return None
    task = lesson.tasks[index]
    return task


def get_answer(
    lesson: LessonBase,
    pk: int,
) -> Optional[Type[AnswerBase]]:
    index = pk - 1
    if index >= len(lesson.answers):
        return None
    answer = lesson.answers[index]
    return answer
