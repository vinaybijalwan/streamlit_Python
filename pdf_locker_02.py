import streamlit as st
import io
import PyPDF2

# Define the Streamlit app
def main():
    st.title("PDF Lock")

    # Allow user to upload a PDF file
    uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

    if uploaded_file is not None:
        # Read the uploaded PDF file and create a PDF writer object
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        pdf_writer = PyPDF2.PdfWriter()

        # Prompt the user to enter a password for the PDF file
        password = st.text_input("Enter a password for the PDF file", type="password")

        # Encrypt the PDF file with the entered password
        pdf_writer.append_pages_from_reader(pdf_reader)
        pdf_writer.encrypt(password)

        # Save the encrypted PDF to a byte stream
        output_stream = io.BytesIO()
        pdf_writer.write(output_stream)

        # Allow the user to download the encrypted PDF file
        st.download_button("Download encrypted PDF", output_stream.getvalue(), "encrypted_pdf.pdf")

if __name__ == "__main__":
    main()
