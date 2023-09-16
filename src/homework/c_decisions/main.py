import decisions 


options = int(input( 'Input your option '))

total = int(input("Input the total: "))

returned_ratio = decisions.get_options_ratio(options, total)        

Score = decisions.get_faculty_rating(returned_ratio)

print ("Your Rating: " + Score)



