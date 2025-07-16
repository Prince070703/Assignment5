# Assignment5

**Task 1 (Task6a.py):**

Python Program: Student Marks Finder Using Dictionary
📌 Objective:
This Python program allows the user to enter a student's name and checks if the name exists in a dictionary. If found, it displays the student’s marks; otherwise, it shows a "student not found" message.

🔍 Code Explanation
dict = {'Prince': 22, 'Sam': 23, 'Carry': 26}
A dictionary is created where each key is a student’s name, and the value is their marks.

name = input('Enter the student name: ')
Takes input from the user for a student’s name.

if name in dict:
Checks if the entered name exists in the dictionary.

print('The marks is:', dict[name])
If the name exists, prints the corresponding marks.

else: print('student not found')
If the name is not found in the dictionary, prints an error message.

✅ Sample Output:
Enter the student name: Sam
The marks is: 23

Enter the student name: John
student not found



**Task 2(task6b.py) :**

Code Description: Reversing First Five Elements of a List
📌 Objective:
This Python program demonstrates how to:

Create a list of numbers.

Extract the first five elements using list slicing.

Reverse the extracted sublist.

Display the original list, the extracted elements, and their reversed order.

🔢 Step-by-Step Explanation:
number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
A list named number is created with elements from 1 to 10.
print('The original sequence is:', number)
Prints the entire original list.

num1 = number[0:5]
Slices the list from index 0 to 4 (first 5 elements) and stores it in a new list called num1.

number[0:5] gives [1, 2, 3, 4, 5]

print('The first five extracted elements are:', num1)
Displays the extracted first five elements.

num1.reverse()
Reverses the elements in the num1 list. Now, num1 becomes [5, 4, 3, 2, 1].

print('Reverse order of first five elements:', num1)
Prints the reversed list of the first five elements.

✅ Output Example:
The original sequence is: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
The first five extracted elements are: [1, 2, 3, 4, 5]
Reverse order of first five elements: [5, 4, 3, 2, 1]
