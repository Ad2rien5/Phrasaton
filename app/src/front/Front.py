import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from app.src.model.Dico import Dico


class Front:
    """
        Classe qui défini le front-end de l'application

        Attribut
        --------
        dico: Dico
            Dictionnaire de l'appli
        
        window: tk.TK
            fenêtre de l'application

        output_text: tk.ScrolledText
            boîte d'affichage du dialogue entre l'utilisateur et le Phrasaton

        intput_text: tk.Text
            boîte d'entré de texte pour l'utilisateur
    """
    def __init__(self) -> None:
        """
            Constructeur
            
            Initialise la fenêtre et les différents widgets
        """
        # Création du dictionnaire
        self.dico = Dico()

        # Création de la fenêtre principale
        self.window = tk.Tk()
        self.window.title("Phrasaton")
        self.window.geometry("800x600")
        self.window.colormapwindows = "white"


        # Zone de texte pour afficher l'entrée et la sortie
        self.output_text = ScrolledText(self.window, bg="black", fg="white", insertbackground="white", height=20, font=("Courier", 12), border= 5)
        self.output_text.pack(fill=tk.X, expand=False)
        self.output_text.configure(state="disabled")
        self.output_text.tag_configure("bot", foreground="green")
        self.output_text.tag_configure("error", foreground="red")

        self.input_text = tk.Text(self.window, bg="black", fg="white", insertbackground="white", height=20, font=("Courier", 12), border= 10)
        self.input_text.pack(fill=tk.X, expand=False)


    def process_command(self) -> None:
        """
            Méthode qui va lancer l'algorithme quand l'utilisateur appuie sur 'enter'
        """
        command = self.input_text.get("1.0", tk.END).strip()
        self.input_text.delete("1.0", tk.END)
        self.input_text.configure(state="disabled")
        self.use_outputbox(command)
        
        try:
            self.dico.apprends(command)
            retour = self.dico.parle()
            self.use_outputbox(retour, "bot")

        except AssertionError as err:
            self.use_outputbox(err, "error")

        self.input_text.configure(state="normal")


    def start(self) -> None:
        """
            Méthode qui va faire une boucle infinie afin de pouvoir utiliser l'application
        """
        # Capture de la touche "Enter" pour traiter la commande
        self.window.bind("<Return>", lambda event: self.process_command())
        self.window.mainloop()


    def use_outputbox(self, text: str, style: str = None) -> None:
        """
            Méthode qui permet d'utiliser la boîte output

            Paramètre
            ---------
            text: str
                Le texte à afficher
            style: str
                Style à utiliser pour afficher le texte. IL existe deux style
                    - bot
                    - error
                Possède pour valeur par défaut 'None', ce qui correspond à un texte pour l'utilisateur
        """
        self.output_text.configure(state="normal")

        if style != None:
            assert style in ["bot", "error"], "Invalid style use for the prompt"
            self.output_text.insert(tk.END, f"{text}\n\n", style)

        else:
            self.output_text.insert(tk.END, f"> {text}\n\n")
        
        self.output_text.configure(state="disabled")
        self.output_text.see(tk.END)


# Lancement du programme
Test = Front()
Test.start()