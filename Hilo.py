class Director:
    def _init_ (self):
        self.guesses=[]
        self.is_playing= True
        self.score=300
        
    def start_game(self):
        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_updates()

    def get_inputs(self):
        dealer= int(input("please guess a card number [1,13]: "))

    def do_updates(self):
        if not self.is_playing:
            return
            guess=random.randint(1,13)
            self.score+=guess.points
            self.total_score += self.score

    def do_outputs(self):
        if not self.is_playing:
            return
        values
        guess=random.randint(1,13)
        values+=f'{guess.value}'   