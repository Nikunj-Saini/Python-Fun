def mad_libs():
    print("Welcome to the Mad Libs Game! Fill in the blanks to create a fun story.\n")

    # Prompting user inputs
    adjective1 = input("Enter an adjective: ")
    noun1 = input("Enter a noun: ")
    verb1 = input("Enter a verb: ")
    place = input("Enter a place: ")
    noun2 = input("Enter another noun: ")
    adjective2 = input("Enter another adjective: ")
    verb2 = input("Enter another verb: ")

    # Mad Libs story template
    story = f"""
    Once upon a time there was a {noun1} who was  {verb1} which is very {adjective1} and the {noun2} has also joined {noun1}
    they both were  {verb2}  very  {adjective2}
    """

    print("\nHere's your story:")
    print(story)


mad_libs()
