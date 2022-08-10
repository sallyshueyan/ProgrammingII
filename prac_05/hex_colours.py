def main():
    COLOUR_NAME_TO_CODE = {"Puce": '#cc8899', "Pear": '#d1e231', "Light": '#eedd82',
                           "Inchworm": "#b2ec5d", "LightSkyBlue": "#87cefa",
                           "Lemon": "#fff700", "Purple": '#a020f0', "Khaki": "#f0e68c", "Jade": "#00a86b",
                           "Iceberg": "#71a6d2"}

    colour_name = input("Enter a colour name: ").title()
    while colour_name != "":
        if colour_name in COLOUR_NAME_TO_CODE:
            print(colour_name, "is", COLOUR_NAME_TO_CODE[colour_name])
        else:
            print("Invalid colour name")
        colour_name = input("Enter a colour name: ").title()


main()
