# 🇦🇱 Albania Travel Metadata Editor

A visual JSON editor for your Albania travel data files that makes editing safe and easy!

## 🚀 Quick Start

### Option 1: Easy Launch (Recommended)

**On macOS:**
- Double-click `start-editor.command`

**On Windows:**  
- Double-click `start-editor.bat`

**On Linux:**
- Run: `python3 server.py`

### Option 2: Manual Launch

```bash
cd atc-metadata
python3 server.py
```

The editor will automatically open in your browser at `http://localhost:8080/json-editor.html`

## 📁 What's Included

- **`json-editor.html`** - The visual JSON editor interface
- **`server.py`** - HTTP server to avoid CORS issues  
- **`start-editor.command`** - macOS launcher script
- **`start-editor.bat`** - Windows launcher script
- **`data/`** - Your JSON travel data files
  - `eat-drink.json` - Restaurant and café data
  - `experiences.json` - Activities and entertainment
  - `explore.json` - Travel guide information  
  - `places.json` - Tourist destinations

## ✨ Features

### 🎨 Visual Interface
- Clean, modern design with Albania-themed colors
- Mobile-responsive for editing on tablets/phones
- Intuitive form-based editing (no more JSON syntax!)

### 🗂️ Smart Data Handling
- **Tree View**: Navigate large JSON structures easily
- **Type-Aware Editing**: Different inputs for strings, numbers, booleans
- **Array Management**: Add/remove items with visual buttons
- **Image Previews**: See image URLs as actual images
- **Collapsible Sections**: Organize complex nested data

### 🛡️ Safety Features
- **JSON Validation**: Prevents syntax errors before saving
- **Auto-backup**: Saves to browser storage every 30 seconds
- **Change Detection**: Warns before losing unsaved work
- **Reset Function**: Easily revert to original data
- **Download-based Saving**: Safe file replacement workflow

### 🔧 Technical Benefits
- **No CORS Issues**: HTTP server eliminates browser security blocks
- **Local Development**: Works completely offline
- **No Dependencies**: Pure HTML/CSS/JavaScript + Python server
- **Cross-Platform**: Works on Windows, macOS, and Linux

## 📖 How to Use

1. **Launch the editor** using one of the quick start methods above
2. **Select a file** from the dropdown (Eat & Drink, Experiences, etc.)
3. **Click "Load File"** to see your data in the editor
4. **Edit visually** using the form fields - no JSON syntax needed!
5. **Navigate easily** using the tree structure on the left
6. **Save changes** by clicking "Save Changes" (downloads updated file)
7. **Replace manually** - move the downloaded file back to replace the original

## 🔄 Editing Workflow

### Making Changes
- **Text fields** for short strings
- **Text areas** for long descriptions  
- **Number inputs** for numeric values
- **Checkboxes** for true/false values
- **Add/Remove buttons** for array items
- **Collapsible sections** for nested objects

### Saving Changes  
1. Click **"Save Changes"** button
2. File downloads to your Downloads folder
3. **Manually replace** the original file in `data/` folder
4. Click **"Reset"** to clear unsaved changes (optional)

*Note: Manual replacement is required due to browser security - the editor cannot directly overwrite files.*

## 🛠️ Requirements

- **Python 3.x** (usually pre-installed on macOS/Linux)
- **Modern web browser** (Chrome, Firefox, Safari, Edge)
- **Internet connection** (for loading fonts and some UI elements)

### Installing Python (if needed)
- **Windows/macOS**: Download from [python.org](https://python.org)
- **Linux**: `sudo apt install python3` (Ubuntu/Debian) or equivalent

## 🐛 Troubleshooting

### "Python not found" Error
- Install Python 3 from [python.org](https://python.org)
- On Windows, make sure to check "Add to PATH" during installation

### "Port already in use" Error  
- Close other applications using port 8080
- The server will automatically try ports 8081, 8082, etc.

### "Access denied" on macOS
- Right-click `start-editor.command` → Open → Open (security prompt)
- Or run: `chmod +x start-editor.command` in Terminal

### Browser doesn't open automatically
- Manually open: `http://localhost:8080/json-editor.html`
- Check the terminal output for the exact URL

### File loading fails
- Make sure you're using the server launcher (not opening HTML directly)
- Check that JSON files exist in the `data/` folder
- Look for error messages in browser developer console (F12)

## 📊 File Structure

```
atc-metadata/
├── json-editor.html          # Main editor interface
├── server.py                 # HTTP server script  
├── start-editor.command      # macOS launcher
├── start-editor.bat          # Windows launcher
├── README.md                 # This file
└── data/                     # Your JSON data files
    ├── eat-drink.json
    ├── experiences.json  
    ├── explore.json
    └── places.json
```

## 🔐 Security Notes

- **Local only**: Server only accepts connections from localhost
- **No external access**: Cannot be reached from other computers
- **CORS headers**: Only for local file access, not external APIs
- **No data transmission**: All editing happens locally in your browser

## 💡 Tips & Best Practices

### Editing Tips
- **Use the tree view** to navigate large files quickly
- **Expand/collapse sections** to focus on what you're editing
- **Save frequently** - changes download as new files
- **Test your changes** by reloading the file after editing

### Backup Strategy  
- **Original files stay safe** until you manually replace them
- **Auto-backup in browser** storage (cleared when you clear browser data)
- **Download history** keeps previous versions in your Downloads folder

### Working with Large Files
- **Edit one section at a time** using collapsible interface
- **Use browser search** (Ctrl+F) to find specific content
- **Take breaks** - browser saves your progress automatically

## 🆘 Support

If you encounter issues:

1. **Check this README** for common solutions
2. **Restart the server** (Ctrl+C, then restart launcher)
3. **Clear browser cache** and reload the page
4. **Check browser console** (F12) for error messages
5. **Try a different browser** if problems persist

## 🎯 Made For

This editor was specifically designed for the Albania travel metadata project, but can be adapted for any JSON editing needs. The interface is optimized for the specific data structures in your travel files.

---

**Happy editing! 🚀✨**