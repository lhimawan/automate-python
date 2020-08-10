import re
def regexAppend(compile_string, input_text, output_list):
  basicRegex = re.compile(compile_string)
  basic = basicRegex.search(input_text).group(1)
  output_list.append(basic)
