# This is the ascii_art used in the task of Day 9 of 100 days of Python


def ascii_art(name: str):
    """
        This function prints the selected ascii art for the project.
    """
    ascii_art = ""
    match name:
        case "title":
            return """
                    _________
                   {         }
                    )_______(
                    |       |_.-._,.---------.,_.-._
                    |       | | |               | | ''-.
                    |       |_| |_             _| |_..-'
                    |_______| '-'''---------''' '-'
                    )       (
                   /_________|
                 .-------------.
                /_______________|
                             
            """
        case "divider":
            return "------------------------------------------------------" 
    return ascii_art
