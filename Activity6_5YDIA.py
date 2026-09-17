#  5 Student Score Entry --------------------------------------
try:
    exam_score = input('Enter examination score: ')
    exam_score = int(exam_score)

    if 0 <= exam_score <= 100:
        print('Valid score.')
    else:
        print('Invalid input. Please enter a number in 0-100.')
except ValueError:
    print('Invalid input. Please enter a number.')