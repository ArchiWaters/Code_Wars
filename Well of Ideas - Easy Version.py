#For every good kata idea there seem to be quite a few bad ones!
#In this kata you need to check the provided array (x) for good ideas 'good' and bad ideas 'bad'. #
# If there are one or two good ideas, return 'Publish!', if there are more than 2 return 'I smell a series!'.
# #If there are no good ideas, as is often the case, return 'Fail!'.
#Version_1
def well(x):
    k_good = 0;
    for num in x:
        if num == 'good':
            k_good += 1
    if 1 <= k_good <= 2:
        return 'Publish!'
    elif k_good > 2:
        return 'I smell a series!'
    elif k_good == 0:
        return 'Fail!'

#Version_2
def well(x):
    c = x.count('good')
    return 'I smell a series!' if c > 2 else 'Publish!' if c else 'Fail!'