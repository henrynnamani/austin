# Comment - DONE

# Indentation - DONE

# Value | Literal - DONE

# Variable - DONE

# Typecasting - DONE

# Operators

# print("I am working")

"""
    Comment

    - used to explain a particular section of code to a developer

    Python ignores comments
    Comments are only relevant to your fellow developers

    types:
    - single line - #
    - multiline comment -
"""

"""
    Indentation(space)

    `Javascript`

    () -> braces
    {} -> parenthesis

    if (name == "Augustine") { # block of code 
        statements;
        print("if statement executed")
    }   

    `Python`

    for ...:
        do_something();

    if name == "Augustine":
        statements;
        print("if statement executed")

"""

"""
    type() - determine the type of a variable or value
    VALUES OR LITERAL

    - String(str) => ""
        NOTE: Anything enclosed within double apostrophe is a string
        "Augustine", "Miva Open University", "Enugu"
        NOTE: "5" so "5" is no longer a number but a string(Numeric string), 5
    - Number
        - Integer(int) - -5, 9, 5, 8, 10, 12, 67, 88, 100
        - Float(float) - -4.5, 8.9, 2.0, 1.4, 1.0, 0.5
    - Boolean(bool)
        - Two values -> True or False || true or false
        NOTE: The first letter must be capitalized
"""

"""
    price of property
    house rent
"""
# meaning
myname = "Augustine"

# print(myname)

"""
    RULE FOR VARIABLE DECLARATIONS
    - Variable must not start with a digit/number
    - Variable must not contain space
    - Variable must not contain any other symbol besides _(underscore)
    NOTE; _(underscore) | -(hyphen)
    - Variables are case sensitive
    - Variable must start with either a letter or an underscore
"""

# NOT defined => that variable does not exist or has not been created

"""
    TYPECASTING
    - changing a value from one data type to another

    "5"(string) -> 5(int) | 5.0(float)
    5(int)  => "5"(string)

    NOTE: 
    addition operator(+)

    two string => "Hello" + "world" = "Helloworld" (concatenate|join)
    two string => "5" + "4" = "54"

    addition operation(+)

    two number => 5 + 4 = 9

    Functions
    int(x) -> 
        if x = "5"
        int("5") -> 5
        if x = "6.0"
        int("6.0") = 6
    float(x) -> 
        if x = 5
        float(5) = 5.0
    str(x) -> 
        if x = 5 | 7.6
        str(5) = "5"
        str(7.6) = "7.6"

"""

# print(float(5))
# print(int(5.6)) # 5.6(float) -> 5(int)

# number_one = "5" # "5" -> 5
# number_two = 4

# result = int(number_one) + number_two # 9

# print(result)

# augustine_age = 21 # "21"

# print("Augustine is " + str(augustine_age) + " years old") # Augustine is 21 years old

number_one = input("Enter number: ")
number_two = 3

result = number_one * number_two

print(result)