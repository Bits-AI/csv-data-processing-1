# Python CSV data processing
This is a lightweight Python script responsible to process "Computation Chain Report" data generated from a third party software to the expected output of the client.

<br />

Problem Statement
======
The client is using a commercial software that gathers the data from their dataloggers that are used to detects and measures the quantity of rainfalls at each location. These dataloggers are installed at multiple locations in Malaysia. The software can process the data as intended and generate them in various time intervals, but the produced outputs in CSV files do not meet their business requirements. As the commercial software does not allow any changes to the format of the data generated, the client needed an easy-to-use tool that helps them to convert the data sets into the desired format.

The workflow and solutions provided
======
Develop a lightweight script that runs on user request, with acceptable processing time and most importantly, easy to use.

- Some folder structures discussed with the client
    - A folder which stores the configuration file, the code and the main executable file. (A .bat file was given because the client is using it in Windows OS, and they want to run the script easily, so I didn't wrapped it into a .exe file.)

    - A folder that lets the user put the file/s that require processing.

    - A folder that lets the user 'collects' the processed file/s.

- Able to process multiple time intervals, they are: 

1. 15 minutes
2. Hourly
3. Daily
4. Monthly
5. Yearly
6. Water Year (I am not sure what is a Water Year...but looks like yearly)

- Show some statistics to indicate that the script is running (Lines processed are displayed).

- Able to configure the prefix of the processed file name. (A configuration file written in .txt is provided)

Requirements
======
Python 3.6 or later (f-Strings is used). No external packages or dependency is required to run the script. [Official Website for Python Downloads](https://www.python.org/downloads/).

Notable Packages and Dependencies used
======

* os - Miscellaneous operating system interfaces for Python. (This is only used to read the configuration file)

* csv - The CSV (Comma Separated Values) handler in Python. (Used to read the CSV files...obviously)

* datetime - The Python module to manipulate dates and times.

Note
======
This is a completed project and the script is sold to the client. Uploaded here for reference purposes.