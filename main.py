def sort(width: float, height: float, length: float, mass: float) -> str:
    volume = width * height * length
    bulky = volume >= 1_000_000 or max(width, height, length) >= 150
    heavy = mass >= 20
    return "REJECTED" if (bulky and heavy) else ("SPECIAL" if (bulky or heavy) else "STANDARD")


# ---- Basic tests ----
if __name__ == "__main__":
    # STANDARD (neither bulky nor heavy)
    assert sort(10, 20, 30, 5) == "STANDARD"

    # SPECIAL (bulky by volume threshold)
    assert sort(100, 100, 100, 5) == "SPECIAL"            

    # SPECIAL (bulky by dimension threshold)
    assert sort(150, 10, 10, 5) == "SPECIAL"             

    # SPECIAL (heavy only)
    assert sort(10, 10, 10, 20) == "SPECIAL"         
    
    # REJECTED (both bulky and heavy)
    assert sort(200, 10, 10, 25) == "REJECTED"

    # More edges
    assert sort(149.9, 149.9, 44.5, 19.99) == "STANDARD"  # just under both
    assert sort(149.9, 149.9, 44.5, 20.0) == "SPECIAL"    # just heavy
    assert sort(149.9, 149.9, 44.5, 25.0) == "SPECIAL"    # heavy only
    assert sort(200.0, 1.0, 1.0, 19.0) == "SPECIAL"       # bulky only
    assert sort(200.0, 1.0, 1.0, 20.0) == "REJECTED"      # both

    print("All tests passed.")
