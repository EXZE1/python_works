student_name = None
student_point = None
student_list = {}

for i in range(0,3):  
    student_name = input("Öğrencinin adini giriniz ")
    student_point = int(input("Öğrencinin puanini giriniz "))
    # list = {student_name:student_point}
    student_list[student_name] = student_point

print(student_list)
sum = 0
for point in student_list.values():
    print(point)
    sum = sum + point

ortalama = int(sum/len(student_list))
print("Sinif Oratalamasi: ", ortalama)

