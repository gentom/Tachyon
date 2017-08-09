#
#  Tachyon
#  objgen.py
#
#  Created on 06/08/17
#  Ryan Maugin <ryan.maugin@adacollege.org.uk>
#

class ObjectGenerator():


    def __init__(self, source_ast):
        # This will contain all the AST's in forms of dictionaries to help with creating AST object
        self.source_ast  = source_ast['main_scope']
        # This will hold the executable string of transplied tachyon code to python
        self.exec_string = ""
        


    def object_definer(self):
        """ Object Definer 
        
        This method will find all the different objects and call all the objects
        and pass in the ast dictionary to them to get a python string of code back
        which transpiles the tachyon source code into python
        
        returns:
            python_code (str) : This will written a string of python code
        """
        
        # Iterate through all ast dictionaries
        for ast in self.source_ast:
            # This will check check if the current AST dict is of which type
            if self.check_ast('VariableDecleration', ast):
                print('var')

            if self.check_ast('ConditionalStatement', ast):
                print('condition')

            if self.check_ast('PrebuiltFunction', ast):
                print('prebuilt')



    def check_ast(self, astName, ast):
        """ Call and Set Exec 
        
        This method will check if the AST dictionary item being looped through has the
        same key name as the `astName` argument
        
        args:
            astName (str)  : This will hold the ast name we are matching
            ast     (dict) : The dict which the astName match will be done against
        returns:
            True    (bool) : If the astName matches the one in `ast` arg
            False   (bool) : If the astName doesn't matches the one in `ast` arg
        """
        try:
            if ast[astName]: return True
        except: return False