PYTHON = python3.6

# ========== Linux (Debian) ==========


# ----- Install -----

install:
	$(if $(shell apt-cache search $(PYTHON)), , \
		sudo apt-get -q update \
		&& apt-get install --no-install-recommends -y apt-utils software-properties-common \
		&& add-apt-repository -y ppa:jonathonf/python-3.6 \
		&& apt-get -q update)
	sudo apt-get install --no-install-recommends -y \
		build-essential \
		$(PYTHON) $(PYTHON)-dev $(PYTHON)-venv cython \
		libssl-dev libffi-dev openssl


# ----- Virtualenv -----

venv_init:
	@if [ ! -d "venv" ]; then $(PYTHON) -m venv venv ; fi;

venv_update:
	@bash -c "source venv/bin/activate && $(MAKE) update"

venv_remove:
	rm -rf venv

# ----- Update -----

update:
	@echo "----- Updating requirements -----"
	@export XXHASH_FORCE_CFFI=1
	@pip install --upgrade wheel pip
	@pip install --upgrade --requirement requirements.txt


# ----- Setup -----

setup: install venv_init venv_update


# ----- Clean -----

clean:
	@find . \( \
		-name "__pycache__" -o \
		-name "*.pyc" -o \
		-name ".cache" -o \
		-name "*.egg-info" \) \
		-prune \
		-exec rm -rf {} \;


# ----- Server -----

runserver:
	python runserver.py