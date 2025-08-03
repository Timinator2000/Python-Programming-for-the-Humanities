import random
import timinator_tools


section, exercise_name = timinator_tools.get_section_and_exercise_names(__file__)
exec(f'from {exercise_name} import {exercise_name} as user_solution')
exec(f'from {exercise_name}_solution import {exercise_name} as suggested_solution')


success_message = 'This is not the end. It is not even the beginning of the end. '
success_message += 'But it is, perhaps, the end of the beginning.'
success_message += '\n\n'
success_message += '     —— Winston Churchill'


class StartToFinish(timinator_tools.PrintBasedExercise):
    
    def __init__(self):
        
        super().__init__(user_solution, suggested_solution, f'{section}{exercise_name}_solution.py')
        self.success_message = success_message
        self.num_random_test_cases = 100

        self.fixed_test_cases = [
            [1, 5],
            [-3, 0],
            [-4, 4],
            [5, -1],
            [0, 9]
        ]

        
    def display_test_case(self, test_case) -> None:
        start, finish = test_case
        self.send_msg(self.bug_channel, f'   start = {start}     finish = {finish}')
        
        
    def generate_random_test_case(self):
        return [random.randint(-20, 10), random.randint(0, 30)]


if __name__ == "__main__":
    exercise = StartToFinish()
    exercise.run()
