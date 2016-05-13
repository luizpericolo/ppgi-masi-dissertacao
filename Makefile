install-deps:
	sudo apt-get install python-virtualenv
	sudo apt-get install python-dev
	sudo apt-get install libtiff5-dev libjpeg8-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python-tk
	virtualenv venv

install-pip-deps:
	pip install -r requirements.txt
