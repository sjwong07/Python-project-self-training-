import customtkinter as ctk

equipment_frame = ctk.CTkFrame(root,fg_color="transparent")

equipment_title = ctk.CTkLabel(equipment_frame,text = "Equipment page",font = ("Arial",20,"bold"))
equipment_title.pack(pady = 20)
label1 = ctk.CTkLabel(equipment_frame,text = "Equipment ? is available")
label1.pack()