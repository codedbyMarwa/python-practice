def main():
    names=["Mario", "Luigi", "Daisy", "Yoshi"]
    for name in names:
        print(write_letter(name, "Princess Peach"))

def write_letter(receiver, sender):
    return f"""
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
        Dear {receiver},

        You are cordially invited to a ball at 
        Peach's castle in the evening, 7:00pm.

        Sincerely,
        {sender}
"""
main()