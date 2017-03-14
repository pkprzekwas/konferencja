ctr = 0

while ctr < 10:
    ctr += 1
    if ctr == 3:
        print('omitting {ctr} ...'.format(ctr=ctr))
        continue
    elif ctr == 8:
        print('breaking {ctr} ...'.format(ctr=ctr))
        break
    print('ctr => {ctr}'.format(ctr=ctr))
