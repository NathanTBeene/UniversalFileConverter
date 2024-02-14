import ttkbootstrap as ttk
from editorgui import GUI
from controller import Controller
import os

#Setup Initials
root = ttk.Window(themename='darkly')
gui = GUI(root)
controller = Controller()
export_path = './Export'

# Establish References
gui.set_controller(controller)
controller.set_gui(gui)

#Create Dir
if not os.path.exists(export_path):
    os.makedirs(export_path)

def main():
    root.mainloop()


if __name__ == "__main__":
    main()
    
    
    