def main():
    spacecraft={
    "name":"James Webb Telescope"
    }
    print(create_report(spacecraft))


def create_report(spacecraft):
    return f"""
    =============== REPORT ========================

    Name:{spacecraft.get("name","Unknown")}
    Distance:{spacecraft.get("distance","Unknown")}

    ================================================
"""

main()