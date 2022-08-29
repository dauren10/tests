def full_name(f,l,m=''):
    if m:
        full=f + ' ' + l + ' ' + m
    else:
        full=f + ' ' + l
    return full.title()

#print(full_name('dauren','shalabayev'))