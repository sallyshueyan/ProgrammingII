def main():
    COLOUR_NAME_TO_CODE = {"puce": '#cc8899', "pear": '#d1e231', "light": '#eedd82',
                           "inchworm": "#b2ec5d", "lightSkyBlue": "#87cefa",
                           "lemon": "#fff700", "purple": '#a020f0', "khaki": "#f0e68c", "jade": "#00a86b",
                           "iceberg": "#71a6d2"}

    colour_name = input("Enter a colour name: ").lower() #ask user for colour name
    while colour_name != "":
        if colour_name in COLOUR_NAME_TO_CODE: 
            print(colour_name, "is", COLOUR_NAME_TO_CODE[colour_name]) #formatting to print colour code
        else:
            print("Invalid colour name")
        colour_name = input("Enter a colour name: ").lower()


main()
