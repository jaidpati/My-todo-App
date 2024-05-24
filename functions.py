FILEPATH = "todos.txt"


def get_todos(filepath = FILEPATH):
    """
    Read a text file and return the list of
    to do items.
    """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """
     write the todo items list in todos file

    """
    with open(filepath, "w") as file:
        file.writelines(todos_arg)
def converter(feet, inches):
    meters = 0.3048 * feet + 0.0254 * inches
    return meters
