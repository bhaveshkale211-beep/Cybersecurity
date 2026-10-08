# Assignment 01 — Student Record Management System

The earlier Python assignments just printed a result and forgot it as soon as the program ended. This one is the first where the data actually sticks around: the program saves student details into a text file, reads them back, and adds new ones later without losing the old ones (when the right file mode is used, more on that below).

## The scenario

A training institute wants a simple way to keep track of its students. The program asks for a student's name, roll number and course, saves them to `student_records.txt` along with the date and time, shows what's stored, lets me add another student, and finally reports how big the file is.

## What I used

- Python 3, run from VS Code on Windows
- `open()` for file handling
- `datetime` to stamp each record with the time it was added
- `os` to check whether the file exists and to get its size

The real point of the assignment is the three file modes:

| Mode | What it does | Where I used it |
|---|---|---|
| `"w"` | Write. Creates the file, or empties it if it already exists | Saving the first student |
| `"r"` | Read. Opens the file just to look at it | Printing the stored records |
| `"a"` | Append. Adds to the end and leaves existing content alone | Adding the second student |

## Running it, step by step

The full script is [`student_record_management.py`](./student_record_management.py). Here's how each part went.

### 1. Does the file exist yet?

The program starts with `os.path.exists()` and then asks for the student's details.

```python
if os.path.exists(file_name):
    print("The student record file is already there.")
else:
    print("No record file found, so creating one...")

student_name = input("Student Name: ")
roll_number = input("Roll Number: ")
course_name = input("Course Name: ")
```

On the first run there was no file yet, so it printed `No record file found, so creating one...` and went straight to the input prompts.

![First run in VS Code](./screenshots/01-file-check-and-first-input.png)

### 2. Saving the first record with "w"

```python
date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open(file_name, "w") as file:
    file.write("Student Name: " + student_name + "\n")
    file.write("Roll Number: " + roll_number + "\n")
    file.write("Course Name: " + course_name + "\n")
    file.write("Date & Time Added: " + date_time + "\n")
    file.write("--------------------------------\n")
```

Every record is five lines: name, roll number, course, the timestamp, and a dashed line so records are easy to tell apart. Using `with open(...)` means the file closes itself when the block ends, so there's no `file.close()` to forget.

To check what actually landed on disk I ran `cat student_records.txt` in the terminal. This one is from an early test run, which is why it shows two students: the first was written with `"w"` and the second added with `"a"`, and their timestamps are 19 seconds apart.

![cat of the records file](./screenshots/02-cat-records-write-then-append.png)

### 3. Reading it back with "r"

```python
with open(file_name, "r") as file:
    records = file.read()
    print(records)
```

The screenshot shows the write block in the editor, and in the terminal below it the records printed back from the file. The entry at the top of that list is a student named `sunny` (roll 11, data science), added at 22:34:58.

![Write block and read-back](./screenshots/03-write-block-and-read-back.png)

### 4. Adding another student with "a"

```python
with open(file_name, "a") as file:
    file.write("Student Name: " + new_name + "\n")
    file.write("Roll Number: " + new_roll + "\n")
    file.write("Course Name: " + new_course + "\n")
    file.write("Date & Time Added: " + new_date_time + "\n")
    file.write("--------------------------------\n")
```

After the append, the program prints `New student record added successfully!`, lists all the records, and shows the file info. In this run there are two records (`Niru` and `none`) and the file is 274 bytes.

![Append result and file size](./screenshots/04-append-result-and-file-size.png)

### 5. Checking the real file

`ls` shows the file and its size, and `cat` shows exactly what's in it. By this point there are three records, and the file is 403 bytes. The third one (`sec`) was added at 22:52, several minutes after the other two, in a run where only the append part of the script was active.

![ls and cat of the final file](./screenshots/05-ls-and-cat-final-records.png)

### 6. File size with os.path.getsize()

```python
file_size = os.path.getsize(file_name)

print("File Information")
print("----------------")
print("File Name:", file_name)
print("File Size:", file_size, "bytes")
```

![getsize code and output](./screenshots/06-getsize-code-and-output.png)

The output here is short because the other sections of the script were commented out for this run. Only the banner and the file information ran, which matches the note at the top of the script about commenting out the modes you don't want.

## Do the file sizes add up?

The 274 and 403 bytes in the screenshots match what's actually in the file:

| Record | Size | Running total | Matches |
|---|---|---|---|
| Niru | 142 bytes | 142 | |
| none | 132 bytes | 274 | Screenshot 4 |
| sec | 129 bytes | 403 | Screenshots 5 and 6 |

One detail that explains the numbers: the file has 15 lines, and every line ends in two bytes (`\r\n`), not one. On Windows, Python turns each `\n` it writes into `\r\n`, so the file ends up a bit bigger than the visible text suggests.

## Things I noticed

- **Running the whole script wipes the file.** The first save uses `"w"`, so every complete run starts by emptying `student_records.txt`. The final file only contains `Niru`, `none` and `sec`. The earlier test records visible in the screenshots (the 21:56 and 22:34 ones) are gone. That's what the comment at the top of the script is warning about: comment out the parts you don't want before running.
- **The "file exists" check doesn't change anything.** It only prints a message. A better version would use `"a"` when the file already exists and `"w"` only when it doesn't, so the script would be safe to re-run.
- **There's no input validation.** One entry was saved with `none` as the name, roll number and course, and the program accepted it without complaint.
- **Plain text is easy to read but awkward to search.** Fine for this, but something like a CSV file or a database would suit anything bigger.

## Files in this folder

| File | What it is |
|---|---|
| `student_record_management.py` | The final script |
| `student_records.txt` | The records file as it was after my last run (3 records, 403 bytes) |
| `screenshots/` | Screenshots from each step above |

The script in this folder is the final version, so it can differ slightly from what's visible in the screenshots. I edited it between runs.
