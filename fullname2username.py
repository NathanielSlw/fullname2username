#!/usr/bin/env python3
import argparse
import os

ALL_FORMATS = {
    # No separator
    "fnln":     lambda f, l, _: f"{f}{l}",
    "filn":     lambda f, l, _: f"{f[0]}{l}",
    "fnli":     lambda f, l, _: f"{f}{l[0]}",
    "fili":     lambda f, l, _: f"{f[0]}{l[0]}",
    "lnfn":     lambda f, l, _: f"{l}{f}",
    "lnfi":     lambda f, l, _: f"{l}{f[0]}",
    "lifn":     lambda f, l, _: f"{l[0]}{f}",
    "lifi":     lambda f, l, _: f"{l[0]}{f[0]}",
    "fn":       lambda f, l, _: f,
    "ln":       lambda f, l, _: l,

    # Dot
    "fn.ln":    lambda f, l, _: f"{f}.{l}",
    "fi.ln":    lambda f, l, _: f"{f[0]}.{l}",
    "fn.li":    lambda f, l, _: f"{f}.{l[0]}",
    "fi.li":    lambda f, l, _: f"{f[0]}.{l[0]}",
    "ln.fn":    lambda f, l, _: f"{l}.{f}",
    "ln.fi":    lambda f, l, _: f"{l}.{f[0]}",
    "li.fn":    lambda f, l, _: f"{l[0]}.{f}",
    "li.fi":    lambda f, l, _: f"{l[0]}.{f[0]}",

    # Dash
    "fn-ln":    lambda f, l, _: f"{f}-{l}",
    "fi-ln":    lambda f, l, _: f"{f[0]}-{l}",
    "fn-li":    lambda f, l, _: f"{f}-{l[0]}",
    "fi-li":    lambda f, l, _: f"{f[0]}-{l[0]}",
    "ln-fn":    lambda f, l, _: f"{l}-{f}",
    "ln-fi":    lambda f, l, _: f"{l}-{f[0]}",
    "li-fn":    lambda f, l, _: f"{l[0]}-{f}",
    "li-fi":    lambda f, l, _: f"{l[0]}-{f[0]}",

    # Underscore
    "fn_ln":    lambda f, l, _: f"{f}_{l}",
    "fi_ln":    lambda f, l, _: f"{f[0]}_{l}",
    "fn_li":    lambda f, l, _: f"{f}_{l[0]}",
    "fi_li":    lambda f, l, _: f"{f[0]}_{l[0]}",
    "ln_fn":    lambda f, l, _: f"{l}_{f}",
    "ln_fi":    lambda f, l, _: f"{l}_{f[0]}",
    "li_fn":    lambda f, l, _: f"{l[0]}_{f}",
    "li_fi":    lambda f, l, _: f"{l[0]}_{f[0]}",
}

FORMAT_DESCRIPTIONS = {
    "fnln": "firstname + lastname",
    "filn": "first initial + lastname",
    "fnli": "firstname + last initial",
    "fili": "first initial + last initial",
    "lnfn": "lastname + firstname",
    "lnfi": "lastname + first initial",
    "lifn": "last initial + firstname",
    "lifi": "last initial + first initial",
    "fn":   "firstname only",
    "ln":   "lastname only",

    "fn.ln": "firstname.lastname",
    "fi.ln": "first initial.lastname",
    "fn.li": "firstname.last initial",
    "fi.li": "first initial.last initial",
    "ln.fn": "lastname.firstname",
    "ln.fi": "lastname.first initial",
    "li.fn": "last initial.firstname",
    "li.fi": "last initial.first initial",

    "fn-ln": "firstname-lastname",
    "fi-ln": "first initial-lastname",
    "fn-li": "firstname-last initial",
    "fi-li": "first initial-last initial",
    "ln-fn": "lastname-firstname",
    "ln-fi": "lastname-first initial",
    "li-fn": "last initial-firstname",
    "li-fi": "last initial-first initial",

    "fn_ln": "firstname_lastname",
    "fi_ln": "first initial_lastname",
    "fn_li": "firstname_last initial",
    "fi_li": "first initial_last initial",
    "ln_fn": "lastname_firstname",
    "ln_fi": "lastname_first initial",
    "li_fn": "last initial_firstname",
    "li_fi": "last initial_first initial",
}

