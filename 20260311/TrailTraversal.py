def navigate_trail(map):  
  rows = len(map)
    cols = len(map[0])

    for r in range(rows):
        for c in range(cols):
            if map[r][c] == "C":
                start = (r, c)

    r, c = start
    prev = None
    moves = ""

    directions = [
        (0, 1, "R"),
        (1, 0, "D"),
        (0, -1, "L"),
        (-1, 0, "U")
    ]

    while map[r][c] != "G":
        for dr, dc, move in directions:
            nr = r + dr
            nc = c + dc

            if 0 <= nr < rows and 0 <= nc < cols:
                if (nr, nc) != prev and map[nr][nc] in ("T", "G"):
                    moves += move
                    prev = (r, c)
                    r, c = nr, nc
                    break
    
    return moves


# ChatGPT has provided a universal solution for this kind of puzzle/grid/matrix trail problems.
# The following 5 steps are commonly used in all these poblems:
# 1. Get the rows and cols:
#     rows = len(grid)
#     cols = len(grid[0])
# 2. Define 4 directions:
#     directions = [
#           (0, 1, "R"),
#           (1, 0, "D"),
#           (0, -1, "L"),
#           (-1, 0, "U")
#       ]
# 3. Calculate new coordinations:
#     nr = r + dr
#     nc = c + dc
# 4. Check on borders:
#     0 <= nr < rows
#     0 <= nc < cols
# 5. Validate moves:
#     if grid[nr][nc] == "T"
#     if grid[nr][nc] != "-"








