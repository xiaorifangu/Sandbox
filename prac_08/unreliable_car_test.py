from prac_08.unreliable_car import UnreliableCar

def main():
    good_one = UnreliableCar("a", 100, 50)
    bad_one = UnreliableCar("b", 100, 5)

    for i in range(1, 12):
        print("Attempting to drive {}km:".format(i))
        print("{} drove {}km".format(good_one.name, good_one.drive(i)))
        print("{} drove {}km".format(bad_one.name, bad_one.drive(i)))

    print(good_one)
    print(bad_one)
main()