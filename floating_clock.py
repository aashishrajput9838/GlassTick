import tkinter as tk
from time import strftime
import win32gui
import win32con
import sys
import traceback
import json
import os
from tkinter import ttk
from tkinter import colorchooser

class SettingsWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        
        # Configure settings window
        self.title("Clock Settings")
        self.configure(bg='#2b2b2b')
        self.attributes('-topmost', True)
        
        # Load current settings
        self.load_settings()
        
        # Create main frame
        main_frame = tk.Frame(self, bg='#2b2b2b', padx=20, pady=20)
        main_frame.pack(fill='both', expand=True)
        
        # Style configuration
        style = ttk.Style()
        style.configure('Settings.TButton', 
                       background='#0078d7',
                       foreground='white',
                       padding=10)
        style.configure('Settings.TLabel',
                       background='#2b2b2b',
                       foreground='white',
                       font=('Segoe UI', 10))
        style.configure('Settings.TScale',
                       background='#2b2b2b',
                       troughcolor='#0078d7')
        
        # Title
        title_label = tk.Label(main_frame,
                             text="Clock Settings",
                             font=('Segoe UI', 16, 'bold'),
                             bg='#2b2b2b',
                             fg='white')
        title_label.pack(pady=(0, 20))
        
        # Transparency slider
        transparency_frame = tk.Frame(main_frame, bg='#2b2b2b')
        transparency_frame.pack(fill='x', pady=5)
        
        tk.Label(transparency_frame,
                text="Transparency",
                font=('Segoe UI', 10),
                bg='#2b2b2b',
                fg='white').pack(side='left')
        
        self.transparency_scale = ttk.Scale(transparency_frame,
                                          from_=0.1,
                                          to=1.0,
                                          orient='horizontal',
                                          value=self.settings['transparency'],
                                          command=self.update_transparency)
        self.transparency_scale.pack(side='right', fill='x', expand=True)
        
        # Font size slider
        font_frame = tk.Frame(main_frame, bg='#2b2b2b')
        font_frame.pack(fill='x', pady=5)
        
        tk.Label(font_frame,
                text="Font Size",
                font=('Segoe UI', 10),
                bg='#2b2b2b',
                fg='white').pack(side='left')
        
        self.font_scale = ttk.Scale(font_frame,
                                  from_=12,
                                  to=48,
                                  orient='horizontal',
                                  value=self.settings['font_size'],
                                  command=self.update_font_size)
        self.font_scale.pack(side='right', fill='x', expand=True)
        
        # Color buttons
        color_frame = tk.Frame(main_frame, bg='#2b2b2b')
        color_frame.pack(fill='x', pady=5)
        
        tk.Label(color_frame,
                text="Colors",
                font=('Segoe UI', 10),
                bg='#2b2b2b',
                fg='white').pack(side='left')
        
        self.bg_button = tk.Button(color_frame,
                                 text="Background",
                                 command=self.choose_bg_color,
                                 bg='#0078d7',
                                 fg='white',
                                 font=('Segoe UI', 9),
                                 relief='flat',
                                 padx=10)
        self.bg_button.pack(side='left', padx=5)
        
        self.fg_button = tk.Button(color_frame,
                                 text="Text",
                                 command=self.choose_fg_color,
                                 bg='#0078d7',
                                 fg='white',
                                 font=('Segoe UI', 9),
                                 relief='flat',
                                 padx=10)
        self.fg_button.pack(side='left', padx=5)
        
        # Time format
        format_frame = tk.Frame(main_frame, bg='#2b2b2b')
        format_frame.pack(fill='x', pady=5)
        
        tk.Label(format_frame,
                text="Time Format",
                font=('Segoe UI', 10),
                bg='#2b2b2b',
                fg='white').pack(side='left')
        
        self.format_var = tk.StringVar(value=self.settings['time_format'])
        format_12 = tk.Radiobutton(format_frame,
                                 text="12-hour",
                                 variable=self.format_var,
                                 value="12",
                                 command=self.update_time_format,
                                 bg='#2b2b2b',
                                 fg='white',
                                 selectcolor='#2b2b2b',
                                 activebackground='#2b2b2b',
                                 activeforeground='white')
        format_12.pack(side='left', padx=5)
        
        format_24 = tk.Radiobutton(format_frame,
                                 text="24-hour",
                                 variable=self.format_var,
                                 value="24",
                                 command=self.update_time_format,
                                 bg='#2b2b2b',
                                 fg='white',
                                 selectcolor='#2b2b2b',
                                 activebackground='#2b2b2b',
                                 activeforeground='white')
        format_24.pack(side='left', padx=5)
        
        # Save button
        save_button = tk.Button(main_frame,
                              text="Save Settings",
                              command=self.save_settings,
                              bg='#0078d7',
                              fg='white',
                              font=('Segoe UI', 10, 'bold'),
                              relief='flat',
                              padx=20,
                              pady=10)
        save_button.pack(pady=20)
        
        # Center the window
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f'{width}x{height}+{x}+{y}')
        
        # Make window modal
        self.transient(parent)
        self.grab_set()
        
    def load_settings(self):
        try:
            with open('clock_settings.json', 'r') as f:
                self.settings = json.load(f)
        except:
            self.settings = {
                'transparency': 0.8,
                'font_size': 24,
                'bg_color': '#000000',
                'fg_color': '#ffffff',
                'time_format': '24'
            }
    
    def save_settings(self):
        with open('clock_settings.json', 'w') as f:
            json.dump(self.settings, f)
        self.parent.apply_settings(self.settings)
        self.destroy()
    
    def update_transparency(self, value):
        self.settings['transparency'] = float(value)
        self.parent.attributes('-alpha', float(value))
    
    def update_font_size(self, value):
        self.settings['font_size'] = int(float(value))
        self.parent.clock_label.configure(font=('Segoe UI', int(float(value)), 'bold'))
    
    def choose_bg_color(self):
        color = colorchooser.askcolor(color=self.settings['bg_color'])[1]
        if color:
            self.settings['bg_color'] = color
            self.parent.configure(bg=color)
            self.parent.clock_label.configure(bg=color)
    
    def choose_fg_color(self):
        color = colorchooser.askcolor(color=self.settings['fg_color'])[1]
        if color:
            self.settings['fg_color'] = color
            self.parent.clock_label.configure(fg=color)
    
    def update_time_format(self):
        self.settings['time_format'] = self.format_var.get()

