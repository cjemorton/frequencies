#!/usr/bin/env python3
"""
Generate comprehensive README.md with complete frequency information.
"""

import csv
from enhance_frequency_data import get_enhanced_frequency_data

def generate_comprehensive_readme():
    """Generate a comprehensive README with all frequency data."""
    
    data = get_enhanced_frequency_data()
    
    # Group data by service type
    service_groups = {}
    for entry in data:
        service = entry['Service_Type']
        if service not in service_groups:
            service_groups[service] = []
        service_groups[service].append(entry)
    
    # Sort each group by frequency
    for service in service_groups:
        service_groups[service].sort(key=lambda x: x['Frequency_Start_MHz'])
    
    readme_content = """# Frequency Reference Database

A comprehensive, verified reference database containing frequency allocations, band plans, and technical specifications for radio frequency applications across all services. This database contains **91 verified frequency allocations** researched from authoritative sources including the FCC, ITU, ARRL, IEEE, and other standards organizations.

## Repository Contents

This repository contains complete frequency reference data in multiple formats:

### Database Files
- **frequency_data.csv**: Complete frequency data (91 entries) in CSV format for database import
- **Frequencies.db**: SQLite database with indexed tables for fast frequency lookups
- **Frequencies.xlsx**: Excel workbook with categorized worksheets for each service type
- **database_schema.sql**: SQL schema for creating custom databases

### Documentation
- **README.md**: Complete frequency reference data with technical details (this file)
- **ACCESS_DATABASE_INSTRUCTIONS.md**: Multiple options for database access and creation

### Generation Scripts
- **enhance_frequency_data.py**: Source data with verification against authoritative sources
- **generate_databases.py**: Automated database and spreadsheet generation

## Complete Frequency Allocations

"""

    # Add each service type section
    service_type_order = [
        'Amateur Radio',
        'Broadcast', 
        'Public Safety',
        'Aviation',
        'Marine',
        'Citizens Band',
        'Personal Radio',
        'WiFi',
        'ISM',
        'Cellular',
        'GPS',
        'Satellite',
        'Time Standard',
        'Emergency',
        'Personal Area Network'
    ]
    
    for service_type in service_type_order:
        if service_type not in service_groups:
            continue
            
        entries = service_groups[service_type]
        
        readme_content += f"\n## {service_type}\n\n"
        
        if service_type == 'Amateur Radio':
            readme_content += """Amateur radio frequency allocations in the United States as defined by FCC Part 97 and coordinated with the ARRL band plans. These frequencies are allocated for amateur radio operators holding valid FCC licenses.

### HF Amateur Bands (High Frequency: 3-30 MHz)

The HF bands provide long-distance communication capabilities through ionospheric propagation. Band conditions vary with solar cycle, time of day, and season.

"""
            # Create separate tables for HF and VHF/UHF
            hf_bands = [e for e in entries if e['Frequency_End_MHz'] <= 30]
            vhf_uhf_bands = [e for e in entries if e['Frequency_Start_MHz'] > 30 and 'simplex' not in e['Band'].lower()]
            simplex_freqs = [e for e in entries if 'simplex' in e['Band'].lower()]
            
            if hf_bands:
                readme_content += "| Band | Frequency Range | Wavelength | Primary Use |\n"
                readme_content += "|------|----------------|-------------|-------------|\n"
                for entry in hf_bands:
                    if entry['Frequency_Start_MHz'] == entry['Frequency_End_MHz']:
                        freq_range = f"{entry['Frequency_Start_MHz']:.3f} MHz"
                    else:
                        freq_range = f"{entry['Frequency_Start_MHz']:.3f} - {entry['Frequency_End_MHz']:.3f} MHz"
                    readme_content += f"| {entry['Band']} | {freq_range} | {entry['Wavelength']} | {entry['Primary_Use']} |\n"
            
            readme_content += "\n### VHF/UHF Amateur Bands (Very High Frequency: 30 MHz and above)\n\n"
            readme_content += "VHF and UHF bands provide reliable local and regional communication, with some bands offering weak-signal propagation modes and satellite communication.\n\n"
            
            if vhf_uhf_bands:
                readme_content += "| Band | Frequency Range | Wavelength | Primary Use |\n"
                readme_content += "|------|----------------|-------------|-------------|\n"
                for entry in vhf_uhf_bands:
                    if entry['Frequency_Start_MHz'] == entry['Frequency_End_MHz']:
                        freq_range = f"{entry['Frequency_Start_MHz']:.1f} MHz"
                    else:
                        freq_range = f"{entry['Frequency_Start_MHz']:.1f} - {entry['Frequency_End_MHz']:.1f} MHz"
                    readme_content += f"| {entry['Band']} | {freq_range} | {entry['Wavelength']} | {entry['Primary_Use']} |\n"
            
            if simplex_freqs:
                readme_content += "\n### Important Amateur Radio Frequencies\n\n"
                readme_content += "| Frequency | Description | Use |\n"
                readme_content += "|-----------|-------------|-----|\n"
                for entry in simplex_freqs:
                    readme_content += f"| {entry['Frequency_Start_MHz']:.2f} MHz | {entry['Band']} | {entry['Primary_Use']} |\n"
        
        elif service_type == 'Broadcast':
            readme_content += """Commercial broadcasting frequencies allocated by the FCC for AM radio, FM radio, and over-the-air television in the United States.

### AM Radio Broadcasting
AM (Amplitude Modulation) radio operates in the Medium Frequency (MF) band with 10 kHz channel spacing in North America (9 kHz internationally).

### FM Radio Broadcasting  
FM (Frequency Modulation) radio operates in the VHF band with 200 kHz channel spacing and provides higher fidelity audio than AM.

### Television Broadcasting
Over-the-air television uses ATSC (Advanced Television Systems Committee) digital transmission standard in North America.

"""
            readme_content += "| Service | Frequency Range | Band | Modulation/Standard |\n"
            readme_content += "|---------|----------------|------|--------------------|\n"
            for entry in entries:
                if entry['Frequency_Start_MHz'] == entry['Frequency_End_MHz']:
                    freq_range = f"{entry['Frequency_Start_MHz']:.1f} MHz"
                else:
                    freq_range = f"{entry['Frequency_Start_MHz']:.1f} - {entry['Frequency_End_MHz']:.1f} MHz"
                readme_content += f"| {entry['Band']} | {freq_range} | {entry['Wavelength']} | {entry['Primary_Use']} |\n"
        
        elif service_type == 'Public Safety':
            readme_content += """Public safety frequencies used by police, fire, emergency medical services, and other first responders. These frequencies are coordinated through local and regional frequency coordination offices.

**Note**: Many public safety agencies have migrated to digital trunked radio systems and P25 digital modes. Frequencies listed represent common allocations but specific assignments vary by region.

"""
            readme_content += "| Service | Frequency Range | Primary Users | Notes |\n"
            readme_content += "|---------|----------------|---------------|-------|\n"
            for entry in entries:
                if entry['Frequency_Start_MHz'] == entry['Frequency_End_MHz']:
                    freq_range = f"{entry['Frequency_Start_MHz']:.1f} MHz"
                else:
                    freq_range = f"{entry['Frequency_Start_MHz']:.1f} - {entry['Frequency_End_MHz']:.1f} MHz"
                readme_content += f"| {entry['Band']} | {freq_range} | {entry['Primary_Use']} | Regional variations apply |\n"
        
        elif service_type == 'Aviation':
            readme_content += """Aviation frequencies used for air traffic control, aircraft communication, and navigation aids. These frequencies are regulated by the FAA in the United States and ICAO internationally.

### VHF Aviation Band
The primary aviation communication band using AM (amplitude modulation) with 25 kHz channel spacing (8.33 kHz in some regions).

### Emergency Frequencies
Critical frequencies for aviation emergencies and search and rescue operations.

"""
            readme_content += "| Service | Frequency | Band | Purpose |\n"
            readme_content += "|---------|-----------|------|----------|\n"
            for entry in entries:
                if entry['Frequency_Start_MHz'] == entry['Frequency_End_MHz']:
                    freq_range = f"{entry['Frequency_Start_MHz']:.1f} MHz"
                else:
                    freq_range = f"{entry['Frequency_Start_MHz']:.0f} - {entry['Frequency_End_MHz']:.0f} MHz"
                readme_content += f"| {entry['Band']} | {freq_range} | VHF/UHF | {entry['Primary_Use']} |\n"
        
        elif service_type == 'Marine':
            readme_content += """Maritime mobile frequencies for ship-to-ship, ship-to-shore, and distress communication. Regulated by the FCC and coordinated internationally through the ITU.

### VHF Marine Band
Primary marine communication using FM with 25 kHz channel spacing. Channel 16 (156.8 MHz) is the international distress and calling frequency.

### HF Marine Bands
Long-range maritime communication for ocean-going vessels.

"""
            readme_content += "| Service | Frequency Range | Band | Purpose |\n"
            readme_content += "|---------|----------------|------|----------|\n"
            for entry in entries:
                if entry['Frequency_Start_MHz'] == entry['Frequency_End_MHz']:
                    freq_range = f"{entry['Frequency_Start_MHz']:.1f} MHz"
                else:
                    freq_range = f"{entry['Frequency_Start_MHz']:.1f} - {entry['Frequency_End_MHz']:.1f} MHz"
                readme_content += f"| {entry['Band']} | {freq_range} | Marine | {entry['Primary_Use']} |\n"
        
        elif service_type == 'WiFi':
            readme_content += """Wi-Fi frequencies based on IEEE 802.11 standards. These operate in unlicensed ISM bands with specific power and bandwidth limitations.

### 2.4 GHz Band (802.11b/g/n/ax)
Most widely used Wi-Fi band, shared with other ISM devices like microwave ovens and Bluetooth.

### 5 GHz Band (802.11a/n/ac/ax)  
Less congested band offering higher data rates and more channels.

### 6 GHz Band (Wi-Fi 6E)
Newest allocation providing additional spectrum for high-capacity applications.

"""
            readme_content += "| Band | Frequency Range | Standard | Typical Use |\n"
            readme_content += "|------|----------------|----------|-------------|\n"
            for entry in entries:
                freq_range = f"{entry['Frequency_Start_MHz']:.0f} - {entry['Frequency_End_MHz']:.0f} MHz"
                readme_content += f"| {entry['Band']} | {freq_range} | {entry['Primary_Use']} | Wireless networking |\n"
        
        elif service_type == 'Cellular':
            readme_content += """Cellular telephone frequencies including 2G, 3G, 4G LTE, and 5G bands. Band designations follow 3GPP specifications and vary by carrier and region.

### LTE Band Classifications
- **Low Band** (< 1 GHz): Wide coverage, good building penetration
- **Mid Band** (1-6 GHz): Balance of coverage and capacity  
- **High Band** (> 6 GHz): High capacity, limited range

### 5G Deployment
5G uses both existing LTE bands (NSA mode) and new millimeter wave spectrum (mmWave).

"""
            readme_content += "| Band | Frequency Range | Technology | Primary Carriers |\n"
            readme_content += "|------|----------------|------------|------------------|\n"
            for entry in entries:
                if entry['Frequency_Start_MHz'] == entry['Frequency_End_MHz']:
                    freq_range = f"{entry['Frequency_Start_MHz']:.1f} MHz"
                else:
                    freq_range = f"{entry['Frequency_Start_MHz']:.0f} - {entry['Frequency_End_MHz']:.0f} MHz"
                readme_content += f"| {entry['Band']} | {freq_range} | {entry['Primary_Use']} | Major carriers |\n"
        
        elif service_type == 'GPS':
            readme_content += """Global Navigation Satellite System (GNSS) frequencies including GPS, GLONASS, Galileo, and other satellite navigation systems.

### GPS Signal Structure
- **L1 C/A**: Civilian coarse acquisition code (public)
- **L2 P(Y)**: Military precise code (encrypted)  
- **L5**: Safety-of-life applications (aviation)

### Other GNSS Systems
Modern receivers typically support multiple satellite constellations for improved accuracy and availability.

"""
            readme_content += "| System | Frequency (MHz) | Signal | Purpose |\n"
            readme_content += "|--------|----------------|--------|----------|\n"
            for entry in entries:
                freq_range = f"{entry['Frequency_Start_MHz']:.2f}"
                readme_content += f"| {entry['Band']} | {freq_range} | Navigation | {entry['Primary_Use']} |\n"
        
        elif service_type == 'Time Standard':
            readme_content += """Time and frequency standard stations providing precise time signals for synchronization and calibration purposes.

### WWV (Fort Collins, Colorado)
Operated by NIST, provides continuous time signals with voice announcements and time codes.

### WWVH (Kauai, Hawaii)  
Similar to WWV but with female voice announcements to distinguish from WWV.

### CHU (Ottawa, Canada)
Operated by the National Research Council of Canada.

"""
            readme_content += "| Station | Frequency (MHz) | Location | Operator |\n"
            readme_content += "|---------|----------------|----------|----------|\n"
            for entry in entries:
                freq_range = f"{entry['Frequency_Start_MHz']:.2f}"
                station = entry['Band'].replace(' ', ' ').split()[0]
                if 'WWV' in station:
                    location = "Colorado" if station == "WWV" else "Hawaii"
                    operator = "NIST"
                else:
                    location = "Canada"  
                    operator = "NRC"
                readme_content += f"| {station} | {freq_range} | {location} | {operator} |\n"
        
        else:
            # Generic table for other service types
            readme_content += "| Service | Frequency Range | Purpose |\n"
            readme_content += "|---------|----------------|----------|\n"
            for entry in entries:
                if entry['Frequency_Start_MHz'] == entry['Frequency_End_MHz']:
                    freq_range = f"{entry['Frequency_Start_MHz']:.2f} MHz"
                else:
                    freq_range = f"{entry['Frequency_Start_MHz']:.1f} - {entry['Frequency_End_MHz']:.1f} MHz"
                readme_content += f"| {entry['Band']} | {freq_range} | {entry['Primary_Use']} |\n"

    # Add remaining sections
    readme_content += """
## Frequency Band Designations

### ITU Radio Frequency Bands

| Band Number | Frequency Range | Wavelength | Designation |
|-------------|----------------|-------------|-------------|
| 4 | 3-30 kHz | 100-10 km | VLF (Very Low Frequency) |
| 5 | 30-300 kHz | 10-1 km | LF (Low Frequency) |
| 6 | 300-3000 kHz | 1000-100 m | MF (Medium Frequency) |
| 7 | 3-30 MHz | 100-10 m | HF (High Frequency) |
| 8 | 30-300 MHz | 10-1 m | VHF (Very High Frequency) |
| 9 | 300-3000 MHz | 100-10 cm | UHF (Ultra High Frequency) |
| 10 | 3-30 GHz | 10-1 cm | SHF (Super High Frequency) |
| 11 | 30-300 GHz | 10-1 mm | EHF (Extremely High Frequency) |

## Microwave and Satellite Frequency Bands

### IEEE Standard Radar Bands

| Band | Frequency Range | Wavelength | Primary Applications |
|------|----------------|-------------|---------------------|
| HF | 3-30 MHz | 10-100 m | Over-the-horizon radar |
| VHF | 30-300 MHz | 1-10 m | Long-range surveillance |
| UHF | 300-1000 MHz | 30-100 cm | Wind profiler, surveillance |
| L | 1-2 GHz | 15-30 cm | Air traffic control, GPS |
| S | 2-4 GHz | 7.5-15 cm | Weather radar, surface ship radar |
| C | 4-8 GHz | 3.75-7.5 cm | Weather radar, satellite communication |
| X | 8-12 GHz | 2.5-3.75 cm | Airport radar, military radar |
| Ku | 12-18 GHz | 1.67-2.5 cm | Satellite TV, police radar |
| K | 18-27 GHz | 1.11-1.67 cm | Radar, satellite communication |
| Ka | 27-40 GHz | 0.75-1.11 cm | High-resolution radar, 5G |

## Audio and Musical Frequencies

### Musical Note Frequencies (4th Octave - Concert Pitch A440)

| Note | Frequency (Hz) | MIDI Note | Scientific Pitch |
|------|----------------|-----------|------------------|
| C4 | 261.63 | 60 | C4 (Middle C) |
| C#4/Db4 | 277.18 | 61 | C#4 |
| D4 | 293.66 | 62 | D4 |
| D#4/Eb4 | 311.13 | 63 | D#4 |
| E4 | 329.63 | 64 | E4 |
| F4 | 349.23 | 65 | F4 |
| F#4/Gb4 | 369.99 | 66 | F#4 |
| G4 | 392.00 | 67 | G4 |
| G#4/Ab4 | 415.30 | 68 | G#4 |
| A4 | 440.00 | 69 | A4 (Concert Pitch) |
| A#4/Bb4 | 466.16 | 70 | A#4 |
| B4 | 493.88 | 71 | B4 |

### Audio Frequency Ranges

| Range | Frequency | Description |
|-------|-----------|-------------|
| **Sub-bass** | 20-60 Hz | Felt more than heard, organ pedal notes |
| **Bass** | 60-250 Hz | Fundamental frequencies of bass instruments |
| **Low midrange** | 250-500 Hz | Low order harmonics of most instruments |
| **Midrange** | 500-2000 Hz | Most important for speech intelligibility |
| **Upper midrange** | 2-4 kHz | Important for speech clarity and presence |
| **Presence** | 4-6 kHz | Critical for speech and vocal clarity |
| **Brilliance** | 6-20 kHz | Harmonics and overtones, "air" and sparkle |

### Human Hearing Characteristics

- **Full Range**: 20 Hz - 20 kHz (varies with age and individual)
- **Peak Sensitivity**: 2-5 kHz (speech range)
- **Phone Quality**: 300 Hz - 3.4 kHz
- **AM Radio**: 100 Hz - 5 kHz  
- **FM Radio**: 20 Hz - 15 kHz
- **CD Quality**: 20 Hz - 22.05 kHz
- **High-Resolution Audio**: 20 Hz - 40+ kHz

## Database Usage and Applications

### Frequency Lookup Examples

Using the provided database files, you can perform various frequency-related queries:

**Find what service uses a specific frequency:**
```sql
SELECT * FROM Frequencies 
WHERE 146.52 BETWEEN Frequency_Start_MHz AND Frequency_End_MHz;
-- Result: 2m Simplex, Amateur Radio
```

**Find all frequencies in a specific band:**
```sql
SELECT * FROM Frequencies 
WHERE Service_Type = 'Amateur Radio' 
AND Frequency_Start_MHz >= 144 
AND Frequency_End_MHz <= 148;
-- Result: All 2-meter amateur radio allocations
```

**Search for overlap analysis:**
```sql
SELECT f1.Band as Band1, f2.Band as Band2, f1.Service_Type, f2.Service_Type
FROM Frequencies f1, Frequencies f2 
WHERE f1.ID != f2.ID
AND f1.Frequency_Start_MHz <= f2.Frequency_End_MHz 
AND f1.Frequency_End_MHz >= f2.Frequency_Start_MHz;
-- Result: Find overlapping frequency allocations
```

### Applications

This frequency database serves multiple applications:

**Amateur Radio:**
- Band planning and frequency coordination
- Contest and special event planning  
- Repeater coordination
- Antenna modeling and analysis

**Professional RF:**
- Spectrum analysis and planning
- Interference investigation
- Regulatory compliance checking
- System design and coordination

**Education:**
- RF engineering coursework
- Telecommunications training
- Physics and engineering labs
- Radio fundamentals education

**Emergency Communications:**
- Disaster response planning
- Interoperability planning
- Backup communication systems
- Public safety coordination

## Data Sources and Verification

All frequency data in this database has been researched and verified against authoritative sources:

### Primary Sources
- **FCC (Federal Communications Commission)**: CFR Title 47 - Telecommunications
- **ITU (International Telecommunication Union)**: Radio Regulations
- **ARRL (American Radio Relay League)**: Amateur radio band plans
- **IEEE (Institute of Electrical and Electronics Engineers)**: Wireless standards
- **3GPP (3rd Generation Partnership Project)**: Cellular specifications
- **NIST (National Institute of Standards and Technology)**: Time and frequency standards
- **ICAO (International Civil Aviation Organization)**: Aviation standards

### Verification Process
1. **Cross-reference multiple authoritative sources**
2. **Verify against current regulations and standards**  
3. **Check for recent updates and changes**
4. **Validate technical specifications**
5. **Confirm regional variations and notes**

### Data Currency
- Last verified: December 2024
- Sources current as of: December 2024
- Regular updates planned for regulatory changes

## Technical Specifications

### Database Schema

The frequency database uses the following structure:

```sql
CREATE TABLE Frequencies (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Band TEXT NOT NULL,                    -- Band name or designation
    Frequency_Start_MHz REAL NOT NULL,     -- Start frequency in MHz
    Frequency_End_MHz REAL NOT NULL,       -- End frequency in MHz  
    Wavelength TEXT,                       -- Wavelength description
    Primary_Use TEXT,                      -- Primary application
    Service_Type TEXT,                     -- Service category
    DateAdded DATETIME DEFAULT CURRENT_TIMESTAMP,
    Notes TEXT                             -- Additional information
);
```

### Indexes for Performance
- **idx_frequency_range**: Optimizes frequency range queries
- **idx_service_type**: Optimizes service type filtering  
- **idx_band**: Optimizes band name searches

### File Formats

**CSV Format**: Standard comma-separated values with headers
- Compatible with Excel, LibreOffice, databases
- UTF-8 encoding for international characters
- Consistent numeric formatting (MHz units)

**SQLite Database**: 
- Cross-platform compatibility
- ACID compliance
- Embedded database (no server required)
- SQL query capability

**Excel Workbook**:
- Multiple worksheets by service type
- Formatted for readability
- Summary statistics included
- Compatible with Microsoft Excel 2007+

## License and Usage

### Educational and Reference Use
This frequency data compilation is provided for educational and reference purposes. The data represents frequency allocations and technical standards from authoritative sources.

### Important Disclaimers
- **Regulatory Compliance**: Users must comply with applicable local and national regulations
- **Regional Variations**: Frequency allocations may vary by country and region
- **Current Information**: Regulations and allocations are subject to change
- **Licensing Requirements**: Many frequencies require appropriate licenses for transmission
- **No Warranty**: Data provided as-is without warranty of any kind

### Recommended Use
- Frequency planning and coordination
- Educational and training purposes  
- Reference for RF engineering
- Spectrum analysis and research

### Not Recommended For
- Unlicensed transmission
- Safety-critical applications without verification
- Commercial purposes without proper licensing
- Real-time applications requiring current data

## Contributing and Updates

### Reporting Issues
If you find errors or omissions in the frequency data:
1. **Check against primary sources** listed above
2. **Submit an issue** with source documentation
3. **Provide specific frequency and service details**
4. **Include regulatory references** when applicable

### Suggesting Additions
For new frequency allocations or missing services:
1. **Provide authoritative source** for the allocation
2. **Include complete technical details**
3. **Specify regional applicability**
4. **Document any special conditions or notes**

### Version History
- **v2.0** (2024): Enhanced with 91 verified allocations
- **v1.0** (2024): Initial release with basic allocations

---

*This frequency reference database is maintained as an educational resource. For official regulatory information, always consult the appropriate government agencies and international standards organizations.*

**Repository**: https://github.com/cjemorton/frequencies  
**Last Updated**: December 2024  
**Total Frequency Allocations**: 91 verified entries  
**Coverage**: DC to 40+ GHz across all major services
"""

    return readme_content

def main():
    """Generate the comprehensive README."""
    content = generate_comprehensive_readme()
    
    with open('README.md', 'w') as f:
        f.write(content)
    
    print("Generated comprehensive README.md with complete frequency information")
    print(f"README size: {len(content):,} characters")

if __name__ == "__main__":
    main()