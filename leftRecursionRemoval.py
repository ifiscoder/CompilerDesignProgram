# @Remove Left Recursion
# enter the grammar Here
import string
newProductionSet = []
unusedVaraible = list(string.ascii_uppercase)
# can be x;z;y etc
Grammar = "S->S+a|S-b|x|y"
seprateProduction = Grammar.split(';')
print(seprateProduction)
for production in seprateProduction:
    splitProduction = production.split('->')
    # print(splitProduction)
    LeftGrammar = splitProduction[1].split('|')
    # print(LeftGrammar)
    if any((splitProduction[0] in _) for _ in LeftGrammar):
        newVariable = unusedVaraible.pop()
        newProduction = f"{splitProduction[0]}->"
        if (newVariable == splitProduction[0]):
            temp = unusedVaraible.pop()
            unusedVaraible.append(newVariable)
            newVariable = temp
        ExtraProduction = f"{newVariable}->"
        for count, splitEle in enumerate(LeftGrammar):
            if splitProduction[0] in splitEle:
                reConf = f"{splitEle[1:]}{splitProduction[0]}"
                ExtraProduction += f"{reConf}|"
            if splitProduction[0] not in splitEle:
                reConf = f"{splitEle.replace(splitProduction[0],'')}{newVariable}"
                # print(f"reconf={reConf}")
                # print(newVariable)
                # print(unusedVaraible)
                newProduction += f"{reConf}|"
        newProductionSet.append(newProduction[0:-1])
        newProductionSet.append(f"{ExtraProduction[0:-1]}|@")
        print(newProductionSet)
