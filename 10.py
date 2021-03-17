def change_to_snake_case(str1):
    snake_case = ""
    for i in str1:
        if 'A' <= i <= 'Z':
            snake_case += '_' + i.lower()
        else:
            snake_case += i
    return snake_case


def change_to_kebab_case(str1, selector):
    kebab_case = ""
    for i in str1:
        if 'A' <= i <= 'Z':
            kebab_case += selector + i.lower()
        else:
            kebab_case += i
    return kebab_case


print(change_to_snake_case(input("enter the string for snake case : ")))
print(change_to_kebab_case(input("enter the string for kebab case : "), input("enter the selector :")))
