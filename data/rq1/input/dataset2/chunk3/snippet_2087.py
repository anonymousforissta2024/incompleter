#Source: https://stackoverflow.com/questions/56035632/peewee-model-has-no-select-attribute-error
active_courses = Course.select().where(Course.active == True)