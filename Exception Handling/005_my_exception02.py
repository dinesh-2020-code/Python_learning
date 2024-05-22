class NegativeAgeException(Exception):

    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return f"{self.msg}"
    

if __name__ == "__main__":

    try:
        age = int(input("Enter age:"))

        if age < 0:
            raise NegativeAgeException("Age cannot be negative")
        elif 0 <= age < 13:
            print("Kid")
        elif 13 <= age <= 19:
            print("Teen")
        elif 19 < age < 50:
            print("Young")
        else:
            print("Old")

    except NegativeAgeException as e:
        print(e)
