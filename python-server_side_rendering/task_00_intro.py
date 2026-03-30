import sys

def generate_invitations(template, attendees):
    """
    Generate personalized invitation files from a template and list of attendees.
    
    Args:
        template (str): The template string with placeholders
        attendees (list): List of dictionaries containing attendee information
    """
    # Check input types
    if not isinstance(template, str):
        error_message = f"Error: Template must be a string, got {type(template).__name__}"
        print(error_message, file=sys.stderr)
        return
    
    if not isinstance(attendees, list):
        error_message = f"Error: Attendees must be a list, got {type(attendees).__name__}"
        print(error_message, file=sys.stderr)
        return
    
    # Check if attendees list contains dictionaries
    if attendees and not all(isinstance(attendee, dict) for attendee in attendees):
        error_message = "Error: All items in attendees list must be dictionaries"
        print(error_message, file=sys.stderr)
        return
    
    # Handle empty template
    if not template.strip():
        error_message = "Template is empty, no output files generated."
        print(error_message, file=sys.stderr)
        return
    
    # Handle empty attendees list
    if not attendees:
        error_message = "No data provided, no output files generated."
        print(error_message, file=sys.stderr)
        return
    
    # Process each attendee
    for index, attendee in enumerate(attendees, start=1):
        processed_template = template
        
        # List of placeholders to replace
        placeholders = ['name', 'event_title', 'event_date', 'event_location']
        
        # Replace each placeholder
        for placeholder in placeholders:
            placeholder_text = f"{{{placeholder}}}"
            value = attendee.get(placeholder, "N/A")
            
            # Handle None values
            if value is None:
                value = "N/A"
            
            processed_template = processed_template.replace(placeholder_text, str(value))
        
        # Create output file
        filename = f"output_{index}.txt"
        
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(processed_template)
        except Exception as e:
            print(f"Error writing file {filename}: {e}", file=sys.stderr)
