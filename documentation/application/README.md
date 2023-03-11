The specification given is to create a CLI application. However, I built a web-based application to make it easier for reviewers to try the modules that have been built.

web application built using django (fullstack framework for python). This application is divided into 4 major modules, namely:
- modul wrapper (Utility/wrapper.py) : provide functions - functions for data processing
- url (komoditas_ikan/urls.py) : application routing
- controller (komoditas_ikan/views.py) : controller for the application
- view (komoditas/templates/index.html) : view for the application

In this application, the use of the functions in the wrapper module is used entirely. You can try all the features at the same time. However, the filter will only work for the last action. The list of features in this application is as follows:
- Get Schema
- Get All Data
- Get Data By Id
- Get Data By Column Value
- Filter Data by Range
- Get Max Value
- Get Max Value by Range (Timestamp)
- Get Min Value
- Get Min Value by Range (Timestamp)