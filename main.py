import engine as en
import sys, time, random, re

story = {}

en.write_page(story)
en.replace_tuple_num(story)
counter = 1
page = story[counter]['Text']
for line in page:
    en.slow_type(line)
#en.get_response(story[1]['Options'])
