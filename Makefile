
test:
	for t in *.in; do python3 aqueducte.py $$t > sortida; diff -q `basename $$t .in`.ap.ans sortida; done
