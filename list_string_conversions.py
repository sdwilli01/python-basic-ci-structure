def list_to_string(list: list) -> str:
    return ''.join(list)

def string_to_list(string: str) -> list:
    return list(string)

def main():
    print("You've executed list_string_conversion.py")
    test_list = ["1", "5", "a", "b", "z"]
    test_string = "Potato1234!!"

    converted_string = list_to_string(test_list)
    converted_list = string_to_list(test_string)

    print(f"The new string is: {converted_string}")
    print(f"The new list is: {converted_list}")

if __name__ == "__main__":
    main()
