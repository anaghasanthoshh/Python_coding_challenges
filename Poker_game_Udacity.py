bad_list=["anu","isha","jo","sa"]
#called as list comprehension
upper_list=[name.upper() for  name in bad_list]
print(upper_list)

comp_list=[{"name":"anu","place":"UK","subject":"English"},
           {"name":"Isha","place":"Kerala","subject":"LKg"}]

#x= [a['name'] +' is the name and lives in '+b['place']+' and studies '+c['subject']
    #for a,b,c in comp_list]
x= [a['name']+ " is the name and "+ a['place']+ " is the place" for a in comp_list]
#print(x)

ta_data = [['Peter', 'USA', 'CS262'],
           ['Andy', 'USA', 'CS212'],
           ['Sarah', 'England', 'CS101'],
           ['Gundega', 'Latvia', 'CS373'],
           ['Job', 'USA', 'CS387'],
           ['Sean', 'USA', 'CS253']]

ta_300 =[f'{name} is the TA for {course}' for name,place,course in ta_data if course.find("CS3")==0]
print(ta_300)

