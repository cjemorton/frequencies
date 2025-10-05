# Creating the Frequencies Access Database

Since Access database files (.accdb) are binary files that require Microsoft Access to create properly, this repository provides the data and schema needed to create the database.

## Files Provided

1. **frequency_data.csv** - Complete frequency data in CSV format
2. **database_schema.sql** - SQL schema for creating the database structure
3. **README.md** - Complete frequency reference documentation

## How to Create the Access Database

### Step 1: Create New Database
1. Open Microsoft Access
2. Create a new blank database
3. Save it as "Frequencies.accdb"

### Step 2: Import Data
1. Go to External Data → Text File
2. Select "frequency_data.csv"
3. Choose "Import the source data into a new table"
4. Follow the Import Text Wizard:
   - Choose "Delimited"
   - Select "Comma" as delimiter
   - Check "First Row Contains Field Names"
   - Set appropriate data types for each field

### Step 3: Apply Schema
1. Open the imported table in Design View
2. Set the ID field as AutoNumber and Primary Key
3. Apply the indexes as specified in database_schema.sql
4. Add any additional fields (DateAdded, Notes) as needed

### Step 4: Create Queries
Use the sample queries in database_schema.sql to create useful views:
- Frequency range lookup
- Service type filtering
- Band-specific searches

## Database Features

The completed database will include:
- **45+ frequency bands** across all services
- **Searchable by frequency range** - find what service uses a specific frequency
- **Categorized by service type** - Amateur Radio, Public Safety, Broadcast, etc.
- **Indexed for fast searches** - optimized for frequency lookups
- **Expandable** - easy to add new frequency allocations

## Usage Examples

Once created, you can:
- Look up what service uses 146.520 MHz (2m simplex)
- Find all amateur radio HF bands
- Identify public safety frequencies in your area
- Research broadcast allocations
- Plan frequency coordination for events

## Data Sources

Frequency data compiled from:
- FCC frequency allocations
- Amateur radio band plans
- Public safety frequency databases
- Commercial broadcast allocations
- Satellite frequency coordination

---

*For the actual binary .accdb file, please follow the instructions above to create it from the provided CSV data.*