import asyncio
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk


class AdLib:
    """Encapsulates a single Madlib template and its inputs."""
    
    def __init__(self, title, template, placeholders):
        self.title = title
        self._original_template = template
        self.placeholders = placeholders
        self._vars = []
        self._entries = []

    def build_inputs(self, parent_frame):
        """Create labeled Entry widgets for each placeholder."""
        self._vars.clear()
        self._entries.clear()

        for idx, label in enumerate(self.placeholders):
            var = tk.StringVar()
            self._vars.append(var)

            lbl = tk.Label(
                parent_frame,
                text=f"Enter a {label}:",
                font=('Courier', 11),
                pady=5, padx=10
            )
            lbl.grid(row=idx, column=0, sticky='w')

            entry = tk.Entry(
                parent_frame,
                textvariable=var,
                justify='center',
                font=('Courier', 11),
                width=30
            )
            entry.grid(row=idx, column=1, sticky='w')
            self._entries.append(entry)

        tk.Button(
            parent_frame,
            text="Generate Sentence",
            command=self.generate_sentence,
            width=18, pady=5
        ).grid(row=len(self.placeholders), column=1, sticky='e', pady=(10,0))

        tk.Button(
            parent_frame,
            text="Clear",
            command=self.clear_inputs,
            width=18, pady=5
        ).grid(row=len(self.placeholders), column=0, sticky='w', pady=(10,0))

    def clear_inputs(self):
        """Clear all entry fields."""
        for entry in self._entries:
            entry.delete(0, tk.END)

    def generate_sentence(self):
        """Fill in the template with user inputs and show the result."""
        inputs = [var.get().strip() for var in self._vars]
        if '' in inputs:
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        result = self._original_template
        for i, text in enumerate(inputs, 1):
            result = result.replace(f"[{i}]", text)

        # Copy to clipboard and show
        root.clipboard_clear()
        root.clipboard_append(result)
        root.update()
        messagebox.showinfo("Your Madlib", result)
        self.clear_inputs()


class MadlibsApp:
    """Main application class for the Madlibs GUI."""
    
    def __init__(self, master):
        self.master = master
        master.title("Welcome to Madlibs")
        master.minsize(800, 550)
        master.columnconfigure(0, weight=1)

        self.selected_game = tk.IntVar()
        self.games = self._load_games()

        self._setup_logo()
        self._setup_game_selector()
        self._setup_input_frame()
        self._show_game(0)

    def _setup_logo(self):
        """Load and display the logo at the top."""
        img = Image.open("madlibs_logo_small.jpg")
        logo = ImageTk.PhotoImage(img)
        lbl = tk.Label(self.master, image=logo)
        lbl.image = logo
        lbl.grid(row=0, column=0, pady=10)

    def _setup_game_selector(self):
        """Create radio buttons to choose between templates."""
        frame = tk.LabelFrame(self.master, text="Choose a Template", padx=20, pady=10)
        frame.grid(row=1, column=0, pady=(10, 0), sticky='ew')

        for idx, game in enumerate(self.games):
            rb = tk.Radiobutton(
                frame,
                text=game.title,
                variable=self.selected_game,
                value=idx,
                command=lambda i=idx: self._show_game(i),
                padx=10, pady=5
            )
            rb.pack(side='left', expand=True)

    def _setup_input_frame(self):
        """Prepare the frame where input fields will appear."""
        self.input_frame = tk.LabelFrame(
            self.master,
            text="Please fill in the Text Boxes",
            padx=20, pady=10
        )
        self.input_frame.grid(row=2, column=0, pady=20, sticky='nsew')

    def _show_game(self, index):
        """Display input fields for the selected game."""
        # Clear previous widgets
        for widget in self.input_frame.winfo_children():
            widget.destroy()
        # Build new inputs
        self.games[index].build_inputs(self.input_frame)

    def _load_games(self):
        """Instantiate all AdLib templates."""
        templates = [
            (
                "Be Kind",
                "Be kind to your [1]-footed [2]. "
                "For a duck may be somebody's [3]. "
                "Be kind to your [2] in [4], "
                "Where the weather is always [5]. "
                "You may think that this is the [6]. Well it is.",
                ["NOUN", "NOUN (plural)", "NOUN", "PLACE", "ADJECTIVE", "NOUN"]
            ),
            (
                "Letter From Camp",
                "Dear [1], I am having a(n) [2] time at camp. "
                "The counselor is [3] and the food is [4]. "
                "I met [5] and we became [6] friends. "
                "Unfortunately, [5] is [7] and I [8] my [9] so we couldn't go [10] like everybody else. "
                "I need more [11] and a [12] sharpener, so please [13] [14] more when you [15] back. "
                "Your [16], [17]",
                [
                    "RELATIVE", "ADJECTIVE", "ADJECTIVE", "ADJECTIVE",
                    "NAME", "ADJECTIVE", "ADJECTIVE", "VERB (past)",
                    "BODY PART", "VERB (ing)", "NOUN (plural)", "NOUN",
                    "ADVERB", "VERB", "VERB", "RELATIVE", "NAME"
                ]
            ),
            (
                "Romeo and Juliet",
                "Two [1], both alike in dignity, "
                "In fair [2], where we lay our scene, "
                "From ancient [3] break to new mutiny, "
                "Where civil blood makes civil hands unclean. "
                "From forth the fatal loins of these two foes "
                "A pair of star-crossed [4] take their life; "
                "Whole misadventured piteous overthrows "
                "Do with their [5] bury their parents' strife. "
                "The fearful passage of their [6] love, "
                "And the continuance of their parents' rage, "
                "Which, but their children's end, nought could [7]. "
                "Is now the [8] hours' traffic of our stage; "
                "The which if you with [9] [10] attend, "
                "What here shall [11], our toil shall strive to mend.",
                [
                    "NOUN (plural)", "PLACE", "NOUN", "NOUN (plural)",
                    "NOUN", "ADJECTIVE", "VERB", "NUMBER",
                    "ADJECTIVE", "BODY PART", "VERB"
                ]
            )
        ]

        return [AdLib(title, tmpl, ph) for title, tmpl, ph in templates]


if __name__ == "__main__":
    root = tk.Tk()
    app = MadlibsApp(root)
    root.mainloop()
