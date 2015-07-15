install-deps:
	sudo apt-get install python-virtualenv
	sudo apt-get install python-dev
	virtualenv venv

install-pip-deps:
	pip install -r requirements.txt
	
	

