
def card_printer(name, seat, plane_model, flight_number):
    text = f"| Pasażer: {name} Siedzenie: {seat} Model: {plane_model} FN: {flight_number} |"  # f - format
    frame = f"+{'-' * (len(text) - 2)}+"
    empty_frame = f"|{' ' * (len(text) - 2)}|"

    border = [frame, empty_frame, text, empty_frame, frame] # lista 5 elementow (stringow)
    border_text = "\n".join(border)    # join -metoda stringu
    print(border_text)