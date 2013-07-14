voting_data = list(open("voting_record_dump109.txt"))
dems = [col[0] for col in [line.split() for line in voting_data] if col[1] == 'D']

## Task 1

def create_voting_dict():
    """
    Input: None (use voting_data above)
    Output: A dictionary that maps the last name of a senator
            to a list of numbers representing the senator's voting
            record.
    Example: 
        >>> create_voting_dict()['Clinton']
        [-1, 1, 1, 1, 0, 0, -1, 1, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         -1, 1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1, -1, 1, 1, 1]

    This procedure should return a dictionary that maps the last name
    of a senator to a list of numbers representing that senator's
    voting record, using the list of strings from the dump file (strlist). You
    will need to use the built-in procedure int() to convert a string
    representation of an integer (e.g. '1') to the actual integer
    (e.g. 1).

    You can use the split() procedure to split each line of the
    strlist into a list; the first element of the list will be the senator's
    name, the second will be his/her party affiliation (R or D), the
    third will be his/her home state, and the remaining elements of
    the list will be that senator's voting record on a collection of bills.
    A "1" represents a 'yea' vote, a "-1" a 'nay', and a "0" an abstention.

    The lists for each senator should preserve the order listed in voting data. 
    """
    votes = {}
    for line in list(open("voting_record_dump109.txt")):
        cols = line.split()
        senator = cols[0]
        votes[senator] = [int(c) for c in cols[3:] if c in ['-1','0','1']]
    return votes
    

#create voting dict for others
voting_dict = create_voting_dict()
print ("Task 1 create a voiting dict")
# print(voting_dict)

## Task 2

def policy_compare(sen_a, sen_b, voting_dict):
    """
    Input: last names of sen_a and sen_b, and a voting dictionary mapping senator
           names to lists representing their voting records.
    Output: the dot-product (as a number) representing the degree of similarity
            between two senators' voting policies
    Example:
        >>> voting_dict = {'Fox-Epstein':[-1,-1,-1,1],'Ravella':[1,1,1,1]}
        >>> policy_compare('Fox-Epstein','Ravella', voting_dict)
        -2
    """
    x = sum([x * y for x, y in zip(voting_dict[sen_a], voting_dict[sen_b])])
    return x


## Task 3

def most_similar(sen, voting_dict):
    """
    Input: the last name of a senator, and a dictionary mapping senator names
           to lists representing their voting records.
    Output: the last name of the senator whose political mindset is most
            like the input senator (excluding, of course, the input senator
            him/herself). Resolve ties arbitrarily.
    Example:
        >>> vd = {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
        >>> most_similar('Klein', vd)
        'Fox-Epstein'

    Note that you can (and are encouraged to) re-use you policy_compare procedure.
    """
    best_score = -10000
    best_sen = sen
    for k, v in voting_dict.items():
        if k==sen:
            continue
        score = policy_compare(sen, k, voting_dict)
        if score > best_score:
            best_score = score
            best_sen = k
    return best_sen
    

## Task 4

def least_similar(sen, voting_dict):
    """
    Input: the last name of a senator, and a dictionary mapping senator names
           to lists representing their voting records.
    Output: the last name of the senator whose political mindset is least like the input
            senator.
    Example:
        >>> vd = {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
        >>> least_similar('Klein', vd)
        'Ravella'
    """
    best_score = 10000
    best_sen = sen
    for k, v in voting_dict.items():
        if k==sen:
            continue
        score = policy_compare(sen, k, voting_dict)
        if score < best_score:
            best_score = score
            best_sen = k
    return best_sen
    
    

## Task 5
most_like_chafee    = most_similar('Chafee', voting_dict)
least_like_santorum = least_similar('Santorum', voting_dict)
print("Task 5 find most and least like senators")
print ('Most like Chafee: {0}'.format(most_like_chafee))
print ('Least like Santorum: {0}'.format(least_like_santorum))

