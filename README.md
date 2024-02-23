## Altor Assignment

##### Setting up the environment

Create virtual environment
```
python3 -m virtualenv venv
```
Activate the virtual environment for linux and mac
```
source venv/bin/activate
```
For windows figure out yourself

Install the Requrements
```
pip install -r requirements.txt
```

##### Running the application

Run the application
```
python3 app.py
```

##### Working of the application

Well you run the application and load the index page it will fetch all the data from assignment API and populate our table in config.db<br>

Since in the UI we have many charts which require different set of data depending on the filtering conditions.<br>

Mentioned below are the different endpoints for the same

1. List all the user config data
    
    ` GET table_data/get_all`
    
    Get a list of all the user config data
    
    Parameters:

    - None

    Response:

    ```
    [
        {
        "device_brand": "Realme",
        "name": "user_1",
        "sdk_int": 33,
        "vehicle_brand": "Bajaj",
        "vehicle_cc": "100-125 cc",
        "zone": "Zone_2"
        },
        {
        "device_brand": "Samsung",
        "name": "user_2",
        "sdk_int": 34,
        "vehicle_brand": "Bajaj",
        "vehicle_cc": "100-125 cc",
        "zone": "Zone_1"
        }
    ]
    ```

```
    function FilterComponent() {
    const [filters, setFilters] = useState({
        // Initialize your filter conditions here
        // For example:
        category: '',
        priceRange: '',
        // Add more filter conditions as needed
    });
```