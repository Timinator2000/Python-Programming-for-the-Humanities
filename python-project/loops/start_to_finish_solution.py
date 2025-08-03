def start_to_finish(start: int, finish: int) -> None:
    for i in range(start, finish + 1):
        print(i)


# alternate solution using str.join()
def start_to_finish_alt(start: int, finish: int) -> None:
    if finish >= start:
        print('\n'.join(str(i) for i in range(start, finish + 1)))