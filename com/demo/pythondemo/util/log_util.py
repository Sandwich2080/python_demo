IS_DEBUG = True


def print_log(str_content):
    r"""A custom log print method.

    :param str_content: The content to print to console
    """
    if IS_DEBUG:
        print(str_content)
