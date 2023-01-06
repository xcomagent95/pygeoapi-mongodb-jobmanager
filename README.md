# A MongoDB jobmanager for the pygeoapi

## Overview
This repositoty contains a jobmanager for the pygeoapi which employs [MongoDB](https://www.mongodb.com/cloud/atlas/lp/try4?utm_source=bing&utm_campaign=search_bs_pl_evergreen_atlas_core_prosp-brand_gic-null_emea-de_ps-all_desktop_eng_lead&utm_term=mongodb&utm_medium=cpc_paid_search&utm_ad=e&utm_ad_campaign_id=415204543&adgroup=1214960818277975&msclkid=7356def9446915fcc7bcbd41669ea71e). The pygeoapi offers a default jobmanager which employs TinyDB. TinyDB is not specifically build for usage in web application. For example TinyDB does [not guarantee ACID](https://tinydb.readthedocs.io/en/latest/intro.html#why-not-use-tinydb) under all conditions.

## Setup
In order to use the MongoDB jobmanager some requirements need to be installed. They can be found in the ```requirements.txt```. A MongoDB instance must be running as well. In order to enable the usage of the MongoDB jobmanager some steps need to be performed. 

Step 1: Copy the ```mongodb_.py``` into the ```process/manager``` directory of the pygeoapi.
 
