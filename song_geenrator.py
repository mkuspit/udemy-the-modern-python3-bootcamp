def make_song(verses=99, beverage="soda"):
    for num in range(verses, -1, -1):
        if num > 1:
            yield f"{num} bottles of {beverage} on the wall."
        elif num == 1:
            yield "Only 1 bottle of {beverage} left!"
        else:
            yield "No more {beverage}!"