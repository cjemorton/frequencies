# Creating the Frequencies Access Database

Since Access database files (.accdb) are binary files that require Microsoft Access to create properly, this repository provides multiple options for accessing the frequency data.

## Available Database Files

1. **Frequencies.db** - SQLite database (cross-platform, can be opened with many tools)
2. **Frequencies.xlsx** - Excel workbook with categorized worksheets  
3. **frequency_data.csv** - Enhanced CSV file with all frequency data
4. **database_schema.sql** - SQL schema for creating Access database

## Option 1: Use the SQLite Database (Recommended)

The `Frequencies.db` file is a complete SQLite database that can be:
- Opened with DB Browser for SQLite (free)
- Accessed from Python, Java, .NET, and most programming languages
- Imported into Access if needed
- Used with any SQLite-compatible application

### SQLite Query Examples:
```sql
-- Find what service uses a specific frequency
SELECT * FROM Frequencies 
WHERE 146.52 BETWEEN Frequency_Start_MHz AND Frequency_End_MHz;

-- Find all amateur radio bands
SELECT * FROM Frequencies 
WHERE Service_Type = 'Amateur Radio' 
ORDER BY Frequency_Start_MHz;

-- Find frequencies in a range
SELECT * FROM Frequencies 
WHERE Frequency_Start_MHz >= 144 AND Frequency_End_MHz <= 148;
```

## Option 2: Use the Excel Workbook

The `Frequencies.xlsx` file contains:
- **Summary** - Overview of all service types
- **Complete Database** - All frequency data sorted
- **Service-specific sheets** - Separate worksheet for each service type

## Option 3: Create Access Database from SQLite

1. Open Microsoft Access
2. Go to External Data → More → ODBC Database
3. Select "Import the source data into a new table"
4. Choose SQLite ODBC driver
5. Point to the `Frequencies.db` file
6. Import the Frequencies table

## Option 4: Manual Access Database Creation

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

## Database Features

The completed database includes:
- **90+ frequency allocations** across all major services
- **Searchable by frequency range** - find what service uses a specific frequency
- **Categorized by service type** - Amateur Radio, Public Safety, Broadcast, etc.
- **Indexed for fast searches** - optimized for frequency lookups
- **Expandable** - easy to add new frequency allocations

## Data Sources

Frequency data compiled and verified from:
- FCC frequency allocations (CFR Title 47)
- ARRL Amateur Radio band plans
- ITU Radio Regulations
- 3GPP cellular specifications  
- IEEE wireless standards
- NIST time and frequency standards
- ICAO aviation standards
- Public safety frequency databases

---

*The frequency data in this repository has been researched and verified against authoritative sources as of 2024.*
