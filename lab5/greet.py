def greet(name: str, country_code: str = "HU") -> None:
    """
    Greets a person in different languages based on the provided country code.

    Parameters:
    name (str): The name of the person to greet.
    country_code (str, optional): The country code to determine the greeting language.
                                    Defaults to "HU" (Hungary).
    """
    # Match statement to choose greeting based on country code
    match country_code:
        case "HU":
            print("Szia {}!".format(name))  # Hungarian greeting
        case "EN":
            print("Hi {}!".format(name))    # English greeting
        case "FI":
            print("Moi {}!".format(name))   # Finnish greeting
        case _:
            print("Country code not found!")  # Default case for unknown country codes

# Examples of function usage
greet("Anna")           # Defaults to Hungarian greeting
greet("John", "EN")     # English greeting
greet("Liisa", "FI")    # Finnish greeting
greet("Carlos", "ES")   # Unknown country code
