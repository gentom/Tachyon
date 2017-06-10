#
#  Tachyon
#  parser.py
#
#  Created on 03/06/17
#  Ryan Maugin <ryan.maugin@adacollege.org.uk>
#

from ast import literal_eval # To perform ast literal eval to figure out a strings data type
import constants # for constants like tachyon keywords and datatypes

class Parser(object):

    def parse(self, token_stream):
        """ Parsing

        This will parse the tokens given as argument and turn the sequence of tokens into 
        abstract syntax trees

        Args:
         token_stream (list) : The tokens produced by lexer
        """
        print('---------------------------------------------')
        print(token_stream)
        print('---------------------------------------------')

        # Complete Abstract Syntax tree
        source_ast = [{ 'main': [] }]

        # This will hold the token index we are parsing at
        token_index = 0

        # Loop through each token
        while token_index < len(token_stream):

            # Set the token values in variables for clearer and easier debugging and readability
            token_type = token_stream[token_index][0]
            token_value = token_stream[token_index][1]

            # This will check for an if statement token
            #if token_type == 'IDENTIFIER' and token_value.lower() == 'if':
            #    source_ast['main'][0].append(self.parse_if_statement(token_stream[token_index:len(token_stream)]))

            # This will parse for a vraible decleration token
            if token_type == 'DATATYPE' and token_value.lower() in constants.DATATYPE:
                source_ast[0]['main'].append(self.parse_variable_decleration(token_stream[token_index:len(token_stream)]))

            # Increment token index by 1 when a loop finishes
            token_index += 1
        
        print(source_ast)


    def parse_if_statement(self, token_stream):
        """ Parsing If Statement

        This will parse through an if statement and create it's abstract tree and handle any
        syntax error

        Args:
            token_stream (list) : List of tokens starting from where if statement was found

        Returns:
            AST : The if statement abstract syntax tree
        """
        print("IF STATEMENT")


    def parse_variable_decleration(self, token_stream):
        """ Parsing Variable decleration

        This will parse through a variable decleration and create it's abstract tree and handle any
        syntax errors

        Args:
            token_stream (list) : List of tokens starting from where if statement was found

        Returns:
            AST : The variable decleration abstract syntax tree
        """

        # Will hold the vraible decleration abstract syntax tree being built
        ast = []

        # Keeps track of the index within variable decleration
        index = 0

        for item in token_stream:
            
            # This will add one every loop to the index of the var decleration
            index += 1

            # This will get the variable type
            if index == 1:

                # This will check if the token for varibale type is valid
                if item[1] in constants.DATATYPE: ast.append({ 'VariableDeclerator': [ {'type': item[1]} ] })
                else: print('VARIBALE TYPE ERROR IN PARSER!')
            
            # This will check for the variable name
            if index == 2:

                # This will check to make sure that the name of the doesn't start wih a number
                if not item[1][0].isdigit():  ast[0]['VariableDeclerator'].append({ 'name': item[1] })

                # This will print an error if variable begins with a number
                else: print('Illegal Variable Name "' + item[1] + '" variable name cannot begind with a number')

            # This will check the variable value but will skip the equal sign
            if index == 4:

                # Check if the value is the same value as the datatype in decleration
                if str(type(literal_eval(item[1]))) == "<class " + "'" + ast[0]['VariableDeclerator'][0]['type'] + "'>":
                    ast[0]['VariableDeclerator'].append({ 'value': item[1] })

                # TODO If it is not the same then throw an exception not a print
                else: print("TypeError: Variable value does not conform to data type of " + str(type(literal_eval(item[1]))))
                
            # If the for loop reaches the end statement then break because it is the end of the var decleration
            if item[1] == ';': break
        
        # Append this var declerating ast to the complete source ast
        return ast


    def parse_print(self, token_stream):
        """ Parsing print

        This will parse through a variable decleration and create it's abstract tree and handle any
        syntax errors

        Args:
            token_stream (list) : List of tokens starting from where if statement was found

        Returns:
            AST : The variable decleration abstract syntax tree
        """
        print("PRINT")