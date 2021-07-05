
all: pack.zip
	

clean:
	rm pack.zip

pack.zip:
	python3 mcrpw-export.py . pack.zip
	

deploy: pack.zip
	scp -P 69 pack.zip root@hatkid.cf:/var/www/fs/pack.zip
