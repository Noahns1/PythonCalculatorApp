# dockerfile, Image, Container

# Specify we're using python and the version
FROM python:3.9

# Adding our main file into the container
ADD main.py .

# Install libraries tkinter & numpy
# note: docker accepted "tk" not "tkinter"
RUN pip install requests tk numpy

# Command to run main.py
CMD ["python", "./main.py"]
