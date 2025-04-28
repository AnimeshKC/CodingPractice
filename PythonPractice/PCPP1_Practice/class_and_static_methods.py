class LuxuryWatch:
    _watches_created = 0
    
    def __init__(self):
        self.__class__._watches_created += 1
        self._engraving = None
    @classmethod
    def get_number_of_watches_created(cls):
        return cls._watches_created
    
    """
    This method just returns the data on whether the validation passed or failed.
    It's up to the consumer of this call to raise exceptions.
    """
    @staticmethod 
    def validate_engraving(engraving):
        if not isinstance(engraving, str):
            return (False, TypeError, "Engraving must be a string")
        value_error_list = []
        if len(engraving) > 40:
            value_error_list.append("Engraving cannot exceed 40 characters")
        if not engraving.isalnum():
            value_error_list.append("Engraving can only have alphenumeric characters")
        if value_error_list:
            return (False, ValueError, "; ".join(value_error_list))
        return (True, None, "Engraving passes")
        
            
    @classmethod
    def create_engraving_watch(cls, engraving):
        passes, error, error_message = cls.validate_engraving(engraving)
        if not passes:
            raise error(error_message)
        new_watch = cls()
        new_watch._engraving = engraving
        return new_watch

if __name__ == "__main__":
    default_watch = LuxuryWatch()
    engraved_watch = LuxuryWatch.create_engraving_watch("ValidEngraving")

    try: 
        non_string_engraving = LuxuryWatch.create_engraving_watch(56)
    except TypeError as e:
        print(f"An error with the type of entered value: {e}")
        
    try:
        #This one contains more Value Errors
        too_long_non_alphanumeric_engraved_watch = LuxuryWatch.create_engraving_watch("the class may allow you to create a watch with a dedicated engraving (text). ")
    except ValueError as e:
        print(f"An error with the content of entered value: {e}")

    try:
        non_alpha_engraving = LuxuryWatch.create_engraving_watch("foo@baz.com")
    except ValueError as e:
        print(f"An error with the content of entered value: {e}")

    print(f"{LuxuryWatch.get_number_of_watches_created()} watches created")

    #use the validator outside of the class, without an exception. This can be used by the user however they wish
    print(LuxuryWatch.validate_engraving("TooLongInTermsOfCharacterCountWithoutHavingAnySpacesToTestSingleError"))
