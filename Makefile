
all: pack.zip
	

clean:
	rm -vf pack.zip

pack.zip: check extra_files/sounds.json
	python3 mcrpw-export.py . pack.zip
	
check:
	python3 mcrpw-source-check.py

extra_files/sounds.json:
	python3 merge-sounds-json.py
