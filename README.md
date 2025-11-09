# Kiwellin-NOX4 Docking Project

> Explored Kiwellin’s bioactive properties through protein-protein docking with NOX4 using AutoDock and CLUSPRO, identifying therapeutic potential for oxidative stress-related diseases, enhancing drug discovery for myocardial infarction, metabolic syndromes, and autoimmune conditions.

---

## Methodology

This project aimed to determine the binding affinity between the Kiwellin protein (ligand) and the NOX4 protein (receptor), which is implicated in oxidative stress.

* **Protein Structures:** 3D structures for both proteins (`KIWELLIN.pdb` and `NOX4.pdb`) were obtained.
* **Docking Server:** The protein-protein docking simulation was performed using the **CLUSPRO** web server.

## 🏁 Results

The docking simulation successfully predicted the binding interactions between Kiwellin and NOX4.

The top-ranked model (Model 0), which represented the largest and most favorable cluster, showed a **Weighted Score of -717.3**. This strong negative score suggests a stable and favorable binding interaction, supporting the hypothesis that Kiwellin may interact with NOX4.

## 📁 Project Data

* **`/protein_structures`**: This folder contains the input `.pdb` files for Kiwellin and NOX4.
* **`Docking_Score_Kiwi.xlsx`**: Excel sheet containing initial docking score analysis.
* **`Kiwellin.xlsx`**: Excel sheet containing background research on Kiwellin.
* **`analyze_results.py`**: A Python script to parse the results from the Excel file.

---

## 💻 Setup and Running the Analysis

This repository includes a Python script (`analyze_results.py`) to parse the docking score data from the Excel file.

### 1. Download the Project

* Click the green **"<> Code"** button at the top of this page.
* Select **"Download ZIP"**.
* Unzip the downloaded folder to your computer.

### 2. Install Dependencies

This script requires Python 3 and the `pandas` and `openpyxl` libraries.

1.  Make sure you have [Python 3](https://www.python.org/downloads/) installed.
2.  Open your terminal or command prompt.
3.  Install the required libraries using pip:

```bash
pip install pandas openpyxl
