import os
import json
import yaml
import re
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from formatting.formatting import Formatter
from docutils import get_creds, save_doc
from datetime import date
from additional_components.dropdowns import ENGINEER, QE, FORKED, DEPLOYED, IQETESTED, UITESTED, CCB, SC_UPDATED


# If modifying these scopes, delete the file token.json.
SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

OPTION = 'RAW'

class GoogleSheet:
    def __init__(self, settings):
        self.settings = settings
        self.creds = get_creds()
        self.formatter = Formatter()
        self.gsheet_service = build('sheets', 'v4', credentials=self.creds)
        self.drive_service = build('drive', 'v3', credentials=self.creds)

    
    def update_values(self, spreadsheet_id, my_range, valueInput, update_request_body):
        try:
            self.gsheet_service.spreadsheets().values().update(
                spreadsheetId=spreadsheet_id, range = my_range, valueInputOption = valueInput, 
                body =  update_request_body).execute() 
        except HttpError as error:
            print(f"An error occurred: {error}")


    def drop_down_request_builder(self, cell_range, drop_values):
        body = {
                "setDataValidation": {
                    "range": cell_range,
                    "rule": {
                        "condition": {
                            "type": "ONE_OF_LIST",
                            "values": [{"userEnteredValue": value} for value in drop_values["values"]]
                        },
                        "showCustomUi": True,
                        "strict": True
                    }
                }
            }
        
        return body


    def get_image_values(self):
        today = date.today()
        service_dict = {}
        current_file_directory = os.path.dirname(__file__)
        file_name = f"service_data_{today.strftime('%Y-%m-%d')}.json"
        path_to_data = os.path.join(current_file_directory, file_name)

        if not os.path.exists(path_to_data):
            raise FileNotFoundError(f"Error: The file '{path_to_data}' does not exist.")
        else: 
            try:
                with open(path_to_data, 'r') as file:
                    data = json.load(file)
                    service_dict.update(data)
            except json.JSONDecodeError:
                print("Error: Invalid JSON.")
            except Exception as e:
                print(f"An error occurred: {e}")
        return service_dict
    
    def get_service_image(self, current_service, service_dict):
        if 'notifications' in current_service and current_service != "notifications-frontend":
            image_values = service_dict['notifications-backend']
        elif current_service == "iam-console":
            image_values = {
                "commercial_hash": "No Change",
                "new_sc_image_tag": "Reroll Image Job",
                "config_file_status": "No Changes"
            }
        elif current_service in ["frontend-starter-app", "mbop", "cyndi-operator", "amq-streams/strimzi-rhel8-operator", "insights-kafka-connect"]:
            image_values = {
                "commercial_hash": "Check deployment",
                "new_sc_image_tag": "Update Image Tag",
                "config_file_status": "Check Configs"
            }
        elif current_service == "caddy-ubi":
            image_values = {
                "commercial_hash": "N/A",
                "new_sc_image_tag": "N/A",
                "config_file_status": "N/A"
            }
        else:
            image_values = service_dict[current_service]
        
        return image_values


    def component_row(self, spreadsheet_id, component_file, component_name = ""):
        component = yaml.safe_load(open(component_file, 'r'))
        sheet_range = component[component_name]["range"]
        value = component[component_name]["value"]
        if component_name == "title":
            format_body = self.formatter.title_format(component[component_name])
        elif component_name == "legend":
            format_body = self.formatter.legend_format(component[component_name])
        elif component_name == "steps":
            format_body = self.formatter.steps_format(component[component_name])

        body={'values':[value]}

        self.update_values(spreadsheet_id, sheet_range, OPTION, body)

        self.gsheet_service.spreadsheets().batchUpdate(
            spreadsheetId=spreadsheet_id,
            body= format_body
        ).execute()


    def build_dropdowns(self, spreadsheet_id):
        requests = []
        dropdowns = [ENGINEER, QE, FORKED, DEPLOYED, IQETESTED, UITESTED, CCB, SC_UPDATED]

        for dropdown in dropdowns:
            for phase in ["phase_one", "phase_two", "phase_three"]:
                if isinstance((dropdown[phase]['startColumnIndex'] and dropdown[phase]['endColumnIndex']), list):
                    for i in range(len(dropdown[phase]['startColumnIndex'])):
                        cell_range = {
                            'sheetId':0,
                            'startColumnIndex': dropdown[phase]['startColumnIndex'][i],
                            'startRowIndex': dropdown[phase]['startRowIndex'],
                            'endColumnIndex': dropdown[phase]['endColumnIndex'][i],
                            'endRowIndex': dropdown[phase]['endRowIndex']
                        }
                        requests.append(self.drop_down_request_builder(cell_range, dropdown))
                else:
                    cell_range = {
                        'sheetId': 0,
                        'startColumnIndex': dropdown[phase]['startColumnIndex'],
                        'startRowIndex': dropdown[phase]['startRowIndex'],
                        'endColumnIndex': dropdown[phase]['endColumnIndex'],
                        'endRowIndex': dropdown[phase]['endRowIndex']
                    }

                    requests.append(self.drop_down_request_builder(cell_range, dropdown))

        body = {"requests": requests}

        self.gsheet_service.spreadsheets().batchUpdate(
            spreadsheetId=spreadsheet_id,
            body= body
        ).execute()

        body = self.formatter.drop_down_format(dropdowns)

        self.gsheet_service.spreadsheets().batchUpdate(
            spreadsheetId=spreadsheet_id,
            body= body
        ).execute()
        


    def phase_title(self, spreadsheet_id, phase_file):
        phase_titles = yaml.safe_load(open(phase_file, 'r'))["phase_title"]
        column_title_body = phase_titles["column_values"]

        for phase in phase_titles["phases"]:
            self.update_values(spreadsheet_id, phase["range"], OPTION, {'values':[[phase["title"]]]})
            self.update_values(spreadsheet_id, phase["column_range"], OPTION, {'values': [column_title_body]})

        format_body = self.formatter.phase_column_title_format(phase_titles["phases"])

        self.gsheet_service.spreadsheets().batchUpdate(
            spreadsheetId=spreadsheet_id,
            body= format_body
        ).execute()


    def service_rows(self, spreadsheet_id, service_directory):
        new_image_data = self.get_image_values()
        format_body = []

        for item_name in os.listdir(service_directory):
            values = []
            service_file = os.path.join(service_directory, item_name)
            application_data = yaml.safe_load(open(service_file, 'r'))["app"]

            
            for index, service in enumerate(application_data["services"]):
                image_data = self.get_service_image(service, new_image_data)
                if index == 0:
                    values.append([application_data["risk"], application_data["linked"], 
                                    application_data["application_name"], service , image_data["commercial_hash"], "",
                                    "", "", "",image_data["new_sc_image_tag"], image_data["config_file_status"]])
                else:
                    values.append(["", "", "", service, image_data["commercial_hash"], "", "", "", "", 
                                   image_data["new_sc_image_tag"], image_data["config_file_status"]]) 
            
            self.update_values(spreadsheet_id, application_data["app_range"], OPTION, {"values": values})
            format_body.append(self.formatter.service_format(application_data))  

        self.gsheet_service.spreadsheets().batchUpdate(
            spreadsheetId=spreadsheet_id,
            body= {'requests': format_body}
        ).execute()

    

    def generate(self, doc_name):
        title = doc_name
        folder_name = self.settings['google_api']['folder_name']
        properties = {"properties": {"title": title}}
        update_tracker = self.gsheet_service.spreadsheets().create(body=properties, fields="spreadsheetId").execute()        
        spreadsheet_id = update_tracker.get('spreadsheetId')
        module_dir = os.path.dirname(__file__)
        
        additional_components = os.path.join(module_dir, "./additional_components/")
        # generate title row
        self.component_row(spreadsheet_id, os.path.join(additional_components, "components.yml"), "title")

        # generate legend row
        self.component_row(spreadsheet_id, os.path.join(additional_components, "components.yml"), "legend")

        # generate steps row
        self.component_row(spreadsheet_id, os.path.join(additional_components, "components.yml"), "steps")

        #Drop Downs
        self.build_dropdowns(spreadsheet_id)

        # Generate phase title rows:
        self.phase_title(spreadsheet_id, os.path.join(module_dir, "./formatting/phases.yml"))

        # Generate service rows:
        service_directory = os.path.join(module_dir, "./services")
        # applications = list({services["application_name"] for services in services if "application_name" in services})
        self.service_rows(spreadsheet_id, service_directory)


        # Final formatting column width
        body = self.formatter.format_column_width()

        self.gsheet_service.spreadsheets().batchUpdate(
            spreadsheetId=spreadsheet_id,
            body= body
        ).execute()


        save_doc(spreadsheet_id, self.drive_service, folder_name)