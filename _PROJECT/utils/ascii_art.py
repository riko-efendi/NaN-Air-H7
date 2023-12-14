import time
from utils.ui_utils import UIUtils

# nanair_logo = """
#         _  __     _  __  ___   _    
#        / |/ /__ _/ |/ / / _ | (_)___
#       /    / _ `/    / / __ |/ / __/
#      /_/|_/\_,_/_/|_/ /_/ |_/_/_/ 
# """

class AsciiArt():
    def closing_screen(self):
        ui_utils = UIUtils()
        ui_utils.clear_screen()
        print("""
            ________             __            ___                    _          
            /_  __/ /  ___ ____  / /__ ___     / _/__  ____  __ _____ (_)__  ___ _
            / / / _ \/ _ `/ _ \/  '_/(_-<    / _/ _ \/ __/ / // (_-</ / _ \/ _ `/
            /_/ /_//_/\_,_/_//_/_/\_\/___/  _/_/ \___/_/  __\_,_/___/_/_//_/\_, / 
            ___  __ ______   ___ __ _____ / /____ __ _  / /               /___/  
            / _ \/ // / __/  (_-</ // (_-</ __/ -_)  ' \/_/                       
            \___/\_,_/_/    /___/\_, /___/\__/\__/_/_/_(_)                        
                                /___/                                             
            """)
        time.sleep(1.5)
        ui_utils.clear_screen()

    def nanair_logo(self, spacing=0):
        nanair_logo = f"""
{spacing}   _  __     _  __  ___   _    
{spacing}  / |/ /__ _/ |/ / / _ | (_)___
{spacing} /    / _ `/    / / __ |/ / __/
{spacing}/_/|_/\_,_/_/|_/ /_/ |_/_/_/ 
"""
        return nanair_logo
