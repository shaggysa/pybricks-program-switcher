from pybricks.parameters import Button
from robot import HUB
from pybricks.tools import wait
class Program:
    def __init__(self, func:callable, run_number:int):
        self.func = func
        self.run_number = run_number

class ProgramSwitcher:
    def __init__(self):
        self.program_list = []

    def add_programs(self, programs:list[Program]):
        for i in programs:
            self.program_list.append(i)

    def run(self, wait_time_ms : int = 150, start_button:Button = Button.BLUETOOTH):
        self.program_list.sort(key=lambda program: program.run_number)

        current_run = 0
        current_program = self.program_list[current_run]
        while True:
            buttons = HUB.buttons.pressed()

            if Button.LEFT in buttons:
                if current_run == 0:
                    current_run = len(self.program_list) - 1
                else:
                    current_run -= 1
                current_program = self.program_list[current_run]

            if Button.RIGHT in buttons:
                if current_run == len(self.program_list) - 1:
                    current_run = 0
                else:
                    current_run += 1
                current_program = self.program_list[current_run]

            HUB.display.number(current_program.run_number)

            if start_button in buttons:
                current_program.func()

            else:
                wait(wait_time_ms)







