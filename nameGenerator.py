import random
def characterNameGenerator():
    fNSeg= {
        1:"fay",
        2:"mon",
        3:"shi",
        4:"ren",
        5:"dem",
        6:"grog",
        7:"meon",
        8:"dawr",
        9:"freg",
        10:"con",
        11:"don",
        12:"ferg",
        13:"peow",
        14:"brun",
        15:"gein",
        16:"hun",
        17:"kirn",
        18:"pron",
        19:"dert",
        20:"qwey",
        21:"yuop",
        22:"greyn",
        23:"watt",
        24:"weil",
        25:"quin",
        26:"hut",
        27:"drag",
        28:"yunk",
        29:"brein",
        30:"sull"
        }
    firstSeg = random.randint(1,len(fNSeg))
    secondSeg = firstSeg
    while secondSeg == firstSeg:

        secondSeg = random.randint(1,len(fNSeg))
    name = fNSeg[firstSeg] + fNSeg[secondSeg]

    return name
