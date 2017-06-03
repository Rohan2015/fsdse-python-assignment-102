def is_rotation(s1,s2):
    if s1 == None:
        return False
    elif s1 == '' and len(s2) != 0:
        return False
    elif s1 == '' and s2 == '':
        return True
    elif len(s1) != len(s2):
        return False
    else:
        for i in range(len(s1)):
            if s1[i:] and s2[:i]:
                return True

s1 = 'foobarbaz'
s2 = 'barbazfoo'
is_rotation(s1,s2)
