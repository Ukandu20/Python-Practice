your_drink = "whiskey"

def reverse(s):
    return s[::-1]

str2 = reverse("rap")
str1 = "ers"
str3 = "amet"

request = f"{your_drink}. Secret word: {str2}{str3}{str1}"

print(request)
