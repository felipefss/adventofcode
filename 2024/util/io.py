def readfile(filename: str) -> list[str]:
    with open(filename, encoding="utf-8") as file:
        lines = []

        for line in file:
            lines.append(line.strip())

        return lines
