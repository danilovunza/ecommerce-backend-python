"""
E-Commerce Backend

Author: Danilo Vunza
Course: COSC 2436

Description:
A simplified e-commerce backend
demonstrating OOP, inheritance,
and composition.
"""


class Person:

    def __init__(
        self,
        person_id,
        name
    ):

        self.person_id = person_id
        self.name = name


class Customer(Person):

    def __init__(
        self,
        customer_id,
        name,
        email
    ):

        super().__init__(
            customer_id,
            name
        )

        self.email = email


class Product:

    def __init__(
        self,
        product_id,
        name,
        price
    ):

        self.product_id = product_id
        self.name = name
        self.price = price


class ShoppingCart:

    def __init__(self):

        self.products = []

    def add_product(
        self,
        product
    ):

        self.products.append(product)

    def display_cart(self):

        print("\nSHOPPING CART")

        print("-" * 50)

        if len(self.products) == 0:

            print("Cart is empty.")

            return

        total = 0

        for product in self.products:

            print(
                f"{product.name} "
                f"- ${product.price:.2f}"
            )

            total += product.price

        print("-" * 50)

        print(
            f"Total: ${total:.2f}"
        )

    def calculate_total(self):

        total = 0

        for product in self.products:

            total += product.price

        return total


class Payment:

    def __init__(
        self,
        amount,
        payment_method
    ):

        self.amount = amount
        self.payment_method = payment_method


class Order:

    def __init__(
        self,
        order_id,
        customer,
        products,
        payment
    ):

        self.order_id = order_id
        self.customer = customer
        self.products = products
        self.payment = payment

    def display_order(self):

        print("\nORDER DETAILS")

        print("-" * 50)

        print(
            f"Order ID: {self.order_id}"
        )

        print(
            f"Customer: {self.customer.name}"
        )

        print(
            f"Payment: "
            f"{self.payment.payment_method}"
        )

        print(
            f"Amount: "
            f"${self.payment.amount:.2f}"
        )


class Store:

    def __init__(self):

        self.products = []

        self.orders = []

        self.load_products()

    def load_products(self):

        self.products.append(
            Product(
                1,
                "Laptop",
                999.99
            )
        )

        self.products.append(
            Product(
                2,
                "Keyboard",
                49.99
            )
        )

        self.products.append(
            Product(
                3,
                "Mouse",
                24.99
            )
        )

    def display_products(self):

        print("\nPRODUCT CATALOG")

        print("-" * 50)

        for product in self.products:

            print(
                f"{product.product_id} | "
                f"{product.name} | "
                f"${product.price:.2f}"
            )

    def get_product(
        self,
        product_id
    ):

        for product in self.products:

            if (
                product.product_id
                ==
                product_id
            ):

                return product

        return None


def display_menu():

    print("\n" + "=" * 50)

    print("E-COMMERCE BACKEND")

    print("=" * 50)

    print("1. View Products")

    print("2. Add Product To Cart")

    print("3. View Cart")

    print("4. Checkout")

    print("5. Order History")

    print("6. Exit")

    print("=" * 50)


def main():

    store = Store()

    customer = Customer(
        1,
        "Danilo Vunza",
        "danilo@email.com"
    )

    cart = ShoppingCart()

    while True:

        display_menu()

        choice = input(
            "Select an option: "
        )

        if choice == "1":

            store.display_products()

        elif choice == "2":

            product_id = int(
                input(
                    "Product ID: "
                )
            )

            product = store.get_product(
                product_id
            )

            if product:

                cart.add_product(product)

                print(
                    "\nProduct added to cart."
                )

            else:

                print(
                    "\nProduct not found."
                )

        elif choice == "3":

            cart.display_cart()

        elif choice == "4":

            total = (
                cart.calculate_total()
            )

            payment = Payment(
                total,
                "Credit Card"
            )

            order = Order(
                len(store.orders) + 1,
                customer,
                cart.products,
                payment
            )

            store.orders.append(order)

            print(
                "\nCheckout successful."
            )

            order.display_order()

            cart = ShoppingCart()

        elif choice == "5":

            print("\nORDER HISTORY")

            print("-" * 50)

            if len(store.orders) == 0:

                print(
                    "No orders found."
                )

            else:

                for order in store.orders:

                    order.display_order()

        elif choice == "6":

            print(
                "\nThank you for using the system."
            )

            break

        else:

            print(
                "\nInvalid option."
            )


main()
