names = ['Larry', 'Curly', 'Moe']
message = "The Three Stooges: "
for index, name in enumerate(names): # loop through BOTH the index and the list elements.
    if index > 0: # if index is greate than 0
        message += ', '
    if index == len(names) - 1:
        message += 'and '
    message += name
print(message)

# ^^ better to make into a function, so we can change the order of the lineup on demand below
#####################################################################################
def introduce_stooges(names):
    message = 'The Three Stooges: '
    for index, name in enumerate(names):
        if index > 0:
            message += ', '
        if index == len(names) - 1:
            message += 'and '
        message += name
    print(message)

introduce_stooges(["Moe", "Larry", "Shemp"])
introduce_stooges(["Larry", "Curly", "Moe"])
###############################################

# decompose further...
def introduce(title, names):
    message = f'{title}'
    for index, name in enumerate(names):
        if index > 0:
            message += ', '
        if index == len(names) - 1:
            message += 'and '
        message += name
    print(message)

###############################################
# decompose by concerns, even more!!
def join_names(names): # this function only handles how NAMES are joined
    name_string = ''
    for index, name in enumerate(names):
        if index > 0:
            name_string += ', '
        if index == len(names) - 1:
            name_string += 'and '
        name_string += name
    return name_string

def introduce(title, names):
    print(f'{title}: {join_names(names)}')