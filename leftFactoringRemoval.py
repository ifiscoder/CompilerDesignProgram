import string


def getComman(RhsGrammar):
    isMatched = False
    for i, Rg in enumerate(RhsGrammar):
        testingCondition = [(RhsGrammar[i][0] == _[0])
                            for _ in RhsGrammar[i+1:]]
        if(any(testingCondition)):
            # print("matched")
            isMatched = True
        if(isMatched):
            indexMatched = testingCondition.index(True)
            # print(indexMatched+(i+1))
            indices = [(index+(i+1))
                       for index, _ in enumerate(testingCondition) if (_)]
            indices.append(i)
            # print(indices)
            break
    return indices


def longestCommonPrefix(listInput):
    longest_pre = ""
    if not listInput:
        return longest_pre
    shortest_str = min(listInput, key=len)
    for i in range(len(shortest_str)):
        if all([x.startswith(shortest_str[:i+1]) for x in listInput]):
            longest_pre = shortest_str[:i+1]
        else:
            break
    return longest_pre


newProductionSet = []
unusedVaraible = list(string.ascii_uppercase)
# can be x;y;z multiple grrammar
Grammar = "S->iEtS|iEtSeS|a|b"
seprateProduction = Grammar.split(';')
# print(seprateProduction)
for production in seprateProduction:
    splitProduction = production.split('->')
    # print(splitProduction)
    RhsGrammar = splitProduction[1].split('|')
    # print(RhsGrammar)
    commonIndices = getComman(RhsGrammar)
    # print(commonIndices)
    commonEle = [_ for index, _ in enumerate(
        RhsGrammar) if (index in commonIndices)]
    longestPrefix = longestCommonPrefix(commonEle)
    # print(longestPrefix)
    NewRhsGrammar = [f"|{_}" for _ in RhsGrammar if (_ not in commonEle)]
    # print(NewRhsGrammar)
    newVariable = unusedVaraible.pop()
    if (newVariable == splitProduction[0]):
        temp = unusedVaraible.pop()
        unusedVaraible.append(newVariable)
        newVariable = temp
    newParentProduction = f"{splitProduction[0]}->{longestPrefix}{newVariable}{''.join(map(str,NewRhsGrammar))}"
    # print(newParentProduction)
    newProductionSet.append(newParentProduction)
    temp = ''.join(map(str, ["@|" if _.replace(longestPrefix, '') ==
                   '' else f"{_.replace(longestPrefix, '')}|" for _ in commonEle]))
    newChildProduction = f"{newVariable}->{temp[:-1]}"
    newProductionSet.append(newChildProduction)
    # print(newChildProduction)
for newProduction in newProductionSet :
    print(newProduction)
