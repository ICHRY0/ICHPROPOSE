import time
import os

black="\033[0;30m"
red="\033[0;31m"
bred="\033[1;31m"
green="\033[0;32m"
bgreen="\033[1;32m"
yellow="\033[0;33m"
byellow="\033[1;33m"
blue="\033[0;34m"
bblue="\033[1;34m"
purple="\033[0;35m"
bpurple="\033[1;35m"
cyan="\033[0;36m"
bcyan="\033[1;36m"
white="\033[0;37m"
nc="\033[00m"

propose=f"""

{blue}▬▬▬.◙.▬▬▬
═▂▄▄▓▄▄▂
◢◤ █▀▀████▄▄▄▄◢◤
█▄ █ █▄ ███▀▀▀▀▀▀▀╬
◥█████◤
══╩══╩═{white}
╬═╬
╬═╬ 
╬═╬ 
╬═╬   {bpurple}Do You Love me?{white}
╬═╬{bcyan}☻/{white}
╬═╬{bcyan}/▌{white}
╬═╬{bcyan}/\.{white}
"""
pose=f"""{purple}
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⠉⠉⠛⢿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⡄⢹⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⡊⠀⢠⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⠀⣠⠊⠀⣠⣾⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⡃⠀⠀⠀⠉⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⠟⠷⣶⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⢐⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠁⠀⠀⠀⠻⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⡀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠄⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠛⠛⠲⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⡀⠀⠀⠈⢿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⢠⡿⠀⠀⠀⠈
⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠘⠁⠀⠀⣠⣾
⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⠉⠉⠉⠻⣿⣿⠇⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠻⣿⣿⣿⣿⣿⠿⢿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠈⣿⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⢠⣿⣆⠀⠀⠀⠙⣿⡿⠉⠀⠀⠀⠈⢿⠀⠀⠀⠀⠀⠀⠀⠀⣸⡀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⣾⣿⠿⠷⣄⠀⠀⠈⠀⠀⠀⠀⠀⢀⣾⣆⠀⠀⠀⠀⠀⠀⣠⣿⡇⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⢰⡟⠁⠀⠀⠈⠣⡀⠀⠀⠙⣿⣿⣿⣿⡿⠿⠷⢦⣤⣤⣴⣾⣿⣿⡇⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠘⠢⠤⠞⠉⠉⠁⠀⠀⠀⠀⠀⠙⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⢸⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⣤⣤⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿
⣿⡿⠛⠛⠛⠛⠛⠃⠀⠀⠀⠀⢸⣿⡆⠀⠀⠀⠀⣿⣿⣿⣿⣿⣄⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿
⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡟⠃⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣶⡿⠀⠀⠀⠛⠛⠻⠿⠿⠿⢿⣿⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿
⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠁⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣄⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣶⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿

            {bgreen}Fuck {bblue}You
"""

girl=f"""

_{bcyan}▀█║────────────▄▄───────────​─{bpurple}▄──▄_
──{bcyan}█║───────▄─▄─█▄▄█║──────{bpurple}▄▄──{bpurple}​█║─█║
──{bcyan}█║───▄▄──█║█║█║─▄║{bpurple}▄──▄{bpurple}║█║─█║​█║▄█║
──{bcyan}█║──█║─█║█║█║─▀▀──{bpurple}█║─█║█║─█║​─▀─▀
──{bcyan}█║▄║█║─█║─▀───────{bpurple}█║▄█║─▀▀
──{bcyan}▀▀▀──▀▀────────────{bpurple}▀─█║
───────{bred}▄▄─▄▄▀▀▄▀▀▄{green}──{bpurple}▀▄▄▀{green}
──────{bred}███████───▄▀{green}
──────{bred}▀█████▀▀▄▀{white}
────────{bred}▀█▀{green}
    {yellow}I {bblue}Love {bpurple} {bcyan}You{bred}♥
"""



if __name__=="__main__":
    os.system("clear")
    print(propose)
    ask=input(f"{bgreen}Do You Love Me:[y/n]:")
    if ask == "y" or ask == "Y":
        os.system("clear")
        print(girl)
    elif ask == "n" or ask == "N":
        os.system("clear")
        print(pose)
    else:
        print(f"{red}invalid option....")
        time.sleep(1)
        os.system("python3 main.py")


                                                                           
# 8 8888     ,o888888o.    8 8888        8 8 888888888o. `8.`8888.      ,8' 
# 8 8888    8888     `88.  8 8888        8 8 8888    `88. `8.`8888.    ,8'  
# 8 8888 ,8 8888       `8. 8 8888        8 8 8888     `88  `8.`8888.  ,8'   
# 8 8888 88 8888           8 8888        8 8 8888     ,88   `8.`8888.,8'    
# 8 8888 88 8888           8 8888        8 8 8888.   ,88'    `8.`88888'     
# 8 8888 88 8888           8 8888        8 8 888888888P'      `8. 8888      
# 8 8888 88 8888           8 8888888888888 8 8888`8b           `8 8888      
# 8 8888 `8 8888       .8' 8 8888        8 8 8888 `8b.          8 8888      
# 8 8888    8888     ,88'  8 8888        8 8 8888   `8b.        8 8888      
# 8 8888     `8888888P'    8 8888        8 8 8888     `88.      8 8888      


# instaram:- https://instagram.com/ichry__



#      _            _ _                             _   _                          _                        _   _                  __            _             
#   __| | ___  _ __( ) |_    ___ ___  _ __  _   _  | |_| |__   ___    ___ ___   __| | ___   _ __ ___   ___ | |_| |__   ___ _ __   / _|_   _  ___| | _____ _ __ 
#  / _` |/ _ \| '_ \/| __|  / __/ _ \| '_ \| | | | | __| '_ \ / _ \  / __/ _ \ / _` |/ _ \ | '_ ` _ \ / _ \| __| '_ \ / _ \ '__| | |_| | | |/ __| |/ / _ \ '__|
# | (_| | (_) | | | || |_  | (_| (_) | |_) | |_| | | |_| | | |  __/ | (_| (_) | (_| |  __/ | | | | | | (_) | |_| | | |  __/ |    |  _| |_| | (__|   <  __/ |   
#  \__,_|\___/|_| |_| \__|  \___\___/| .__/ \__, |  \__|_| |_|\___|  \___\___/ \__,_|\___| |_| |_| |_|\___/ \__|_| |_|\___|_|    |_|  \__,_|\___|_|\_\___|_|   
