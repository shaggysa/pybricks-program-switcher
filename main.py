from program_switcher import *
from example_programs import *
import block_template

#example_program, adapt to fit your use case

prog_1 = Program(drive_forever, 0)
prog_2 = Program(turn_left_90, 1)
prog_3 = Program(turn_right_90, 2)
prog_4 = Program(drive_5_seconds, 3)
prog_5 = Program(block_template.run, 4)

switcher = ProgramSwitcher()
switcher.add_programs([prog_1, prog_2, prog_3, prog_4])
switcher.run()