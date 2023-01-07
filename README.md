
<!--![GitHub repo size](https://img.shields.io/github/repo-size/rtazaki1205/AggScatVIR)-->

# Caveat!
*THIS PACKAGE IS STILL UNDER TESTING. PLEASE WAIT FOR AN OFFICIAL RELEASE*


# *AggScatVIR*

*AggScatVIR* stands for AGGregate SCATtering at Visual and InfraRed wavelengths. This project aims to provide the optical properties of complex-shaped dust particles that can be used to interpret scattered light observations of circumstellar disks (such as protoplanetary disks and debris disks) at visible and near-infrared wavelengths. The database consists of the scattering matrix and opacity of various dust particles studied in Tazaki & Dominik (2022) and Tazaki, Ginski, and Dominik (submitted). A simple python package *aggscatpy* that can be used to analyze the data is provided as well.

Regarding how the database is organized and the basic usage of the python package (*aggscatoy*), please read the [document](https://rtazaki1205.github.io/AggScatVIR/).

# Download and Install

You can download *AggScatVIR* via

    git clone https://github.com/rtazaki1205/AggScatVIR.git

If you would like to use our python package *aggscatpy* that can be used to analyze the database, enter the python directory in the database and run 

    pip install -e .    

# Attribution

If you would like to publish results generated by using *AggScatVIR*, please cite both of the following papers.
 - [Tazaki and Dominik 2022, A&A, 663, 57](https://ui.adsabs.harvard.edu/abs/2022A%26A...663A..57T)
 - Tazaki, Ginski, and Dominik (submitted).

# License
Copyright 2022-2023 Ryo Tazaki

*AggScatVIR* is distributed under the MIT License. See the LICENSE file for the terms and conditions.

# History
*Version 0.0.0* Pre-release
