from abc import ABC, abstractmethod


# ==============================
# 1. Base Subscription Class
# ==============================

class Subscription(ABC):
    def __init__(self, monthly_fee: float, min_period: int, channels: list):
        self.monthly_fee = monthly_fee
        self.min_period = min_period
        self.channels = channels

    def get_info(self, duration):
        total_price = round(self.monthly_fee * duration, 2)

        print("\nSubscription successfully created!")
        print(f"Monthly fee: {self.monthly_fee}")
        print(f"Minimum period (months): {self.min_period}")
        print(f"Chosen duration: {duration}")
        print(f"Total price: {total_price}")
        print(f"Channels: {self.channels}")
        print("-" * 40)


# ==============================
# 2. All Subscriptions
# ==============================

class DomesticSubscription(Subscription):
    def __init__(self):
        super().__init__(
            monthly_fee=9.99,
            min_period=1,
            channels=["News", "Movies", "Entertainment"]
        )


class EducationalSubscription(Subscription):
    def __init__(self):
        super().__init__(
            monthly_fee=5.99,
            min_period=6,
            channels=["Discovery", "National Geographic", "History"]
        )


class PremiumSubscription(Subscription):
    def __init__(self):
        super().__init__(
            monthly_fee=19.99,
            min_period=12,
            channels=["All Channels", "4K Content", "Sports", "Exclusive Shows"]
        )


# ==============================
# 3. Fabrics
# ==============================

class SubscriptionCreator(ABC):

    @abstractmethod
    def create_subscription(self, sub_type: str) -> Subscription:
        pass

    def order_subscription(self, sub_type: str, duration: int):
        subscription = self.create_subscription(sub_type)

        if duration < subscription.min_period:
            raise ValueError(
                f"Minimum subscription period is {subscription.min_period} months!"
            )

        subscription.get_info(duration)
        return subscription


# ==============================
# 4. Abstraction Fabrics
# ==============================

class WebSite(SubscriptionCreator):

    def create_subscription(self, sub_type: str) -> Subscription:
        print("\nCreating subscription via Website...")
        return create_by_type(sub_type)


class MobileApp(SubscriptionCreator):

    def create_subscription(self, sub_type: str) -> Subscription:
        print("\nCreating subscription via Mobile App (10% discount)...")
        subscription = create_by_type(sub_type)
        subscription.monthly_fee = round(subscription.monthly_fee * 0.9, 2)
        return subscription


class ManagerCall(SubscriptionCreator):

    def create_subscription(self, sub_type: str) -> Subscription:
        print("\nCreating subscription via Manager Call (bonus support)...")
        subscription = create_by_type(sub_type)
        subscription.channels.append("Personal Support")
        return subscription


# ==============================
# 5. Help Function
# ==============================

def create_by_type(sub_type: str) -> Subscription:
    if sub_type == "1":
        return DomesticSubscription()
    elif sub_type == "2":
        return EducationalSubscription()
    elif sub_type == "3":
        return PremiumSubscription()
    else:
        raise ValueError("Invalid subscription type selected.")


# ==============================
# 6. Main Programm
# ==============================

if __name__ == "__main__":

    print("Choose device:")
    print("1 - Website")
    print("2 - Mobile App")
    print("3 - Manager Call")

    device_choice = input("Enter number: ")

    if device_choice == "1":
        creator = WebSite()
    elif device_choice == "2":
        creator = MobileApp()
    elif device_choice == "3":
        creator = ManagerCall()
    else:
        print("Invalid device selection!")
        exit()

    print("\nChoose subscription type:")
    print("1 - Domestic")
    print("2 - Educational")
    print("3 - Premium")

    sub_choice = input("Enter number: ")

    try:
        duration = int(input("Enter subscription duration (months): "))

        creator.order_subscription(sub_choice, duration)

    except ValueError as e:
        print(f"\nError: {e}")
