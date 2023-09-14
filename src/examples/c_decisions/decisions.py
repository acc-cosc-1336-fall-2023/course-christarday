def test_config():
    return True

def get_letter_grade(grade):
    letter_grade = ""
    
    if(grade >= 90 and grade <= 100):
        letter_grade = "A"
    elif(grade >= 80 and grade < 90 ):
         letter_grade = "B"
    elif(grade >= 70 and grade < 80):
        letter_grade = "C"
    elif(grade >= 60 and grade < 70):
        letter_grade = "D"
    elif(grade >= 0 and grade < 60):
        letter_grade = "F"
    else:
        letter_grade = "Invalid Grade"


    return letter_grade


    return letter_grade    
    
