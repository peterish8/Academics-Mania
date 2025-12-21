# 📋 List Methods Cheatsheet

## 🔧 Adding Elements
- ➕ **append(item)**: Add single element to end of list
  - `my_list.append(value)`
- 📥 **insert(index, item)**: Insert element at specific position
  - `my_list.insert(position, value)`
- 🔗 **extend(iterable)**: Add all elements from another iterable
  - `my_list.extend(another_list)`

## 🗑️ Removing Elements
- 🎯 **remove(item)**: Remove first occurrence of value (error if not found)
  - `my_list.remove(value)`
- 📤 **pop(index)**: Remove and return element at index (last if no index)
  - `item = my_list.pop(index)`
- 🧹 **clear()**: Remove all elements from list
  - `my_list.clear()`

## 🔍 Finding Elements
- 🎯 **index(item)**: Return index of first occurrence (error if not found)
  - `position = my_list.index(value)`
- 🔢 **count(item)**: Count occurrences of value in list
  - `frequency = my_list.count(value)`

## 📊 Sorting & Reversing
- 📈 **sort()**: Sort list in ascending order in-place
  - `my_list.sort()`
- 📉 **sort(reverse=True)**: Sort list in descending order in-place
  - `my_list.sort(reverse=True)`
- 🔄 **reverse()**: Reverse order of elements in-place
  - `my_list.reverse()`

## 📋 Copying
- 📄 **copy()**: Create shallow copy of list
  - `new_list = my_list.copy()`

#list-methods #python #cheatsheet