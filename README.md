Simple Python script to generate username permutations from full names.

The goal of this script is to automate the creation of common username variants, useful for pentesting, user enumeration, or auditing.

Inspired by `linkedin2username`.

## Use Case

**fullname2usernamess** takes either a single full name or a file containing multiple full names (one per line) and generates a list of username permutations based on common patterns like `first.last`, `f.last`, `firstlast`, etc.

The output is a combined file with all generated usernames (`all_usernames.txt`), and optionally individual files per format (if requested).

## Options

```
usage: fullname2usernamess.py [-h] -u USERS [--save-individual [FORMAT]] [-l]

Generate username permutations from full names.

options:
  -h, --help            show this help message and exit
  -u USERS, --users USERS
                        Full name or file with full names
  --save-individual [FORMAT]
                        Save individual username files.
                        Optionally provide a single format to save (e.g. --save-individual fn.ln).
                        Use -l/--list-formats to view available formats.
                        Legend: fn = firstname, fi = first initial, ln = lastname, li = last initial
  -l, --list-formats    List all available username formats with descriptions.
```

## Examples

- Generate usernames from a single full name:
```sh
python fullname2usernames.py -u "Elon Musk"
```
- Generate usernames from a file containing multiple full names:
```sh
python fullname2usernames.py -u users.txt
```
- Save individual files for all formats:
```sh
python fullname2usernames.py -u users.txt --save-individual
```
- Save individual files for a specific format only:
```sh
python fullname2usernames.py -u users.txt --save-individual fn.ln
```
- List all available formats:
```sh
python fullname2usernames.py -l
```

## Output

- All generated usernames combined in `all_usernames.txt`
- If `--save-individual` is used, individual files for each format are saved in the folder `./individual-usernames/`

## Install

To use `fullname2usernames.py` globally:

1. Copy the script to `/opt` and make it executable:
```sh
sudo cp fullname2usernames.py /opt/
sudo chmod +x /opt/fullname2usernames.py
```
2. Create a wrapper script in `/usr/local/bin/fullname2usernames`:
```sh
#!/bin/bash
/opt/fullname2usernames.py "$@"
```
3. Make the wrapper executable:
```sh
sudo chmod +x /usr/local/bin/fullname2usernames
```

You can now run the script anywhere by calling `fullname2usernames`.

## Features
- Accepts single full name or file with multiple full names
- Generates a wide variety of common Active Directory username formats
- Optionally saves individual files per username format
- Validates requested formats before generation
- Lists all available formats with descriptions
- Simple, fast, and requires only Python 3