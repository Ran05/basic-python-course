

#Day 2 activity #2

first_noun = input("Enter the first noun: ")
second_noun = input("Enter the second noun: ")
third_noun = input("Enter the third noun: ")

first_adj = input("Enter the first adjective: ")
second_adj = input("Enter the second adjective: ")
third_adj = input("Enter the third adjective: ")

output = output = f"""
        ==============
        """

sampleText = "On the seventh day of Christmas\n my true love sent to me:\n Seven Swans a Swimming\n Six Geese a Laying \nFive Golden Rings Four Calling Birds\n Three French Hens\n Two Turtle Doves\n and a Partridge in a Pear Tree"


sampleText2 = sampleText.replace("Christmas", str(first_noun.upper())).replace("Seven Swans",str(second_noun.upper())).replace("Rings",str(third_noun.upper())).replace("Calling",str(first_adj.lower())) + sampleText[170] + (str(third_adj))
print(output)
print(sampleText2)