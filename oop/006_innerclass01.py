
class Customer:

    def __init__(self, id, name, bdno, bstreet, bcity, bcountry, bpin, sdno, sstreet, scity, scountry, spin) -> None:
        self.customer_id = id
        self.customer_name = name
        self.billing_address = self.Address(bdno, bstreet, bcity, bcountry, bpin)
        self.shipping_address = self.Address(sdno, sstreet, scity, scountry, spin)
        print(f"Inside Customer class ctor:\n{dir(self)}")


    class Address:

        def __init__(self, dno, street, city, country, pin) -> None:
            self.dno = dno
            self.street = street
            self.city = city
            self.country = country
            self.pin = pin
            print(f"Inside Address class ctor:\n{dir(self)}")

        def display(self):
            print(self.dno)
            print(self.street)
            print(self.city)
            print(self.country)
            print(self.pin)
    

c = Customer(101, 'John', 401, 'balewadi high street', 'Pune', 'India', 10021, 1001, 'Pimpri Street', 'Pune', 'India', 10022)
print(f"Billing address is:\n")
c.billing_address.display()
print("\nShipping Address is:\n")
c.shipping_address.display()
