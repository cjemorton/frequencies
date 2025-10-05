-- Frequency Database Schema for Microsoft Access
-- This script creates the table structure for the frequency database

CREATE TABLE Frequencies (
    ID AUTOINCREMENT PRIMARY KEY,
    Band TEXT(20) NOT NULL,
    Frequency_Start_MHz DOUBLE NOT NULL,
    Frequency_End_MHz DOUBLE NOT NULL,
    Wavelength TEXT(20),
    Primary_Use TEXT(100),
    Service_Type TEXT(30),
    DateAdded DATETIME DEFAULT NOW(),
    Notes MEMO
);

-- Index for faster searching
CREATE INDEX idx_frequency_range ON Frequencies (Frequency_Start_MHz, Frequency_End_MHz);
CREATE INDEX idx_service_type ON Frequencies (Service_Type);
CREATE INDEX idx_band ON Frequencies (Band);

-- Sample queries for the database:

-- Find all frequencies in a specific range
-- SELECT * FROM Frequencies WHERE ? BETWEEN Frequency_Start_MHz AND Frequency_End_MHz;

-- Find all amateur radio bands
-- SELECT * FROM Frequencies WHERE Service_Type = "Amateur Radio" ORDER BY Frequency_Start_MHz;

-- Find all public safety frequencies
-- SELECT * FROM Frequencies WHERE Service_Type = "Public Safety" ORDER BY Frequency_Start_MHz;

-- Instructions for use:
-- 1. Create a new Access database
-- 2. Import the frequency_data.csv file
-- 3. Run this SQL to create proper indexes and relationships
-- 4. The database will be ready for frequency lookups and analysis