text = "hello world"
num_text = "12345"
mixed_text = "Hello123"
whitespace_text = "   Hello   "
tabbed_text = "Hello\tWorld"
title_text = "Hello World"
uppercase_text = "HELLO"
lowercase_text = "hello"
symbol_text = "©2025"
multi_line_text = "Line1\nLine2"
separator_text = "apple,banana,orange"
replace_text = "I like apples"
identifier_text = "variable1"
nonprintable_text = "Hello\nWorld"
space_text = "     "
join_list = ["Hello", "World"]

print("capitalize():", text.capitalize())
print("casefold():", text.casefold())
print("center():", text.center(20, '*'))
print("count():", text.count("l"))
print("encode():", text.encode())
print("endswith():", text.endswith("world"))
print("expandtabs():", tabbed_text.expandtabs(4))
print("find():", text.find("world"))
print("format():", "My name is {}".format("Rahul"))
print("format_map():", "Name: {name}, Age: {age}".format_map({"name": "Rahul", "age": 25}))
print("index():", text.index("world"))
print("isalnum():", mixed_text.isalnum())
print("isalpha():", text.isalpha())
print("isascii():", symbol_text.isascii())
print("isdecimal():", num_text.isdecimal())
print("isdigit():", num_text.isdigit())
print("isidentifier():", identifier_text.isidentifier())
print("islower():", text.islower())
print("isnumeric():", num_text.isnumeric())
print("isprintable():", nonprintable_text.isprintable())
print("isspace():", space_text.isspace())
print("istitle():", title_text.istitle())
print("isupper():", uppercase_text.isupper())
print("join():", " ".join(join_list))
print("ljust():", text.ljust(20, "-"))
print("lower():", title_text.lower())
print("lstrip():", whitespace_text.lstrip())
print("maketrans() and translate():", text.translate(str.maketrans("hel", "xyz")))
print("partition():", text.partition(" "))
print("replace():", replace_text.replace("apples", "bananas"))
print("rfind():", text.rfind("l"))
print("rindex():", text.rindex("l"))
print("rjust():", text.rjust(20, "-"))
print("rpartition():", text.rpartition(" "))
print("rsplit():", separator_text.rsplit(","))
print("rstrip():", whitespace_text.rstrip())
print("split():", separator_text.split(","))
print("splitlines():", multi_line_text.splitlines())
print("startswith():", text.startswith("hello"))
print("strip():", whitespace_text.strip())
print("swapcase():", text.swapcase())
print("title():", text.title())
print("upper():", text.upper())
print("zfill():", num_text.zfill(10))
