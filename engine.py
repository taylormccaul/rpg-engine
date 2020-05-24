import sys, time, random, re

def basic_dict(target_dict, page_num):
    target_dict.update({page_num: {'Text': [], 'Options': []}})
    return target_dict

f = open("story.txt", "r")

def replace_new_line(target_dict):
    counter = 0
    for item in target_dict:
        z = re.search("\n", item)
        if z != None:
            z = re.sub("\n", "", item)
            item = z
            target_dict[counter] = item
        counter += 1
    return target_dict

def replace_tuple_num(target_dict):
    counter = 0
    for item in target_dict[1]['Options']:
        int_temp = int(target_dict[1]['Options'][counter][1])
        new_tuple = target_dict[1]['Options'][counter][0], int_temp
        target_dict[1]['Options'][counter] = new_tuple
        counter += 1
    return target_dict

def loop_pages(user_input, input_dict, page_count):
    if user_input != 'Options\n' and user_input != 'Page {}\n'.format(page_count) and user_input != '\n' and re.search("([A-z]+\W*,\s*\d)", user_input) == None:
        input_dict[page_count]['Text'].append(user_input)

    if user_input == 'Options':
        print("Found an options header")
    elif user_input != 'Options' and re.search("([A-z]+\W*,\s*\d)", user_input) != None:
        input_dict[page_count]['Options'].append((tuple(user_input.replace('\n', '').split(","))))

def write_page(target_dict):
    page_counter = 1
    basic_dict(target_dict, page_counter)

    for line in f:
        if line == 'Page {}\n'.format(page_counter + 1):
            replace_new_line(target_dict[page_counter]['Text'])
            page_counter += 1
            basic_dict(target_dict, page_counter)
            loop_pages(line, target_dict, page_counter)
        elif line != 'Options' and re.search("([A-z]+\W*,\s*\d)", line) != None:
            loop_pages(line, target_dict, page_counter)
        else:
            loop_pages(line, target_dict, page_counter)
        replace_new_line(target_dict[page_counter]['Text'])
        replace_tuple_num(target_dict)
    return target_dict

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
    return option_index

def story_flow(story):
    curr_page = 1
    while curr_page != None:
        page = story.get(curr_page, None)

        if page == None:
            curr_page = None
            break

        display_text_lines(page['Text'])

        if len(page['Options']) == 0:
            curr_page = None
            break

        curr_page = get_response(page['Options'])
        print(curr_page)
