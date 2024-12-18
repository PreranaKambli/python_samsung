import pandas as pd

# Function to create HTML files from the template with student data
def create_html_from_template(name, usn, template_file, output_file):
    # Read the template HTML file
    with open(template_file, "r") as template:
        content = template.read()
    
    # Replace placeholders with actual student data
    content = content.replace("{{name}}", name)
    content = content.replace("{{usn}}", usn)
    
    # Save the populated HTML content to a new HTML file
    with open(output_file, "w") as new_file:
        new_file.write(content)
    
    print(f"Generated HTML file: {output_file}")

# Function to process the Excel or CSV file
def process_student_data(file_path, template_file):
    # Read data from the Excel or CSV file
    try:
        if file_path.endswith(".csv"):
            df = pd.read_csv(file_path)
        elif file_path.endswith(".xlsx"):
            df = pd.read_excel(file_path)
        else:
            print("Unsupported file format. Please provide a CSV or Excel file.")
            return
        
        # Loop through each row in the dataframe
        for _, row in df.iterrows():
            name = row['Name']
            usn = row['USN']
            
            # Create the HTML file name (e.g., USN_certificate.html)
            html_filename = f"{usn}_certificate.html"
            
            # Create the HTML file with the student data
            create_html_from_template(name, usn, template_file, html_filename)
    
    except FileNotFoundError:
        print(f"Error: {file_path} not found. Please ensure the file exists.")
    except KeyError:
        print("Error: The input file must contain 'Name' and 'USN' columns.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Main function to run the program
def main():
    # Path to the Excel or CSV file
    file_path = input("Enter the path to the Excel or CSV file (e.g., students.csv): ")
    
    # Path to the template HTML file
    template_file = "template.html"  # Make sure this file exists
    
    # Process the student data and create the HTML files
    process_student_data(file_path, template_file)

# Run the main program
if __name__ == "__main__":
    main()
