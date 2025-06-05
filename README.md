# LALR Parsing Table Generator

## Overview
This project provides a **LALR Parsing Table Generator** with a **Streamlit-based frontend**. It allows users to upload transition and CLR state files to generate and visualize an LALR parsing table. This project was implemented as part of the course requirements for Compiler Design in our academic curriculum.
Deployed at- https://lalrparser.streamlit.app/

## Features
- Upload **Transitions** and **CLR States** text files.
- Parse the files to extract the transition table and CLR states.
- Generate and display the **LALR Parsing Table**.
- Expandable sections to view CLR states and lookaheads.
- Download the generated parsing table as a CSV file.

## Technologies Used
- **Python** for backend processing
- **Streamlit** for the frontend interface
- **Pandas** for data handling

## File Descriptions
### 1. Frontend Code (`app.py`)
Contains the Streamlit UI to:
- Upload files
- Parse and process the input files
- Display the LALR parsing table
- Provide options for downloading the output

### 2. Transition File (`transitions.txt`)
Defines state transitions in **key-value** pairs, where each state maps to possible transitions.

Example:
```plaintext
0|{'S': 1, 'C': 2, 'c': 3, 'd': 4}
2|{'C': 5, 'c': 6, 'd': 7}
```

### 3. CLR States File (`clr_states.txt`)
Defines the **canonical LR(1) states** along with lookaheads.

Example:
```plaintext
0|["S' -> • S", "S -> • C C", "C -> • c C", "C -> • d"]|[{'$'}, {'$'}, {'c', 'd'}, {'c', 'd'}]
1|["S' -> S •"]|[{'$'}]
```

## Installation and Setup
### Prerequisites
- Python 3.x
- Streamlit (`pip install streamlit`)
- Pandas (`pip install pandas`)

### Steps to Run the Application
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/LALR-Parsing-Table-Generator.git
   cd LALR-Parsing-Table-Generator
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the Streamlit app:
   ```sh
   streamlit run app.py
   ```

## Usage
1. Upload **Transitions** and **CLR States** files.
2. View the generated LALR parsing table.
3. Expand individual CLR states to inspect lookaheads.
4. Download the parsing table as a CSV file.

## Future Enhancements
- Implement **error handling** for invalid input files.
- Add **automated parsing validation**.
- Support for **visualizing the parsing steps**.

## Contributors
- **Mayuri Barapatre** - [GitHub](https://github.com/mayuri06b)
- **Shinosha Jain** - [GitHub](https://github.com/srj2005)
- **Vaishnavi Paswan** - [GitHub](https://github.com/vaishnavipaswan)

## License
This project is licensed under the MIT License - see the LICENSE file for details.

