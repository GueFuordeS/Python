from sys import argv

def pa(a1, an, r):
    i = 1
    ax = a1
    
    if (an >= 1):
        seq.append(a1)
        while i < an:
            ax += r
            seq.append(ax)
            i += 1
    else:
        return


seq = []
pa(int(argv[1]), int(argv[2]), int(argv[3]))
print(seq)
