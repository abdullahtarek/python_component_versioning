from module1 import greet

def run():
    return "Module2 → " + greet("User")

if __name__ == "__main__":
    print(run())
