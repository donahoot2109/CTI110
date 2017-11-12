# CTI-110
# M6HW1 - Test Average and Grade
# Timothy Donahoo
# 12NOV2017

# Get average test scores.
def average( score1, score2, score3, score4, score5):
    average = (score1 + score2 + score3 + score4 + score) / 5
    return avarage
    
# avarage test score based off of the users input
def grade (userScore):
    if (userScore < 60):
        return "F"
    elif(userScore < 70):
        return "D"
    elif (userScore < 80):
        return "C"
    elif (userScore < 90):
        return "B"
    elif (userScore < 101):
        return "A"
    
# Ask user to input there test score.
def askForScores():
   score1 = float(input( 'Please enter score 1: '))
   score2 = float(input( 'Please enter score 2: '))
   score3 = float(input( 'Please enter score 3: '))
   score4 = float(input( 'Please enter score 4: '))
   score5 = float(input( 'Please enter score 5: '))

   return score1, score2, score3, score4, score5
                         
# print users results.
def printResults(score1, score2, score3, score4, score5):
    print('Score\tLetter Grade')
    print(str(score1) + "\t\t" + grade(score1), \
          str(score2) + "\t\t" + grade(score2), \
          str(score3) + "\t\t" + grade(score3), \
          str(score4) + "\t\t" + grade(score4), \
          str(score5) + "\t\t" + grade(score5), sep = '\n')
    
# define the main function 
def main():
   score1, score2, score3, score4, score5 = askForScores()
   
# space
   print()
   printResults (score1, score2, score3, score4, score5)

# call the main function
main()
