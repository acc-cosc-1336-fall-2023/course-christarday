

def get_options_ratio(option, total):
 
    if total != 0:
        ratio = option / total
    else:
        ratio = 0 
    return ratio
#print(get_options_ratio(10, 5)) 
 
def get_faculty_rating(ratio):
    result = ""

    if(ratio >= 0.9 and ratio <=1):
        result = "Excellent"
    elif(ratio >= 0.8 and ratio <.9):
        result = "Very Good"
    elif( ratio >= 0.7 and ratio < 0.8 ):
        result = "Good"
    elif(ratio >= 0.6 and ratio < 0.7):
        result = "Needs Improvement"
    elif(ratio >= 0.0 and ratio < 0.6):
        result = "Unacceptable"
    else:
        result = "Invalid"
    
    return result 
# print(get_faculty_rating(1.9))