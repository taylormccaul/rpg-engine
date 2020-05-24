import sys, time, random, re

story = {
  1: {'Text': [ "Hello there..", "I bet you werent exepecting to hear from me so soon...", "...you seem a little confused do you know who I am?"],
    'Options': [("Yeah of course!", 2), ("I'm sorry I don't", 3), ("I'm busy right now", 3)]}
}

def basic_dict(target_dict, page_num):
    target_dict.update({page_num: {'Text': [], 'Options': []}})
    #print(target_hash)
    return target_dict

f = open("story.txt", "r")

#Do text, options, and page appending separately

def loop_pages(user_input, input_dict, page_count):

    if user_input != 'Options\n' and user_input != 'Page {}\n'.format(page_count) and user_input != '\n' and re.search("([A-z]+\W*,\s*\d)", user_input) == None:
        input_dict[page_count]['Text'].append(user_input)
        #print(input_dict[page_count]['Text'])

    if user_input == 'Options':
        print("Found an options header")
    elif user_input != 'Options' and re.search("([A-z]+\W*,\s*\d)", user_input) != None:
        input_dict[page_count]['Options'].append((tuple(user_input.replace('\n', '').split(","))))
        """#while user_input != 'Page {}'.format(page_count + 1):
            #if user_input == 'Page {}'.format(page_count + 1):
                #break

        option_text = user_input
        try:
            option_num = int(user_input)
        except:
            return False

        input_dict[page_count]['Options'].append((user_input, option_num))
        print(input_dict[page_count]['Options'])

    elif user_input == 'Page {}'.format(page_count + 1):
        print('Hello from page {}'.format(page_count + 1))
        return True"""
    """while user_input != 'o' and user_input != 'quit' and user_input != 'Next':
        input_dict[page_count]['Text'].append(user_input)
        print(input_dict[page_count]['Text'])
        user_input = input('')

    if user_input == 'o':
        #user_input = input('Moving to options settings...')
        while user_input != 'quit' and user_input != 'Next':

            if user_input == 'Next':
                break

            user_input = input("Enter the text of the option: ")

            try:
                option_num = int(input("Enter the number of the page to jump to: "))
            except:
                #print(user_input)
                break

            input_dict[page_count]['Options'].append((user_input, option_num))
            print(input_dict[page_count]['Options'])

    if user_input == 'quit' or user_input == 'Next':
            print("hello")"""


test = {}

def write_page():
    page_counter = 1
    basic_dict(test, page_counter)

    for line in f:
        if line == 'Page {}\n'.format(page_counter + 1):
            page_counter += 1
            basic_dict(test, page_counter)
            loop_pages(line, test, page_counter)
        elif line == 'Options':
            loop_pages(line, test, page_counter)
        elif line == '\n':
            line.replace("\n", "")
        elif line != 'Options' and re.search("([A-z]+\W*,\s*\d)", line) != None:
            loop_pages(line, test, page_counter)
        else:
            loop_pages(line, test, page_counter)
write_page()
print(test)

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
