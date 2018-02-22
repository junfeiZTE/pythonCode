def hello_world():
    print("Hello world")

def three_hellos():
    for i in range(3):
        hello_world()

three_hellos()
