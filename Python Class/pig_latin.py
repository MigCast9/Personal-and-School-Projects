################################################################################
# Author: Miguel Castilho Oliveir
# Date: 03/26/2021
# Description lkemfwmfiwifjiowfwnfuwbfuiwfiuwnfuwfuiwnfiwfwnf
################################################################################

def pig(String):
    #Does allthe necesssary stuff yeah!
    splitStringList = String.split()
    listPigLatin = []

    for word in splitStringList:
    
        firstLetter = word[0]
        
        pigTranslation = word.strip(word[0]) + firstLetter + "ay"
        
        listPigLatin.append(pigTranslation)
    
    newString = " ".join(listPigLatin)
    
    newStringLower = newString.lower()
    newStringCap = newStringLower.capitalize()
    
    return(newStringCap)
#Main functio noufnwuinfuiwfuiwfuiwfwfwf
def main():
    
    userString = (input("Enter a string: "))
    
    pigLatin = pig(userString)
    
    print(pigLatin)


if __name__ == '__main__':
    main()
