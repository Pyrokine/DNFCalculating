def handle(content):
    result = ""
    indent_space = 4
    indent_times = 0
    need_line_break = True
    double_bracket = False

    len_content = len(content)
    i = 0

    while i < len_content:
        letter = content[i]
        if letter == "{":
            indent_times += 1
            result += "{\n" + "".join([" "] * indent_space * indent_times)
        elif letter == "}":
            indent_times -= 1
            result += "\n" + "".join([" "] * indent_space * indent_times) + "}"
        elif letter == "[":
            if not need_line_break:
                double_bracket = True
            need_line_break = False
            result += "["
        elif letter == "]":
            if double_bracket:
                double_bracket = False
            else:
                need_line_break = True
            result += "]"
        elif letter == ",":
            if need_line_break:
                result += ",\n" + "".join([" "] * indent_space * indent_times)
                if i + 1 < len_content:
                    if content[i + 1] == " ":
                        i += 1
            else:
                result += ","
        else:
            result += letter

        i += 1

    return result
