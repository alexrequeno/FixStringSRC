def gramatica(letra):
	grammar = {"A" : "1N", "B" : "7C", "C" : "faF", "D" : "aW", "E" : "","F" : "dY", "G" : "aS", "H" : "eZ", "I" : "aX", "J" : "bM","K" : "1J", "L" : "g—", "M" : "cK", "N" : "dO", "—" : "fH", "O" : "aT", "P" : "gQ", "Q" : "1E", "R" : "5L", "S" : "67R", "T" : "bA", "U" : "2D", "V" : "aU", "W" : "egV", "X" : "4W", "Y" : "3Z", "Z" : "6J", "a" : "Xv", "b" : "0c", "c" : "Aa", "d" : "Cz", "e" : "Xy", "f" : "Yx", "g" : "Yx", "h" : "8i", "i" : "9k", "j" : "0j", "k" : "@s", "l" : "Za", "m" : "Bt", "n" : "%\q", "Ò" : "&...(line truncated)...
	if grammar[letra]:
		letra = grammar[letra]
	return letra

palabras = "Alex Requeno"
palabras = palabras.replace(" ", "")
tam = len(palabras)
res = ""
for e in palabras:
        res += gramatica(e)        
print res
raw_input()
