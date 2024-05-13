import barcode_info

class Basket:

    products = {}

    def __init__(self, name=None, date=None):
        self.__name = name
        self.__date = date
        self.__shop = 'ТЦ'
    
    shop = property()

    @shop.setter
    def shop(self, value):
        self.__shop = value
    
    @shop.getter
    def shop(self):
       return self.__shop
    
    @staticmethod
    def add_to_basket(product):
        if product.barcode in Basket.products:
            Basket.products[product.barcode].append(product)
        else:
            Basket.products[product.barcode] = [product]
    
    @staticmethod
    def remove_from_basket(product):
        if len(Basket.products[product.barcode]) == 1:
            Basket.products.pop(product.barcode)
        else:
            Basket.products[product.barcode].pop()

    def __str__(self):
        res = f'Корзина в магазине "{self.__name}" на {self.__date}\n'
        for barcode, product in Basket.products.items():
            res += f'Штрих-код: {barcode}, Продукт: {product[0].name}, '
            res += f'Кол-во: {len(Basket.products[barcode])} шт, '
            res += f'Производитель: {product[0].company}, Страна: {product[0].country}\n'

        return res
    
class Product:

    def __init__(self, barcode):

        self.barcode = barcode

        cntr_code = int(barcode[:3])
        for name_country, list_code in barcode_info.COUNTRY_CODES.items():
            if cntr_code in list_code:
                self.country = name_country

        cmpn_code = int(barcode[3:7])
        self.company = barcode_info.COMPANY_CODES[cmpn_code]

        name_code = int(barcode[7:12])
        self.name = barcode_info.PRODUCT_CODES[name_code]

    def __str__(self):
        return f'Штрих-код: {self.barcode}, Продукт: {self.name}, \
Производитель: {self.company}, Страна: {self.country}'
    def __repr__(self):
        return self

def products_info(text):

    with open(text, 'r') as f:

        for barc in f:

            if '\n' in barc:
                barc = barc[:-1]

            prod = Product(barc)
            print(prod)
            if prod not in products:
                products[barc] = prod
    print()

products = {}
shop_name = input('Введите название магазина: ')
date = input('Введите дату покупки: ')
print()
basket = Basket(shop_name, date)

num_func = 0
while num_func != 5:

    print('Возможные команды: ')
    print('1. Загрузить данные о товарах из файла.')
    print('2. Добавить товар в корзину.')
    print('3. Удалить товар из корзины.')
    print('4. Посмотреть содержание корзины.')
    print('5. Завершить работу с товарами.')

    flag = True
    while flag:
        try:
            num_func = int(input('Введите номер команды: '))
        except:
            print('Неправильно введен номер команды.')
        else:
            flag = False

    if num_func not in [1, 2, 3, 4, 5]:
        print('Неправильно введен номер команды.')
        continue
    else:
        print()

    if num_func == 1:
        flag = True
        while flag:
            file_name = input('Введите название файла полностью: ')
            try:
                products_info(file_name)
            except:
                print('Неправильно введено имя файла.')
            else:
                flag = False
    
    elif num_func == 2:
        flag = True
        while flag:
            product_barcode = input('Введите штрих-код товара: ')
            if product_barcode in products:
                basket.add_to_basket(products[product_barcode])
                print('Товар добавлен в корзину.\n')
                flag = False
            else:
                print('Такого товара нет.')

    elif num_func == 3:
        flag = True
        while flag:
            product_barcode = input('Введите штрих-код товара: ')
            if product_barcode in basket.products:
                basket.remove_from_basket(products[product_barcode])
                print('Товар убран из корзины.\n')
                flag = False
            else:
                print('Такого товара в корзине нет.')

    elif num_func == 4:
        print(basket)
 