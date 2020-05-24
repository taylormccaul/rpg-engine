import sys, time, random

story = {
  1: {'Text': [ "Hello there..", "I bet you werent exepecting to hear from me so soon...", "...you seem a little confused do you know who I am?"],
    'Options': [("Yeah of course!", 2), ("I'm sorry I don't", 3), ("I'm busy right now", 3)]}
}

def basic_struct(target_hash, page_num):
    target_hash.update({page_num: {'Text': [], 'Options': []}})
    #print(target_hash)
    return target_hash

test = {}

def write_page():
    print("Starting on page 1. Enter input line-by-line")

    page_counter = 1
    basic_struct(test, page_counter)
    line = input('')

    while line != 'Options' and line != 'quit' and line != 'Next page':
        test[page_counter]['Text'].append(line)
        print(test[page_counter]['Text'])
        line = input('')

    if line == 'Options':
        while line != 'quit' and line != 'Next page':
            option_text = input("Enter the text of the option: ")
            option_num = int(input("Enter the number of the page to jump to: "))

            test[page_counter]['Options'].append((option_text, option_num))
            print(test[page_counter]['Options'])
            
            if line == 'quit' or line == 'Next page':
                break
    elif line == 'Next page':
        

#write_page()

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

def get_valid_input(valid_input):
    user_input = input('Enter an input: ')

    while str(user_input) not in valid_input:
        print("Invalid input. Your input options are:")
        print(valid_input)
        user_input = input('Enter an input: ')

    if str(user_input) in valid_input:
        return user_input

def get_response(options):
    for index, option in enumerate(options):
        print('{}. {}'.format(index + 1, option[0]))
        valid_inputs = [str(num+1) for num in range(len(options))]
    option_index = int(get_valid_input(valid_inputs))
    print(option_index)
        #print(options[option_index][1])

#print(story[1]['Options'])
#get_response(story[1]['Options'])
"""def story_flow(story):
    curr_page = 1
    while curr_page != None:
        page = story.get(curr_page, None)
        if page == None:
            curr_page = none
            break

        display_text_lines(page['Text'])

        if len(page['Options']) == 0:
            curr_page = None
            break

        curr_page = get_response(page['Options'])"""
