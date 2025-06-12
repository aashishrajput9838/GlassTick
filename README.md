# Floating Clock Widget

A minimal, transparent floating clock widget that stays on top of other windows. Features a clean Windows 8.1 style interface with customizable settings.

## Features
- Always on top of other windows
- Transparent background
- Draggable interface
- Clean, minimal design
- Customizable settings
- Windows 8.1 style UI/UX
- Settings icon appears on double-click
- Settings persist between sessions

## Quick Start (Using Executable)
1. Download the latest release
2. Run "Floating Clock.exe"
3. The clock will appear in the top-right corner
4. Double-click to show/hide settings
5. Click the settings icon to customize

## Development Setup

### Requirements
- Python 3.x
- Windows OS

### Installation

1. Clone the repository:
```bash
git clone [repository-url]
cd floating-clock-widget
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

### Running from Source
```bash
python floating_clock.py
```

## Usage

### Basic Controls
- Click and drag to move the clock
- Double-click to show/hide settings icon
- Click settings icon (⚙) to open settings

### Settings
The settings window allows you to customize:
- Transparency level (10% to 100%)
- Font size (12pt to 48pt)
- Background color
- Text color
- Time format (12-hour/24-hour)

### Building Executable
To create your own executable:

1. Install required packages:
```bash
pip install -r requirements.txt
```

2. Generate the icon:
```bash
python create_icon.py
```

3. Build the executable:
```bash
pyinstaller clock.spec
```

The executable will be created in the `dist` folder.

## Customization
You can modify the following aspects in the code:
- Font size and style
- Transparency level
- Colors
- Time format
- Window position
- Settings persistence

## File Structure
- `floating_clock.py` - Main application code
- `clock.spec` - PyInstaller specification file
- `create_icon.py` - Icon generation script
- `requirements.txt` - Python dependencies
- `clock_settings.json` - User settings (created on first run)

## Contributing
Feel free to submit issues and enhancement requests!

## License
This project is open source and available under the MIT License. 