from goldenglobe import findinfo

MPDrama = ["Argo","Life of Pi", "Django Unchained", "Zero Dark Thirty","Lincoln"]

print "1: Best Motion Picture - Drama"
print "2: X"
print "3: X"
print "4: X"
print "5: X"
print "6: X"
print "7: X"
print "8: X"
print "9: X"
print "10: X"
print "11: X"
print "12: X"
print "13: X"
print "14: X"
print "15: X"
print "16: X"
print "17: X"
print "18: X"
print "19: X"
print "20: X"
print "21: X"
print "22: X"
print "23: X"
print "24: X"
print "25: X"
print "26: X"

var = raw_input("Choose the number of award you want to see: ")
print "you entered", var

if (var == "1"):
	print "u made it here"
	top20=findinfo("best motion picture drama")
	unis=top20[0]
	bis=top20[1]
	print unis
	print bis