print(policy_compare('Chafee', 'Jeffords', voting_dict))
print(policy_compare('Santorum', 'Feingold', voting_dict))
print(policy_compare('Martinez', 'Nelson1', voting_dict))



# Task 6

def find_average_similarity(sen, sen_set, voting_dict):
    """
    Input: the name of a senator, a set of senator names, and a voting dictionary.
    Output: the average dot-product between sen and those in sen_set.
    Example:
        >>> vd = {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
        >>> find_average_similarity('Klein', {'Fox-Epstein','Ravella'}, vd)
        -0.5
    """
    x = sum([policy_compare(sen, sen2, voting_dict) for sen2 in sen_set]) / len(sen_set)
    return x

def find_most_average_senator(sen_set, voting_dict):
    most_avg_name = ''
    most_avg = 0.0
    for sen in sen_set:
        curr_avg = find_average_similarity(sen, sen_set, voting_dict)
        if curr_avg > most_avg:
            most_avg = curr_avg
            most_avg_name = sen
    return most_avg_name

most_average_Democrat = find_most_average_senator(dems, voting_dict) # give the last name (or code that computes the last name)

print ("Task 6 Most Average Democrat: ", most_average_Democrat)


# Task 7

def find_average_record(sen_set, voting_dict):
    """
    Input: a set of last names, a voting dictionary
    Output: a vector containing the average components of the voting records
            of the senators in the input set
    Example: 
        >>> voting_dict = {'Klein': [-1,0,1], 'Fox-Epstein': [-1,-1,-1], 'Ravella': [0,0,1]}
        >>> find_average_record({'Fox-Epstein','Ravella'}, voting_dict)
        [-0.5, -0.5, 0.0]
    """
    sen_vote = [voting for voting in [voting_dict[sen] for sen in sen_set]]
    sen_count = len(sen_vote)
    vote_count = len(sen_vote[0])
    vote_avg = [0.0]*vote_count
    for i in range(vote_count):
        vote_avg[i] = sum([vote[i] for vote in sen_vote]) / sen_count
    return vote_avg


average_Democrat_record = find_average_record(dems, voting_dict)
print("Task 7 Senators and Average Votes")
print(dems)
print(average_Democrat_record)

# Task 8

def bitter_rivals(voting_dict):
    """
    Input: a dictionary mapping senator names to lists representing
           their voting records
    Output: a tuple containing the two senators who most strongly
            disagree with one another.
    Example: 
        >>> voting_dict = {'Klein': [-1,0,1], 'Fox-Epstein': [-1,-1,-1], 'Ravella': [0,0,1]}
        >>> bitter_rivals(voting_dict)
        ('Fox-Epstein', 'Ravella')
    """
    sen_1 = ''
    sen_2 = ''
    lowest_score = 0.0
    for sen_a in voting_dict.keys():
        for sen_b in voting_dict.keys():
            if sen_b == sen_a: continue
            curr_score = policy_compare(sen_a, sen_b, voting_dict)
            if curr_score < lowest_score:
                lowest_score = curr_score
                sen_1 = sen_a
                sen_2 = sen_b

    return (sen_1, sen_2)

print("Task 8 Bitter rivals")
print(bitter_rivals(voting_dict))


def best_friends(voting_dict):
    """
    Input: a dictionary mapping senator names to lists representing
           their voting records
    Output: a tuple containing the two senators who most strongly
            agree with one another.
    """
    sen_1 = ''
    sen_2 = ''
    best_score = 0.0
    for sen_a in voting_dict.keys():
        for sen_b in voting_dict.keys():
            if sen_b == sen_a: continue
            curr_score = policy_compare(sen_a, sen_b, voting_dict)
            if curr_score > best_score:
                best_score = curr_score
                sen_1 = sen_a
                sen_2 = sen_b

    return (sen_1, sen_2)


print("Task 8a Best Friends")
print(best_friends(voting_dict))


