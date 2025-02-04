FILEPATH= 'todo.txt'


def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of
    to-do items.
    :param filepath:
    :return: todos_list
    """
    with open(filepath, "r") as file_r:
         todos_local = file_r.readlines()
    return todos_local


def write_todos(new_todos,filepath=FILEPATH):
    """ Write the to-do items list in the text file.
    """
    with open(filepath, "w") as file_w:
        file_w.writelines(new_todos)


if __name__=='__main__':
    print('hello')