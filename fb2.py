def check_identity(name):
    """Given a name as an argument, prints out who they are and
    what their role is on the #ShefCodeFirst Python course."""

    # Reading in a file into a list containing #ShefCodeFirst Python course members, so
    # either they are a student, instructor or ambassador
    with open("python_course_members.txt") as input_file:
        python_course_members = [member.strip() for member in input_file]

    if name == "Pauline" or name == "Lakshika":
        print("{name} is an awesome #ShefCodeFirst ambassador! Go {name}!")
    
    if name == "Darren" or name == "Chris" or name == "Tania" or name == "Nina":
        print("{name} is our awesome instructor! :D")

    if name in python_course_members:
        print("{name} is a student of #ShefCodeFirst's Python course! #SheCodes")

check_identity("Pauline")