def getDestination(finalorNot, temp):
    ReachedStates = []
    if(finalorNot):
        itemIndex = fList.index(temp)
        get0Reach = fStates[itemIndex][1][0]
        get1Reach = fStates[itemIndex][1][1]
        ReachedStates = [get0Reach, get1Reach]
    else:
        itemIndex = nfList.index(temp)
        get0Reach = nfStates[itemIndex][1][0]
        get1Reach = nfStates[itemIndex][1][1]
        ReachedStates = [get0Reach, get1Reach]
    return ReachedStates


def getIndexEqui(temp):
    r_index = [(i, equi.index(temp))
               for i, equi in enumerate(Equivalence) if temp in equi]
    return r_index


dfa_file_path = "D:\\VS_CODE\\Python\\5_2\\dfav1.txt"  # @param {type:"string"}
fStates = []
nfStates = []
fList = []
nfList = []
Equivalence = []
previousEquivalence = []
counter = 0
with open(dfa_file_path, 'r') as in_:
    all_lines = in_.readlines()
    for line in all_lines:
        if line[0] == ":":
            temp = line.split("-")
            fStates.append([temp[0][1:], temp[1].strip()])
        else:
            temp = line.split("-")
            nfStates.append([temp[0], temp[1].strip()])
    fList.extend([_[0] for _ in fStates])
    nfList.extend([_[0] for _ in nfStates])
    Equivalence.append(fList)
    Equivalence.append(nfList)
    print(f"{counter}th Equivalence {Equivalence}")
    while(previousEquivalence != Equivalence):
        tempEquivalence = []
        dontCareState = []
        counter += 1
        previousEquivalence = Equivalence
        for Estate in Equivalence:
            if len(Estate) == 1:
                dontCareState.append(Estate)
                pass
            else:
                for i, x in enumerate(Estate):
                    isAppended = False
                    if i == 0:
                        tempEquivalence.append([x])
                        pass
                    else:
                        isAppended = False
                        for t_index, item in enumerate(tempEquivalence):
                            temp = "".join(item[0])
                            itemIndex = 0
                            yfinalorNot = False
                            xfinalorNot = False
                            if temp in fList:
                                xfinalorNot = True
                            if x in fList:
                                yfinalorNot = True
                            reachedStatesx = getDestination(xfinalorNot, temp)
                            reachedStatesy = getDestination(yfinalorNot, x)
                            temIndexEqi = getIndexEqui(temp)
                            if all((((rx in (Equivalence[temIndexEqi[0][0]]+list(temp))) or (rx == ry)) and ((ry in (Equivalence[temIndexEqi[0][0]]+list(x))) or (rx == ry))) for rx, ry in zip(reachedStatesx, reachedStatesy)) or (reachedStatesx == reachedStatesy):
                                tempEquivalence[t_index].append(x)
                                isAppended = True
                        if(not isAppended):
                            tempEquivalence.append([x])
        tempEquivalence += dontCareState
        print(f"{counter}th Equivalence {tempEquivalence}")
        Equivalence = tempEquivalence
print(f"Final :: Equivalence {tempEquivalence}")
# @Replacing States
toChange = [_ for _ in Equivalence if len(_) > 1]
# @Creating table of minimi
print("\n----------------- Generating Equivalence Table -----------------\n")
print("{:<5}=====>{:^5}  || {:^8}".format("[Q:S]","[0]", "[1]"))
print("-----------------------------------------")
for states in Equivalence:
    getInitial = states[0]
    if states[0] in fList:
        reachedStates = getDestination(True, states[0])
        for c in toChange:
            for i in range(2):
                if reachedStates[i] in c:
                    reachedStates[i] = "".join(c)
        print("{:<5}=====>{:^5}  || {:^8}".format(
            "".join(states), reachedStates[0], reachedStates[1]))
    else:
        reachedStates = getDestination(False, states[0])
        for c in toChange:
            for i in range(2):
                if reachedStates[i] in c:
                    reachedStates[i] = "".join(c)
        print("{:<5}=====>{:^5}  || {:^8}".format(
            "".join(states), reachedStates[0], reachedStates[1]))
