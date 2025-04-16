import datetime

class Product:
    def __init__(self, product_type, name, brand, catalog_number, price, delivery_price, quantity):
        self.product_type = product_type
        self.name = name
        self.brand = brand
        self.catalog_number = catalog_number
        self.price = price
        self.delivery_price = delivery_price
        self.quantity = quantity

    def total_price(self):
        return self.price + self.delivery_price

    def __repr__(self):
        return (f"Type: {self.product_type}, Name: {self.name}, Brand: {self.brand}, "
                f"Number: {self.catalog_number}, Price: {self.price}, Delivery: {self.delivery_price}, "
                f"Quantity: {self.quantity}")

class Store:
    def __init__(self):
        self.products = []
        self.sales_history = []
        self.total_earnings = 0.0
        self.admin_password = "Ilovedevchuli"

    def set_admin_password(self, new_password):
        self.admin_password = new_password
        return "Пароль успешно изменен."

    def verify_admin(self, password):
        return password == self.admin_password

    def update_catalog_numbers(self):
        for index, product in enumerate(self.products, start=1):
            product.catalog_number = index

    def update_product_quantity(self, catalog_number, new_quantity):
        for product in self.products:
            if product.catalog_number == catalog_number:
                product.quantity = new_quantity
                return f"Updated quantity for {product.name} to {new_quantity}"
        return "Product not found."

    def update_product_price(self, catalog_number, new_price, new_delivery_price):
        for product in self.products:
            if product.catalog_number == catalog_number:
                product.price = new_price
                product.delivery_price = new_delivery_price
                return f"Updated price for {product.name} to {new_price} and delivery to {new_delivery_price}"
        return "Product not found."

    def delete_product(self, catalog_number):
        for product in self.products:
            if product.catalog_number == catalog_number:
                self.products.remove(product)
                self.update_catalog_numbers()
                return f"Product {product.name} has been removed."
        return "Product not found."

    def list_products(self, for_customer=False):
        if not self.products:
            return ["No products available."]
        if for_customer:
            return [
                f"{p.catalog_number}. {p.name} ({p.brand}) - {p.price} руб. (Доставка: {p.delivery_price}) руб. В наличии: {p.quantity}"
                for p in self.products if p.quantity > 0]
        return [str(product) for product in self.products]

    def add_product(self):
        print("Введите данные о продукте:")
        product_type = input("Тип продукта: ")
        name = input("Название продукта: ")
        brand = input("Бренд: ")

        while True:
            try:
                price = float(input("Цена: "))
                if price < 0:
                    print("Цена не может быть отрицательной. Попробуйте снова.")
                    continue
                break
            except ValueError:
                print("Ошибка: Пожалуйста, введите числовое значение для цены.")

        while True:
            try:
                delivery_price = float(input("Цена доставки: "))
                if delivery_price < 0:
                    print("Цена доставки не может быть отрицательной. Попробуйте снова.")
                    continue
                break
            except ValueError:
                print("Ошибка: Пожалуйста, введите числовое значение для цены доставки.")

        while True:
            try:
                quantity = int(input("Количество: "))
                if quantity < 0:
                    print("Количество не может быть отрицательным. Попробуйте снова.")
                    continue
                break
            except ValueError:
                print("Ошибка: Пожалуйста, введите целочисленное значение для количества.")

        catalog_number = len(self.products) + 1
        new_product = Product(product_type, name, brand, catalog_number, price, delivery_price, quantity)
        self.products.append(new_product)
        return f"Продукт {name} добавлен в магазин с номером каталога {catalog_number}."

    def record_sale(self, items, total_amount):
        sale = {
            "items": items.copy(),
            "total_amount": total_amount,
            "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.sales_history.append(sale)
        self.total_earnings += total_amount

    def view_sales_report(self):
        if not self.sales_history:
            return "Пока нет данных о продажах."

        report = ["Отчет о продажах:", f"Общий доход: {self.total_earnings:.2f} руб.", "Последние продажи:"]
        for sale in self.sales_history[-5:]:
            report.append(f"\nДата: {sale['timestamp']}")
            report.append(f"Общая сумма: {sale['total_amount']:.2f} руб.")
            report.append("Товары:")
            for item in sale['items']:
                report.append(f"{item['name']} ({item['quantity']} шт.) - {item['total_price']:.2f} руб.")
        return "\n".join(report)

class Customer:
    def __init__(self, store):
        self.store = store
        self.cart = []

    def view_products(self):
        products = self.store.list_products(for_customer=True)
        if not products:
            print("В магазине пока нет товаров.")
        else:
            print("\nДоступные товары:")
            for product in products:
                print(product)

    def add_to_cart(self):
        self.view_products()
        if not self.store.products:
            return

        try:
            catalog_number = int(input("\nВведите номер товара для добавления в корзину: "))
            quantity = int(input("Введите количество: "))

            if quantity <= 0:
                print("Количество должно быть положительным числом.")
                return

            product = next((p for p in self.store.products if p.catalog_number == catalog_number), None)

            if not product:
                print("Товар с таким номером не найден.")
                return

            if product.quantity < quantity:
                print(f"Недостаточно товара в наличии. Доступно: {product.quantity}")
                return

            item_in_cart = next((item for item in self.cart if item['product'].catalog_number == catalog_number), None)

            if item_in_cart:
                new_quantity = item_in_cart['quantity'] + quantity
                if new_quantity > product.quantity:
                    print(f"Недостаточно товара в наличии. Доступно: {product.quantity}")
                    return
                item_in_cart['quantity'] = new_quantity
                item_in_cart['total_price'] = new_quantity * (product.price + product.delivery_price)
            else:
                self.cart.append({
                    'product': product,
                    'quantity': quantity,
                    'total_price': quantity * (product.price + product.delivery_price)
                })

            print(f"{product.name} ({quantity} шт.) добавлен в корзину.")

        except ValueError:
            print("Ошибка: Пожалуйста, введите корректные числовые значения.")

    def view_cart(self):
        if not self.cart:
            print("Ваша корзина пуста.")
            return

        total = 0.0
        print("\nВаша корзина:")
        for item in self.cart:
            print(f"{item['product'].name} ({item['quantity']} шт.) - {item['total_price']:.2f} руб.")
            total += item['total_price']
        print(f"\nОбщая сумма: ${total:.2f}")

    def checkout(self):
        if not self.cart:
            print("Ваша корзина пуста.")
            return

        self.view_cart()
        confirm = input("\nВы хотите оформить заказ? (да/нет): ").lower()

        if confirm != 'да':
            print("Заказ отменен.")
            return

        sale_items = []
        total_amount = 0.0

        for item in self.cart:
            product = item['product']
            quantity = item['quantity']

            product.quantity -= quantity

            sale_items.append({
                'name': product.name,
                'quantity': quantity,
                'unit_price': product.price,
                'delivery_price': product.delivery_price,
                'total_price': item['total_price']
            })
            total_amount += item['total_price']

        self.store.record_sale(sale_items, total_amount)

        print("\nСпасибо за покупку! Ваш заказ оформлен.")
        print(f"Общая сумма заказа: {total_amount:.2f} руб.")

        self.cart = []

def admin_menu(store):
    attempts = 3
    while attempts > 0:
        password = input("Введите пароль администратора: ")
        if store.verify_admin(password):
            break
        attempts -= 1
        print(f"Неверный пароль. Осталось попыток: {attempts}")
    else:
        print("Доступ запрещен. Исчерпаны все попытки.")
        return

    while True:
        print("\nМеню администратора:")
        print("1 - Добавить товар")
        print("2 - Удалить товар")
        print("3 - Просмотреть весь каталог")
        print("4 - Изменить количество товара")
        print("5 - Изменить стоимость товара")
        print("6 - Просмотреть отчет о продажах")
        print("7 - Изменить пароль администратора")
        print("8 - Выйти из меню администратора")

        choice = input("Ваш выбор: ")

        if choice == '1':
            print(store.add_product())
        elif choice == '2':
            print("\nСписок товаров:")
            for product in store.list_products():
                print(product)
            try:
                catalog_number = int(input("\nВведите номер каталога товара для удаления: "))
                print(store.delete_product(catalog_number))
            except ValueError:
                print("Ошибка: Пожалуйста, введите корректный номер каталога.")
        elif choice == '3':
            print("\nСписок всех товаров:")
            for product in store.list_products():
                print(product)
        elif choice == '4':
            print("\nСписок товаров:")
            for product in store.list_products():
                print(product)
            try:
                catalog_number = int(input("\nВведите номер каталога товара для изменения: "))
                new_quantity = int(input("Введите новое количество: "))
                print(store.update_product_quantity(catalog_number, new_quantity))
            except ValueError:
                print("Ошибка: Пожалуйста, введите корректные значения.")
        elif choice == '5':
            print("\nСписок товаров:")
            for product in store.list_products():
                print(product)
            try:
                catalog_number = int(input("\nВведите номер каталога товара для изменения: "))
                new_price = float(input("Введите новую цену: "))
                new_delivery_price = float(input("Введите новую стоимость доставки: "))
                print(store.update_product_price(catalog_number, new_price, new_delivery_price))
            except ValueError:
                print("Ошибка: Пожалуйста, введите корректные значения.")
        elif choice == '6':
            print("\n" + store.view_sales_report())
        elif choice == '7':
            new_password = input("Введите новый пароль: ")
            confirm_password = input("Подтвердите новый пароль: ")
            if new_password == confirm_password:
                print(store.set_admin_password(new_password))
            else:
                print("Пароли не совпадают.")
        elif choice == '8':
            print("Выход из меню администратора.")
            break
        else:
            print("Неверный ввод. Пожалуйста, выберите действие от 1 до 8.")

def customer_menu(store):
    customer = Customer(store)

    while True:
        print("\nМеню покупателя:")
        print("1 - Просмотреть товары")
        print("2 - Добавить товар в корзину")
        print("3 - Просмотреть корзину")
        print("4 - Оформить заказ")
        print("5 - Выйти из меню покупателя")

        choice = input("Ваш выбор: ")

        if choice == '1':
            customer.view_products()
        elif choice == '2':
            customer.add_to_cart()
        elif choice == '3':
            customer.view_cart()
        elif choice == '4':
            customer.checkout()
        elif choice == '5':
            print("Выход из меню покупателя.")
            break
        else:
            print("Неверный ввод. Пожалуйста, выберите действие от 1 до 5.")

def main():
    store = Store()

    while True:
        print("\nГлавное меню:")
        print("1 - Войти как администратор")
        print("2 - Войти как покупатель")
        print("3 - Выйти из программы")

        role = input("Ваш выбор: ")

        if role == '1':
            admin_menu(store)
        elif role == '2':
            customer_menu(store)
        elif role == '3':
            print("До свидания!")
            break
        else:
            print("Неверный ввод. Пожалуйста, выберите 1, 2 или 3.")

main()
