################################################################################
# Author: Miguel Castilho Oliveira
# Date: 03/17.2021
# Description afnkjwnfjkwnekjfnwejkfnkjwnfkjwnfwbfwbfkwbfkwfwf
################################################################################

def print_square(theList):
    print(theList[0])
    print(theList[1])
    print(theList[2])
    
def is_magic(theList):
    if ((theList[0][0] + theList[1][0] + theList[2][0]) == 15):
        if ((theList[0][1] + theList[1][1] + theList[2][1]) == 15):
           if ((theList[0][2] + theList[1][2] + theList[2][2]) == 15):
               if theList[0][0] + theList[0][1] + theList[0][2] == 15:
                  if ((theList[1][0] + theList[1][1] + theList[1][2]) == 15):
                    if ((theList[2][0] + theList[2][1] + theList[2][2]) == 15):
                        if ((theList[0][0] + theList[1][1] + theList[2][2]) == 15):
                            if ((theList[0][2] + theList[1][1] + theList[2][0]) == 15):
                               x = True
                            else:
                                x = False
                                
                        else:
                            x = False
           #efjkwjkfnwkflkwflkwfklwflkwfkljfwjflkwf                 
                    else:
                       x = False
                  else:
                      x = False
               else:
                 x = False
           else:
              x = False
           #jkwfjkwnfjkwiufhwjkf wf
        else:
           x = False
    else:
       x = False
    
    return(x)

def main():
#jknfkjnwkjfkwnfwflkwnfklwfwfw
    m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    m2 = [[5, 5, 5], [5, 5, 5], [5, 5, 5]]
    m3 = [[4, 9, 2], [3, 5, 7], [8, 1, 6]] 
    
    print("Your square is:")
    print_square(m1)
    if is_magic(m1) == True:
        print("It is a Lo Shu magic square!")
    else:
        print("It is not a Lo Shu magic square.")

    
if __name__ == '__main__':
    main()
