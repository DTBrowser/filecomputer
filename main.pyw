import os
import main_GUI
from pathlib import Path
def get_extension(strpath):
    last = len(str(strpath)) - 4
    final_last = len(str(strpath))
    return str(strpath)[last:final_last]
def order_pathfiles(strpath):
    startnumber = 1
    fileorder = sorted(Path(strpath).iterdir(), key=os.path.getmtime)
    pathfile = str(fileorder[0])
    for pathfile in fileorder:
        os.rename(pathfile, strpath + "\\" + str(startnumber) + get_extension(pathfile))
        startnumber += 1
interface = main_GUI.mainGUI()
if None in interface.getValues():
    quit()
else:
    order_pathfiles(interface.browsepath())








