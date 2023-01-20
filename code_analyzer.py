# write your code here
import os
import argparse
import re

ISSUE_DICT = {
    'S001': "Too long",
    'S002': "Indentation is not a multiple of four",
    'S003': "Unnecessary semicolon after a statement",
    'S004': "Less than two spaces before inline comments",
    'S005': "TODO found",
    'S006': "More than two blank lines preceding a code line",
}


def space_counter(string):
    """Return number of start spaces in given string."""
    num = 0
    for char in string:
        if char == ' ':
            num += 1
        else:
            break
    return num


def get_issue_meaasge(line_num, error_code):
    """Return formatted message for give line number and issue code"""
    message = f"Line {line_num}: {error_code} {ISSUE_DICT[error_code]}"
    return message


def check_issues1(data):
    """
    Return a dictionary contains issue01-06 for given file data with line number as keys.

    :param data: list of strings
    :return: dict = {
        1: [issue1, issue2, ...],
        2: [issue1, ...],
        ...,
    }
    """
    issue_dict = {}
    for i in range(len(data)):
        issue_on_line = []

        if data[i] == '':
            continue

        if issue_s001(data[i]):
            issue_on_line.append('S001')

        if issue_s002(data[i]):
            issue_on_line.append('S002')

        if issue_s003(data[i]):
            issue_on_line.append('S003')

        if issue_s004(data[i]):
            issue_on_line.append('S004')

        if issue_s005(data[i]):
            issue_on_line.append('S005')

        if i > 2 and data[i] != '':
            if data[i - 1] == '' and data[i - 2] == '' and data[i - 3] == '':
                issue_on_line.append('S006')

        issue_dict[i + 1] = issue_on_line

    return issue_dict


def check_issues2(data):
    """
    Return a list contains issue info of issue07-09 for given file data.

    :param data: file data
    :return: list = [info of issue7, info of issue8, ...]
    """
    issue_list = []
    for i in range(len(data)):

        if data[i] == '':
            continue

        if issue_s007(data[i]):
            message = issue_s007(data[i])
            issue_list.append(f"Line {i + 1}: S007 {message}")

        if issue_s008(data[i]):
            message = issue_s008(data[i])
            issue_list.append(f"Line {i + 1}: S008 {message}")

        if issue_s009(data[i]):
            message = issue_s009(data[i])
            issue_list.append(f"Line {i + 1}: S009 {message}")

    return issue_list


def get_files(path):
    """Return a list of all file path in the given dictionary path."""
    file_list = []
    for root, dirs, files in os.walk(path, topdown=True):
        for name in files:
            if name.split('.')[-1] == 'py' and name != 'tests.py':
                file_path = os.path.join(root, name)
                file_list.append(file_path)
    return file_list


# --------------------------- issue functions ----------------------- #
def issue_s001(s):
    """Return True if the length of the line > 79."""
    if len(s) > 79:
        return True


def issue_s002(s):
    """Return True if the indentation is not a multiple of four."""
    count = space_counter(s)
    if count % 4 != 0:
        return True
    return False


def issue_s003(s):
    """Return True if there's unnecessary semicolon."""
    if '#' in s:
        if ';' in s.split('#')[0]:
            return True
    else:
        if s[-1] == ';':
            return True
    return False


def issue_s004(s):
    """Return True if there's less than two spaces before inline comments."""
    if '#' in s:
        if s[0] != '#':
            part1 = s.split('#')[0]
            if part1[-2:] != '  ':
                return True
    return False


def issue_s005(s):
    """Return True if there's more than two blank lines preceding a code line"""
    if '#' in s:
        if s[0] == '#':
            todo_check = s
        else:
            comment_index = s.index('#')
            todo_check = s[comment_index:]

        if 'todo' in todo_check.lower():
            return True

    return False


def issue_s007(s):
    """Return issue message if there are too many spaces after construction_name (def or class)."""
    s = s.strip()  # s with no start spaces
    if s.split()[0] == 'class':
        if space_counter(s[5:]) > 1:
            return "Too many spaces after 'class'"
    if s.split()[0] == 'def':
        if space_counter(s[3:]) > 1:
            return "Too many spaces after 'def'"
    return False


def issue_s008(s):
    """Return issue message if Class name is not written in CamelCase."""
    s = s.strip()  # s with no start spaces
    if s.split()[0] == 'class':
        class_name = s.split()[1][:-1]
        if '_' in class_name or not re.match(r'[A-Z].+', class_name):
            if '(' in class_name:
                class_name = class_name.split('(')[0]
            return f"Class name '{class_name}' should use CamelCase"

    return False


def issue_s009(s):
    """Return issue message if function name is not written in snake_case."""
    s = s.strip()  # s with no start spaces
    if s.split()[0] == 'def':
        func_name = s.split()[1].split('(')[0]
        if not re.match(r'[a-z0-9_]+', func_name):
            return f"Function name '{func_name}' should use snake_case"
    return False


# --------------------------- main function ----------------------- #
def main():
    parser = argparse.ArgumentParser(description='Check the code style of python file.')
    parser.add_argument("path", help='Enter the path of dictionary or file to check.', default=None, nargs='?')
    args = parser.parse_args()
    path_to_check = args.path
    path_list = []

    # Check the path is a file or dictionary
    if os.path.isfile(path_to_check):
        if path_to_check.endswith('py'):
            path_list.append(path_to_check)
    else:
        path_list = get_files(path_to_check)

    warnings = {}
    for path in path_list:
        with open(path, 'r') as file:
            data = file.read()
            data = data.splitlines()

        warnings_on_path = []
        # Check issues 1-6
        issues1 = check_issues1(data)
        for line in issues1:
            if len(issues1[line]) > 0:
                for issue in issues1[line]:
                    warnings_on_path.append(get_issue_meaasge(line, issue))
        # Check issues 7-9
        issues2 = check_issues2(data)
        for message in issues2:
            warnings_on_path.append(message)
        # warnings dict with path as keys and all issue messages as values
        warnings[path] = warnings_on_path

    for path in sorted(warnings):
        for info in warnings[path]:
            print(f"{path}: {info}")


if __name__ == "__main__":
    main()
