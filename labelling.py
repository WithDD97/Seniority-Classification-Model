
class labelling:

    """
    Build a column call new label.
  
    by using year of experience and key word in job title
    
    Parameters:
    data (DataFrame): Table with with contain years of exp and key title columns
  
    Returns:
    DataFrame
    
    """

    def __init__(self, data):
        self.data = data

    
    def label(self,data):

        def Labelled(df):

            junior_keys = {'entry', 'i', 'intern', 'junior', 'intership'}
            mid_keys = {'associate', 'ii', 'staff', 'mid', 'mid-senior'}
            senior_keys = {'sr','sr.','senior', 'lead','manager','iii', 'director', 'executive', 'president', 'vice'}
            
            for word in df['Title'].lower().split():
                # If a job has a junior keyword then it is a junior job
                if word in junior_keys:
                    
                    return "Junior"
                    
                # If a job has a junior keyword and years of experience is less than 4 then it is a junior job
                elif word in mid_keys:
                    
                    if df['years of experience'] < 4 :
                        return "Junior"
                    else:
                        return "Senior"
                # If job title has senior keyword than it is a senior job
                elif word in senior_keys:
                    return "Senior"

                # when we don't have any key word in the title
                # less than 4n years of experience the job is a junior job
                else:
                    if df['years of experience'] < 4 :
                        return "Junior"
                    else:
                        return "Senior"
                        
        data['new_label'] = data.apply(Labelled, axis= 1)
        data_labelled = data.dropna(subset = ['new_label'])
        return data_labelled
