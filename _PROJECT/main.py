from ui.main_menu_ui import MainMenuUI
from utils.ascii_art import AsciiArt

ascii_animations = AsciiArt()

main_menu = MainMenuUI()
main_menu.input_prompt()
ascii_animations.closing_screen()

