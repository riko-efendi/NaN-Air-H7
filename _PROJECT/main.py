from ui.main_menu_ui import MainMenuUI
from utils.ascii_art import AsciiAnimations

ascii_animations = AsciiAnimations()

main_menu = MainMenuUI()
main_menu.input_prompt()
ascii_animations.closing_screen()

