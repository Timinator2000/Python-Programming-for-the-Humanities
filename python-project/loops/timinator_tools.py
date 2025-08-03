# Last Edited: August 2, 2025 7:37pm MDT

import re
from copy import deepcopy
import builtins
import sys
import os
import random


GITHUB, PC = range(2)

PLATFORM = PC

CONGRATS = ['Kudos!',
            'Well Done!',
            'Bravo!',
            'Perfect!',
            'Nice Job!',
            'Keep It Up!',
            'Attaboy!',
            'Nice Work!',
            'Excellent My Friend!',
            'Excelente Mi Amigo!',
            'Awesome!',
            'Hooray!',
            'Way To Go!',
            'Encore!',
            'Great Effort!',
            'Top Notch!',
            'There You Go!',
            'Take a Bow!',
            'Great Work!',
            'Outstanding!',
            'Exceptional Work!',
            'Superb!',
            'First-Class Effort!',
            'Brilliant!',
            'You are a Champion!',
            'Stellar!',
            'Magnificent Job!',
            'Dazzling Work!',
            'Stupendous!',
            'Marvelous!',
            'B-E-A-UTIFUL!',
            'Congratulations!']

CONGRATS_EMOJIS = '🌟🔥👏💥🎆🎉🥳💓💖💗🤟💯😀🤩😍'

BUG = ['Oops!',
       'Uh-oh!',
       'Oh no!',
       'Hmmm?',
       'Might have to try again!',
       'Ugh!',
       'Egad!']

BUG_EMOJIS = '🐞🐛🪲🦗😔😢😧'


def get_section_and_exercise_names(file):
    if PLATFORM == GITHUB:
        m = re.search(r"(?P<section>[\w\-]+/)(?P<exercise>\w+)_test.py", file)
        if m is not None:
            return m.group('section'), m.group('exercise')

    if PLATFORM == PC:
        # Normalize path for current OS
        normalized_path = os.path.normpath(file)

        # Split the path into directory and filename
        dir_path, filename = os.path.split(normalized_path)
        dir_path += "\\"

        # Extract the exercise name from the filename
        m = re.match(r"(?P<exercise>\w+)_test\.py$", filename)
        if m:
            exercise = m.group("exercise")
            return dir_path, exercise

    return None

            
