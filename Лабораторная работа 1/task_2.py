# TODO Найдите количество книг, которое можно разместить на дискете
#
volume_Mb = 1.44
pages = 100
lines = 50
symbols = 25
weight_of_symbol_b = 4

#Определение веса одной книги в байтах
weight_of_book = pages * lines * symbols * weight_of_symbol_b

#Перевод объема дискеты из Мб в байты
volume_b = volume_Mb * 1024 ** 2

#Определение количества книг, которое можно разместить на дискете
quantity = int (volume_b // weight_of_book)

print("Количество книг, помещающихся на дискету:", quantity)
