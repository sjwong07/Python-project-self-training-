import customtkinter as ctk
from tkinter import messagebox
import Equipment

ctk.set_appearance_mode("bright")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Fitness Club Management System")
root.geometry("800x450")

main_frame = ctk.CTkFrame(root,fg_color="transparent")
main_frame.pack(fill="both",expand = True)


title_label = ctk.CTkLabel( main_frame,text = "Hello guest!,please choose following option.",
                      font = ("Arial",16,"bold"))
title_label.pack(pady = 12)

#function
def signup_logic():
    print("Signup Successful")


def equipment_logic():
    Equipment.equipment_frame()
    for widget in equipment_frame.winfo_children():
        widget.destroy()
    main_frame.pack_forget()
    equipment_frame.pack(fill="both",expand = True)
    


def schedule_logic():
    messagebox.showinfo("? time is available")
    

#button
option1 = ctk.CTkButton(main_frame,text =" 1.Signup/login",command=signup_logic,width = 250)
option1.pack()
option2 = ctk.CTkButton(main_frame,text = "2.View available equipment",command=equipment_logic,width = 250)
option2.pack()
option3 = ctk.CTkButton(main_frame,text = "3.View Schedule",command=schedule_logic,width = 250)
option3.pack()

root.mainloop()