def generate_usernames(fullname, formats_to_generate):
    try:
        firstname, lastname = fullname.strip().split()
    except ValueError:
        return {}

    firstname = firstname.lower()
    lastname = lastname.lower()
    middle = firstname[1] if len(firstname) > 1 else ""

    usernames = {}
    for key in formats_to_generate:
        if key not in ALL_FORMATS:
            continue
        result = ALL_FORMATS[key](firstname, lastname, middle)
        if result:
            usernames[f"{key}.txt"] = result
    return usernames

def print_available_formats():
    print("\nAvailable formats:\n")
    for key in sorted(ALL_FORMATS):
        desc = FORMAT_DESCRIPTIONS.get(key, "")
        print(f"  {key:<10} : {desc}")
    print()

def main():
    examples_text = """
Examples:

  Generate usernames from a single full name:
    python fullname2username.py -u "Elon Musk"

  Generate usernames from a file containing multiple full names:
    python fullname2username.py -u users.txt

  Save individual files for all formats:
    python fullname2username.py -u users.txt --save-individual

  Save individual files for a specific format only:
    python fullname2username.py -u users.txt --save-individual fn.ln

  List all available formats:
    python fullname2username.py -l
"""

    parser = argparse.ArgumentParser(
        description="Generate username permutations from full names.",
        epilog=examples_text,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("-u", "--users", required=True, help='Full name or file with full names')
    parser.add_argument(
        "--save-individual",
        nargs="?",
        const="__all__",
        metavar="FORMAT",
        help=(
            "Save individual username files. "
            "Optionally provide a single format to save (e.g. --save-individual fn.ln). "
            "Use -l/--list-formats to view available formats.\n"
            "Legend: fn = firstname, fi = first initial, ln = lastname, li = last initial"
        )
    )
    parser.add_argument(
        "-l", "--list-formats",
        action="store_true",
        help="List all available username formats with descriptions."
    )

    args = parser.parse_args()

    if args.list_formats:
        print_available_formats()
        return

    # Determine formats to generate
    if args.save_individual and args.save_individual != "__all__":
        if args.save_individual not in ALL_FORMATS:
            print(f"[!] Invalid format: {args.save_individual}")
            print_available_formats()
            return
        formats_to_generate = [args.save_individual]
    else:
        formats_to_generate = list(ALL_FORMATS.keys())

    individual_usernames_dir = "individual-usernames"
    if args.save_individual:
        os.makedirs(individual_usernames_dir, exist_ok=True)

    output_files = {f"{fmt}.txt": [] for fmt in formats_to_generate}
    all_usernames = []

    # Read input
    input_lines = []
    if os.path.isfile(args.users):
        with open(args.users, "r") as infile:
            input_lines = infile.readlines()
    else:
        input_lines = [args.users]

    for line in input_lines:
        if line.strip():
            variants = generate_usernames(line, formats_to_generate)
            for filename, value in variants.items():
                output_files[filename].append(value)
                all_usernames.append(value)

    # Save individual files (if requested)
    if args.save_individual:
        for filename, lines in output_files.items():
            with open(os.path.join(individual_usernames_dir, filename), "w") as f:
                f.write("\n".join(lines) + "\n")

    # Save all usernames combined
    with open("all_usernames.txt", "w") as f:
        f.write("\n".join(sorted(set(all_usernames))) + "\n")

    print(f"[+] Generated {len(all_usernames)} usernames.")
    print(f"[+] Saved to 'all_usernames.txt'")
    if args.save_individual:
        print(f"[+] Individual file(s) saved in './{individual_usernames_dir}/'")
        print(f"[+] Formats used: {', '.join(formats_to_generate)}")

logo_ascii = r"""
▐▘  ▜ ▜          ▄▖                 
▜▘▌▌▐ ▐ ▛▌▀▌▛▛▌█▌▄▌▌▌▛▘█▌▛▘▛▌▀▌▛▛▌█▌
▐ ▙▌▐▖▐▖▌▌█▌▌▌▌▙▖▙▖▙▌▄▌▙▖▌ ▌▌█▌▌▌▌▙▖

fullname2username v1.0 - by NathanielSlw                                                                                                                                                           
"""

if __name__ == "__main__":
    print(logo_ascii)
    main()
