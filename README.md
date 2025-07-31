Simple Python script to generate username permutations from full names.

The goal of this script is to automate the creation of common username variants, useful for pentesting, user enumeration, OSINT, or auditing.

Inspired by `linkedin2username`.

## Use Case

**fullname2usernames** takes either a single full name or a file containing multiple full names (one per line) and generates a list of username permutations based on common patterns like `first.last`, `f.last`, `firstlast`, etc.

The output is a combined file with all generated usernames (`all_usernames.txt`), and optionally individual files per format (if requested).

### Real-World Use Cases

Some practical scenarios where `f`ullname2usernames proves useful:

- Active Directory user enumeration during internal pentests:
```sh
kerbrute userenum -d <DOMAIN> --dc <DC_IP> all_usernames.txt
```

- OSINT (Open Source Intelligence) investigations to collect potential email addresses or usernames for reconnaissance:
```sh
python fullname2usernames.py -u fullnames.txt -d example.com
# Output: elon.musk@example.com, emusk@example.com, etc.
```

- Audit/account discovery for validating user naming conventions across an organization.

## Usage

```
usage: fullname2usernames.py [-h] -u USERS [--save-formats [FORMAT]] [-l]

Generate username permutations from full names.

options:
  -h, --help            show this help message and exit
  -u USERS, --users USERS
                        Full name or file with full names
  --save-formats [FORMAT]
                        Save each username format in its own file.
                        Optionally provide one or more formats separated by commas (e.g. --save-formats fn.ln,fnln).
                        Use -l/--list-formats to view available formats.
                        Legend: fn = firstname, fi = first initial, ln = lastname, li = last initial
  -l, --list-formats    List all available username formats with descriptions.
  -d DOMAIN, --domain DOMAIN
                        Adds a domain name to the end of each username (ex: -d example.com => elon.musk@example.com)
```

### Examples

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
python fullname2usernames.py -u users.txt --save-formats
```
- Save individual files for specific formats only:
```sh
python fullname2usernames.py -u users.txt --save-formats fn.ln,fnln
```
- Add a domain to all usernames:
```sh
python fullname2usernames.py -u users.txt -d example.com
```
- List all available formats:
```sh
python fullname2usernames.py -l
```

## Output

- All generated usernames combined in `all_usernames.txt`
- If `--save-formats` is used, individual files for each format are saved in the folder `./f2u-individual-usernames/`

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
- Generates a wide variety of common username formats
- Optionally saves individual files per username format
- Validates requested formats before generation
- Lists all available formats with descriptions
- Can append a domain to each username
- Simple, fast, and requires only Python 3