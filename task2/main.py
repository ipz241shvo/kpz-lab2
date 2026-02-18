from abc import ABC, abstractmethod


# ======================================
# 1. Abstraction Products
# ======================================

class Laptop(ABC):
    @abstractmethod
    def get_specs(self):
        pass


class Netbook(ABC):
    @abstractmethod
    def get_specs(self):
        pass


class EBook(ABC):
    @abstractmethod
    def get_specs(self):
        pass


class Smartphone(ABC):
    @abstractmethod
    def get_specs(self):
        pass


# ======================================
# 2. IPhore Products
# ======================================

class IProneLaptop(Laptop):
    def get_specs(self):
        return "IProne Laptop: 16GB RAM, 1TB SSD"


class IProneNetbook(Netbook):
    def get_specs(self):
        return "IProne Netbook: 8GB RAM, 512GB SSD"


class IProneEBook(EBook):
    def get_specs(self):
        return "IProne EBook: 7-inch display"


class IProneSmartphone(Smartphone):
    def get_specs(self):
        return "IProne Smartphone: 256GB, 5G"


# ======================================
# 3. Kiaomi Products
# ======================================

class KiaomiLaptop(Laptop):
    def get_specs(self):
        return "Kiaomi Laptop: 16GB RAM, 512GB SSD"


class KiaomiNetbook(Netbook):
    def get_specs(self):
        return "Kiaomi Netbook: 8GB RAM, 256GB SSD"


class KiaomiEBook(EBook):
    def get_specs(self):
        return "Kiaomi EBook: 6-inch display"


class KiaomiSmartphone(Smartphone):
    def get_specs(self):
        return "Kiaomi Smartphone: 128GB, 5G"


# ======================================
# 4. Balaxy Products
# ======================================

class BalaxyLaptop(Laptop):
    def get_specs(self):
        return "Balaxy Laptop: 32GB RAM, 1TB SSD"


class BalaxyNetbook(Netbook):
    def get_specs(self):
        return "Balaxy Netbook: 16GB RAM, 512GB SSD"


class BalaxyEBook(EBook):
    def get_specs(self):
        return "Balaxy EBook: 8-inch display"


class BalaxySmartphone(Smartphone):
    def get_specs(self):
        return "Balaxy Smartphone: 512GB, 5G"


# ======================================
# 5. Abstraction Fabric
# ======================================

class TechFactory(ABC):

    @abstractmethod
    def create_laptop(self):
        pass

    @abstractmethod
    def create_netbook(self):
        pass

    @abstractmethod
    def create_ebook(self):
        pass

    @abstractmethod
    def create_smartphone(self):
        pass


# ======================================
# 6. Fabrics For Brand
# ======================================

class IProneFactory(TechFactory):
    def create_laptop(self): return IProneLaptop()
    def create_netbook(self): return IProneNetbook()
    def create_ebook(self): return IProneEBook()
    def create_smartphone(self): return IProneSmartphone()


class KiaomiFactory(TechFactory):
    def create_laptop(self): return KiaomiLaptop()
    def create_netbook(self): return KiaomiNetbook()
    def create_ebook(self): return KiaomiEBook()
    def create_smartphone(self): return KiaomiSmartphone()


class BalaxyFactory(TechFactory):
    def create_laptop(self): return BalaxyLaptop()
    def create_netbook(self): return BalaxyNetbook()
    def create_ebook(self): return BalaxyEBook()
    def create_smartphone(self): return BalaxySmartphone()


# ======================================
# 7. Main Programm
# ======================================

if __name__ == "__main__":

    print("Choose brand:")
    print("1 - IProne")
    print("2 - Kiaomi")
    print("3 - Balaxy")

    brand_choice = input("Enter number: ")

    if brand_choice == "1":
        factory = IProneFactory()
    elif brand_choice == "2":
        factory = KiaomiFactory()
    elif brand_choice == "3":
        factory = BalaxyFactory()
    else:
        print("Invalid brand selection!")
        exit()

    products = []

    print("\nChoose products (enter numbers separated by space):")
    print("1 - Laptop")
    print("2 - Netbook")
    print("3 - EBook")
    print("4 - Smartphone")

    choices = input("Your choice: ").split()

    for choice in choices:
        try:
            if choice == "1":
                products.append(factory.create_laptop())
            elif choice == "2":
                products.append(factory.create_netbook())
            elif choice == "3":
                products.append(factory.create_ebook())
            elif choice == "4":
                products.append(factory.create_smartphone())
            else:
                print(f"Unknown product: {choice}")
        except Exception as e:
            print(f"Error: {e}")

    print("\nCreated products:")
    for product in products:
        print(product.get_specs())
