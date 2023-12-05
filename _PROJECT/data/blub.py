import shutil

terminal_size = shutil.get_terminal_size()
columns, rows = terminal_size.columns, terminal_size.lines

header_str_offset = 4
header = "╔" + "═"*header_str_offset + "═" * (columns - 2 - header_str_offset) + "╗"
footer = "╚" + "═" * (columns - 2) + "╝"
boarder = header + "\n"

for _ in range(int((rows - 2))-2):
    boarder += "║" + " " * (columns - 2) + "║" + "\n"
boarder += footer

print(boarder)