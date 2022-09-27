import string
grammar_file_path = "D:\\VS_CODE\\Python\\7\\7_1.txt"
Rhs = []
Grammar = []
CalculatedFirst = []
cFirst = []


def FindFirst(nT):
    if nT in string.ascii_lowercase or (nT in string.punctuation.replace("@", '')):
        cFirst.append(nT)
        return 0
    count = 0
    indexRhs = Rhs.index(nT)
    tmpFirst = Grammar[indexRhs][1]
    for fst in tmpFirst:
        if fst[count].islower() or (fst[count] in string.punctuation.replace("@", '')):
            cFirst.append(fst[count])
            continue
        if fst[count].isupper():
            while(FindFirst(fst[count]) and (count+1 < len(fst))):
                count += 1
            else:
                if not(count+1 < len(fst)):
                    cFirst.append('@')
        else:
            return 1


with open(grammar_file_path, 'r') as in_:
    all_lines = in_.readlines()
    for line in all_lines:
        splitGrammer = line.strip().split('->')
        Rhs.append(splitGrammer[0])
        Grammar.append([splitGrammer[0], splitGrammer[1].strip().split('|')])
for rhs in Rhs:
    if (rhs not in [_[0] for _ in CalculatedFirst]):
        x = FindFirst(rhs)
        if (x):
            cFirst.append('@')
        CalculatedFirst.append([rhs, cFirst])
        cFirst = []
# @printingFirst
for first in CalculatedFirst:
    print(f"First :: ({first[0]}) is ==> {tuple(first[1])}")
