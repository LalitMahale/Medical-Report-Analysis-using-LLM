class Prompts:

    def __init__(self) -> None:
        pass

    def final_prompt():
        return """
        You are a doctor explaining a patient's medical report in simple, easy-to-understand language. Focus only on the areas of concern and explain the health issues, if any, and provide natural suggestions to improve the condition.

        Here is the report:

        Report: {json_data}

        Based on the above report, explain only the report do not give patient details and provide natural remedies or ways to heal.
        """


    def text_json_prompt():
        return """
        You are an expert in text comprehension. Your task is straightforward: understand the provided text and return the output in the specified JSON format.

        Text: {text}

        Output: Please provide the output in the following JSON format:

        {{
        "patient_name": "<patient name>",
        "lab_no": "<lab number>",
        "lab_name": "<laboratory name>",
        "collection_date_time": "<sample collection date and time>",
        "reported_date_time": "<report date and time>",
        "test_name": "<test name>",
        "patient_age": "<patient age>",
        "patient_gender": "<patient gender>",
        "Report": {{
            "<investigation name>": {{
            "result": "<result value>",
            "reference_value": "<reference range>",
            "unit": "<unit of measurement>"
            }}
        }}
        }}
        """
