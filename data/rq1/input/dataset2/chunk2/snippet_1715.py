#Source: https://stackoverflow.com/questions/52681646/python-typeerror-nonetype-object-is-not-iterable-but-every-variables-defined
if slackinput_list and len(slackinput_list) > 0:
  user_answer, user_id, channel, event_type = parse_slack_useranswer(slackinput_list)
  #print(user_answer,user_id)#test
  if user_answer and user_id and user_id != 'U7GRT34H3' and event_type=="message":
    if user_answer=="1" or user_answer=="5":
      print(user_answer, user_id, user_count, total_mood, av_mood) #test
      #if user_id not in user_list:
      av_mood, user_count, total_mood = datamood(user_answer, user_id, user_count, total_mood, av_mood)