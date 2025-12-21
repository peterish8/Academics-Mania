# 🔤 String Methods Cheatsheet

## 🔍 Searching & Finding
- 🎯 **find(substring)**: Return index of first occurrence (-1 if not found)
  - `position = my_string.find(substring)`
- 🔢 **count(substring)**: Count occurrences of substring
  - `frequency = my_string.count(substring)`
- 📍 **index(substring)**: Return index of first occurrence (error if not found)
  - `position = my_string.index(substring)`
- ✅ **startswith(prefix)**: Check if string starts with prefix
  - `starts = my_string.startswith(prefix)`
- ✅ **endswith(suffix)**: Check if string ends with suffix
  - `ends = my_string.endswith(suffix)`

## 🔄 Transforming Case
- 📈 **upper()**: Convert all characters to uppercase
  - `uppercase = my_string.upper()`
- 📉 **lower()**: Convert all characters to lowercase
  - `lowercase = my_string.lower()`
- 🎯 **capitalize()**: Capitalize first character, rest lowercase
  - `capitalized = my_string.capitalize()`
- 📚 **title()**: Capitalize first letter of each word
  - `title_case = my_string.title()`
- 🔄 **swapcase()**: Swap uppercase to lowercase and vice versa
  - `swapped = my_string.swapcase()`

## ✂️ Splitting & Joining
- 💥 **split(separator)**: Split string into list by separator
  - `word_list = my_string.split(separator)`
- 🔗 **join(iterable)**: Join elements of iterable with string as separator
  - `result = separator.join(list_of_strings)`

## 🧹 Cleaning
- 🧽 **strip()**: Remove whitespace from both ends
  - `cleaned = my_string.strip()`
- ◀️ **lstrip()**: Remove whitespace from left end
  - `left_cleaned = my_string.lstrip()`
- ▶️ **rstrip()**: Remove whitespace from right end
  - `right_cleaned = my_string.rstrip()`

## 🔄 Replacing
- 🔄 **replace(old, new)**: Replace all occurrences of old with new
  - `new_string = my_string.replace(old_text, new_text)`

## ✅ Checking Content
- 🔤 **isalpha()**: Check if all characters are alphabetic
  - `is_alpha = my_string.isalpha()`
- 🔢 **isdigit()**: Check if all characters are digits
  - `is_digit = my_string.isdigit()`
- 🔤🔢 **isalnum()**: Check if all characters are alphanumeric
  - `is_alnum = my_string.isalnum()`
- 🔠 **isupper()**: Check if all characters are uppercase
  - `is_upper = my_string.isupper()`
- 🔡 **islower()**: Check if all characters are lowercase
  - `is_lower = my_string.islower()`
- 📚 **istitle()**: Check if string is in title case
  - `is_title = my_string.istitle()`
- ⭐ **isspace()**: Check if all characters are whitespace
  - `is_space = my_string.isspace()`

#string-methods #python #cheatsheet