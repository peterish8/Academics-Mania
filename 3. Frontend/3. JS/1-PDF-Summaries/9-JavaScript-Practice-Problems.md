# 💻 JavaScript Practice Problems

## 🎯 Problem Set Overview
15 practical coding challenges covering arrays, functions, loops, conditionals, and algorithms.

## 📋 Problem Categories

### 🔢 Array & Function Problems
1. **Square & Filter** → Transform array, filter results
2. **Array Manipulation** → Add/remove elements, print states
3. **Array Maximum** → Find largest number using loops

### 🎯 Conditional Logic
4. **Number Classification** → Positive/negative/zero check
5. **Day Checker** → Switch statement for weekdays
6. **Student Grades** → Score to letter grade conversion

### 🔄 Loop Challenges
7. **Even Numbers** → Print evens 1-20, skip odds
8. **Sum Positive** → Calculate sum of positive numbers only
9. **Multiplication Table** → Generate table for user input
10. **Vowel Counter** → Count vowels in string
11. **FizzBuzz** → Classic divisibility problem
12. **Number Reversal** → Reverse digits using while loop
13. **Prime Numbers** → Find primes 1-30 with nested loops
14. **Factorial** → Calculate factorial using for loop

### 🧮 Algorithm Examples

#### Problem 1: Square & Filter
```javascript
// Input: [2, 3, 4, 5]
// Output: [16, 25] (squared numbers > 10)
function squareAndFilter(arr) {
  return arr.map(n => n * n).filter(n => n > 10);
}
```

#### Problem 10: FizzBuzz
```javascript
// Print 1-50: "Fizz" (÷3), "Buzz" (÷5), "FizzBuzz" (÷both)
for (let i = 1; i <= 50; i++) {
  if (i % 15 === 0) console.log("FizzBuzz");
  else if (i % 3 === 0) console.log("Fizz");
  else if (i % 5 === 0) console.log("Buzz");
  else console.log(i);
}
```

## 🎯 Key Concepts Practiced
- **Higher-order functions** (map, filter, reduce)
- **Conditional statements** (if/else, switch)
- **Loops** (for, while, nested loops)
- **Array methods** (push, pop, manipulation)
- **String processing** (character iteration)
- **Mathematical operations** (modulo, factorial)
- **Algorithm thinking** (prime detection, number reversal)

## 💡 Problem-Solving Patterns
- **Transform then filter** → Use map() then filter()
- **Accumulator pattern** → Use reduce() or loop with sum variable
- **Condition checking** → Use modulo (%) for divisibility
- **String iteration** → Use for...of or traditional for loop
- **Prime detection** → Check divisibility up to square root
- **Number manipulation** → Use mathematical operations and string conversion