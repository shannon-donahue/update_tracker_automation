# Update Tracker Automation:

A tool utilized to automatically create a google sheet to help track update cycles for a large number of services.

## Getting Started

The following instructions will help get a local copy of this project up and running

### Prerequisites

* Python 3.8 +
* make
* Google Cloud Project with Google Sheets API enabled

### Virtual Environment Setup
The makefile has a target to set up a new virtual environment

```bash
make venv
```
This command will:
1. Check if a virtual environment exists
2. Create a new one if .venv/ does not exist
3. Install all necessary Python dependencies listed in requirements.txt

### Configuration

#### Settings

This project requires a settings.yml file for configuration. This can be created by following settings.yml.template for formatting and populating with appropriate values.

copy template using:
```bash
cp settings.yml.template settings.yml
```

#### Services
1. Add a directory called `services` to the project's main directory
2. follow `service.yml.template` for formatting service definitition files.
    - This ensures your service configurations are correctly parsed and utilized by the application.

A sample data set that you can use for your team to test and understand the expected structure is available [here](https://drive.google.com/drive/folders/1gj15SMFb87Pd_gCkrS1NfvRgeKaK4z87?usp=drive_link)

### Run Service

The makefile has a target to run the application

```bash
make run
```

This command will:
1. Ensure your virtual environment is set up.
2. Execute the main application script (main.py) with the --gsheet flag, using the Python interpreter from your virtual environment.

Other useful Makefile commands:
1. `make venv`: Creates and sets up the virtual environment and installs dependencies.
2. `make install-deps`: Installs/updates dependencies from requirements.txt into the virtual environment.
3. `make clean`: Removes __pycache__ directories.


### Project Structure
```bash
.
├── Makefile
├── main.py
├── requirements.txt
├── settings.yml.template
├── service.yml.template
├── services/  # You need to create this directory
│   └── ... (your service data files following service.yml.template format)
├── .venv/               # Virtual environment (created by 'make venv')
├── ... (other project files and directories)
```


