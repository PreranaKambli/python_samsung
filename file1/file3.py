def create_html_file_from_template():
    # Step 1: Get the name of the file from the user
    file_name = input("Enter the name for the new HTML file (with .html extension): ")
    
    try:
        # Step 2: Read the content from 'template.html'
        with open("template.html", "r") as template_file:
            template_content = template_file.read()
        
        # Step 3: Create a new HTML file with the user-provided name and write the content
        with open(file_name, "w") as new_file:
            new_file.write(template_content)
        
        print(f"The new HTML file '{file_name}' has been created successfully!")
    
    except FileNotFoundError:
        print("Error: 'template.html' not found. Please ensure the template file exists in the same directory.")

# Run the function to create the HTML file
create_html_file_from_template()
