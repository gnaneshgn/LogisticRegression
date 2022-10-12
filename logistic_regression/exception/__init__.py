from audioop import lin2adpcm
import os,sys

class LogisticRegressionException(Exception):

    def __init__(self,error_message:Exception,error_detail:sys):
        super().__init__(error_message)


    @staticmethod
    def get_detailed_message(error_message:Exception,error_detail:sys):

        """
                error_message: Exception Object
                error_detail: Object of system module
        """
        _,_,exception_traceback=sys.exc_info()
        line_number=exception_traceback.tb_frame.f_lineno
        file_name=exception_traceback.tb_frame.f_code.co_filename
        error_message="Error occured in script{} at line number {} error message:{}".format(file_name,line_number,error_message)
        return error_message

    def __str__(self) -> str:
        return self.error_message

    def __repr__(self) -> str:
        return LogisticRegressionException.__name__.str()