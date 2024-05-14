#Source: https://stackoverflow.com/questions/75224761/multiprocess-package-baseprocess-typeerror-baseprocess-popen
def __initialise_strat_class_obj(self, *, strat_name: str, strat_config: StratInput): 
    try:
        strat_instance = strat_class_dict[strat_name](strat_args=self.strat_args, strat_input=strat_config)  # dynamically fetching & calling the class
        strat_instance.init()
    except Exception as e:
        self._logger.error(f"unable to init strategy `{strat_config.id}`: {e}")
        return False 
    strat_process = Process(target=strat_instance.run)
    strat_process.start()# starting the class method in a separate process