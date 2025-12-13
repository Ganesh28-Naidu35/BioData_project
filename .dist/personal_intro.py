# Student Bio-Data Program
# This program collects detailed user information


print("🌟 Welcome to the Bio-Data Project 🌟\n")

# Collecting user information
name = input("What is your full name? ")
age = int(input("How old are you? "))
birth_place = input("Where were you born? ")
city = input("Which city do you currently live in? ")

school_10 = input("Which school did you complete your 10th class from? ")
board_10 = input("Which board (CBSE/ICSE/State) did you study in 10th? ")

school_12 = input("Which school/college did you complete your 12th class from? ")
stream_12 = input("What was your 12th stream (Science/Commerce/Arts)? ")

btech_college = input("Which college are you pursuing/completed B.Tech from? ")
btech_domain = input("What is your B.Tech domain (CSE/IT/EEE/Mechanical etc.)? ")

fav_sport = input("What is your favorite sport? ")
fav_personality = input("Who is your favorite personality? ")
hobby = input("What is your favorite hobby? ")

# Displaying the bio-data
print("\n🎉 Thank You for Sharing Your Details! 🎉")
print("========================================")

print(f"👤 Name              : {name}")
print(f"🎂 Age               : {age}")
print(f"📍 Born In           : {birth_place}")
print(f"🏙️ Current City      : {city}")

print("\n📘 Education Details")
print("----------------------------------------")
print(f"🏫 10th School       : {school_10}")
print(f"📚 10th Board        : {board_10}")
print(f"🏫 12th School       : {school_12}")
print(f"🎓 12th Stream       : {stream_12}")
print(f"🏛️ B.Tech College    : {btech_college}")
print(f"💻 B.Tech Domain     : {btech_domain}")

print("\n⭐ Personal Interests")
print("----------------------------------------")
print(f"🏅 Favorite Sport    : {fav_sport}")
print(f"🌟 Favorite Person   : {fav_personality}")
print(f"🎯 Hobby             : {hobby}")

print("\n🚀 Wishing you great success in your journey!")
print("========================================")
