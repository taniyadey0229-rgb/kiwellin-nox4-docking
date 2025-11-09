import pandas as pd
import os

# --- Configuration ---
# Define the name of the Excel file to read
RESULTS_FILE = 'Docking_Score_Kiwi.xlsx'

# Define the protein we are looking for
TARGET_PROTEIN = 'NOX4'

# Define the docking program column to check
DOCKING_COLUMN = 'ClusPro'
# --- End of Configuration ---

def analyze_scores(file_path):
    """
    Reads the docking results from an Excel file, cleans the data,
    and finds the score for the target protein.
    """
    print(f"--- Starting Analysis of {file_path} ---")

    # Check if the file exists
    if not os.path.exists(file_path):
        print(f"Error: Cannot find the file '{file_path}'.")
        print("Please make sure the Excel file is in the same directory.")
        return

    try:
        # Read the Excel file. 
        # We use 'header=7' because the first 7 rows are empty/headers.
        # Note: In Excel, row 8 is index 7 for pandas.
        df = pd.read_excel(file_path, header=7)

        print("\nSuccessfully loaded data:")
        print(df.head()) # Print the first few rows to check

        # Clean the column names (remove any leading/trailing spaces)
        df.columns = df.columns.str.strip()

        # Find the row that contains our target protein
        # We rename the 'Unnamed: 3' column to 'Protein' for easier access
        df.rename(columns={'Unnamed: 3': 'Protein'}, inplace=True)

        # Find the specific row for our target
        target_row = df[df['Protein'] == TARGET_PROTEIN]

        if target_row.empty:
            print(f"\nError: Could not find '{TARGET_PROTEIN}' in the 'Protein' column.")
            return

        # Get the score from the CLUSPRO column
        score = target_row[DOCKING_COLUMN].values[0]

        print("\n--- 🔬 Analysis Complete ---")
        print(f"Target Protein: {TARGET_PROTEIN}")
        print(f"Docking Server: {DOCKING_COLUMN}")
        print(f"Best Score: {score}")
        print("------------------------------")

    except Exception as e:
        print(f"\nAn error occurred while processing the file: {e}")
        print("Please check that the file format and column names are correct.")


# --- Run the analysis ---
if __name__ == "__main__":
    analyze_scores(RESULTS_FILE)
