# -*- coding: utf-8 -*-
#!python3

import re
import os
import csv

#Initializes CSV file and writes header

output = open('output.csv', 'w', newline='', encoding='utf-8')
output_writer = csv.writer(output)
output_writer.writerow(["Path", "Document_Name", "Record_ID"])
#============================================================================
#Parses through folders

rootdir = r"I:/Cases"
for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            #excludes thumbs.db files
            if file ==("Thumbs.db"):
                continue
#============================================================================
#Retrieves Path and Document Name

            path = (subdir).replace("\\", "/")
            doc_name = file

#LOGIC FOR FINDING RECORD NAME ON FILES PRIOR TO 2014

            #Test for complete record id in folder name
            record_in_folder_complete_match = re.match(
                ".*(\d\d\d\d\.(\d)?(\d)?(\d)?(\d))("
                "([a-zA-Z])?([a-zA-Z])?([a-zA-Z!])).*$", subdir)

            #Stores record name from folder name
            record_in_folder_complete = re.sub(".*(\d\d\d\d\.(\d)?(\d)?(\d)?(\d)"
                                "[a-zA-Z!]).*$", "\\1",
                     subdir)

            #Test for complete record id in file name
            record_in_file_complete_match = re.match(
                ".*(\d\d\d\d[.](\d)?(\d)?(\d)?(\d))("
                "[a-zA-Z!]).*$", file)

            #Stores record name from file name

            record_in_file_complete = re.sub(".*(\d\d\d\d\.(\d)?(\d)?(\d)(\d)"
                                "[a-zA-Z!]).*$", "\\1",
                     file)


            #Test for record id in folder name without letters
            record_test = re.sub(".*(\d\d\d\d[.](\d)?(\d)?(\d)(\d)).*$",
                                 "\\1",
                                 subdir)
            #Test for record id in file name
            file_match = re.match(".*((\d)?(\d)?\d\d[.](\d)?(\d)?(\d)?(\d))("
                                "[a-zA-Z]).*$", file)

            if file_match != None:
                file_test = re.sub(".*((\d)?(\d)?\d\d[.](\d)?(\d)?(\d)?(\d))("
                                   "[a-zA-Z]).*$",
                                   "\\8",
                                     file)
            else:
                file_test = "Null"


#Handles 1979 and 1981, adding "19" to the record name

            if "1979" in subdir or "1981" in subdir:

                if file_match != None:
                    record_name = re.sub(".*(\d\d[.]\d\d\d\w).*$", "19" +"\\1",
                                     file)

                output_writer.writerow([path, doc_name, record_name])



            elif "1979" not in subdir\
            and "1981" not in subdir \
            and "2014" not in subdir \
            and "2015" not in subdir\
            and "2016" not in subdir \
            and "2017" not in subdir \
            and "2018" not in subdir:

                if record_in_folder_complete_match != None:
                     record_name = record_in_folder_complete

                     output_writer.writerow([path, doc_name, record_name])

                elif record_in_file_complete_match != None:
                     record_name = record_in_file_complete

                     output_writer.writerow([path, doc_name, record_name])

                elif file_match != None and record_test !=None:
                    record_name = record_test + file_test

                    output_writer.writerow([path, doc_name, record_name])

                else:
                    record_name = "NULL"

                    output_writer.writerow([path, doc_name, record_name])

 # LOGIC FOR FINDING RECORD NAME ON FILES FROM 2014+

            # Test for complete record id in folder name
            record_in_folder_complete_match = re.match(
                ".*(\d\d\d\d[-.](\d)(\d)(\d)(\d)(\d)?(\d)?)(\s)?("
                "([a-zA-Z])([a-zA-Z])([a-zA-Z!])).*$", subdir)

            # Stores record name from folder name
            record_in_folder_complete = re.sub(
                ".*(\d\d\d\d[-.](\d)(\d)(\d)(\d)(\d)?(\d)?(\s)?("
                "([a-zA-Z])([a-zA-Z])([a-zA-Z!]))).*$", "\\1", subdir)

            # Test for complete record id in file name
            record_in_file_complete_match = re.match(
                 ".*(\d\d\d\d[-.](\d)(\d)(\d)(\d)(\d)?(\d)?)("
                "([a-zA-Z])([a-zA-Z])?([a-zA-Z!])?).*$", file)

            # Stores record name from file name

            record_in_file_complete = re.sub(
                 ".*(\d\d\d\d[-.](\d)(\d)(\d)(\d)(\d)?(\d)?("
                "([a-zA-Z])([a-zA-Z])?([a-zA-Z!])?)).*$", "\\1", file)

#============================================================================

#PROVISORY (CURRENTLY NOT BEING USED)
            # Test for record id in folder name without letters
            record_test = re.sub(".*(\d\d\d\d[.-](\d)(\d)(\d)(\d)(\d)(\d)).*$",
                                 "\\1",
                                 subdir)
            # Test for record id in file name incomplete
            file_match = re.match(".*((\d)?(\d)?\d\d[.](\d)?(\d)?(\d)?(\d))("
                                  "[a-zA-Z]).*$", file)

            if file_match != None:
                file_test = re.sub(".*((\d)?(\d)?\d\d[.](\d)?(\d)?(\d)?(\d))("
                                   "[a-zA-Z]).*$",
                                   "\\8",
                                     file)
#============================================================================

# Handles records from 2014+

            if "2014" in subdir \
            or "2015" in subdir \
            or "2016" in subdir \
            or "2017" in subdir \
            or "2018" in subdir:
                if record_in_folder_complete_match != None:
                    record_name = record_in_folder_complete

                    output_writer.writerow([path, doc_name, record_name])

                elif record_in_file_complete_match != None:
                    record_name = record_in_file_complete

                    output_writer.writerow([path, doc_name, record_name])

                else:
                    record_name = "NULL"

                    output_writer.writerow([path, doc_name, record_name])

#============================================================================
#Closes CSV file

output.close()
