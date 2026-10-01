# Ánh xạ (Mapping): Chuyển dổi GPA của sinh viên. Điểm trong danh sách là hệ số 10. Viết chương trình chuyển đổi danh sách điểm này sang danh sách điểm tích luỹ hệ số 4.
scores_student_list_sample_10 = [5.0, 7.0, 8.0, 10.0, 9.0]
scores_student_list_sample_4 = [0] * len(scores_student_list_sample_10)
i = 0
for i, score in enumerate(scores_student_list_sample_10):
  scores_student_list_sample_4[i] = (score / 10) * 4
print(scores_student_list_sample_4)

gpa_10 = [5, 7, 8, 10, 9]
# Tạo list trực tiếp
gpa_4 = [gpa/10 * 4 for gpa in gpa_10]
print(gpa_4)

# Hàm map
# map(function, iterable)
    # function: là hàm để biến đổi phần tử
    # iterable: là đối tượng có thể duyêt (như list, set,...)
gpa_10 = [5, 7, 8, 10, 9]
gpa_4 = map(lambda gpa: gpa/10 * 4, gpa_10)
print(list(gpa_4))

gpa_10 = [5, 7, 8, 10, 9]
def convert_gpa_10_to_4(score):
  return score/10 * 4
gpa_4_user_defined_function = map(convert_gpa_10_to_4, gpa_10)
print(list(gpa_4_user_defined_function))

students = ["Tú", "Tân", "Tuấn", "Minh", "Dương"]
students_upper = map(str.upper, students)
print(list(students_upper))

