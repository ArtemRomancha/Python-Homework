import sys , math #Добавление используемых модулей

try: 
	infilename = sys.argv [1] #Читаем со второй позиции имя файла со входными данными 
	outfilename = sys.argv [2] #Читаем с третьей позиции имя файла куда будем записывать результирующие данные
except:
	print("Usage:", sys.argv[0], "infile  outfile") #Если отсутствует какой либо файл, то выводим ошибку 
	sys.exit (1) #и завершаем выполнение программы 

ifile = open(infilename , "r") #Открываем файл с входными данными  на чтение 
ofile = open(outfilename , "w") #Открываем файл для результатов на запись 

for  line in ifile: #Для каждой строки из файла с входящими данными 
	substr = line.split () #Разбиваем строку по пробелу 
	summ = 0 #переменная для суммы элементов в столбце
	for number in substr: #цикл по всем числам строки 
		x = float(number) #преобразуем данные из строки в переменную
		summ += x #добавляем новое число к сумме
		ofile.write("%12.6f" % x) #записываем число из исходного файла
	ofile.write("%12.6f\n" % (summ / len(substr))) #записываем среднее
ifile.close() # закрытие доступа к файлам
ofile.close() # закрытие доступа к файлам
