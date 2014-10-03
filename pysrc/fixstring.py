def gramatica(letra):
	grammar = {"A" : "1N", "B" : "7C", "C" : "faF", "D" : "aW", "E" : "","F" : "dY", "G" : "aS", "H" : "eZ", "I" : "aX", "J" : "bM","K" : "1J", "L" : "gÑ", "M" : "cK", "N" : "dO", "Ñ" : "fH", "O" : "aT", "P" : "gQ", "Q" : "1E", "R" : "5L", "S" : "67R", "T" : "bA", "U" : "2D", "V" : "aU", "W" : "egV", "X" : "4W", "Y" : "3Z", "Z" : "6J", "a" : "Xv", "b" : "0c", "c" : "Aa", "d" : "Cz", "e" : "Xy", "f" : "Yx", "g" : "Yx", "h" : "8i", "i" : "9k", "j" : "0j", "k" : "@s", "l" : "Za", "m" : "Bt", "n" : "%\q", "ñ" : "&r", "o" : "#p", "p" : "Eñ", "q" : "0%", "r" : "@$", "s" : "$m", "t" : "", "u" : "8w", "v" : "9$", "w" : "B0", "x" : "Yv", "y" : "#7a", "z" : "Xu", "0" : "x9", "1" : "z0", "2" : "m3", "3" : "k8", "4" : "g5", "5" : "j2", "6" : "x3", "7" : "h1", "8" : "l6", "9" : "x0"}
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
