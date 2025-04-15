class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage

    def make_call(self, number):
        return f"Calling {number} from {self.model}..."

    def send_message(self, number, message):
        return f"Sending message to {number}: {message}"

    def __str__(self):
        return f"{self.brand} {self.model} with {self.storage}GB storage."


# Inherited class to demonstrate polymorphism
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, storage, gpu):
        super().__init__(brand, model, storage)
        self.gpu = gpu

    def play_game(self, game_name):
        return f"Playing {game_name} on {self.model} with {self.gpu} GPU."

    def __str__(self):
        return f"{self.brand} {self.model} (Gaming Edition) with {self.storage}GB storage and {self.gpu} GPU."


# Example usage
if __name__ == "__main__":
    phone = Smartphone("Samsung", "Samsung A15", 128)
    gaming_phone = GamingSmartphone("Asus", "ROG Phone 6", 256, "Adreno 730")

    print(phone)
    print(phone.make_call("0703-746-282"))
    print(phone.send_message("0703-746-282", "Good Evening Cupcake!"))

    print(gaming_phone)
    print(gaming_phone.play_game("Grand theft Auto V"))