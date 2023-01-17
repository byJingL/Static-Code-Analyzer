# write your code here
import os
import argparse

ISSUE_DICT = {
    'S001': 'Too long',
    'S002': 'Indentation is not a multiple of four',
    'S003': 'Unnecessary semicolon after a statement',
    'S004': 'Less than two spaces before inline comments',
    'S005': 'TODO found',
    'S006': 'More than two blank lines preceding a code line',
}


def get_issue_meaasge(line_num, error_code):
    """Return formatted message for give line number and issue code"""
    message = f"Line {line_num}: {error_code} {ISSUE_DICT[error_code]}"
    return message


def check_issues(data):
    """
    Return a dictionary contains all issue numbers for given file data with line number as keys.

    :param data: file data
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
    count = 0
    for char in s:
        if char == ' ':
            count += 1
        else:
            break
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
        issues = check_issues(data)
        for line in issues:
            if len(issues[line]) > 0:
                for issue in issues[line]:
                    warnings_on_path.append(get_issue_meaasge(line, issue))
        # warnings dict with path as keys and all issue messages as values
        warnings[path] = warnings_on_path

    for path in sorted(warnings):
        for info in warnings[path]:
            print(f"{path}: {info}")


if __name__ == "__main__":
    main()
