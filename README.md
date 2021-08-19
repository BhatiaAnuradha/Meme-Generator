# Meme-Generator

This is an application to generate memes given an image and a quote. The quotes along with their authors can be read in via .pdf, .txt, .docx or .csv. A quote can be inserted manually as well via the command line.

### General Overview

The application will parse files and extract quotes and authors, adding them to an image to generate a meme. Files with the following extensions can be used as inputs: csv, docx, txt and pdf. Images will be loaded, resized and a caption written across at a random location. The application can be run via Flask as well as the command line. 

### Folders in the Project

*_data*: contains folders SimpleLines, DogQuotes with various documents containing quotes, a fonts folder and an images folder

*templates*: HTML files for the web service interface

*QuoteEngine*: The module contains the IngestorInterface abstract base class which enables data extraction from the document files as listed above. The folder also contains the PDFIngestor, CSVIngestor, TextIngestor and DocxIngestor. The __init__.py file imports all the classes and functions. 

*MemeEngine*: This module contains the MemeEngine class which processes the images and inserts the quotes. 

### Setting Up and Running the Program

The application needs several libraries as listed below:

*  *sys*
*  *subprocess*
*  *random*
*  *requests*
*  *typing*
*  *argparse*
*  *os*

Along with the above mentioned Python libraries, the following libraries were installed using `<pip>`:
* *python-docx*
* *pandas*
* *numpy*
* *Pillow*
* *Flask*
* *xpdf*

To run the application via flask:
`export FLASK_APP = app.py`
`flask run --host 0.0.0.0 --port 3000`

To run the application via command line:
`python3.7 meme.py --body quote --author author --path path_to_image`

