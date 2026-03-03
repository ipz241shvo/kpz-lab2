import threading


# ===============================
# Singleton Metaclass
# ===============================

class SingletonMeta(type):
    _instance = None
    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        if SingletonMeta._instance is None:
            with SingletonMeta._lock:
                if SingletonMeta._instance is None:
                    SingletonMeta._instance = super().__call__(*args, **kwargs)
        return SingletonMeta._instance


# ===============================
# Authenticator (Singleton)
# ===============================

class Authenticator(metaclass=SingletonMeta):

    def __init__(self):
        # Захист від повторної ініціалізації
        if getattr(self, "_initialized", False):
            return
        self._initialized = True

        self.users = {"admin": "1234", "user": "pass"}
        self.current_user = None

    def login(self, username, password):
        if self.users.get(username) == password:
            self.current_user = username
            return True
        return False

    def logout(self):
        self.current_user = None


# Клас-нащадок
class AdminAuthenticator(Authenticator):
    def is_admin(self):
        return self.current_user == "admin"


# ===============================
# Перевірка роботи (Main)
# ===============================

def thread_test(results, index):
    obj = Authenticator()
    results[index] = id(obj)


if __name__ == "__main__":

    print("=== Перевірка звичайного створення ===")
    a1 = Authenticator()
    a2 = Authenticator()
    a3 = AdminAuthenticator()

    print("a1 is a2:", a1 is a2)
    print("a1 is a3:", a1 is a3)

    print("ID a1:", id(a1))
    print("ID a2:", id(a2))
    print("ID a3:", id(a3))

    print("\n=== Перевірка в потоках ===")

    threads = []
    results = [None] * 10

    for i in range(10):
        t = threading.Thread(target=thread_test, args=(results, i))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    unique_ids = set(results)

    print("Унікальні ID з потоків:", unique_ids)
    print("Кількість створених екземплярів:", len(unique_ids))