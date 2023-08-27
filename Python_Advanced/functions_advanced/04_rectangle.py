def rectangle(lenght, width):
    result = ""
    try:
        result += f"Rectangle area: {lenght * width}" + '\n'
        result += f"Rectangle perimeter: {2 * (lenght + width)}"
    except Exception:
        return "Enter valid values!"
    return result
