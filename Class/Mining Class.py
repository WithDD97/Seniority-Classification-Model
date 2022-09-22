class Mining:
    '''
    Summary line.
    Extended description of function
    Parameters:
    arg1 (int): Description of arg1
    Returns:
    int: Description of return value
    '''
    
    # this function extract years of experience and key word like "senior, ..." and return a dataframe with title, description, key_title, and years of experience
    
    def extractor_years (self,description):
        '''
        Summary line.
        Extended description of function
        Parameters:
        arg1 (int): Description of arg1
        Returns:
        int: Description of return value
        '''

        # Years
        # extract the years form the jobs description by taking the last caracter before '+ years'
        return description.apply(lambda x : x.split("+ years")[0].split()[-1] )

        
    # Key title
    # this function search for a key word in a job title and extract it
    
    def extract_key_title(self, title):
        """.gifdf
        """

        # designated key title that we are looking for
        adj = {'entry', 'i', 'intern', 'junior', 'intership',
       'associate', 'ii', 'staff', 'mid','mid-senior',
       'sr','sr.','senior', 'lead','manager','iii', 'director', 'executive', 'president', 'vice'}

        # Extract key words for jobs title
        for word in title.lower().split():
            if word in adj: 
                return word
        return None
     
    def cleaner_years(self,years):

        """.gifdf
        """

        years.replace('3-5','4',inplace=True)
        years.replace('(5','5',inplace=True)
        years.replace('5-7','6',inplace=True)
        years.replace('7-10','8',inplace=True)
        years.replace('2-3','3',inplace=True)
        years.replace('(3','3',inplace=True)
        years.replace('(2','2',inplace=True)
        years.replace('(10','10',inplace=True)
        years.replace('1-3','2',inplace=True)
        years.replace('2-5','4',inplace=True)
        years.replace('8-10','9',inplace=True)
        years.replace('5-10','8',inplace=True)
        years.replace('Five','5',inplace=True)
        years.replace('1-2','2',inplace=True)
        
        listofyears =  ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20']
        
        return years.apply(lambda x : None if x not in listofyears else int(x))
