################################################################################
# Author: Miguel Castilho Oliveira
# Date: 04/02/2021
# Description Checks the state capital for every US state, which is way better than looking on google if you ask me
################################################################################
def get_state_data():
    with open("state_capitals.txt", 'r') as fid:
        stateCap = []
        for line in fid:
            stateCap.append(line.strip())

    pureStateCap = []
    for i in range(len(stateCap)):
        newList = stateCap[i].split(",")
        pureStateCap.append(newList[0])
        pureStateCap.append(newList[1])
    
    stateDic = {}
    for item in range(0,100, 3):
    #state names as keys and states as values
          stateDic[pureStateCap[i]] = pureStateCap[i+1]
    print(stateDic)
        


def main():
    get_state_data()

if __name__ == '__main__':
    main()
