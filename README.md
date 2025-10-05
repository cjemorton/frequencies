# Frequency Reference Database

A comprehensive reference database containing frequency allocations, band plans, and technical specifications for various radio frequency applications.

## Contents

This repository contains:
- **README.md**: Complete frequency reference data (this file)
- **frequency_data.csv**: Frequency data in CSV format for database import
- **database_schema.sql**: SQL schema for creating Access database
- **ACCESS_DATABASE_INSTRUCTIONS.md**: Instructions for creating the Access database

## Ham Radio Frequency Allocations

### HF Bands (3-30 MHz)

| Band | Frequency Range | Wavelength | Primary Use |
|------|----------------|-------------|-------------|
| 160m | 1.8 - 2.0 MHz | 160 meters | Long distance communication |
| 80m | 3.5 - 4.0 MHz | 80 meters | Regional/DX communication |
| 40m | 7.0 - 7.3 MHz | 40 meters | Reliable regional/DX |
| 30m | 10.1 - 10.15 MHz | 30 meters | Digital modes, CW |
| 20m | 14.0 - 14.35 MHz | 20 meters | Premier DX band |
| 17m | 18.068 - 18.168 MHz | 17 meters | DX communication |
| 15m | 21.0 - 21.45 MHz | 15 meters | DX when propagation good |
| 12m | 24.89 - 24.99 MHz | 12 meters | Regional/DX |
| 10m | 28.0 - 29.7 MHz | 10 meters | Local/DX, repeaters |

### VHF/UHF Bands

| Band | Frequency Range | Wavelength | Primary Use |
|------|----------------|-------------|-------------|
| 6m | 50 - 54 MHz | 6 meters | Sporadic E propagation |
| 2m | 144 - 148 MHz | 2 meters | Local/repeater communication |
| 1.25m | 222 - 225 MHz | 1.25 meters | Regional communication |
| 70cm | 420 - 450 MHz | 70 centimeters | Local/repeater/satellites |
| 33cm | 902 - 928 MHz | 33 centimeters | Weak signal/digital |
| 23cm | 1240 - 1300 MHz | 23 centimeters | ATV, digital, microwave |

## Commercial Broadcast Frequencies

### AM Radio
- **Frequency Range**: 535 - 1705 kHz
- **Channel Spacing**: 10 kHz (9 kHz internationally)
- **Modulation**: Amplitude Modulation (AM)

### FM Radio
- **Frequency Range**: 88.1 - 107.9 MHz
- **Channel Spacing**: 200 kHz
- **Modulation**: Frequency Modulation (FM)

### Television Channels (ATSC)
| Channel | Frequency Range | Band |
|---------|----------------|------|
| 2-6 | 54-88 MHz | VHF Low |
| 7-13 | 174-216 MHz | VHF High |
| 14-36 | 470-608 MHz | UHF |

## Public Safety Frequencies

### Common Public Safety Bands
| Service | Frequency Range | Notes |
|---------|----------------|-------|
| Police VHF | 150-174 MHz | Local police departments |
| Police UHF | 450-470 MHz | Municipal police |
| Fire/EMS VHF | 150-174 MHz | Fire and emergency medical |
| Fire/EMS UHF | 450-470 MHz | Fire and emergency medical |
| Highway Patrol | 42-50 MHz | State highway patrol |
| Aviation | 118-137 MHz | Air traffic control |
| Marine VHF | 156-162 MHz | Coast Guard, marine |

## WiFi and ISM Bands

### 2.4 GHz Band
| Channel | Center Frequency | Bandwidth |
|---------|-----------------|-----------|
| 1 | 2412 MHz | 20 MHz |
| 6 | 2437 MHz | 20 MHz |
| 11 | 2462 MHz | 20 MHz |

