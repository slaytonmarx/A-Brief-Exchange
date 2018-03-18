import Tkinter;

class App:
    def __init__(self):
        # Main Window Related:
        self.main_window = Tkinter.Tk();
        self.main_window.geometry("1120x300");
        self.twitchUserString = Tkinter.StringVar();
        self.gateKeyString = Tkinter.StringVar();
        # Frame Related
        # Border decoration. The default is FLAT. Other possible values are SUNKEN, RAISED, GROOVE, and RIDGE.
        self.titleFrame = Tkinter.Frame(self.main_window, borderwidth=3, relief="groove", width=1500, height=500);
        self.titleFrame.grid(row=0, column=0, columnspan=2, padx=10, pady=5, sticky='w');

        # Input Frame username
        self.interactionFrame = Tkinter.Frame(self.main_window);
        self.interactionFrame.grid(row=5, column=0, sticky=("w"), padx=10);
        
        # Input Frame gatekey
        self.interactionFrame2 = Tkinter.Frame(self.main_window);
        self.interactionFrame2.grid(row=6, column=0, sticky=("w"), padx=10);

        # Label Related
        self.titleLabel = Tkinter.Label(self.titleFrame, text="Twitch Plays Robotics", width=26);
        self.titleLabel.config(font=("Cambria", 24));
        self.titleLabel.pack(side="left");

        self.choiceLabel = Tkinter.Label(self.main_window, text="Your username: ")
        self.choiceLabel.config(font=("Cambria", 16));
        self.choiceLabel.grid(row=1, column=0, sticky="w", padx=10);

        self.choiceLabel = Tkinter.Label(self.main_window, text="Your Stream Key: ")
        self.choiceLabel.config(font=("Cambria", 16));
        self.choiceLabel.grid(row=2, column=0, sticky=("w"), padx=10);

        
        # Input Related
        self.entry = Tkinter.Entry(self.main_window, width=40);
        self.entry.config(relief="groove", borderwidth=2, font=("Cambria", 18, "bold"));
        self.entry.grid(row=1, column=1);
        
        self.entry = Tkinter.Entry(self.main_window, width=40);
        self.entry.config(relief="groove", borderwidth=2, font=("Cambria", 18, "bold"));
        self.entry.grid(row=2, column=1);
        
        # Buttons
        self.contBut = Tkinter.Button(self.interactionFrame, text="Engage", command=self.activate);
        self.contBut.config(relief="groove", borderwidth=2, font=("Cambria", 18, "bold"));
        self.contBut.grid(row=0, column=1);
        
        self.quit = Tkinter.Button(self.interactionFrame, text="Quit", command=self.main_window.destroy);
        self.quit.config(relief="groove", borderwidth=2, font=("Cambria", 18, "bold"))
        self.quit.grid(row=0, column=2);

        console = "";
        Tkinter.mainloop();
        
    def activate(self):
        playerInput = self.entry.get();
    
main_window = App()