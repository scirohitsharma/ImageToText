# Image to Text OCR Project

# Overview

This project is a Python-based graphical user interface (GUI) application that extracts text from images using Optical Character Recognition (OCR). The application allows users to select an image, perform OCR to extract printed or handwritten text, and export the extracted text to a text file. The GUI is built using Tkinter, and the OCR functionality is provided by PyTesseract.
Features

**Image Selection**: Users can select image files for OCR processing.
**Thumbnail Display**: Selected images are displayed as thumbnails in the GUI.
**OCR Processing**: Extract text from printed or handwritten images.
**Export Text**: Save the extracted text to a text file.
**Discard Image**: Remove the currently selected image and reset the interface.
**User-Friendly Interface**: Intuitive GUI with easy-to-use controls.
# Requirements

## Hardware

**Processor**: Multi-core processor (Intel i3 or better, AMD Ryzen 3 or better)
**RAM**: Minimum 4 GB (8 GB or more recommended)
**Storage**: At least 500 MB of free disk space
**Graphics**: Integrated graphics card sufficient
**Display**: Monitor with at least 1024x768 resolution
**Input Devices**: Mouse and keyboard

## Software

**Operating System**: Windows 7/8/10/11, macOS 10.14 or later, Linux (Ubuntu 18.04 or later)
**Python Version**: Python 3.6 or later

## Python Libraries

`tkinter` (comes pre-installed with Python)
`Pillow` for image processing (`pip install pillow`)
`pytesseract` for OCR (`pip install pytesseract`)
`opencv-python` for additional image processing (`pip install opencv-python`)
`numpy` for array operations (`pip install numpy`)

## Tesseract-OCR

**Installation**: Tesseract-OCR must be installed separately. [Installation Instructions](https://github.com/tesseract-ocr/tesseract)
**Configuration**: Set the path to the Tesseract executable in the code.

## Text Editor or IDE

 Visual Studio Code (VS Code), PyCharm, Sublime Text, Atom, or any other preferred editor.
