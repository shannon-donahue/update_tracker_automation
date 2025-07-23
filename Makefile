# Define variables
VENV_DIR := ./.venv
PYTHON_EXEC := $(VENV_DIR)/bin/python
APP_SCRIPT := main.py                  
GSHEET_FLAG := --gsheet

# Default target
all: run

# Target to set up virtual environment
venv:
	@echo "Checking for virtual environment..."
	@if [ ! -d "$(VENV_DIR)" ]; then \
		echo "Creating virtual environment at $(VENV_DIR)..."; \
		python3 -m venv $(VENV_DIR); \
		echo "Installing dependencies from requirements.txt..."; \
		$(VENV_DIR)/bin/pip install -r requirements.txt; \
	else \
		echo "Virtual environment already exists."; \
	fi

# Target run dependent on venv existing
run: venv
	@echo "Running application..."
	$(PYTHON_EXEC) $(APP_SCRIPT) $(GSHEET_FLAG)
	
# Target to install dependencies
install-deps: venv
	@echo "Installing/updating dependencies..."
	$(PYTHON_EXEC) -m pip install -r requirements.txt


# Target to clean up  __pycache__
clean:
	@echo "Cleaning up..."
	find . -type d -name "__pycache__" -exec rm -rf {} +

.PHONY: all run venv install-deps clean