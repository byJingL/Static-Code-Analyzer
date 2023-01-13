# write your code here
Code_dict = {
    'S001': 'Too long',
    'S002': 'Indentation is not a multiple of four',
    'S003': 'Unnecessary semicolon after a statement',
    'S004': 'Less than two spaces before inline comments',
    'S005': 'TODO found',
    'S006': 'More than two blank lines preceding a code line',
}


def get_issue_meaasge(line_num, error_code):
    message = f"Line {line_num}: {error_code} {Code_dict[error_code]}"
    return message


def issue_s001(s):
    if len(s) > 79:
        return True


def issue_s002(s):
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
    if '#' in s:
        if ';' in s.split('#')[0]:
            return True
    else:
        if s[-1] == ';':
            return True
    return False


def issue_s004(s):
    if '#' in s:
        if s[0] != '#':
            part1 = s.split('#')[0]
            if part1[-2:] != '  ':
                return True
    return False


def issue_s005(s):
    if '#' in s:
        if s[0] == '#':
            todo_check = s
        else:
            comment_index = s.index('#')
            todo_check = s[comment_index:]

        if 'todo' in todo_check.lower():
            return True

    return False


def main():
    file_path = input()
    with open(file_path, 'r') as file:
        data = file.read()
        data = data.splitlines()

    warnings = []
    for i in range(len(data)):

        if data[i] == '':
            continue

        if issue_s001(data[i]):
            warnings.append(get_issue_meaasge(i + 1, 'S001'))

        if issue_s002(data[i]):
            warnings.append(get_issue_meaasge(i + 1, 'S002'))

        if issue_s003(data[i]):
            warnings.append(get_issue_meaasge(i + 1, 'S003'))

        if issue_s004(data[i]):
            warnings.append(get_issue_meaasge(i + 1, 'S004'))

        if issue_s005(data[i]):
            warnings.append(get_issue_meaasge(i + 1, 'S005'))

        if i > 2 and data[i] != '':
            if data[i - 1] == '' and data[i - 2] == '' and data[i - 3] == '':
                warnings.append(get_issue_meaasge(i + 1, 'S006'))

    for info in warnings:
        print(info)


if __name__ == "__main__":
    main()
