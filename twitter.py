import math      
import string
import random
from twitterSqlCon import TWITTERSQLCONN    
from datetime import datetime
import os
import getopt,sys
from random import randrange



class TWITTER:
    NO_TIMER=0
    UNIFORM_TIMER=1
    EXP_TIMER=2
    EXP_TIMER_DECAY=3    
    CONS_FRIEND=4
    def __init__(self):
        #self.v_dirpath='D:\workspace\Data\Network data\citation network\Terms map\\'
        self.v_dirpath='/Users/biru/workspace/Twitter/'
        #self.v_dirpath='D:/workspace/Data/Network data/Digg/'
        self.v_sql = TWITTERSQLCONN()
        self.v_sql.openConn('localhost', 'root', 'cui', 'Twitter')

    def createTabs(self):
        #this function create all tables
        #self.v_sql.createTabFollowers()
        #self.v_sql.createTabUsers()
        #self.v_sql.createTabTweets()
        
        self.v_sql.createTabLinks()
        
    def loadCSVFiles(self):
        # user_id: user id
        # user_screen_name: user name
        # indegree: number of followers
        # outdegree: number of friends/followees
        # bad_user_id: alternate user id
        self.v_sql.loadCSVFile(self.v_dirpath + "distinct_users_from_search_table_real_map.csv", 'users', " (user_id, user_screen_name, indegree, outdegree, bad_user_id)")
        print "users-----"
        self.v_sql.commit()
        print "commit-----"
        
        
        #         Tweets
        # 
        # Table (in csv format) link_status_search_with_ordering_real_csv contains tweets with the following information
        # 
        # link: URL within the text of the tweet
        # id: tweet id
        # create_at: date added to the db
        # create_at_long
        # inreplyto_screen_name: screen name of user this tweet is replying to
        # inreplyto_user_id: user id of user this tweet is replying to
        # source: device from which the tweet originated
        # bad_user_id: alternate user id
        # user_screen_name: tweeting user screen name
        # order_of_users: tweet's index within sequence of tweets of the same URL
        # user_id: user id
        self.v_sql.loadCSVFile(self.v_dirpath + "link_status_search_with_ordering_real.csv", 'tweets', " (link, id, create_at, create_at_long,"\
                               + " inreplyto_screen_name, inreplyto_user_id, source, bad_user_id, user_screen_name, order_of_users, user_id)")
        print "tweets-----"
        self.v_sql.commit()
        print "commit-----"
        
        
    def cascadesDistribution(self, split, total):
        # each initial seed create a cascade (the cascade could be trivial: single node; or small: several nodes)
        CNUM=self.v_sql.storiesNum()
        
        # output it
        fileName=self.v_dirpath + 'twitter_cascade_size_distribution_' + str(split) + '_' + str(total) + '.txt'
        fo = open(fileName, "w+")
         
        fo.write("storyNum \t cascadeSize \t depth \n")
        
#        fileName2=self.v_dirpath + 'digg_cascade_steps_prob.txt'
#        fo2 = open(fileName2, "w+")
#        
#        fo2.write("storyNum \t level \t infected \t potential \n")
      
        fileName3=self.v_dirpath + 'twitter_influence_size_distribution_' + str(split) + '_' + str(total) + '.txt'
        fo3 = open(fileName3, "w+")
        
        fo3.write("storyNum \t influenceSize \t seedsNum \n")      
      
        
        start=(CNUM/total)*(split-1)+1
        end = (CNUM/total)*(split)
        if total==split:
            end=CNUM
        print start,end
        for i in range(start,end+1):
            # for each story
            print i,end        
            # find all cascades of this story
            (cascades) = self.v_sql.extractCascades(i)
            
            
            influenceSize=0
            for k in cascades.keys():
                fo.write(str(i))
                fo.write(" \t")
                size = cascades[k].treeSize()
                fo.write(str(size))
                influenceSize += size - 1
                fo.write(" \t")
                fo.write(str(cascades[k].treeDepth()))
                fo.write("\n")

            fo3.write(str(i))
            fo3.write("\t")
            fo3.write(str(influenceSize))
            fo3.write("\t")
            fo3.write(str(len(cascades)))
            fo3.write("\n")

#             startTime = self.v_sql.firstVoteTimeStory(i+1)
#             for k in seedsHist.keys():
#                 timediff = self.v_sql.hourDiff(startTime, seedsHist[k])
#                 fo.write(str(i))
#                 fo.write(" \t")
#                 fo.write(str(timediff))
#                 fo.write("\n")
            
        fo.close()
        fo3.close()        
        pass
        
     
    def cascadesDistribution2(self, start, end):
        # each initial seed create a cascade (the cascade could be trivial: single node; or small: several nodes)
        CNUM=self.v_sql.storiesNum()
        
        # output it
        fileName=self.v_dirpath + 'twitter_cascade_size_distribution_' + str(start) + '_' + str(end) + '.txt'
        fo = open(fileName, "w+")
         
        fo.write("storyNum \t cascadeSize \t depth \n")
        
#        fileName2=self.v_dirpath + 'digg_cascade_steps_prob.txt'
#        fo2 = open(fileName2, "w+")
#        
#        fo2.write("storyNum \t level \t infected \t potential \n")
      
        fileName3=self.v_dirpath + 'twitter_influence_size_distribution_' + str(start) + '_' + str(end) + '.txt'
        fo3 = open(fileName3, "w+")
        
        fo3.write("storyNum \t influenceSize \t seedsNum \n")      
      
        
        print start,end
        for i in range(start,end+1):
            # for each story
            print i,end        
            # find all cascades of this story
            (cascades) = self.v_sql.extractCascades(i)
            
            
            influenceSize=0
            for k in cascades.keys():
                fo.write(str(i))
                fo.write(" \t")
                size = cascades[k].treeSize()
                fo.write(str(size))
                influenceSize += size - 1
                fo.write(" \t")
                fo.write(str(cascades[k].treeDepth()))
                fo.write("\n")

            fo3.write(str(i))
            fo3.write("\t")
            fo3.write(str(influenceSize))
            fo3.write("\t")
            fo3.write(str(len(cascades)))
            fo3.write("\n")

#             startTime = self.v_sql.firstVoteTimeStory(i+1)
#             for k in seedsHist.keys():
#                 timediff = self.v_sql.hourDiff(startTime, seedsHist[k])
#                 fo.write(str(i))
#                 fo.write(" \t")
#                 fo.write(str(timediff))
#                 fo.write("\n")
            
        fo.close()
        fo3.close()        
        pass 
     
        
def main(argv):
    optlist,args=getopt.getopt(argv,'')
    twitter=TWITTER()
    #twitter.createTabs()
    #twitter.loadCSVFiles()
    #twitter.cascadesDistribution(int(args[0]), int(args[1]))
    twitter.cascadesDistribution2(int(args[0]), int(args[1]))
    
if __name__=="__main__":
    main(sys.argv[1:])