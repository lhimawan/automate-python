import re
def RegexDataScan(input_data, output_list, regex):
  for i in range(len(input_data)):
    if regex.search(input_data[i]) == None:
      output_list.append('Null')
    else:
      output_list.append(regex.search(input_data[i]).group(0))
