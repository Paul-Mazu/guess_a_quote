
def replace1(text, author):
    first, last = author.split()
    return text.replace(first, '******').replace(last, '******')
    


text = 'Theodor Seuss Geisel was born 2 March 1904 in Springfield'
author ='Dr. Seuss'
print(replace1(text, author))