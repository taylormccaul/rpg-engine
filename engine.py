import sys, time, random

def slow_type(string):
    type_speed = 50
    for letter in string:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(random.random() * 10.0 / type_speed)
        print(end='')

def display_text_lines(text):
    for line in text:
        slow_type(line)
        input('')
