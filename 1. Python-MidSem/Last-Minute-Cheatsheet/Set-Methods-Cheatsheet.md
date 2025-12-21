# 🎲 Set Methods Cheatsheet

## 🔧 Adding Elements
- ➕ **add(item)**: Add single element to set (no effect if already exists)
  - `my_set.add(value)`
- 🔗 **update(iterable)**: Add multiple elements from iterable
  - `my_set.update(another_set)`

## 🗑️ Removing Elements
- 🎯 **remove(item)**: Remove element (error if not found)
  - `my_set.remove(value)`
- 🛡️ **discard(item)**: Remove element (no error if not found)
  - `my_set.discard(value)`
- 📤 **pop()**: Remove and return random element (error if empty)
  - `item = my_set.pop()`
- 🧹 **clear()**: Remove all elements from set
  - `my_set.clear()`

## 🔍 Set Operations
- 🤝 **union(other)**: Return new set with elements from both sets
  - `result = set1.union(set2)` or `set1 | set2`
- 🎯 **intersection(other)**: Return new set with common elements only
  - `result = set1.intersection(set2)` or `set1 & set2`
- ➖ **difference(other)**: Return elements in first set but not second
  - `result = set1.difference(set2)` or `set1 - set2`
- ⚡ **symmetric_difference(other)**: Return elements in either set but not both
  - `result = set1.symmetric_difference(set2)` or `set1 ^ set2`

## 🔍 Set Relationships
- 📊 **issubset(other)**: Check if all elements are in other set
  - `is_subset = set1.issubset(set2)`
- 📈 **issuperset(other)**: Check if contains all elements of other set
  - `is_superset = set1.issuperset(set2)`
- 🚫 **isdisjoint(other)**: Check if no common elements with other set
  - `no_overlap = set1.isdisjoint(set2)`

## 📋 Copying
- 📄 **copy()**: Create shallow copy of set
  - `new_set = my_set.copy()`

#set-methods #python #cheatsheet