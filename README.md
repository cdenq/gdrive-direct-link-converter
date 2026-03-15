<img src="assets/tofu.png" width="100">

# Google Drive Link Converter

A simple Streamlit app to convert Google Drive sharing links into direct download links.

Paste comma-separated Google Drive links, click Convert, and get direct download links that can be used for batch downloads or sharing. I made this for ease of mass importing assets to Tabletop Simulator.

## Usage

1. Paste your Google Drive links in the input box (comma-separated).
2. Click "Convert".
3. The converted direct download links will appear in the output box and be automatically copied to your clipboard.
4. Use the "Copy to Clipboard" button if needed again.

## Local Installation

1. Clone the repository:
```bash
git clone https://github.com/cdenq/gdrive-direct-link-converter.git
cd gdrive-direct-link-converter
```

2. Create a new conda environment:
```bash
conda create --name dl_gdrive
conda activate dl_gdrive
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the app locally:
```bash
streamlit run app.py
```

## Project Structure

```
gdrive-direct-link-converter/
├── app.py                   # Main application entry point
├── config/
│   └── settings.py          # Configuration constants
├── src/
│   └── pages/
│       └── home.py          # Home page with converter
├── assets/
│   └── icons/
│       └── tofu.png         # App logo
├── requirements.txt         # Python dependencies
└── README.md                # This file
```