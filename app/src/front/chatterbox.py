import tkinter as tk
from tkinter.scrolledtext import ScrolledText

from model.dico import Dico


class Chatterbox:
    """
        Front for the chatterbox

        Attributes
        ----------
        dico: Dico
            Dictionary of the app
        
        window: tk.TK
            window of the application

        output_text: tk.ScrolledText
            dialog box between the user and Phrasaton

        input_text: tk.Text
            entry box for the user
    """
    def __init__(self) -> None:
        # create the dictionary
        self.dico = Dico()

        # create the main window
        self.window = tk.Tk()
        self.window.title("Phrasaton")
        self.window.geometry("800x600")
        self.window.colormapwindows = "white"

        # text zone for conversation
        self.output_text = ScrolledText(self.window, bg="black", fg="white", insertbackground="white", height=20, font=("Courier", 12), border= 5)
        self.output_text.pack(fill=tk.X, expand=False)
        self.output_text.configure(state="disabled")
        self.output_text.tag_configure("bot", foreground="green")
        self.output_text.tag_configure("error", foreground="red")

        self.input_text = tk.Text(self.window, bg="black", fg="white", insertbackground="white", height=20, font=("Courier", 12), border= 10)
        self.input_text.pack(fill=tk.X, expand=False)


    def process_command(self) -> None:
        """
            Process the user's request
        """
        command = self.input_text.get("1.0", tk.END).strip()
        self.input_text.delete("1.0", tk.END)
        self.input_text.configure(state="disabled")
        self.use_output_box(command)
        
        try:
            self.dico.learn(command)
            answer = self.dico.speak()
            self.use_output_box(answer, "bot")

        except AssertionError as err:
            self.use_output_box(str(err), "error")

        self.input_text.configure(state="normal")


    def start(self) -> None:
        """
            Loophole for the application to work.
        """
        # Capture de la touche "Enter" pour traiter la commande
        self.window.bind("<Return>", lambda event: self.process_command())
        self.window.mainloop()


    def use_output_box(self, text: str, style: str = None) -> None:
        """
            Allow the user to use the output box

            Parameters
            ----------
            text : str
                the text to prompt
            style : str
                style to use for the text. Two exist:
                    - bot
                    - error
                The 'None' value define the style for the user
        """
        self.output_text.configure(state="normal")

        if style is not None:
            assert style in ["bot", "error"], "Invalid style use for the prompt"
            self.output_text.insert(tk.END, f"{text}\n\n", style)

        else:
            self.output_text.insert(tk.END, f"> {text}\n\n")
        
        self.output_text.configure(state="disabled")
        self.output_text.see(tk.END)