class Exercise():
    
    PRINT_TEST_CASES = False
    CONTAINERS = ['list', 'tuple', 'set']
    
    def __init__(self, user_solution, suggested_solution, solution_path):
        self.fixed_test_cases = []
        self.num_random_test_cases = 0
        self.user_solution = user_solution
        self.suggested_solution = suggested_solution
        self.success_message = ''
        self.first_failed_test_case = None

        with open(solution_path, 'r') as f:
            self.suggested_solution_text = f.read()

        self.success_channel = f'{random.choice(CONGRATS)} {random.choice(CONGRATS_EMOJIS)}'
        self.bug_channel = f'{random.choice(BUG)} {random.choice(BUG_EMOJIS)}'


    def send_multiline_text(self, channel, msg):
        for line in msg.strip().split('\n'):
            self.send_msg(channel, line)

        
    def send_msg(self, channel, msg):
        print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))

            
    def success(self):
        print("TECHIO> success true")

            
    def fail(self):
        print("TECHIO> success false")

            
    def container_element_types(self, container) -> str:
        element_types = {self.data_type(element) for element in container}
        
        if len(element_types) > 1:
            return '[multiple types]'
        
        if len(element_types) == 1:
            return f'[{element_types.pop()}]'

        return '[]'
    
    
    def data_type(self, data) -> str:
        string = str(type(data)).split("'")[-2]
        
        if string in Exercise.CONTAINERS:
            string += self.container_element_types(data)
        
        if string == 'dict':
            key_types = self.container_element_types(data.keys())
            value_types = self.container_element_types(data.values())

            if len(data) == 0:
                string += '[]'
            else:
                string += f'[{key_types[1: -1]}, {value_types[1: -1]}]'
            
        return string
    
    
    def display_test_case(self, test_case):
        print('THIS METHOD MUST BE OVERRIDDEN')
        return None


    def generate_random_test_case(self):
        print('THIS METHOD MUST BE OVERRIDDEN')
        return None


    def display_first_failed_test_case(self):
        expected_answer = self.generate_answer(self.suggested_solution, self.first_failed_test_case)
        user_answer = self.generate_answer(self.user_solution, self.first_failed_test_case)
            
        expected_answer_format = self.data_type(expected_answer)
        user_answer_format = self.data_type(user_answer)

        if expected_answer != user_answer:
        
            self.send_msg(self.bug_channel, 'First Failed Test Case:')
            self.send_msg(self.bug_channel, '')
            self.send_msg(self.bug_channel, f'Input:')
            self.display_test_case(self.first_failed_test_case)
            self.send_msg(self.bug_channel, '')
            self.send_msg(self.bug_channel, f'Expected answer = {expected_answer}')
            self.send_msg(self.bug_channel, f'Your answer     = {user_answer}')
            self.send_msg(self.bug_channel, '')
            self.send_msg(self.bug_channel, f'Expected answer format = {expected_answer_format}')
            self.send_msg(self.bug_channel, f'Your answer format     = {user_answer_format}')
            self.send_msg(self.bug_channel, '')
            
            
    def generate_answer(self, solution, test_case):
        return solution(*deepcopy(test_case))

                
    def run_test_case(self, test_case):
        if Exercise.PRINT_TEST_CASES:
            print(f'{test_case=}')

        expected_answer = self.generate_answer(self.suggested_solution, test_case)
        user_answer = self.generate_answer(self.user_solution, test_case)
            
        expected_answer_format = self.data_type(expected_answer)
        user_answer_format = self.data_type(user_answer)

        if expected_answer_format != user_answer_format:
            if not self.first_failed_test_case:
                self.first_failed_test_case = test_case
            return False

        if expected_answer != user_answer:
            if not self.first_failed_test_case:
                self.first_failed_test_case = test_case
            return False

        return True
                
        
    def run(self):
        
        count = 0
        for test_case in self.fixed_test_cases:
            if self.run_test_case(test_case):
                count += 1

        self.send_msg('Standard Output', f'{count} of {len(self.fixed_test_cases)} fixed test cases solved correctly.')
        
        count = 0
        for _ in range(self.num_random_test_cases):
            if self.run_test_case(self.generate_random_test_case()):
                count += 1
                
        self.send_msg('Standard Output', f'{count} of {self.num_random_test_cases} random test cases solved correctly.')

        if self.first_failed_test_case:
            self.fail()
            self.display_first_failed_test_case()
            return
                
        self.success()
        self.send_multiline_text(self.success_channel, self.success_message)
        self.send_multiline_text(f'Suggested Solution ✅', self.suggested_solution_text)



