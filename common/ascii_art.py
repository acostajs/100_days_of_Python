# This contains ALL the ascii art for the whole 100 days of Python

def ascii_art(pick: str) -> str:

    match pick:
        case "menu":
            ascii_art = """
  █    ███   ███     ████   ███  █   █  ████     ███  █████    ████  █   █ █████ █   █  ███  █   █ 
 ██   █   █ █   █    █   █ █   █  █ █  █        █   █ █        █   █  █ █    █   █   █ █   █ ██  █ 
  █   █   █ █   █    █   █ █████   █    ███     █   █ ████     ████    █     █   █████ █   █ █ █ █ 
  █   █   █ █   █    █   █ █   █   █       █    █   █ █        █       █     █   █   █ █   █ █  ██ 
 ███   ███   ███     ████  █   █   █   ████      ███  █        █       █     █   █   █  ███  █   █ 
"""
        case "divider":
            ascii_art =f"{"-" * 100}"
            
    return ascii_art
