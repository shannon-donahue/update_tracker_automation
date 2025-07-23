import formatting.colors as colors
from additional_components.columns import COLUMNS

# merge types:
MERGEALL= 'MERGE_ALL'
MERGECOLUMNS = 'MERGE_COLUMNS'
MERGEROWS = 'MERGE_ROWS'

PHASE_COLORS = {'phase_one': {'color': colors.GREEN, 'column_color': colors.LIGHT_GREEN}, 
                'phase_two': {'color': colors.BLUE, 'column_color': colors.LIGHT_BLUE}, 
                'phase_three': {'color': colors.YELLOW, 'column_color': colors.LIGHT_YELLOW} }


class Formatter:

    def cell_range(self, start_row, end_row, start_column, end_column):
        cell_range = {
            'sheetId': 0,
            'startColumnIndex': start_column,
            'startRowIndex': start_row,
            'endColumnIndex':end_column,
            'endRowIndex': end_row
        }

        return cell_range

    def get_bold(self):
        bold = {
            "format": {"bold": True},
            "field": {"fields": 'userEnteredFormat.textFormat.bold'}
        }
        return bold

    def bold_cell(self, cell_range):
        bold_cell_request = {
            'repeatCell': {
                    'range': cell_range,
                    'cell': {
                        'userEnteredFormat':{
                            "textFormat": {
                                "bold": True
                            }
                        }
                    },
                    'fields': 'userEnteredFormat.textFormat.bold'
                }
        }
        return bold_cell_request
    
    def underline_cell(self, cell_range):
        underline_cell_request = {
            'repeatCell': {
                    'range': cell_range,
                    'cell': {
                        'userEnteredFormat':{
                            "textFormat": {
                                "underline": True
                            }
                        }
                    },
                    'fields': 'userEnteredFormat.textFormat.underline'
                }
        }
        return underline_cell_request
    
     
    def align_text(self, cell_range, horizontal, vertical):
        align_text_request = {
            'repeatCell': {
                    'range': cell_range,
                    'cell': {
                        'userEnteredFormat':{
                            "horizontalAlignment": horizontal,
                            "verticalAlignment": vertical
                        }
                    },
                    "fields": "userEnteredFormat.horizontalAlignment,userEnteredFormat.verticalAlignment"
                }
        }

        return align_text_request
    
    
    def bold_font(self, cell_range, bold_range):
        bold_font_request = {
            'updateCells': {
                'range': cell_range,
                'rows': [
                    {'values': [{'textFormatRuns':[
                        {'format': {'bold': True}, 'startIndex': 0},
                        {'format': {'bold': False}, 'startIndex': 12}
                ]}]}],
                'fields': 'textFormatRuns.format.bold'
            }
        }

        return bold_font_request
    
    
    def background_color(self, cell_range, color):
        background_request = {
            'repeatCell': {
                    'range': cell_range,
                    'cell': {
                        'userEnteredFormat':{
                            "backgroundColor": color
                        }
                    },
                    'fields': 'userEnteredFormat.backgroundColor'
                }
        }

        return background_request
    

    def merge_cells(self, cell_range, merge_type):
        merge_request = {
            'mergeCells': {
                'mergeType': merge_type,
                'range': cell_range
            },
        }

        return merge_request
    

    def title_format(self, component):
        requests = []
        cell_range = component["cell_range"]
    
        requests.append(self.merge_cells(cell_range, MERGEALL))
        requests.append(self.background_color(cell_range, colors.LIGHTGRAY))
        requests.append(self.bold_cell(cell_range))

        return {'requests': requests}
    

    def legend_format(self, component):
        requests = []
        requests.append(self.merge_cells(component["cell_range"], MERGEALL))

        return {'requests': requests}
    

    def steps_format(self, component):
        requests = []
        for merge_range in component["merge_ranges"]:
            requests.append(self.merge_cells(merge_range["merge_range"], MERGEALL))
        
        cell_range = component["cell_range"]
        requests.append(self.background_color(cell_range, colors.LIGHTGRAY))
        requests.append(self.bold_cell(cell_range))
        requests.append(self.align_text(cell_range, "CENTER", "MIDDLE"))
        requests.append(self.underline_cell(cell_range))
        
        return {'requests': requests}
    
    
    def phase_column_title_format(self, phases):
        requests = []

        for phase, phase_color in zip(phases, PHASE_COLORS):
            cell_range = phase["cell_range"]
            column_cell_range = phase["column_cell_range"]
            requests.append(self.row_height_request(cell_range['startRowIndex'], cell_range['endRowIndex'], 40))
            requests.append(self.background_color(cell_range, PHASE_COLORS[phase_color]['color']))
            requests.append(self.background_color(column_cell_range, PHASE_COLORS[phase_color]['column_color']))
            requests.append(self.merge_cells(cell_range, MERGEALL))
            requests.append(self.align_text(column_cell_range, "CENTER", "MIDDLE"))
            requests.append(self.bold_cell(cell_range))
            requests.append(self.bold_cell(column_cell_range))
            requests.append(self.underline_cell(cell_range))
            requests.append(self.underline_cell(column_cell_range))
            
        return {'requests': requests}
    
    def service_format(self, service_data):
        requests = []
        phase = service_data["phase"]
        cell_range = service_data["cell_range"]

        if service_data["application_name"] in ["Cyndi", "Insights-Kafka"]:
            requests.append(self.background_color(cell_range, colors.LIGHT_RED))
        elif service_data["services"][0] == "caddy-ubi":
            requests.append(self.background_color(cell_range, colors.CYAN))
        else:
            requests.append(self.background_color(cell_range, PHASE_COLORS[phase]['column_color']))

        if "merge_range" in service_data:
            requests.append(self.merge_cells(service_data["merge_range"], MERGECOLUMNS))
        
        requests.append(self.align_text(cell_range, "CENTER", "MIDDLE"))
        

        return requests

    
    def dropdown_request_builder(self, cell_range, column_letter, row, option, color):
        request  = {
            "addConditionalFormatRule": {
                "rule": {
                    "ranges": [
                        cell_range
                    ],
                    "booleanRule": {
                        "condition": {
                            "type": "CUSTOM_FORMULA",
                            "values": [{"userEnteredValue": f"=${column_letter}${row}=\"{option}\""}]
                        },
                        "format": {
                            "backgroundColor": {"red": color["red"], "green": color["green"], "blue": color["blue"]},
                        }
                    }
                },
                "index": 0
            }
        }

        return request
    
    def drop_down_format(self, dropdowns):
        requests = []
        for dropdown in dropdowns:
            for phase in ["phase_one", "phase_two", "phase_three"]:
                if phase in dropdown:
                    for i in range(dropdown[phase]['startRowIndex'], dropdown[phase]['endRowIndex']+1):
                        if isinstance((dropdown[phase]['startColumnIndex'] and dropdown[phase]['endColumnIndex']), list):
                            for j in range(len(dropdown[phase]['startColumnIndex'])):
                                cell_range = self.cell_range(i-1, i, dropdown[phase]['startColumnIndex'][j], dropdown[phase]['endColumnIndex'][j])
                                column_letter = dropdown["column_letter"][j] 
                                for key, color in dropdown["colors"].items():
                                    requests.append(self.dropdown_request_builder(cell_range, column_letter, i, key, color))
                        else:
                            cell_range = self.cell_range(i-1, i, dropdown[phase]['startColumnIndex'], dropdown[phase]['endColumnIndex'])
                            column_letter = dropdown["column_letter"]
                            for key, color in dropdown["colors"].items():
                                    requests.append(self.dropdown_request_builder(cell_range, column_letter, i, key, color))
            
                    body = {"requests": requests}

        return body
    
     
    def row_height_request(self, start, end, height):
        request = {
            'updateDimensionProperties': {
                'range': {
                    'sheetId': 0,
                    'dimension': 'ROWS',
                    'startIndex': start,
                    'endIndex': end
                },
                'properties': {
                    'pixelSize': height
                },
                'fields': 'pixelSize'
            }
        }
        return request
    
    def format_column_width(self):
        requests = []

        for column in COLUMNS:
            start_index = column["start"]
            end_index = column["end"]
            width = column["width"]
            request = {
                'updateDimensionProperties': {
                    'range': {
                        'sheetId': 0,  
                        'dimension': 'COLUMNS',
                        'startIndex': start_index,  
                        'endIndex': end_index   
                    },
                    'properties': {
                        'pixelSize': width
                    },
                    'fields': 'pixelSize'
                }
            }

            requests.append(request)

        body = {"requests": requests}

        return body