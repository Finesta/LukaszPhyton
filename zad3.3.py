itemki = { "banany": "kg",
		"jajka": "sztuki",
      	"Mleko": "l",
      	"fajki": "sztuki",
		"telefony": "sztuki",
		"mąka": "kg"}
print([key for key,value in itemki.items() if value == "sztuki"])