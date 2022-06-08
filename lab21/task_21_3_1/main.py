import strategies
from customer import Customer


def main():
    pay_pal_customer = Customer()
    pay_pal_customer.set_strategy(strategies.PayPalPayment())
    pay_pal_customer.make_payment(1000)

    ba_customer = Customer()
    ba_customer.set_strategy(strategies.BankAccountPayment())
    ba_customer.make_payment(2000)


if __name__ == "__main__":
    main()
