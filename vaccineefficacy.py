control=0
vaccinated=0
a_control_yes=0
a_vaccine_yes=0
b_control_yes=0
b_vaccine_yes=0
c_control_yes=0
c_vaccine_yes=0
for _ in range(int(input())):
    ip=input()
    if ip[0]=='N':
        control+=1
        if ip[1]=='Y':
            a_control_yes+=1
        if ip[2]=='Y':
            b_control_yes+=1
        if ip[3]=='Y':
            c_control_yes+=1
    else:
        vaccinated+=1
        if ip[1]=='Y':
            a_vaccine_yes+=1
        if ip[2]=='Y':
            b_vaccine_yes+=1
        if ip[3]=='Y':
            c_vaccine_yes+=1
if control!=0:
    a_control_yes_percent=(a_control_yes/control)*100
    b_control_yes_percent=(b_control_yes/control)*100
    c_control_yes_percent=(c_control_yes/control)*100
elif control==0:
    a_control_yes_percent=0
    b_control_yes_percent=0
    c_control_yes_percent=0
if vaccinated!=0:
    a_vaccine_yes_percent=(a_vaccine_yes/vaccinated)*100
    b_vaccine_yes_percent=(b_vaccine_yes/vaccinated)*100
    c_vaccine_yes_percent=(c_vaccine_yes/vaccinated)*100
elif vaccinated==0:
    a_vaccine_yes_percent=0
    b_vaccine_yes_percent=0
    c_vaccine_yes_percent=0
if a_vaccine_yes_percent>=a_control_yes_percent or a_control_yes_percent==0:
    print('Not Effective')
if a_vaccine_yes_percent<a_control_yes_percent:
    diff=((a_control_yes_percent-a_vaccine_yes_percent)/(a_control_yes_percent))*100
    print((round(diff,6)))
if b_vaccine_yes_percent>=b_control_yes_percent or b_control_yes_percent==0:
    print('Not Effective')
if b_vaccine_yes_percent<b_control_yes_percent:
    diff=((b_control_yes_percent-b_vaccine_yes_percent)/(b_control_yes_percent))*100
    print((round(diff,6)))
if c_vaccine_yes_percent>=c_control_yes_percent or c_control_yes_percent==0:
    print('Not Effective')
if c_vaccine_yes_percent<c_control_yes_percent:
    diff=((c_control_yes_percent-c_vaccine_yes_percent)/(c_control_yes_percent))*100
    print((round(diff,6)))