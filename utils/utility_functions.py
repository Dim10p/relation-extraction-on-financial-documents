import ast

def convert_to_list(value):
    try:
        return ast.literal_eval(value)
    except (SyntaxError, ValueError):
        return value

def create_input(token_list, e1_start, e2_start, ner_list):
  output_text = ""
  for i in range(0, len(token_list)):
    if i == e1_start:
      text = str(ner_list[i]) + " "+ str(token_list[i])
    elif i == e2_start:
      text = str(ner_list[i]) + " "+ str(token_list[i])
    else:
      text = token_list[i]
    output_text= output_text + " " + text
  return output_text