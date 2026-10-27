# Scan security_log.txt for common security-related keywords

file_name = "security_log.txt"

keywords = ["ERROR", "FAILED LOGIN", "WARNING"]

counts = {
    "ERROR": 0,
    "FAILED LOGIN": 0,
    "WARNING": 0
}

try:
    with open(file_name, "r") as file:
        for line in file:
            line = line.upper()

            for keyword in keywords:
                if keyword in line:
                    counts[keyword] += 1

    print("Security Log Scan Results")
    print("-------------------------")

    for keyword in keywords:
        print(keyword, ":", counts[keyword])

except FileNotFoundError:
    print("Error: security_log.txt was not found.")