class FloatingClock(tk.Tk):
    def __init__(self):
        try:
            super().__init__()

            # Load settings
            self.load_settings()

            # Configure the window
            self.overrideredirect(True)
            self.attributes('-topmost', True)
            self.attributes('-alpha', self.settings['transparency'])
            self.configure(bg=self.settings['bg_color'])

            # Create the clock label
            self.clock_label = tk.Label(
                self,
                font=('Segoe UI', self.settings['font_size'], 'bold'),
                background=self.settings['bg_color'],
                foreground=self.settings['fg_color'],
                padx=10,
                pady=5
            )
            self.clock_label.pack()

            # Create settings button
            self.settings_button = tk.Label(
                self,
                text="⚙",
                font=('Segoe UI', 8),
                bg=self.settings['bg_color'],
                fg=self.settings['fg_color'],
                cursor="hand2",
                padx=2,
                pady=0
            )
            self.settings_button.pack(side='right', padx=2)
            self.settings_button.bind('<Button-1>', self.show_settings)
            self.settings_button.pack_forget()  # Hide the settings button initially

            # Make the window draggable
            self.clock_label.bind('<Button-1>', self.start_move)
            self.clock_label.bind('<B1-Motion>', self.on_move)
            self.clock_label.bind('<Double-Button-1>', self.toggle_settings_icon)  # Add double-click binding

            # Update the clock
            self.update_clock()

            # Set window style
            hwnd = win32gui.GetParent(self.winfo_id())
            style = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
            style = style | win32con.WS_EX_LAYERED | win32con.WS_EX_TRANSPARENT
            win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, style)

            # Position the window in the top-right corner
            screen_width = self.winfo_screenwidth()
            self.geometry(f"+{screen_width-200}+0")

            print("Clock widget initialized successfully!")
            
        except Exception as e:
            print(f"Error initializing clock: {str(e)}")
            print("Full traceback:")
            traceback.print_exc()
            sys.exit(1)

    def load_settings(self):
        try:
            with open('clock_settings.json', 'r') as f:
                self.settings = json.load(f)
        except:
            self.settings = {
                'transparency': 0.8,
                'font_size': 24,
                'bg_color': '#000000',
                'fg_color': '#ffffff',
                'time_format': '24'
            }

    def show_settings(self, event=None):
        SettingsWindow(self)

    def apply_settings(self, settings):
        self.settings = settings
        self.attributes('-alpha', settings['transparency'])
        self.configure(bg=settings['bg_color'])
        self.clock_label.configure(
            font=('Segoe UI', settings['font_size'], 'bold'),
            bg=settings['bg_color'],
            fg=settings['fg_color']
        )
        self.settings_button.configure(
            bg=settings['bg_color'],
            fg=settings['fg_color']
        )

    def update_clock(self):
        try:
            # Update the time
            if self.settings['time_format'] == '12':
                time_string = strftime('%I:%M %p')
            else:
                time_string = strftime('%H:%M')
            self.clock_label.config(text=time_string)
            # Update every 1000ms (1 second)
            self.after(1000, self.update_clock)
        except Exception as e:
            print(f"Error updating clock: {str(e)}")

    def start_move(self, event):
        self.x = event.x
        self.y = event.y

    def on_move(self, event):
        deltax = event.x - self.x
        deltay = event.y - self.y
        x = self.winfo_x() + deltax
        y = self.winfo_y() + deltay
        self.geometry(f"+{x}+{y}")

    def toggle_settings_icon(self, event=None):
        """Toggle the visibility of the settings icon"""
        if self.settings_button.winfo_ismapped():
            self.settings_button.pack_forget()
        else:
            self.settings_button.pack(side='right', padx=2)

if __name__ == "__main__":
    try:
        print("Starting clock widget...")
        app = FloatingClock()
        app.mainloop()
    except Exception as e:
        print(f"Error running clock: {str(e)}")
        print("Full traceback:")
        traceback.print_exc() 