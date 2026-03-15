def get_captured_value(pieces):
    total = 39
    values = {
        "P" : 1,
        "R" : 5,
        "N" : 3,
        "B" : 3,
        "Q" : 9
    }
    if "K" not in pieces:
        return "Checkmate"
    else:
        remain = sum(values.get(piece, 0) for piece in pieces)
        return (total - remain)

# There are many ways to solve this challenge and I chose the way by creating a dictionary of Chess piece -- value pairs.
# Before looping through every input piece and find the total value, the challenge requires a check for the King, 
# if the King is not in the pieces, then it should return "Checkmate".
# After checking for checkmate, the total values of remaining pieces were calculated by looking up the value of each 
# piece in the dictionary, using a get method. The default value is set to 0 so if a piece is not listed in the dictionary
# the value will be counted as 0.
# Finally return the value taken by opponent.
