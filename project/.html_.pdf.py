import pdfkit


input_html = 'path_to_input_file.html'  
output_pdf = 'path_to_output_file.pdf'  


pdfkit.from_file(input_html, output_pdf)

print(f"The HTML file has been successfully converted to {output_pdf}")
