#coding:utf-8
def my_range(inici, fi, increment):
	
  while inici <=fi:
		yield inici
		inici=inici + increment



import calendar
anyo=input("Posa Un Any: ")
mes=input("Posa un Mes: ")
cont=1


num_dias_mes=calendar.monthrange(anyo,mes)[1]
dia_semana=calendar.monthrange(anyo,mes)[0]

print "Lu Ma Mi Ju Vi Sa Do"ç

for col in my_range(1, dia_semana - 1, 1):
	print " " ,

for col in my_range(dia_semana, 7, 1):
	print cont ,

  cont=cont+1

for fil in my_range(1, 5, 1):

  for col in my_range(1, 7, 1):
	
      if (cont<=num_dias_mes):
			    print cont ,
		  else:
			    print "-" ,
		
      cont=cont+1
		
	 print " "
		