class PrintBasedExercise(Exercise):

    def __init__(self, user_solution, suggested_solution, solution_path):
        super().__init__(user_solution, suggested_solution, solution_path)
        self.output_buffer = []
        self.output_buffer_new_line = True

        self.normal_print = builtins.print
        self.test_case_printing = False


    def __del__(self):
        builtins.print = self.normal_print


    def reset_output_buffer(self):
        self.output_buffer.clear()
        self.output_buffer_new_line = True


    def swap_printer(self):
        self.test_case_printing = not self.test_case_printing
        if self.test_case_printing:
            builtins.print = self.new_print
        else:
            builtins.print = self.normal_print

            
    def new_print(self, *args, sep=' ', end='\n', file=sys.stdout, flush=False):
        if file==sys.stderr:
            self.normal_print(*args, sep=sep, end=end, file=file, flush=flush)
        else:
            string = sep.join(str(arg) for arg in args)
            if not self.output_buffer_new_line:
                string = self.output_buffer.pop() + string

            string += end
            if string[-1] == '\n':
                self.output_buffer_new_line = True
                string = string[:-1]
            else:
                self.output_buffer_new_line = False

            self.output_buffer.extend(string.split('\n'))


    def generate_answer(self, solution, test_case):
        self.swap_printer()
        solution(*deepcopy(test_case))
        answer = deepcopy(self.output_buffer)
        self.reset_output_buffer()
        self.swap_printer()
        return answer

            
    def display_first_failed_test_case(self):
        expected_answer = self.generate_answer(self.suggested_solution, self.first_failed_test_case)
        user_answer = self.generate_answer(self.user_solution, self.first_failed_test_case)

        num_expected_lines = len(expected_answer)
        num_user_lines = len(user_answer)

        expected_lines_str = f'{num_expected_lines} line' + ('s' if num_expected_lines != 1 else '')
        user_lines_str = f'{num_user_lines} line' + ('s' if num_user_lines != 1 else '')

        if num_user_lines == 0:
            msg = f'You did not print anything. {len(expected_answer)} line'
            msg += ['s of printed output were ', ' of printed output was '][num_expected_lines == 1] + 'expected.'
            self.send_msg(self.bug_channel, msg)

        elif expected_answer != user_answer:
        
            self.send_msg(self.bug_channel, 'First Failed Test Case:')
            self.send_msg(self.bug_channel, '')

            msg = f'Your Output:'
            if num_expected_lines != num_user_lines:
                verb = 'was' if expected_lines_str == 1 else 'were'
                msg += f'   You printed {user_lines_str}.  {expected_lines_str} {verb} expected.'
            
            self.send_msg(self.bug_channel, msg)
            self.send_msg(self.bug_channel, '')

            expected_answer_length = len(expected_answer)
            user_answer_length = len(user_answer)
            for i in range(max(expected_answer_length, user_answer_length)):
                if i == expected_answer_length:
                    too_many = user_answer_length - i
                    msg = f'Your answer should have ended with {expected_lines_str} printed. The following '
                    msg += f'{too_many} line{"s" if too_many > 1 else ""} should not have been printed.'
                    self.send_msg(self.bug_channel, '')
                    self.send_msg(self.bug_channel, msg)
                    self.send_msg(self.bug_channel, '')

                if i == user_answer_length:
                    missing = expected_answer_length - i
                    msg = f'Your answer is correct so far, but you are missing the following '
                    msg += f'{missing} line' + 's.'[missing == 1:]
                    self.send_msg(self.bug_channel, '')
                    self.send_msg(self.bug_channel, msg)
                    self.send_msg(self.bug_channel, '')
            
                expected_line = '' if i >= expected_answer_length else expected_answer[i]
                user_line = '' if i >= user_answer_length else user_answer[i]

                if user_line:
                    self.send_msg(self.bug_channel, f'> {user_line}')
                    if expected_line and expected_line != user_line:

                        trailing_spaces = False
                        msg = f'There is a problem with the most recent line of output. '
                        if user_line.startswith(expected_line):
                            remaining_output = user_line[len(expected_line):]
                            if all(c.isspace() for c in remaining_output):
                                msg += f'It appears you have unnecessary trailing spaces at the end '
                                msg += f'of your output line.'
                                trailing_spaces = True

                        if not trailing_spaces:
                            msg = f'There is a problem with the most recent line of output. '
                            msg += f'It should have been...'
                        
                        self.send_msg(self.bug_channel, '')
                        self.send_msg(self.bug_channel, msg)

                        if not trailing_spaces:
                            self.send_msg(self.bug_channel, '')
                            self.send_msg(self.bug_channel, f'> {expected_line}')

                        break
 
                else:
                    self.send_msg(self.bug_channel, f'> {expected_line}')
                            
        self.send_msg(self.bug_channel, '')
        self.send_msg(self.bug_channel, f'Input:')
        self.send_msg(self.bug_channel, '')
        self.display_test_case(self.first_failed_test_case)
