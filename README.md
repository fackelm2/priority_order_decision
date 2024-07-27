# priority-order-decision
## Command line tool to prioritise tasks (written in Python)
A simple commandline-tool to prioritise tasks by scoring them. <br>
Prioritise your tasks by comparing two of them and deciding which one to prioritise.<br>
Enter your tasks or task list, answer which task to prioritise and get the priority list.

### Download & Run

```sh 
git clone https://github.com/fackelm2/priority-order-decision
cd df.priority-order-decision
df.priority-order-decision.py
```

### Usage Guide
<pre>
usage: priority-order-decision.py [-h] [-i INPUT_FILE] [-o OUTPUT_FILE] [-f {text,csv,html}] [-d] [-v] [--version] mytask [mytask ...]

Options for command-line tool priority-order-decision.py

positional arguments:
  mytask                list of tasks space separeted or filename [-i <filename>] with one task per line

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT_FILE, --input_file INPUT_FILE
                        set input filename
  -o OUTPUT_FILE, --output_file OUTPUT_FILE
                        set output filename (default <console>)
  -f {text,csv,html}, --output_format {text,csv,html}
                        set output format (default <text>)
  -d, --debug           set debug mode
  -v, --verbose         set verbose mode
  --version             print version

</pre>


### Examples
I want to learn something about Python, Amazon AWS Cloud, Malware Analysis and Android - but with what should i begin?
<pre>
priority-order-decision.py python aws android malware_analysis
task 1 : malware_analysis
task 2 : android
enter more important task 1 or 2: 2

task 1 : malware_analysis
task 2 : aws
enter more important task 1 or 2: 1

task 1 : malware_analysis
task 2 : python
enter more important task 1 or 2: 2

task 1 : android
task 2 : aws
enter more important task 1 or 2: 1

task 1 : android
task 2 : python
enter more important task 1 or 2: 2

task 1 : aws
task 2 : python
enter more important task 1 or 2: 2

[['python', 3], ['aws', 0], ['android', 2], ['malware_analysis', 1]]

</pre>
<pre>
The result of my choices is the following order:
1. Python
2. Android
3. Malware Analysis
4. Amazon AWS Cloud
</pre>

