print("Enter the Years of 3 peoples")
year1 = int(input())
year2 = int(input())
year3 = int(input())
if year1 > year2 and year1 > year3:
    print(f"Input {year1} is the oldest one")
elif year2 > year1 and year2 > year3:
    print(f"Input {year2} is the oldest one")
else:
    print(f"Input {year3} is the oldest one")

