# OCR_dataset_gen
OCR dataset generation via Faker and trdg with annotation

#command for Over400pix generation:
trdg -l ru400 -c 100 -w 1 -b 3 -f 48 -k 2 -rk --margins 12,20,12,20 --fit -bl 1 -rbl

#command for medium generation:
trdg -l 399ru150 -c 100 -w 1 -b 3 -f 48 -k 2 -rk --margins 10,10,10,10 --fit -bl 1 -rbl

#command for small generation:
trdg -l ru150 -c 176800 -w 1 -b 3 -f 48 -k 2 -rk --margins 7,10,7,10 --fit -bl 1 -rbl
