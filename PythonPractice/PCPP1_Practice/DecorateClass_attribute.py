import functools 


def debug_preprocess(method):

    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        print(f"The debugging method, {method.__name__} is being called.")
        if kwargs:
            print(f"The user provided extra info:")
            if not hasattr(self, f"{method.__name__}_extra_data"):
                setattr(self, f"{method.__name__}_extra_data", [{"kwargs": kwargs, "args": args}])
            else:
                getattr(self, f"{method.__name__}_extra_data").append([{"kwargs": kwargs, "args": args}])
            
            print(kwargs)
        return method(self, *args, **kwargs)
    return wrapper


class InfoDistribute:
    default_input_val = 9
    def __init__(self, input_val = default_input_val):
        self._working_val = input_val
        self._original_val = input_val
        self._mutations = 0
        self._confusions = []
    def __add__(self, val):
        try:
            return self._working_val + val
        except TypeError:
            print(f"No update was made. {val} is not an applicable type.")
            return self._working_val
    def __iadd__(self, val):
        try:
            self._working_val += val
            self._mutations += 1
        except TypeError:
            print(f"No update was made. {val} is not an applicable type.")
        return self
    @debug_preprocess
    def debug_executions(self, should_print = True, **kwargs):
        debug_stats = {"original_value": self._original_val, "num_mutations": self._mutations,
                       "current_value": self._working_val, "delta": self._working_val - self._original_val,
                       "default_used": self._original_val == InfoDistribute.default_input_val,
                       "list_of_confusions": self._confusions}
        if should_print:
            print(debug_stats)
        return debug_stats
    @debug_preprocess
    def debug_confusing_indicator(self, confusion_str="I don't understand", **kwargs):
        self._confusions.append(confusion_str)
        self._mutations += 1 #the confusions list is modified
        print("We have been notified that you have been confused by this class.")


if __name__ == "__main__":
    info_obj  = InfoDistribute(14)
    b = info_obj + 92
    info_obj += 8
    info_obj += 12
    info_obj.debug_executions()
    info_obj.debug_confusing_indicator("Help me. I am John and I don't get it.", extra_info = "I want help ASAP.")
    info_obj.debug_executions()
    info_obj.debug_confusing_indicator("I actually do understand.", extra_info="But I like being custom.")
    print(info_obj.debug_confusing_indicator_extra_data)

    