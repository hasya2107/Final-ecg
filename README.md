# ECG Dashboard

The ECG Dashboard offers a state-of-the-art solution for detecting cardiac abnormalities in real-time. It continuously monitors and analyzes the patient's heart activity, providing valuable insights on rhythm, heartbeat, and other significant parameters.

![Dashboard Screenshot](ecg.png)  
*Screenshot of the ECG Dashboard*

## Features

- Real-time visualization of ECG data.
- Early identification of conditions such as myocardial infarction, arrhythmia, and other cardiovascular diseases.
- Selectable lead options for tailored viewing.
- Backend integration with a Flask server and a comprehensive ECG database.
- User-friendly front-end interface optimized for healthcare professionals.

## Technology Stack

- **Frontend**: Built using HTML, CSS, and JavaScript.
- **Backend**: Powered by Flask, a Python web framework, and supplemented with libraries like NumPy and WFDB for ECG data extraction and visualization.
- **Data Source**: Utilizes a 12-lead ECG database available from the PhysioNet website.

## Prerequisites

- Python (>=3.6)
- pip
- A modern web browser

## Setup and Installation

### Back-End

1. **Install Python**: Download and install Python from the [official website](https://www.python.org/downloads/).
   
2. **Install Required Python Packages**: Run the command:
   ```bash
   pip install flask wfdb numpy flask_cors

### Front-End

#### Option 1: Using VS Code's Live Server

1. Open the project folder in VS Code.
2. Install the Live Server extension.
3. Right-click index.html and select "Open with Live Server".
   
#### Option 2: Using a Web Browser

1. Locate and double-click index.html in your file explorer.
Note: Ensure related resources, like function.js and style.css, are in the same directory as index.html.

## Usage

1. Ensure the backend Flask server is running.
2. Launch the ECG Dashboard.
3. Use the dropdown menu to select desired ECG leads.
4. Click "Submit" to display the ECG graphs.

## Contributing
For contributions or major changes, please open an issue for discussion.
