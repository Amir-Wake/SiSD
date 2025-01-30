# Understand programming languages.

# Tasks

## What is the difference between compiled and interpreted languages?

- **Compiled Language (C, C++):** The entire source code is converted into machine language (binary) before running. It's faster and high on performance but harder for debugging and not portable for every machine.

- **Interpreted Language (Ruby, Python, JavaScript):** The source code is translated while running using an interpreter. It's easier for debugging and portable for many machines but slower on performance.

## What is the difference between syntax and semantics in programming?

- **Syntax:** It's like grammar in a language (the set of rules). 
    - In Python:
        ```python
        print("Hello World")
        ```
        is correct syntax, but,
        ```python
        print "Hello world"
        ```
        is incorrect.

- **Semantics:** The behavior of the code when executed.
    - Example:
        ```python
        X = 2 + 3  # means add 2 and 3 then store it in X
        ```

## What is the difference between procedural languages and object-oriented languages?

- **Procedural Languages (C, Pascal):** These languages use functions to perform tasks. They follow a step-by-step approach to solve a problem.    
    - Example:
        ```c
        void main() {
            printf("Hello World");
        }
        ```

- **Object-Oriented Languages (Java, Python):** These languages use objects to represent data and methods. They focus on objects that interact with each other.   
    - Example:
        ```python
        class HelloWorld:
            def say_hello(self):
                print("Hello World")

        hw = HelloWorld()
        hw.say_hello()
        ```

## Key Features of Programming

- **Abstraction:** Simplifying complex functionalities.
- **Encapsulation:** Data and methods grouped together.
- **Inheritance:** Reusing code from parent classes.
- **Polymorphism:** Multiple forms of methods and objects.
- **Modularity:** Dividing programs into modules.
- **Error Handling:** Managing errors.
- **Efficiency:** Optimizing performance and resources.
