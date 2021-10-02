def match_and_print(list_of_student):
    departments = {'Biotech': [], 'Chemistry': [], 'Engineering': [], 'Mathematics': [], 'Physics': []}
    exams = {'Biotech': [3, 2], 'Chemistry': [3], 'Engineering': [5, 4], 'Mathematics': [4], 'Physics': [2, 4]}
    # Number of exams: 2 - physics, 3 - chemistry, 4 - math, 5 - computer science.
    for x in list_of_student:
        x.append(0.0)

    for which_ch in range(7, 10):
        for line in list_of_student:
            line[10] = 0.0
            for dep in departments.keys():
                if dep == line[which_ch].strip():
                    for to_dep in exams.keys():
                        if to_dep == line[which_ch].strip():
                            divider = 0
                            s = 0
                            for exam in exams[to_dep]:
                                divider += 1
                                s = s + float(line[exam])
                            line[10] = s / divider
                            if float(line[6]) > line[10]:
                                line[10] = float(line[6])
        sorted_by_result = sorted(list_of_student, key=lambda x: (-(x[10]), x[0], x[1]))
        list_of_student = []
        for line in sorted_by_result:
            choice = line[which_ch].strip()
            if len(departments[choice]) < N:
                student = line[0], line[1], str(line[10])
                departments[choice].append(student)
            else:
                list_of_student.append(line)

    for dep in departments.keys():
        file2 = open(f'{dep}.txt', 'w', encoding='utf-8')
        for student in sorted(departments[dep], key=lambda x: (-float(x[2]), x[0], x[1])):
            file2.write(' '.join(student) + '\n')
        file2.close()


N = int(input())

# Create list.
file = open('applicant_list_7.txt', 'r+', encoding='utf-8').readlines()

# Create lists in list.
for i in range(len(file)):
    file[i] = file[i].split(' ')

match_and_print(file)
