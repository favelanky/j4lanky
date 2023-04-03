import os
from dotenv import load_dotenv

load_dotenv('.env')

submissions_dir = os.getenv('SUBMISSIONS_DIR')

# mapping from file name to number-symbol
redirection = {}
is_best = {}

was_error = False
# Read judgements
with open('./judgements.txt', 'r') as f:
    line = f.readline()
    number = '000'
    symbol = '?'  # M, H, I
    while line:
        line = line.strip()
        sep = line.split('-')
        print(sep, number, symbol)
        if len(sep) >= 2 and line.find(':') != -1:  # if it's name and symbol
            sep = [sep[0], sep[1].split(':')[0]]
            line = line.replace(':', ' ')
            print(line)
            if line.lower().find('invalid-submissions') != -1:
                number = '000'
                symbol = 'I'
            elif sep[0].isdigit():
                number = sep[0].split(' ')[0].zfill(3)  # because of comments
                symbol = sep[1][0].upper()
            else:
                number = sep[1].split(' ')[0].zfill(3)  # because of comments
                symbol = sep[0][0].upper()
        elif sep[0] != '':  # check if string is not empty
            key = line.split(' ')[0].zfill(3)  # because of comments
            if key.find('best') != -1:
                is_best[key] = True
            if key not in redirection:
                redirection[key] = number + '-' + symbol
            else:
                print('ERROR: ' + key + ' was used twice!')
                was_error = True
        line = f.readline()

if was_error:
    exit(0)

# print('-------')
# for key in redirection:
#     print(key, redirection[key])
# print('-------')

total_warnings = 0
# go into cloned dir and iterate through files
for file in os.listdir(submissions_dir):
    print(file)
    sum = 0
    if file.endswith('md'):
        name = file.split('.')[0]
        if name not in redirection:
            print('WARNING: ' + name + ' is forgotten!')
            total_warnings += 1
            continue
        # create a new directory
        dir_name = redirection[name]
        if dir_name == '000-I':
            dir_name = 'invalid'
        if not os.path.exists(submissions_dir + '/' + dir_name):
            os.mkdir(submissions_dir + '/' + dir_name)
        # move file
        if name in is_best:
            os.rename(submissions_dir + '/' + file, submissions_dir + '/' + dir_name + '/' + file + '-best')
        else:
            os.rename(submissions_dir + '/' + file, submissions_dir + '/' + dir_name + '/' + file)

print('Total warnings: ' + str(total_warnings))
print('Done')
