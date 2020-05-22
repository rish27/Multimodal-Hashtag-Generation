README.md

1. Download InstaPIC-1.1M dataset used in CVPR(2017) from link below:
	https://drive.google.com/uc?export=download&id=0B3xszfcsfVUBdG0tU3BOQWV0a0E

2. Command to run in shell: $ python insta_cvpr(17)_scraper.py -startIndx -endIndx
	startIndx: start index for users
	endIndx  : closing index for users

3. [Optional] There are some posts which are not available and thus lots of error like below:
	JSON Query to p/-jXrOTwDT9/: 404 Not Found

	To avoid this one can use below command is shell:

	$ python insta_cvpr(17)_scraper.py -startIndx -endIndx > error.txt


