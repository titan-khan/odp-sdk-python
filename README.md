<a href="https://www.oceandata.earth/">
    <img src="https://raw.githubusercontent.com/C4IROcean/odp-sdk-python/master/docs/source/img/odp-favicon-rgb-blueandwhite.png" alt="ODP logo" title="ODP" align="right" height="100" />
</a>

# Python SDK for The Ocean Data Platform (ODP)

Connect to the Ocean Data Platform with Python through the Python SDK. Download queried ocean data easily and efficiently into data frames, for easy exploring and further processing in your data science project.

This is an extensions package to the Cognite Python SDK.

## Documentation

[ODP Python SDK Documentation](https://odp-sdk-python.readthedocs.io/en/master/)

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the Ocean Data Platform Python SDK.

```bash
pip3 install odp_sdk
```
 
## Usage

*Note: Accessing the Ocean Data Platform requires a personal api-key. Contact ODP to require one.*

Import the Ocean Data Platform SDK 
```python
from odp_sdk import ODPClient
```
Connect to the platform
```python
client = ODPClient(api_key='your_personal_api_key_from_ODP')
```
Get dataframe of ocean data samples (casts) within search criteria

Basic usage:
```python
df=client.casts(longitude=[8,12],
                latitude=[56,60],
                timespan=['2019-06-01','2019-06-07']) 
```

Basic usage with more options (Specifying the parameters of interest and removing flagged data):
```python
df=client.casts(longitude=[8,12],
                latitude=[56,60],
                timespan=['2018-06-01','2018-08-31'],
                parameters=['date','lon','lat','z','Temperature','Oxygen','Salinity'],
                n_threads=35,
                include_flagged_data=False)
```


## Utility Functions
Utility functions available in the Example folder are not included in the pip install package and have to be downloaded separately.

Examples/UtilityFunctions.py include useful features for interpolating and plotting, and also include functions for plotting aspects of data coverage, distributions, cast breakdowns. 

In order to use UtilityFunctions.py, certain packages are necessary. Please see the README in the Examples folder for instructions.

## Jupyter Notebook Examples 
Example notebooks are found in the Example folder, which includes:
- Basic data retrieaval from ODP
- Download data, plot the casts and create a gridded map of surface temperatures 
- Analyzing temperature trends
- Example Notebook Data Coverage shows how functions from DataStatsFunctions.py can help users understand the data they download from the odp_sdk
- Example Notebook Data Exploration shows how users can explore the data they pull from the WOD (i.e. plot temperature over time)
- Example Notebook Marine Regions shows how users can join Marine Regions data to the WOD data

## World Ocean Database
The data available through the Python SDK is gathered from the World Ocean Database. The World Ocean Database which is a National Centers for Environmental (NCEI) product and International Oceanographic Data and Information Exchange (IODE) project which provides a composite of publicly available ocean profile data, both historic and recent. It consists of over thousands of datasets consisting of millions of water temperatures, salinity, oxygen, and nutrient profiles (1,2).

## Data Organization in WOD and definitions

Cast: A set of one or more profiles taken concurrently or nearly concurrently. All casts from similar instruments with similar resolutions are grouped together. For example, all bathythermograph (BT) data are all part of the same data set (MBT), see below. 

Profile: A set of measurements for a single variable (i.e. temperature salinity) along a specific path, which could be vertically in the water column, horizontally along the surface, or discrete areas based on placement of buoys. 

## Data Description
The data available through the Ocean Data Platform are oceanographic measurements of physical and chemical ocean parameters (temperature, salinity, oxygen, nitrate, ph and chlorophyll), and is based on the data available through NOAA's World Ocean Database. Each cast has a sepcified latitude, longitude and time (lat, lon and datetime), and a depth profile, where each depth has measured physical and chemical parameters. Not all casts have all the the different ocean parameters, missing measurements are populated with nans. Each measurements has a WODflag parameter (i.e Nitrate_WODflag). If flag value is zero, there are no known issues with the measured value. 



Parameter|	      Unit
--- | --- 
lon/lat |        deg
Z|               m             
Oxygen|	        µmol/kg 
Temperature|	    C
Salinity|	      1e-3
Nitrate|	        µmol/kg
Chlorophyll|    µgram/l
Pressure|dbar

Dataset code | Dataset include
--- | --- 
OSD| Ocean Station Data, Low-resolution CTD/XCTD, Plankton data
CTD| High-resolution Conductivity-Temperature-Depth / XCTD data
MBT| Mechanical / Digital / Micro Bathythermograph data
XBT| Expendable Bathythermograph data
SUR| Surface-only data
APB| Autonomous Pinniped data
MRB| Moored buoy data
PFL| Profiling float data
DRB| Drifting buoy data
UOR| Undulating Oceanographic Recorder data
GLD| Glider data

See [WORLD OCEAN DATABASE 2018 User’s Manual](https://rda.ucar.edu/datasets/ds285.0/docs/WOD18-UsersManual_final.pdf) for more information about the datasets

## Data Quality Flag Descriptions

https://www.nodc.noaa.gov/OC5/WOD/CODES/Definition_of_Quality_Flags.html

References:
1.	Boyer, T.P., O.K. Baranova, C. Coleman, H. E., Garcia, A. Grodsky, R.A. Locarnini, A. V., Mishonov, C.R. Paver, J.R. Reagan, D. S. & I.V. Smolyar, K.W. Weathers,  and M. M. Z. World Ocean Atlas 2018, Volume 1: Temperature. Tech. Ed. NOAA Atlas NESDIS 87 (2018).
2.	Boyer, T. P. et al. World Ocean Database 2018. NOAA Atlas NESDIS 87 (2018).

