# parse cmd to flag and args
def parse(cmd):
    parsed = cmd.split(' ')

    program_name = parsed[0]

    flags = []
    args = []

    arg = ''
    for word in parsed[1:]:

        if '-' in word:
            if flags:
                args.append(arg)

            arg = ''
            flags.append(word)
        else:
            if not arg:
                arg = word
            else:
                arg += ' ' + word

    args.append(arg)

    return program_name, flags, args


def checkString(arg):
    for letter in arg:
        if not (letter.isupper() or letter.islower()):
            return False

    return True


def checkNumber(arg):
    for letter in arg:
        if not letter.isnumeric():
            return False
    return True


def solution(program, flag_rules, commands):
    answer = []

    # make dictionary for flag rules
    rule_dict = {}
    for rule in flag_rules:
        parsed_rule = rule.split(' ')
        cmd = parsed_rule[0]
        rule = parsed_rule[1]
        rule_dict[cmd] = rule

    # fo each cmd, parse and check
    for command in commands:
        program_name, flags, args = parse(command)

        # check program
        if program_name != program:
            answer.append(False)
            continue

        # check flag_rules
        fail_flag = 0
        print(flags, args)

        if len(flags) != len(args):
            answer.append(False)
            continue

        for idx in range(len(flags)):


            cmd = flags[idx]
            arg = args[idx]

            print(cmd)
            if cmd in rule_dict:  # check if command is provided
                rule = rule_dict[cmd]

            else:  # no command found
                answer.append(False)
                break

            if rule == 'STRING':
                if not checkString(arg):
                    print("string fail")
                    fail_flag = 1

            elif rule == 'NUMBER':
                if not checkNumber(arg):
                    print("number fail")
                    fail_flag = 1

            elif rule == 'NULL':
                if arg:
                    print("null fail")
                    fail_flag = 1

            if fail_flag:
                answer.append(False)
                break

        # if all flags works,
        else:
            answer.append(True)

    return answer


a= "line"
b=["-s STRING", "-n NUMBER", "-e NULL"]
c=["line -s 123 -n HI", "line fun"]
solution(a,b,c)