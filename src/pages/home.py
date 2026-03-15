# ----------------------------------
# IMPORTS
# ----------------------------------
import streamlit as st
import streamlit.components.v1 as components
from config.settings import TOFU_IMAGE

# ----------------------------------
# FUNCTIONS
# ----------------------------------
def convert_links(text):
    # Replace ", " with newline
    text = text.replace(", ", "\n")
    # Replace "file/d/" with "uc?export=download&id="
    text = text.replace("file/d/", "uc?export=download&id=")
    # Remove "/view?usp=drive_link"
    text = text.replace("/view?usp=drive_link", "")
    return text

def copy_to_clipboard(text):
    components.html(
        f"""
        <button onclick="copyToClipboard()">Copy to Clipboard</button>
        <script>
        function copyToClipboard() {{
            navigator.clipboard.writeText(`{text.replace('`', '\\`')}`);
            alert("Copied to clipboard");
        }}
        </script>
        """,
        height=50
    )

# ----------------------------------
# RENDER MAIN
# ----------------------------------
def render():
    st.image(str(TOFU_IMAGE), width=150)
    st.title("Google Drive Link Converter")
    st.markdown("Paste your comma-separated Google Drive links below and click Convert.")

    input_text = st.text_area("Input Links:", height=200, placeholder="https://drive.google.com/file/d/123/view?usp=drive_link, https://drive.google.com/file/d/456/view?usp=drive_link")

    if st.button("Convert"):
        if input_text.strip():
            converted = convert_links(input_text)
            st.text_area("Converted Links:", value=converted, height=200)
            copy_to_clipboard(converted)
            # Auto copy to clipboard
            components.html(
                f"""
                <script>
                navigator.clipboard.writeText(`{converted.replace('`', '\\`')}`);
                </script>
                """,
                height=10
            )
            st.success("Converted links have been copied to your clipboard!")
        else:
            st.warning("Please paste some links first.")
