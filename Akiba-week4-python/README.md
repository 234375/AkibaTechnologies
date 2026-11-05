     Name: 
Sadya Ibrahim

      Assignment: 

Week 4 – Mutability, References, and Memory Model in Python

    Project:

Student Marks Manager



    1. Why does modifying a shared reference affect the original list?

Because both variables refer to the same list object in memory. Therefore, modifying the list through one variable also affects the other variable.

    2. Why does modifying the copied list not affect the original list?

Because ".copy()" creates a new, independent list object. Therefore, changes made to the copied list do not affect the original list.

     3. What is the difference between equality and identity in Python?

- Equality ("=="): Checks whether two objects have the same values.
- Identity ("is"): Checks whether two variables refer to the same object in memory.
