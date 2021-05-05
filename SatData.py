"""
Author: Masud Hussain
Course: CS162
Assignment: 5C
"""

import json


class SatData:

    def __init__(self):

        """
        Opens the sat.json file when a SatData object is created and reads info from file.
        JSON data is stored in sat_dictionary and then file is closed.
        """

        with open("sat.json", "r") as infile:
            sat_dictionary = json.load(infile)
        self._sat_dictionary = sat_dictionary

    def save_as_csv(self, dbn_list):

        """
        Takes an input of a list of dbns.
        Hard codes the column headers to the output.csv file.
        Searches through the json file to find the matching information.
        Wraps each value from the dictionary in double quotes and separates them with commas.
        Outputs the formatted row to the output.csv file

        :param dbn_list:
        :return: output the matching dbn information to output.csv
        """

        column_list = ["ddDBN", "School Name", "Number of Test Takers", "Critical Reading Mean", "Mathematics Mean", "Writing Mean"]
        for items in column_list:
            columns = ','.join(map(str, column_list))
        with open('output.csv', 'w') as outfile:
            outfile.write(str(columns) + '\n')

        for keys in self._sat_dictionary["data"]:
            for items in keys:
                for dbns in dbn_list:
                    if items == dbns:

                        values = ','.join([str(f'"{keys[i]}"') for i in range(keys.index(dbns), len(keys))])

                        with open('output.csv', 'a') as outfile:
                            outfile.write(str(values) + '\n')
