#!/usr/bin/env python
"""
df.priority-order-decision.py: A Python script (command-line interface) to order your tasks
Development under Python 3.7 (venv)
the intent was a fast first try - not a clean code ;-) 15.11.2021
"""
__version__ = "0.2.20250405"
__author__ = "Dietmar Fackelmann"
__email__ = "fackelm2@nmit.de"
__license__ = "GPLv3"

priorityorderdecisionVersion = 'Version 0.1_20230915-3'


import time
import argparse
import logging as log

# set time string to actual time for debug and verbose time information
time_str = time.strftime("%Y%m%d-%H%M%S")
priority_order_decision_version = 'Version 0.2 [2021-11-15]'


def no_nl(s): return str(s).replace("\r", "").replace("\n", "")   # clean strings (delete carriage return)


def verbose_log():
    # todo - error
    if debug:
        print(time_str + " verbose_log()")

    if verbose:
        log.basicConfig(format="%(level_name)s: %(message)s", level=log.DEBUG)
        log.info("verbose output.")
    else:
        log.basicConfig(format="%(level_name)s: %(message)s")

    log.info("This should be verbose.")
    log.warning("This is a warning.")
    log.error("This is an error.")


def argument_parser():  # command line tool - parse commands
    global debug
    global verbose
    global priority_order_decision_version

    parser = argparse.ArgumentParser(description='Options for command-line tool df.priority-order-decision.py')
    parser.add_argument('mytask', type=str, nargs='+', default=False,
                        help='list of tasks space separeted or filename [-i <filename>] with one task per line')
    parser.add_argument('-i', '--input_file', type=str, default=False,
                        help='set input filename')
    parser.add_argument('-o', '--output_file', type=str, default=False,
                        help='set output filename (default <console>)')
    parser.add_argument('-f', '--output_format', choices=['text', 'csv', 'html'], default='text',
                        help='set output format (default <text>)')
    parser.add_argument('-d', '--debug', action='store_true', default=False,
                        help='set debug mode')
    parser.add_argument('-v', '--verbose', action='count', default=0,
                        help='set verbose mode')  # counts each optional v (-v -vv -vvv ..)
    parser.add_argument('--version', action='store_true', default=False,
                        help='print version')

    args = parser.parse_args()

    if args.debug:  # debug output for argument parser
        print(time_str + ' ' + "argument_parser() args: " + str(args))
        print(time_str + ' ' + "argument_parser() mytask: " + str(args.mytask))
        print(time_str + ' ' + "argument_parser() input_file: " + str(args.input_file))
        print(time_str + ' ' + "argument_parser() output_file: " + str(args.output_file))
        print(time_str + ' ' + "argument_parser() output_format: " + str(args.output_format))
        print(time_str + ' ' + "argument_parser() verbose: " + str(args.verbose))
        print(time_str + ' ' + "argument_parser() debug: " + str(args.debug))

    # print Version and exit (--version)
    if args.version:
        print(priority_order_decision_version)
        exit()

    if (args.input_file is False) and (args.mytask is False):
        print("I need at least a list of 2 tasks (-h for help)")
        exit()

    # until now just a list of tasks OR (excluded or) a filename is implemented
    if args.input_file and args.mytask:
        print("ERROR - Arguments allowed: filename <-i FILE> (excluded OR)")
        exit()

    return args


def get_tasklist_from_file(filename):
    if debug:
        print(time_str + " get_tasklist_from_file()")
    # create list of apps from text file (each line a package name)
    try:
        file = open(filename, "r")  # open text file with package names
        mytask = []  # list of package names from input file

        for line in file:
            try:
                mytask.append(no_nl(line))  # add task from file to list package names
            except ValueError:
                pass
        file.close()
        return mytask
    except IOError:
        print("Cannot find file: ", filename)
        exit()


def prioritize_tasklist(tasklist):
    priotasklist = []
    value = 0
    l = len(tasklist)
    if debug:
        print(time_str + ' prioritize_tasklist() begin work')
        print(time_str + ' prioritize_tasklist() tasklist type: ' + str(type(tasklist)))
    if verbose:
        print(time_str + ' ask for prio: ' + str(tasklist))
    # frage für jedes Element ob es wichtiger ist als eines der anderen Argumente, und erhöhe jeweils die Punkte

    if verbose:
        print(time_str + ' prioritize_tasklist() len(task): ' + str(len(tasklist)))

    # for each task in the list create a counter
    for task in tasklist:                   # generate tasklist with task and prio of task
        if verbose:
            print(time_str + ' prioritize_tasklist() task: ' + str(task))
        priotask = [task, value]            # generate tuppel of each task : task and prionumber
        priotasklist.append(priotask)       # generate list of task tuppels
        if verbose:
            print(time_str + 'prioritize_tasklist() priotasklist: ' + str(priotasklist))

    # for each task compare with the next task and ask user which task to prefer, add  one point to chosen task
    while l >= 2:
        k = l - 1
        while k >= 1:
            print('task 1 : ' + str(priotasklist[l-1][0]))
            print('task 2 : ' + str(priotasklist[k-1][0]))
            num = int(input('prefer task 1 or task 2: '))
            if (num == 1):
                priotasklist[l-1][1] = priotasklist[l-1][1] + 1
                if debug:
                    print(priotasklist[l-1][1])
            if (num == 2):
                priotasklist[k-1][1] = priotasklist[k-1][1] + 1
                if debug:
                    print(priotasklist[k-1][1])
            if not ((num == 1) or (num == 2)):
                print('TODO - false input')
            k = k - 1
        l = l - 1
    return priotasklist


def main():
    global debug
    global verbose

    arguments = argument_parser()
    debug = arguments.debug
    verbose = arguments.verbose

    if debug:
        print(time_str + ' main() argumentparser finished ..')
        print(time_str + ' main() verbose: ' + str(arguments.verbose))
        print(time_str + ' main() debug: ' + str(arguments.debug))

    if verbose >= 1:
        verbose = True
        if debug:
            print(time_str + ' main() verbose_level = ON')

    if arguments.input_file:
        tasklist = get_tasklist_from_file(str(arguments.input_file))
        if debug:
            print(time_str + ' ' + 'main() | type(tasklist) = ' + str(type(tasklist)) + ' tasklist = ' + str(tasklist))
        print('todo - get task list from file input_file: ' + str(arguments.input_file))
    else:
        if debug:
            print(time_str + ' main() get tasks from shell input')
        if verbose:
            print(time_str + ' main() read tasks from shell: ' + str(arguments.mytask))

    resultlist = prioritize_tasklist(arguments.mytask)

    if arguments.output_file:
        if debug:
            print(time_str + ' main() write to output_file:', arguments.output_file)
        print('todo - implement print results in file output_file: ' + str(arguments.output_file))
    else:
        print(resultlist)


if __name__ == '__main__':
    global debug
    global verbose

    main()

