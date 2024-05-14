#Source: https://stackoverflow.com/questions/77660827/im-getting-typeerror-io-textiowrapper-object-is-not-subscriptable-on-my-chat
def AXIS():
  knowledge_base:dict = open('knowledge_base.json','r',errors = 'ignore')
  while True:
    user_input:str = input('You:')
    if user_input.lower() in ("q", "quit", "shut down", "shutdown", "cancel", "power off", "poweroff", "power down", "powerdown", "off", "turn off", "turnoff"):
      print("AXIS: powering down")
      break

    best_match: str | None = find_best_match(user_input, list['q("question") for q in knowledge_base.json("questions")'])
    if best_match:
      answer: str = get_answer_for_question(best_match, knowledge_base)
      print(f'AXIS: {answer}')
    else:
      print('AXIS: I don\'t know the answer. please teach me?')
      new_answer: str = input('Type the answer or "skip" to skip:  ')
      if new_answer.lower() != 'skip':
        knowledge_base["questions"].append({"question": user_input, "answer": new_answer})
        save_knowledge_base('knowledge_base.json', knowledge_base)
        print('AXIS: I have learned a new response!')

if __name__ =='__main__':
  AXIS()