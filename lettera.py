class Letter:
    def __init__(self, letterFrom, letterTo):
        self._letterFrom = letterFrom
        self._letterTo = letterTo
        self._body = []

    def addLine(self, line):
        self._body.append(line)

    def getText(self):
        body_text = "\n".join(self._body)
        return f"Dear {self._letterTo},\n\n{body_text}\n\nSincerely\n\n{self._letterFrom}"


test = Letter("Mario Mario", "Luigi luigi")
""" test.addLine(" corpo \n corpo \n corpo \n corpo.") """
test.addLine("I am sorry we must part.")
test.addLine("I wish you all the best.")

print(test.getText())
