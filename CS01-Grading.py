A = int(input("คะแนนเก็บ : "))
B = int(input("คะแนนสอบกลางภาค : "))
C = int(input("คะแนนสอบปลายภาค : "))
D = A+B+C

if(D <= 100):
    print("A")
elif(D < 80):
    print("B+")
elif(D < 75):
    print("B")
elif(D < 70):
    print("C+")
elif(D < 65):
    print("C")
elif(D < 60):
    print("D+")
elif(D < 55):
    print("D")
elif(D < 50):
    print("F")
else:
    print("คะแนนไม่ถูกต้อง")