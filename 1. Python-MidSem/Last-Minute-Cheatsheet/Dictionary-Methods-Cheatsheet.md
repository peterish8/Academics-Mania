# 🗂️ Dictionary Methods Cheatsheet

## 🔍 Accessing Values
- 🛡️ **get(key, default)**: Safely get value by key (returns None or default if missing)
  - `value = my_dict.get(key, default_value)`
- 🔑 **keys()**: Get all keys as dict_keys object
  - `all_keys = my_dict.keys()`
- 💎 **values()**: Get all values as dict_values object
  - `all_values = my_dict.values()`
- 📋 **items()**: Get all key-value pairs as dict_items object
  - `pairs = my_dict.items()`

## 🔧 Adding & Updating
- 🔄 **update(other)**: Add/update multiple key-value pairs from another dict
  - `my_dict.update(other_dict)`
- 🛡️ **setdefault(key, default)**: Add key only if it doesn't exist
  - `value = my_dict.setdefault(key, default_value)`

## 🗑️ Removing Elements
- 📤 **pop(key, default)**: Remove and return value by key (returns default if missing)
  - `value = my_dict.pop(key, default_value)`
- 📦 **popitem()**: Remove and return last inserted key-value pair as tuple
  - `key, value = my_dict.popitem()`
- 🧹 **clear()**: Remove all key-value pairs from dictionary
  - `my_dict.clear()`

## 📋 Copying
- 📄 **copy()**: Create shallow copy of dictionary
  - `new_dict = my_dict.copy()`

## 🏗️ Creating Dictionaries
- 🔑 **fromkeys(keys, value)**: Create dict with keys and same value for all
  - `new_dict = dict.fromkeys(key_list, default_value)`

#dictionary-methods #python #cheatsheet