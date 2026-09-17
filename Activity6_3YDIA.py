# 3. Student ID Checker -1-2-1-1-1-e3-2-42-34-2-3
import re

id = input('Enter Student ID: ')
pattern_id = r"\d{4}-\d{4}" # pattern is ####-####
if re.fullmatch(pattern_id, id): # if input follows pattern
    print('Valid Student ID.')
else:
    print('Invalid Student ID.')
