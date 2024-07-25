# prints a list in table format


# test = [
#         'wefwe fwefwefwef wefodf 231n29'.split(),
#         'wefjf2o f42o8f 238f 230f273 davs'.split(),
#         '13r fsdouhre wofhweh we hey s'.split(),
#         'ifwe fhw eiufhwiefh eiw'.split()
# ]

# very proud of this one. i been meaning to make it for a while
# * you just gotta hope that there is no extra long characters
def table_print(lis:list[list], header:list=[]):
    lis = [[str(l) for l in i] for i in lis]
    # sets header
    hasHeader = header != []
    if hasHeader:
        lis = [header] + lis

    max_list_items = max([len(i) for i in lis])

    max_char_lengths = []
    # get max length
    for i in range(max_list_items):
        char_lengths = []
        for l in lis:
            if len(l) > i:
                char_lengths += [len(l[i])]
        max_char_lengths += [max(char_lengths)]
    
    # prints breaks +-----+----------+---+
    print('+' + '+'.join(['-'*(length+2) for length in max_char_lengths]) + '+')

    for rowIndex, row in enumerate(lis):

        print('| ', end='')
        for cellIndex, length in enumerate(max_char_lengths):
            cell = ''
            if len(row) > cellIndex:
                cell = row[cellIndex]

            print(f"{cell.ljust(length, ' ')} | ", end='')
        print()
        if hasHeader and rowIndex == 0:
            print('+' + '+'.join(['-'*(length+2) for length in max_char_lengths]) + '+')

    print('+' + '+'.join(['-'*(length+2) for length in max_char_lengths]) + '+')

# table_print(test)
# print()
# table_print(test, header='david was here a lo ng time afo'.split())