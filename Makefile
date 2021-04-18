
test:
	for t in *.in; do python3 aqueducte.py testing/$$t > sortida; diff -q testing/`basename $$t .in`.pa.ans sortida; done
