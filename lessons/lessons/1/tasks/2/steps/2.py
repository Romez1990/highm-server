from numpy import trace


def check(task):
    return task.trace == trace(task.product)
