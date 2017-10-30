all: monsters-cr.md monsters-alphabetical.md

monsters-cr.md: genbycr.py source.json
	cat key.md > monsters-cr.md
	python genbycr.py source.json >> monsters-cr.md

monsters-alphabetical.md: genalpha.py source.json
	cat key.md > monsters-alphabetical.md
	python genalpha.py source.json >> monsters-alphabetical.md
