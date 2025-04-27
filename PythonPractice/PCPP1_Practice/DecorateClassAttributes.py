import functools 


def debug_identifier(class_):
    methods_list = dir(class_)
    for method_name in methods_list:
        if method_name.startswith("debug_"):
            original_method = getattr(class_, method_name)

            @functools.wraps(original_method)
            def new_method(self, *args, binded_method_name = method_name, binded_original_method = original_method, **kwargs):
                print(f"The debugging method, {binded_method_name} is being called.")
                return binded_original_method(self, *args, **kwargs)
            setattr(class_, method_name, new_method)
    return class_

@debug_identifier
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
    def debug_executions(self, should_print = True):
        debug_stats = {"original_value": self._original_val, "num_mutations": self._mutations,
                       "current_value": self._working_val, "delta": self._working_val - self._original_val,
                       "default_used": self._original_val == InfoDistribute.default_input_val,
                       "list_of_confusions": self._confusions}
        if should_print:
            print(debug_stats)
        return debug_stats
    def debug_confusing_indicator(self, confusion_str="I don't understand"):
        self._confusions.append(confusion_str)
        self._mutations += 1 #the confusions list is modified
        print("We have been notified that you have been confused by this class.")


if __name__ == "__main__":
    info_obj  = InfoDistribute(14)
    b = info_obj + 92
    info_obj += 8
    info_obj += 12
    info_obj.debug_executions()
    info_obj.debug_confusing_indicator("Help me. I am John and I don't get it.")
    info_obj.debug_executions()

    