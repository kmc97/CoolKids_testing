import numpy as np
import logging


logging.basicConfig(filename='logging.txt', format='%(asctime)s %(message)s', datefmt='%m/%d/%Y &I:%M:%S %p', level=logging.DEBUG)

class Numbers:
    def __init__ (self, num_list= None):
        self.num_list = num_list

    def sum_list(self):
        """Function takes list of integers and returns the sum of the list

        :param num_list: list of integers
        :returns sum_: the sum of the list of integers
        :raises TypeError: checks for incorrect data types in list
        :raises ValueError: checks for improper values that cause errors
        :raises ImportError: checks for correct importation
        """
        
        logging.info('INFO: starting sum_list function')

        try:
            sum_ = np.sum(self.num_list)
            return sum_
        except TypeError:
            raise TypeError
            logging.debug('DEBUG: check data type of list in sum_list')
        except ValueError:
            raise ValueError
            logging.debug('DEBUG: check values of list, correct data type but unexpected value')
        except ImportError:
            raise ImportError
            logging.debug('DEBUG: issue importing files make sure virtual env activated')

    def find_min_max(self):
        """Function takes list of integers and returns min and max in a tuple

        :param num_list: list of integers
        :returns max_min: a tuple containing the max and min of a list
        :raises TypeError: checks for incorrect data types in list
        :raises ValueError: checks for improper values that cause errors
        :raises ImportError: checks for correct importation
        """ 
        
        logging.info('Info: starting find_min_max function')

        try:
            min_ = np.min(self.num_list)
            max_ = np.max(self.num_list)
            min_max = (min_, max_)
            return min_max
        except TypeError:
            raise TypeError
            logging.debug('Debug: check data type of list')
        except ValueError:
            raise ValueError
            logging.debug('DEBUG: check values of list, unexpected value')
        except ImportError:
            raise ImportError
            logging.debug('DEBUG: issue importing files, make sure virtual env turned on')
       
    def maxdiff(self):
        """Function takes a list of integers and returns the maximum difference between two adjacent numbers

        :param num_list: list of integers
        :returns maxdiff: maximum difference
        :raises TypeError: checks for incorrect data types in list
        :raises ValueError: checks for imporper/unexpected values in list
        :raises ImportError: checks for correct importation 
        """

        logging.info('Info: starting max_diff function')

        try:
            diff = np.diff(self.num_list)
            maxdiff = diff.max()
            return maxdiff
        except TypeError:
            raise TypeError
            logging.debug('Debug: check data type of list')
        except ValueError:
            raise ValueError
            logging.debug('DEBUG: check values of list, unexpected value')
        except ImportError:
            raise ImportError
            logging.debug('DEBUG: issue importing files')
  

def main(num_list):
    x = Numbers(num_list)
    sum_ = x.sum_list()
    min_max = x.find_min_max()
    maxdiff= x.maxdiff()
    print(sum_, min_max, maxdiff)

main([1,2,3])
