from tkinter import filedialog
from tkinter import messagebox as mb
import information as info
import subprocess
from ffmpeg_progress_yield import FfmpegProgress
import os

class Controller:
    def __init__(self) -> None:
        pass

    def set_gui(self,gui):
        self.gui = gui
    
    
    def update_to_format(self):
        from_format = self.gui.SINGLE_FORMAT_FROM_BOX.get()
        to_format = self.gui.SINGLE_FORMAT_TO_BOX
        if from_format in info.conversions:
            to_format['values'] = info.conversions[from_format]
        else:
            mb.showerror("Unrecognized Type", "You have selected a file type that is not recognized. How did you do that?")
    
    
    def update_chosen_file(self):
        chosen_from_format = self.gui.SINGLE_FORMAT_FROM_BOX.get()
        if chosen_from_format in info.file_formats:
            input_path = filedialog.askopenfilename(filetypes=[(f"*.{chosen_from_format.lower()} Files", f"*{chosen_from_format.lower()}")])
            if input_path:
                print("path chosen", input_path)
                self.gui.chosen_file.set(os.path.basename(input_path))
                self.gui.file_path = input_path
        else:
            mb.showerror("Nothing Selected", "There is nothing selected. Please select a from file format before attempting to choose a file.")
    
    def convert_single_file(self, file_path):
        chosen_from_format = self.gui.SINGLE_FORMAT_FROM_BOX.get()
        chosen_to_format = self.gui.SINGLE_FORMAT_TO_BOX.get()
        if file_path != "":
            if chosen_to_format != "":
                if self.check_allowed_conversion(chosen_from_format,chosen_to_format):
                    command = ['ffmpeg', '-i', file_path, self.check_file_name(file_path,increment=0,to_format=chosen_to_format)]
                    ff = FfmpegProgress(command)
                    try:
                        for progress in ff.run_command_with_progress():
                            print(progress)
                            self.gui.SINGLE_FORMAT_PROGRESS_BAR['maximum'] = 100
                            self.gui.SINGLE_FORMAT_PROGRESS_BAR['value'] = int(progress)
                            self.gui.ROOT.update_idletasks()
                        print("completed")
                    except Exception as e:
                        mb.showerror("Error", f"An Error Has occured:\n{e}")
                else:
                    mb.showerror("Conversion not allowed", "This conversion is not supported. How did you do this?")                
            else:
                mb.showerror("No Output Selected", "There is no output format selected. Please select an output format before trying to convert.")
        else:
            mb.showerror("No File Selected","There is no file selected. Please select a file before trying to convert.")
    
    def check_file_name(self,file_path,increment,to_format):
        base_name = os.path.basename(file_path)
        base, ext = os.path.splitext(base_name)
        print(base,ext)
        
        if os.path.exists(f"./Export/{base}{f"_{increment}" if increment != 0 else ""}.{to_format}"):
            print("Path exists", increment)
            return self.check_file_name(file_path=file_path, increment=increment + 1, to_format=to_format)
        else:
            return f"./Export/{base}{f"_{increment}" if increment != 0 else ""}.{to_format}"
        
        
    def check_allowed_conversion(self,from_format, to_format):
        if from_format in info.conversions:
            if to_format in info.conversions[from_format]:
                return True
            else:
                return False
        else:
            return False
    
    def update_batch_to_format(self):
        from_format = self.gui.BATCH_FORMAT_FROM_BOX.get()
        to_format = self.gui.BATCH_FORMAT_TO_BOX
        if from_format in info.conversions:
            to_format['values'] = info.conversions[from_format]
        else:
            mb.showerror("Unrecognized Type", "You have selected a file type that is not recognized. How did you do that?")
    
    def update_chosen_folder(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            print("path chosen", folder_path)
            self.gui.chosen_folder.set(folder_path)
            
    def convert_batch_file(self,chosen_folder):
        from_extension = self.gui.BATCH_FORMAT_FROM_BOX.get()
        to_format = self.gui.BATCH_FORMAT_TO_BOX.get()
        
        # Check if there is a from extension selected
        if from_extension != "":
            # Check if a folder has been selected
            if chosen_folder != "":
                # Check if a to format has been selected
                if to_format != "":
                    # Grab all files of particular format
                    files = self.get_files_with_extension(chosen_folder, f'.{from_extension.lower()}')
                    # Check if there are any files.
                    if files:
                        batch_dir = self.create_batch_folder(increment=0)
                        current_num = 0
                        for each in files:
                            current_num += 1
                            self.gui.progress_num.set(f"{current_num}/{len(files)}")
                            file_path = f"{chosen_folder}/{each}"
                            command = ['ffmpeg', '-i', file_path, self.check_batch_file_name(file_path,increment=0,to_format=to_format, batch_dir=batch_dir)]
                            ff = FfmpegProgress(command)
                            self.gui.current_file_name.set(f"Current File: {each}")
                            try:
                                for progress in ff.run_command_with_progress():
                                    print(progress)
                                    self.gui.BATCH_FORMAT_PROGRESS_BAR['maximum'] = 100
                                    self.gui.BATCH_FORMAT_PROGRESS_BAR['value'] = int(progress)
                                    self.gui.ROOT.update_idletasks()
                                print("completed")
                            except Exception as e:
                                mb.showerror("Error", f"An Error Has occured:\n{e}")
                    
                    else: mb.showerror('No Files to Convert', f"There are no files in this folder of the format {from_extension}. Please select a folder with the appropriate files.")
                else: mb.showerror("No Format Selected", "You hae not selected a format to convert to. Please select a format before trying to convert.")
            else: mb.showerror('No Folder Selected', 'You have not selected a folder. Please select a folder before trying to convert.')
        else: mb.showerror('No Format Selected', 'You have not selected a format to convert from. Please select a from format before trying to convert.')
    
    
    def get_files_with_extension(self,directory, extension):
        list = [file for file in os.listdir(directory)
                if os.path.splitext(file)[1] == extension]
        
        return list
    
    def create_batch_folder(self,increment):
        if os.path.exists(f'./Export/Batch{f"_{increment}" if increment != 0 else ""}'):
            return self.create_batch_folder(increment+1)
        else:
            batch_dir = f'./Export/Batch{f"_{increment}" if increment != 0 else ""}'
            print(batch_dir)
            os.mkdir(batch_dir)
            return batch_dir      
    
    def check_batch_file_name(self,file_path,increment,to_format,batch_dir):
        base_name = os.path.basename(file_path)
        base, ext = os.path.splitext(base_name)
        print(base,ext)
        
        if os.path.exists(f"{batch_dir}/{base}{f"_{increment}" if increment != 0 else ""}.{to_format}"):
            print("Path exists", increment)
            return self.check_file_name(file_path=file_path, increment=increment + 1, to_format=to_format)
        else:
            return f"{batch_dir}/{base}{f"_{increment}" if increment != 0 else ""}.{to_format}"