#Source: https://stackoverflow.com/questions/68443649/attributeerror-object-has-no-attribute-task-id-when-using-celery
@app.task(ignore_result=True, name='pydolphin.dolphin.tasks.tasks')
def pull_channel_impl(channel_id, level):
    print(app.current_task.task_id)
    rss = RssSource()
    source = rss.select_channel_by_id(channel_id)
    RssPullImpl.single_rss_hub(source, rss, level)