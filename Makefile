all: monsters-cr.md

monsters-cr.md: genbycr.py source.json
	cat key.md > monsters-cr.md
	python genbycr.py source.json >> monsters-cr.md
