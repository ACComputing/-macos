import tkinter as tk
import time

class SnowLeopardBIOS:
    def __init__(self, root):
        self.root = root
        self.root.title("Mac OS Snow Leopard")
        self.root.geometry("600x400")
        self.root.resizable(False, False)

        # Phase 1: BIOS startup screen (black background, green/white text)
        self.boot_frame = tk.Frame(root, bg='black')
        self.boot_frame.pack(fill='both', expand=True)

        self.boot_text = tk.Text(
            self.boot_frame,
            bg='black',
            fg='#0f0',           # classic green terminal text
            font=('Courier', 12),
            wrap='word',
            borderwidth=0,
            highlightthickness=0
        )
        self.boot_text.pack(fill='both', expand=True, padx=20, pady=20)

        # Boot messages
        self.boot_messages = [
            "Apple Computer, Inc. - Mac OS Snow Leopard",
            "BIOS version 1.0 (c) 2025",
            "CPU: Intel Core 2 Duo",
            "Memory: 2048MB OK",
            "Hard Disk: 160GB detected",
            "Starting Darwin...",
            "Loading kernel...",
            "Starting system daemons...",
            " ",
            "Welcome to Mac OS X Snow Leopard",
            " ",
            "Press any key to continue..."
        ]

        self.msg_index = 0
        self.show_next_message()

        # Bind any key to skip boot and go to desktop
        self.root.bind('<Key>', self.skip_boot)

    def show_next_message(self):
        if self.msg_index < len(self.boot_messages):
            msg = self.boot_messages[self.msg_index] + "\n"
            self.boot_text.insert(tk.END, msg)
            self.boot_text.see(tk.END)
            self.msg_index += 1
            # Schedule next message (simulate BIOS delays)
            self.root.after(800, self.show_next_message)
        else:
            # Wait a bit then go to desktop
            self.root.after(2000, self.show_desktop)

    def skip_boot(self, event=None):
        # Immediately go to desktop when a key is pressed
        self.root.after_cancel(self.show_next_message)  # stop any pending messages
        self.show_desktop()

    def show_desktop(self):
        # Remove boot frame
        self.boot_frame.destroy()

        # Main desktop frame (Mac OS Snow Leopard style)
        self.desktop = tk.Frame(self.root, bg='#d4d4d4')  # light grey typical of Snow Leopard
        self.desktop.pack(fill='both', expand=True)

        # Top menu bar (simulated)
        menu_bar = tk.Frame(self.desktop, bg='#a0a0a0', height=25)
        menu_bar.pack(fill='x', side='top')
        menu_label = tk.Label(
            menu_bar,
            text="Finder    File    Edit    View    Window    Help",
            bg='#a0a0a0',
            fg='white',
            font=('Lucida Grande', 11)
        )
        menu_label.pack(side='left', padx=10)

        # Main content area: place some buttons (black bg, blue text)
        content = tk.Frame(self.desktop, bg='#d4d4d4')
        content.pack(expand=True, fill='both', padx=40, pady=40)

        # Title
        title = tk.Label(
            content,
            text="Mac OS Snow Leopard",
            bg='#d4d4d4',
            fg='#333333',
            font=('Lucida Grande', 18, 'bold')
        )
        title.pack(pady=(0, 30))

        # Buttons frame
        btn_frame = tk.Frame(content, bg='#d4d4d4')
        btn_frame.pack()

        # Sample buttons with black background and blue text
        btn1 = tk.Button(
            btn_frame,
            text="Finder",
            bg='black',
            fg='blue',
            font=('Lucida Grande', 12),
            width=15,
            relief='flat',
            activebackground='#333333',
            activeforeground='lightblue'
        )
        btn1.grid(row=0, column=0, padx=10, pady=10)

        btn2 = tk.Button(
            btn_frame,
            text="System Preferences",
            bg='black',
            fg='blue',
            font=('Lucida Grande', 12),
            width=15,
            relief='flat',
            activebackground='#333333',
            activeforeground='lightblue'
        )
        btn2.grid(row=0, column=1, padx=10, pady=10)

        btn3 = tk.Button(
            btn_frame,
            text="Terminal",
            bg='black',
            fg='blue',
            font=('Lucida Grande', 12),
            width=15,
            relief='flat',
            activebackground='#333333',
            activeforeground='lightblue'
        )
        btn3.grid(row=1, column=0, padx=10, pady=10)

        btn4 = tk.Button(
            btn_frame,
            text="Safari",
            bg='black',
            fg='blue',
            font=('Lucida Grande', 12),
            width=15,
            relief='flat',
            activebackground='#333333',
            activeforeground='lightblue'
        )
        btn4.grid(row=1, column=1, padx=10, pady=10)

        # Optional: add a dock-like bar at bottom (simulated)
        dock = tk.Frame(self.desktop, bg='#a0a0a0', height=40)
        dock.pack(fill='x', side='bottom')
        dock_label = tk.Label(
            dock,
            text="Finder  Safari  Mail  iTunes  System Preferences  Trash",
            bg='#a0a0a0',
            fg='white',
            font=('Lucida Grande', 10)
        )
        dock_label.pack(pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    app = SnowLeopardBIOS(root)
    root.mainloop()
