VENV := .virtual_environment

all: install

$(VENV):
	python3 -m venv $(VENV)

install: install-deb install-pip

install-deb:
	@echo python3.12-venv is necessary for venv.
	@echo ffmpeg is necessary to read audio files for ASR
	for package in python3.12-venv ffmpeg; do \
		dpkg -l | egrep '^ii *'$${package}' ' 2>&1 > /dev/null || sudo apt install $${package}; \
	done

install-pip: $(VENV)
	. $(VENV)/bin/activate; pip3 install --upgrade -r requirements.txt

sentiment-analysis-demo:
	. $(VENV)/bin/activate; src/sentiment_analysis_demo.py

zero-shot-classification-demo:
	. $(VENV)/bin/activate; src/zero_shot_classification.py

text-generation-demo:
	. $(VENV)/bin/activate; src/text_generation_demo.py

supported-tasks:
	. $(VENV)/bin/activate; src/supported_tasks.py

speech-recognition-demo:
	. $(VENV)/bin/activate; src/speech_recognition_demo.py

image-caption-demo:
	. $(VENV)/bin/activate; src/image_caption_demo.py


