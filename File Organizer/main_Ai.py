import os
import shutil

# Ask the user for confirmation before proceeding
ask = input("Do you want to move all PDFs from Downloads to a new folder on your Desktop? (yes/no): ").strip().lower()

if ask == 'yes':
    # 1. Define the path to your Downloads folder
    # Using os.path.expanduser('~') is a robust way to get the user's home directory
    source_path = os.path.join(os.path.expanduser('~'), "Downloads")

    # 2. Define the path for the new folder on the Desktop
    destination_folder = os.path.join(os.path.expanduser('~'), "Desktop", "All PDFs")

    # 3. Create the destination folder on the Desktop if it doesn't already exist
    # This prevents errors if you run the script more than once.
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
        print(f"Created folder: {destination_folder}")

    # 4. Loop through all the files in the Downloads folder
    try:
        files_found = False
        for file_name in os.listdir(source_path):
            # Check if the file is a PDF
            if file_name.lower().endswith(".pdf"):
                files_found = True
                # Create the full path for the source file
                source_file = os.path.join(source_path, file_name)
                
                # Move the file to the new "All PDFs" folder on the Desktop
                shutil.move(source_file, destination_folder)
                print(f"Moved: {file_name}")

        if not files_found:
            print("No PDF files were found in the Downloads folder.")

    except FileNotFoundError:
        print(f"Error: The source directory was not found: {source_path}")
    
    print("\nPDF organization complete!")
else:
    print("Operation cancelled.")

