# A MongoDB jobmanager for the pygeoapi

## Overview
This repositoty contains a jobmanager for the [pygeoapi](https://pygeoapi.io/) which employs [MongoDB](https://www.mongodb.com/cloud/atlas/lp/try4?utm_source=bing&utm_campaign=search_bs_pl_evergreen_atlas_core_prosp-brand_gic-null_emea-de_ps-all_desktop_eng_lead&utm_term=mongodb&utm_medium=cpc_paid_search&utm_ad=e&utm_ad_campaign_id=415204543&adgroup=1214960818277975&msclkid=7356def9446915fcc7bcbd41669ea71e). The pygeoapi offers a default jobmanager which employs TinyDB. TinyDB is not specifically build for usage in web applications. For example TinyDB does [not guarantee ACID](https://tinydb.readthedocs.io/en/latest/intro.html#why-not-use-tinydb) under all conditions.

## Setup
In order to use the MongoDB jobmanager some requirements need to be installed. The Python package ```pymongo``` is used to access a MongoDB instance via Python. A MongoDB instance must be running as well. In order to enable the usage of the MongoDB jobmanager some steps need to be performed. Details about the configuration of the pygeoapi can be found in the [documentation](https://docs.pygeoapi.io/en/stable/index.html).

Step 1: Copy the ```mongodb_.py``` into the ```process/manager``` directory of the pygeoapi.
 
Step 2: Add the following to manager section the .config of the pygeoapi:
```
manager:  # optional OGC API - Processes asynchronous job management
      name: MongoDB # plugin name (see pygeoapi.plugin for supported process_manager's)
      connection: CONNECTION_URI_OF_MONGODB_INSTANCE # connection info to store jobs (e.g. filepath)
      output_dir: DIRECTORY_FOR_RESULTS  # temporary file area for storing job results (files)
```

Step 3: Add the following to the plugin.py ```PLUGINS``` section of the pygeoapi:
```
'process_manager': {
        'TinyDB': 'pygeoapi.process.manager.tinydb_.TinyDBManager',
        'MongoDB': 'pygeoapi.process.manager.mongodb_.MongoDBManager'
    }
 ```
