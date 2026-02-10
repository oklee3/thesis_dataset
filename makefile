.PHONY: overlap clean_overlap

overlap:
	python3 test_script.py overlap

overlap_bw:
	python3 test_script.py overlap_bw

clean_overlap:
	rm -rf data/images_overlap

clean_overlap_bw:
	rm -rf data/images_overlap_bw
