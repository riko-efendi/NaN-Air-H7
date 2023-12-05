import os
import shutil

class UIUtils:
    def __init__(self) -> None:
        self.terminal_size = shutil.get_terminal_size()
        self.terminal_columns = self.terminal_size.columns
        self.terminal_rows = self.terminal_size.lines

    def clear_screen(self):
        """Clears the screen"""

        os_name = os.name.lower()
        if os_name == 'posix':  # Unix/Linux/MacOS
            os.system("clear")
        elif os_name == 'nt':   # Windows
            os.system("cls")

    def get_boarder(self, header_str="", options="",x_offset=0, y_offset=0):
        """Returns a boarder that goes around the dimensions of your terminal window."""
        
        header_str_offset = 4
        header = "╔" + "═"*header_str_offset + header_str + "═" * (self.terminal_columns - len(header_str) - 2 - header_str_offset) + "╗"
        footer = "╚" + "═" * (self.terminal_columns - 2) + "╝"
        boarder = header + "\n"

        for _ in range(int((self.terminal_rows - 2))-2):
            boarder += "║" + " " * (self.terminal_columns - 2) + "║" + "\n"
        boarder += footer
        boarder = self.append_string(boarder, options, x_offset, y_offset)

        return boarder
    
    def append_string(self, backgrnd, overlay, x_offset=0, y_offset=0):
        """Appends two strings; a background string and a foreground string, together"""

        backgrnd_list = backgrnd.split("\n")
        overlay_list = overlay.split("\n")

        # Calculate the center pivot
        x_offset = int(len(backgrnd_list[0]) / 2) - int(len(overlay_list[0]) / 2) + x_offset

        try:
            for i in range(y_offset, (y_offset + len(overlay_list))):
                backgrnd_list[i] = (
                    backgrnd_list[i][:x_offset] +
                    overlay_list[i - y_offset] +
                    backgrnd_list[i][x_offset + len(overlay_list[i - y_offset]) :]
                )
        except IndexError:
            return backgrnd

        result = "".join(element for element in backgrnd_list)
        return result