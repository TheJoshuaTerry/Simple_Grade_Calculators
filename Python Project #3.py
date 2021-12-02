zy = []
oa = []
ex = []

def grade_input(): #After figuring out this the rest was easy!!!!!!!
    user_input = 0
    values = []
    while user_input != 'q':  
        user_input = input('Enter grade (q to quit):')
        if user_input != 'q':
            for token in user_input.split():
               values.append(float(token))
    return values
    
def weighted_grade(x, y):
    grade = sum(y) / len(y) * x
    return grade


def letter_grade(x):
    if x >= 90:
        return 'A'
    elif x >= 80:
        return 'B'
    elif x >= 70:
        return 'C'
    elif x >= 60:
        return 'D'
    elif x < 60:
        return 'F'

print('Enter Zybooks grades')
zy = grade_input()
print('\nEnter outside assignment grades')
oa = grade_input()
print('\nEnter exam grades')
ex = grade_input()

zyw = weighted_grade(0.5, zy)
oaw = weighted_grade(0.3, oa)
exw = weighted_grade(0.2, ex)

grade = zyw + oaw + exw
lgrade = letter_grade(grade) 

print('')
print('')

print('Zybooks assignments:', "{:.2f}".format(zyw), ' + ')
print('Outside assignments:', "{:.2f}".format(oaw), ' + ')
print('Test grades:        ', "{:.2f}".format(exw))
print('-------------------------------')
print('Overall grade:      ', "{:.2f}".format(grade) + '%', '(' + lgrade + ')')