.PHONY: all
all: data

.PHONY: data
data:
	mkdir -p data/images
	python3 test_script.py

.PHONY: clean
clean:
	rm -rf data/images

.PHONY: regen
regen: clean data
