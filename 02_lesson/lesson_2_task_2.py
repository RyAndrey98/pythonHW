def is_yesr_leap(year):
    if (year % 4 == 0):
        print("Year: " + str(year) + " True")
    else:
        print("Year: " + str(year) + " False")


is_yesr_leap(int(input("Type a year: ")))