def capitalize(lines):
    for line in lines:
        for word in line.split(","):
            yield word.capitalize()