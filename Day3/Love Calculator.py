print("Welcome to the Love calculator")

name1 = input("Enter your name :\n")
name2 = input("Enter your Partner's name :\n")

combined_name = name2 + name1

lower_case_string = combined_name.lower()

# method1
t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

true = t + r + u + e

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

love = l + o + v + e

love_score = true + love


if love_score < 10 or love_score > 90:
    print("You go well together")


# method2
count = 0
for characters in lower_case_string:
    if characters in ('t','r','u','e','l','o','v','u'):
        count +=1

if count < 10 or count > 90:
    print("You go well together")




