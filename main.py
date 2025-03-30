score = 85
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("F")

# If grade is 90 or higher, print "A"
# Else if grade is 80 or higher, print "B"
# Else if grade is 70 or higher, print "C"
# Else if grade is 60 or higher, print "D"
# Else, print "F"
grade = int(input('What is Your Grade ? '));
if grade >=101 :
     print("Invalid Grade: Which Exam Did You do");
elif grade >=90:
    print ('A')
elif grade>=80:
    print('B')
elif grade >=70:
    print("C")
elif grade >=60:
    print('D')
elif grade >=0:
    print("F")
else:
    print("E")