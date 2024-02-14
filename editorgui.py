import ttkbootstrap as ttk
import tkinter as tk
import information as info


class GUI:
    def __init__(self,ROOT) -> None:
        self.ROOT = ROOT
        self.ROOT.title("File Converter")
      
      
        # Single Conversion Frame #
        SINGLE_ROOT_FRAME = ttk.Frame(ROOT)
        SINGLE_ROOT_LABEL = ttk.Label(SINGLE_ROOT_FRAME,text="Single File Conversion", font=('',25))
        SINGLE_ROOT_DESCRIPTION = ttk.Label(
            SINGLE_ROOT_FRAME,
            text="You can use this section to convert a single file from one format to another by choosing the format of what you are converting, finding the file, choosing what you would like to convert it to, and then clicking convert!",
            justify="center",
            wraplength=500
        )
        SINGLE_ROOT_FRAME.pack(pady=30,padx=150)
        SINGLE_ROOT_LABEL.pack()
        SINGLE_ROOT_DESCRIPTION.pack()
        
        
        
        SINGLE_CONVERSION_FRAME = ttk.Frame(SINGLE_ROOT_FRAME)
        SINGLE_CONVERSION_FRAME.pack()
        
        SINGLE_FORMAT_FROM_FRAME = ttk.Frame(SINGLE_CONVERSION_FRAME)
        SINGLE_FORMAT_FROM_LABEL = ttk.Label(SINGLE_FORMAT_FROM_FRAME, text= "From Format:")
        self.SINGLE_FORMAT_FROM_BOX = ttk.Combobox(SINGLE_FORMAT_FROM_FRAME, values=info.file_formats, state="readonly")
        self.SINGLE_FORMAT_FROM_BOX.bind('<<ComboboxSelected>>',lambda x: self.controller.update_to_format())
        SINGLE_FORMAT_FROM_FRAME.pack(side="left", padx=20, pady=15)
        SINGLE_FORMAT_FROM_LABEL.pack()
        self.SINGLE_FORMAT_FROM_BOX.pack()
    
    
        self.chosen_file = tk.StringVar(value="")
        self.file_path = ""
        SINGLE_FORMAT_CHOSEN_FRAME = ttk.Frame(SINGLE_CONVERSION_FRAME)
        SINGLE_FORMAT_CHOSEN_ENTRY = ttk.Entry(SINGLE_FORMAT_CHOSEN_FRAME, state="readonly", textvariable=self.chosen_file)
        SINGLE_FORMAT_CHOSEN_BUTTON = ttk.Button(SINGLE_FORMAT_CHOSEN_FRAME, text="Choose File:", command=lambda: self.controller.update_chosen_file())
        SINGLE_FORMAT_CHOSEN_FRAME.pack(side="left", padx=10, pady=15)
        SINGLE_FORMAT_CHOSEN_ENTRY.pack(side="left", padx=5)
        SINGLE_FORMAT_CHOSEN_BUTTON.pack(side="left", padx=5)
    

        SINGLE_FORMAT_TO_FRAME = ttk.Frame(SINGLE_CONVERSION_FRAME)
        SINGLE_FORMAT_TO_LABEL = ttk.Label(SINGLE_FORMAT_TO_FRAME, text= "To Format:")
        self.SINGLE_FORMAT_TO_BOX = ttk.Combobox(SINGLE_FORMAT_TO_FRAME, state="readonly")
        SINGLE_FORMAT_TO_FRAME.pack(side="left", padx=20)
        SINGLE_FORMAT_TO_LABEL.pack()
        self.SINGLE_FORMAT_TO_BOX.pack()
        
        
        SINGLE_FORMAT_PROGRESS_FRAME = ttk.Frame(SINGLE_ROOT_FRAME)
        SINGLE_FORMAT_PROGRESS_LABEL = ttk.Label(SINGLE_FORMAT_PROGRESS_FRAME, text="Progress...")
        self.SINGLE_FORMAT_PROGRESS_BAR = ttk.Progressbar(SINGLE_FORMAT_PROGRESS_FRAME,orient="horizontal",length=200,mode="determinate")
        SINGLE_FORMAT_PROGRESS_FRAME.pack()
        SINGLE_FORMAT_PROGRESS_LABEL.pack()
        self.SINGLE_FORMAT_PROGRESS_BAR.pack()
        
        SINGLE_FORMAT_CONVERT_FRAME = ttk.Frame(SINGLE_ROOT_FRAME)
        SINGLE_FORMAT_CONVERT_BUTTON = ttk.Button(SINGLE_FORMAT_CONVERT_FRAME, text='Convert!',command= lambda: self.controller.convert_single_file(self.file_path))
        SINGLE_FORMAT_CONVERT_FRAME.pack(pady=10)
        SINGLE_FORMAT_CONVERT_BUTTON.pack()
        
        # Batch Conversion Frame #
        BATCH_ROOT_FRAME = ttk.Frame(ROOT)
        BATCH_ROOT_LABEL = ttk.Label(BATCH_ROOT_FRAME, text="Batch Conversion", font=('',25))
        BATCH_ROOT_DESCRIPTION = ttk.Label(
            BATCH_ROOT_FRAME,
            text="Here you can batch convert by choosing a file type to convert, choosing a folder where those files are held, and then choosing a type to convert to. The program will convert all folders of the chosen type into the format you have picked when you click convert!",
            justify="center",
            wraplength= 500
        )
        BATCH_ROOT_FRAME.pack(pady= 30, padx= 150)
        BATCH_ROOT_LABEL.pack()
        BATCH_ROOT_DESCRIPTION.pack()
        
        
        BATCH_CONVERSION_FRAME = ttk.Frame(BATCH_ROOT_FRAME)
        BATCH_CONVERSION_FRAME.pack()
        
        BATCH_FORMAT_FROM_FRAME = ttk.Frame(BATCH_CONVERSION_FRAME)
        BATCH_FORMAT_FROM_LABEL = ttk.Label(BATCH_FORMAT_FROM_FRAME, text= "From Format:")
        self.BATCH_FORMAT_FROM_BOX = ttk.Combobox(BATCH_FORMAT_FROM_FRAME, values=info.file_formats, state="readonly")
        self.BATCH_FORMAT_FROM_BOX.bind('<<ComboboxSelected>>',lambda x: self.controller.update_batch_to_format())
        BATCH_FORMAT_FROM_FRAME.pack(side="left", padx=20, pady=15)
        BATCH_FORMAT_FROM_LABEL.pack()
        self.BATCH_FORMAT_FROM_BOX.pack()
    
    
        self.chosen_folder = tk.StringVar(value="")
        BATCH_FORMAT_CHOSEN_FRAME = ttk.Frame(BATCH_CONVERSION_FRAME)
        BATCH_FORMAT_CHOSEN_ENTRY = ttk.Entry(BATCH_FORMAT_CHOSEN_FRAME, state="readonly", width=80, textvariable=self.chosen_folder)
        BATCH_FORMAT_CHOSEN_BUTTON = ttk.Button(BATCH_FORMAT_CHOSEN_FRAME, text="Choose Folder:", command=lambda: self.controller.update_chosen_folder())
        BATCH_FORMAT_CHOSEN_FRAME.pack(side="left", padx=10, pady=15)
        BATCH_FORMAT_CHOSEN_ENTRY.pack(side="left", padx=5)
        BATCH_FORMAT_CHOSEN_BUTTON.pack(side="left", padx=5)
    

        BATCH_FORMAT_TO_FRAME = ttk.Frame(BATCH_CONVERSION_FRAME)
        BATCH_FORMAT_TO_LABEL = ttk.Label(BATCH_FORMAT_TO_FRAME, text= "To Format:")
        self.BATCH_FORMAT_TO_BOX = ttk.Combobox(BATCH_FORMAT_TO_FRAME, state="readonly")
        BATCH_FORMAT_TO_FRAME.pack(side="left", padx=20)
        BATCH_FORMAT_TO_LABEL.pack()
        self.BATCH_FORMAT_TO_BOX.pack()
        
        self.current_file_name = tk.StringVar(value="Current File:")
        self.progress_num = tk.StringVar(value="0/0")
        BATCH_FORMAT_PROGRESS_FRAME = ttk.Frame(BATCH_ROOT_FRAME)
        BATCH_FORMAT_PROGRESS_LABEL = ttk.Label(BATCH_FORMAT_PROGRESS_FRAME, text="Progress...")
        BATCH_FORMAT_PROGRESS_NAME_FRAME = ttk.Frame(BATCH_FORMAT_PROGRESS_FRAME)
        self.BATCH_FORMAT_PROGRESS_CURRENT_FILE = ttk.Label(BATCH_FORMAT_PROGRESS_NAME_FRAME, textvariable=self.current_file_name)
        self.BATCH_FORMAT_PROGRESS_BAR = ttk.Progressbar(BATCH_FORMAT_PROGRESS_NAME_FRAME,orient="horizontal",length=200,mode="determinate")
        self.BATCH_FORMAT_PROGRESS_NUM = ttk.Label(BATCH_FORMAT_PROGRESS_NAME_FRAME, textvariable=self.progress_num)
        BATCH_FORMAT_PROGRESS_FRAME.pack()
        BATCH_FORMAT_PROGRESS_LABEL.pack()
        BATCH_FORMAT_PROGRESS_NAME_FRAME.pack()
        self.BATCH_FORMAT_PROGRESS_CURRENT_FILE.pack(side="left", padx= 20)
        self.BATCH_FORMAT_PROGRESS_BAR.pack(side="left")
        self.BATCH_FORMAT_PROGRESS_NUM.pack(side= "left", padx=20)
        
        BATCH_FORMAT_CONVERT_FRAME = ttk.Frame(BATCH_ROOT_FRAME)
        BATCH_FORMAT_CONVERT_BUTTON = ttk.Button(BATCH_FORMAT_CONVERT_FRAME, text='Convert!',command= lambda: self.controller.convert_batch_file(self.chosen_folder.get()))
        BATCH_FORMAT_CONVERT_FRAME.pack(pady=10)
        BATCH_FORMAT_CONVERT_BUTTON.pack()
        
      
      
      
      
      
      
      
    def set_controller(self,controller):
        self.controller = controller