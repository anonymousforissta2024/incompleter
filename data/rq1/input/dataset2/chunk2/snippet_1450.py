#Source: https://stackoverflow.com/questions/70382456/typeerror-function-takes-x-positional-argument-but-x-were-given
class Handler(watchdog.events.PatternMatchingEventHandler):
    def on_deleted(self, event):
        print("Watchdog received deleted event - % s." % event.src_path)