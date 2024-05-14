#Source: https://stackoverflow.com/questions/53339794/pdfkit-filenotfounderror-python
import pdfkit

if __name__ == "__main__":
    with open("test.html") as f:
        t = pdfkit.from_file(f, False)