zybooks = []
assignments = []
exams = []

i = 1
zy = 0 
zy = int(input('How many Zybooks chapters have been completed? '))
while i <= zy:
    zybooks.append(int(input('Enter the grades for chapter ' + str(i) + ': ')))
    i += 1
zybooks_grade = sum(zybooks) / len(zybooks) * 0.5
print('')

o = 1
out = 0
out = int(input('How many outside assignments have been completed? '))
while o <= out:
    assignments.append(int(input('Enter the grade for assignment ' + str(o) + ': ')))
    o += 1
outside_assignments = sum(assignments) / len(assignments) * 0.3
print('')

t = 1
test = 0
test = int(input('How many tests have been taken? '))
while t <= test:
    exams.append(int(input('Enter the grade for test ' + str(t) + ': ')))
    t += 1
tests = sum(exams) / len(exams) * 0.2
print('')

overall_grade = (zybooks_grade ) + (outside_assignments ) + (tests )
print('Intro to Programming Grade for Joshua Terry')
print('Zybooks                   (',zy ,'chapters): ', (zybooks_grade))
print('Outside assignments    (',out,'assignments): ', (outside_assignments))
print('Tests                        (',test, 'tests): ', (tests))
print('------------------------------------------------')
print('Overall grade                       (A): ', (overall_grade))