def colored(seq):
    b_colors = {
        'A': '\033[92m]',
        'C': '\033[94m]',
        'G': '\033[93m]',
        'T': '\033[91m]',
        'U': '\033[91m]',
        'reset': '\033[0;0m]',
    }

    tempStr = ""
    for nuc in seq:
        if nuc in b_colors:
            tempStr += b_colors[nuc] + nuc
        else:
            tempStr += b_colors['reset'] + nuc
    return tempStr + '\033[0;0m'