### 5 GHz Band (Selected Channels)
| Channel | Center Frequency | Bandwidth |
|---------|-----------------|-----------|
| 36 | 5180 MHz | 20/40/80 MHz |
| 40 | 5200 MHz | 20/40/80 MHz |
| 44 | 5220 MHz | 20/40/80 MHz |
| 149 | 5745 MHz | 20/40/80 MHz |
| 153 | 5765 MHz | 20/40/80 MHz |
| 157 | 5785 MHz | 20/40/80 MHz |
| 161 | 5805 MHz | 20/40/80 MHz |

## Cellular Frequencies

### 4G LTE Bands (US)
| Band | Frequency Range | Carrier |
|------|----------------|---------|
| Band 2 | 1850-1910 MHz / 1930-1990 MHz | AT&T, T-Mobile |
| Band 4 | 1710-1755 MHz / 2110-2155 MHz | AT&T, T-Mobile, Verizon |
| Band 5 | 824-849 MHz / 869-894 MHz | AT&T, Verizon |
| Band 12 | 699-716 MHz / 729-746 MHz | AT&T, T-Mobile |
| Band 13 | 777-787 MHz / 746-756 MHz | Verizon |

## Microwave and Satellite Frequencies

### Satellite Bands
| Band | Frequency Range | Application |
|------|----------------|-------------|
| L-Band | 1-2 GHz | GPS, mobile satellite |
| S-Band | 2-4 GHz | Weather radar, WiFi |
| C-Band | 4-8 GHz | Satellite communication |
| X-Band | 8-12 GHz | Radar, satellite |
| Ku-Band | 12-18 GHz | Satellite TV, internet |
| K-Band | 18-27 GHz | Satellite, radar |
| Ka-Band | 27-40 GHz | High-capacity satellite |

## Audio Frequencies

### Musical Note Frequencies (4th Octave)
| Note | Frequency (Hz) |
|------|----------------|
| C4 | 261.63 |
| C#4 | 277.18 |
| D4 | 293.66 |
| D#4 | 311.13 |
| E4 | 329.63 |
| F4 | 349.23 |
| F#4 | 369.99 |
| G4 | 392.00 |
| G#4 | 415.30 |
| A4 | 440.00 |
| A#4 | 466.16 |
| B4 | 493.88 |

### Audio Range
- **Human Hearing**: 20 Hz - 20 kHz
- **Speech**: 300 Hz - 3.4 kHz
- **Music Fundamentals**: 27.5 Hz - 4.186 kHz
- **CD Quality**: 0 Hz - 22.05 kHz

## Time and Frequency Standards

### WWV/WWVH Time Signals
- **WWV (Colorado)**: 2.5, 5, 10, 15, 20 MHz
- **WWVH (Hawaii)**: 2.5, 5, 10, 15 MHz
- **CHU (Canada)**: 3.330, 7.850, 14.670 MHz

### GPS Frequencies
- **L1**: 1575.42 MHz
- **L2**: 1227.60 MHz
- **L5**: 1176.45 MHz

## Usage

This database serves as a reference for:
- Radio frequency planning
- Spectrum analysis
- Communication system design
- Amateur radio operations
- Educational purposes

## Database Files

### Creating the Access Database
To create a functional Microsoft Access database from this data:

1. **Use the CSV file**: Import `frequency_data.csv` into a new Access database
2. **Apply the schema**: Use `database_schema.sql` for proper table structure and indexes
3. **Follow instructions**: See `ACCESS_DATABASE_INSTRUCTIONS.md` for detailed steps

### File Contents
- **frequency_data.csv**: 45+ frequency allocations across all major services
- **database_schema.sql**: Complete table structure with indexes for fast searching
- **ACCESS_DATABASE_INSTRUCTIONS.md**: Step-by-step database creation guide

The resulting database will allow you to:
- Search frequencies by range (e.g., "What uses 146.520 MHz?")
- Filter by service type (Amateur, Public Safety, Broadcast, etc.)
- Browse by frequency band or wavelength
- Add custom notes and additional allocations

## License

This frequency data compilation is provided for educational and reference purposes. Frequency allocations are subject to regional regulations and may vary by country.

---

*Last updated: 2024*
*Repository: https://github.com/cjemorton/frequencies*