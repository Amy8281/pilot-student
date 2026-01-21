from time import sleep
from termcolor import colored
from simpleeval import simple_eval
import random

class Bot:

    wait = 1

    def __init__(self, runtype='once'):
        self.q = ''
        self.a = ''
        self.runtype = runtype

    def _think(self, s):
        return s
    
    def _format(self, s):
        return colored(s, 'blue')
    
    def _say(self, s):
        sleep(Bot.wait)
        print(self._format(s))
    
    def _run_once(self):
        self._say(self.q)
        self.a = input()
        self._say(self._think(self.a))
    
    def _run_looped(self):
        self._say(self.q)
        while True:
            self.a = input()
            if self.a.lower() in ['x', 'q', 'exit', 'quit']:
                break
            else:
                self._say(self._think(self.a))
    
    def run(self):
        if self.runtype == 'once':
            self._run_once()
        elif self.runtype == 'looped':
            self._run_looped()


class HelloBot(Bot):
    def __init__(self, runtype='once'):
        super().__init__(runtype)
        self.q = "Hi, what is your name?"

    def _think(self, s):
        return f"Hello {s}"
    

class GreetingBot(Bot):
    def __init__(self, runtype='once'):
        super().__init__(runtype)
        self.q = "How are you today?"

    def _think(self, s):
        if 'good' in s.lower() or 'fine' in s.lower():
            return "I'm feeling good too"
        else:
            return "Sorry to hear that"
        

class FavoriteColorBot(Bot):
    def __init__(self, runtype='once'):
        super().__init__(runtype)
        self.q = "What's your favorite color?"

    def _think(self, s):
        colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'purple']
        return f"You like {s.lower()}? My fovorite color is {random.choice(colors)}"
        

class CalcBot(Bot):
    def __init__(self, runtype='once'):
        super().__init__(runtype)
        self.q = "Through recent upgrade I can do calculation now. Input some arithmetic expression to try. Type 'x', 'q', 'exit', 'quit' to quit"

    def _think(self, s):
        result = simple_eval(s)
        return f"Done. Result = {result}"


class Garfield:

    def __init__(self, wait=1):
        Bot.wait = wait
        self.bots = []

    def add(self, bot):
        self.bots.append(bot)

    def _prompt(self, s):
        print(s)
        print()

    def run(self):
        self._prompt("This is Garfield dialog system. Let's talk.")
        for bot in self.bots:
            bot.run()

if __name__ == '__main__':
    garfield = Garfield(1)
    garfield.add(HelloBot())
    garfield.add(GreetingBot())
    garfield.add(FavoriteColorBot())
    garfield.add(CalcBot('looped'))
    garfield.run()