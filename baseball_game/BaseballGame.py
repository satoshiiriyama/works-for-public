## Making Player class to create player instances
class Player():   
    def __init__(self, name, salary, batting_ave, one_base_ave, two_base_ave, 
                 three_base_ave, home_run_ave, stolen_base_percentage):
        self.name = name
        self.salary = salary
        self.batting_ave = batting_ave
        self.one_base_ave = one_base_ave
        self.two_base_ave = two_base_ave
        self.three_base_ave = three_base_ave
        self.home_run_ave = home_run_ave
        self.stolen_base_percentage = stolen_base_percentage
        player_list.append(self)

    ## Making __str__ method to print instances   
    def __str__(self):
        return "{0:11s}: {1:>3d}M USD,  Batting Ave{2:>6.3f} (1Base{3:>6.3f}, 2Base{4:>6.3f}, 3Base{5:>6.3f}, HR{6:>6.3f}), Steal Success{7:>3.0f}%"\
                                  .format(self.name, self.salary, self.batting_ave, self.one_base_ave, 
                                          self.two_base_ave, self.three_base_ave, self.home_run_ave, 
                                          self.stolen_base_percentage*100)

## Making MakingTedeam class to create choose players and make line-up
class MakingTeam(): 
    ## A method to view all the available players   
    def viewplayers(self):
        input("Let's play a baseball game!! First, enter any key to get money to buy players: ")
        budgetlist = [60, 70, 80, 90, 100, 110, 120] 
        self.budget = random.choice(budgetlist)
        print("You got {}M USD !!".format(self.budget))
        input("Now you will select 9 players within your budget. Enter any key to see the available players: ")
        print("-------------------------------------------------------------")
        for player in player_list:
            print(player)

    ## A method to select players based on allocated budget 
    def selectplayers(self):
        spent = 0

        ## Looping players in Player_list 
        for player in player_list:
            status = True
            while status == True:
                select_or_not = input("Now you have {}M USD left. Do you select {} {}M USD? (Y or N)".format(self.budget-spent, player.name, player.salary)) 
                ## In case you select this player             
                if select_or_not.lower() == "y":
                    if spent + player.salary > self.budget:
                        print("You don't have enough fund to select this player. Now you have {}M USD left"\
                              .format((self.budget-spent)))
                    else:
                        teamplayers_list.append(player)
                        player_list.remove(player)
                        spent += player.salary
                        status = False

                    if len(teamplayers_list) == 9:
                        print("")
                        print("You selected 9 players.")
                        print("")
                        print("--------------------Your Players--------------------")
                        for teamplayer in teamplayers_list:
                            print("{0:11s}: Batting Ave{1:>6.3f} (1Base{2:>6.3f}, 2Base{3:>6.3f}, 3Base{4:>6.3f}, HR{5:>6.3f}), Steal Success{6:>3.0f}%"\
                                  .format(teamplayer.name, teamplayer.batting_ave, teamplayer.one_base_ave, 
                                          teamplayer.two_base_ave, teamplayer.three_base_ave, teamplayer.home_run_ave, 
                                          teamplayer.stolen_base_percentage*100))
                        break

                ## In case you don't select this player        
                elif select_or_not.lower() == "n":
                    player_list.append(player)
                    print("Let's see the next player.")
                    status = False

                else:
                    print("Invalid input. Please enter [Y]es or [N]o")
                    
            else:
                continue
            break

    ## A method to select Computer's 9 players                            
    def computerplayers(self):
        top_nine_left = player_list[0:9]
        for player in top_nine_left:
            computerplayers_list.append(player)
            
        print("")
        print("Computer selected 9 players.")
        print("")
        print("-----------------Computer's Players-----------------")
        for computerplayer in computerplayers_list:
            print("{0:11s}: Batting Ave{1:>6.3f} (1Base{2:>6.3f}, 2Base{3:>6.3f}, 3Base{4:>6.3f}, HR{5:>6.3f}), Steal Success{6:>3.0f}%"\
                                  .format(computerplayer.name, computerplayer.batting_ave, computerplayer.one_base_ave, 
                                          computerplayer.two_base_ave, computerplayer.three_base_ave, computerplayer.home_run_ave, 
                                          computerplayer.stolen_base_percentage*100))
    
    ## A method to decide batting order          
    def battingorder(self):
        print("Now you will decide the batting order. Enter 1 to 9.")
        
        for player in teamplayers_list:
            status = True
            while status == True:
                try:
                    order = int(input("What is the batting order of {}: ".format(player.name)))-1
                    if order not in range(0, 9):
                        print("Invalid input. Please enter 1 to 9.")
                        status = True
                    elif teamplayers_list_order[order] != None:
                        print("This order is already occupied. Please select an available order")
                        status = True
                    else:
                        teamplayers_list_order[order] = player
                        status = False
                except:
                    print("Invalid input. Please enter 1 to 9.")
                    
        print("You have decided the batting order")
        print("")
        print("------------------Your Team Batting Order------------------")
        print("")
        counter = 1
        for player in teamplayers_list_order:
            print("{}: {}".format(counter, player.name))
            counter += 1
            
        print("")
        print("")
        print("----------------Computer Team Batting Order----------------")
        print("")
        counter = 1
        for player in computerplayers_list:
            print("{}: {}".format(counter, player.name))
            counter += 1

## Creating inning class to defice what to do in each inning
class Inning():
    def __init__(self, playerlist, inningname, computer=False, batterorder=0, 
                 outcount=0, firstbase=None, secondbase=None, thirdbase=None, inningscore=0):
        self.playerlist = playerlist
        self.inningname = inningname
        self.computer = computer
        self.batterorder = batterorder
        self.outcount = outcount
        self.firstbase = firstbase
        self.secondbase = secondbase
        self.thirdbase = thirdbase
        self.inningscore = inningscore

    ## A method to call out a new inning  
    def startingcall(self):
        print("------------------------------------------------")
        print("Starting {} inning".format(self.inningname))
        return self.showbases()

    ## A method to make a decision whether hitting or stealing            
    def decision(self):
        ## In case a runner is on 1st base           
        if self.firstbase!=None and self.secondbase==None and self.thirdbase==None:
            status = True
            while status==True:
                if self.computer == False:
                    action = input("Now batting {}. Enter h to hit the ball or enter s to steal base: "\
                                   .format(self.playerlist[self.batterorder].name))
                elif self.computer == True:
                    actionlist = ["s", "h", "h", "h", "h", "h", "h"]
                    action = random.choice(actionlist)
                    if action == "h":
                        print("Now batting {}. Computer chose to hit"\
                              .format(self.playerlist[self.batterorder].name))
                    elif action == "s":
                        print("Now batting {}. Computer chose to steal base"\
                              .format(self.playerlist[self.batterorder].name))        
                    
                if action.lower() == "s":
                    status = False
                    return self.steal1()
                elif action.lower() == "h":
                    status = False
                    return self.batting()
                else:
                    print("You entered invalid letter")

        ## In case runners are on 1st base and 2nd base            
        elif self.firstbase!=None and self.secondbase!=None and self.thirdbase==None:
            status = True
            while status==True:
                if self.computer == False:
                    action = input("Now batting {}. Enter h to hit the ball or enter s to steal base: "\
                                   .format(self.playerlist[self.batterorder].name))
                elif self.computer == True:
                    actionlist = ["s", "h", "h", "h", "h", "h", "h"]
                    action = random.choice(actionlist)
                    if action == "h":
                        print("Now batting {}. Computer chose to hit"\
                              .format(self.playerlist[self.batterorder].name))
                    elif action == "s":
                        print("Now batting {}. Computer chose to steal base"\
                              .format(self.playerlist[self.batterorder].name))        
                               
                if action.lower() == "s":
                    status = False
                    return self.steal2()
                elif action.lower() == "h":
                    status = False
                    return self.batting()
                else:
                    print("You entered invalid letter")

        ## In case runner is on 2ns base                               
        elif self.firstbase==None and self.secondbase!=None and self.thirdbase==None:
            status = True
            while status==True:
                if self.computer == False:
                    action = input("Now batting {}. Enter h to hit the ball or enter s to steal base: "\
                                   .format(self.playerlist[self.batterorder].name))
                elif self.computer == True:
                    actionlist = ["s", "h", "h", "h", "h", "h", "h"]
                    action = random.choice(actionlist)
                    if action == "h":
                        print("Now batting {}. Computer chose to hit"\
                              .format(self.playerlist[self.batterorder].name))
                    elif action == "s":
                        print("Now batting {}. Computer chose to steal base"\
                              .format(self.playerlist[self.batterorder].name))        
                                   
                if action.lower() == "s":
                    status = False
                    return self.steal2()
                elif action.lower() == "h":
                    status = False
                    return self.batting()
                else:
                    print("You entered invalid letter")            

        ## In case runners are on 1st base and 3rd base         
        elif self.firstbase!=None and self.secondbase==None and self.thirdbase!=None:
            status = True
            while status==True:
                if self.computer == False:
                    action = input("Now batting {}. Enter h to hit the ball or enter s to steal base: "\
                                   .format(self.playerlist[self.batterorder].name))
                elif self.computer == True:
                    actionlist = ["s", "h", "h", "h", "h", "h", "h"]
                    action = random.choice(actionlist)
                    if action == "h":
                        print("Now batting {}. Computer chose to hit"\
                              .format(self.playerlist[self.batterorder].name))
                    elif action == "s":
                        print("Now batting {}. Computer chose to steal base"\
                              .format(self.playerlist[self.batterorder].name))        
                                   
                if action.lower() == "s":
                    status = False
                    return self.steal1()
                elif action.lower() == "h":
                    status = False
                    return self.batting()
                else:
                    print("You entered invalid letter")
                                                 
        else:
            status = True
            while status==True:
                if self.computer == False:
                    action = input("Now batting {}. Enter h to hit the ball: "\
                                   .format(self.playerlist[self.batterorder].name))
                elif self.computer == True:
                    action = "h"
                    print("Now batting {}. Computer hit the ball: "\
                          .format(self.playerlist[self.batterorder].name))
                                     
                if action.lower() == "h":
                    status = False
                    return self.batting()
                else: 
                    print("You entered invalid letter")

    # 1st runner is running                      
    def steal1(self):
        # Making random pickup of "success" which meet steal success %
        steallist = []
        successtimes = int(self.firstbase.stolen_base_percentage*100)
        failuretimes = 100 - successtimes     
        for i in range(0, successtimes):
            steallist.append("success")
        for i in range(0, failuretimes):
            steallist.append("failure")    
        stealresult = random.choice(steallist)
        
        if stealresult == "success":
            print("Stolen base succeeded!!")
            self.secondbase = self.firstbase
            self.firstbase = None
            return self.showbases() 
            
        else:
            print("Stolen base failed!!")
            self.secondbase = None
            self.firstbase = None
            self.outcount += 1
            if self.outcount == 3:
                print("3 outs. Score of this inning: {}".format(self.inningscore))
                print("Go to next inning")
                print("------------------------------------------------") 
            elif self.outcount < 3:
                return self.showbases() 

    # 2nd runner is running                        
    def steal2(self):
        # Making random pickup of "success" which meet steal success %
        steallist = []
        successtimes = int(self.secondbase.stolen_base_percentage*100)
        failuretimes = 100 - successtimes     
        for i in range(0, successtimes):
            steallist.append("success")
        for i in range(0, failuretimes):
            steallist.append("failure")
            
        stealresult = random.choice(steallist)
        
        if stealresult == "success":
            print("Stolen base succeeded!!")
            self.thirdbase = self.secondbase
            self.secondbase = self.firstbase
            self.firstbase = None
            return self.showbases()       
        else:
            print("Stolen base failed!!")
            self.thirdbase = None
            self.secondbase = self.firstbase
            self.firstbase = None
            self.outcount += 1
            if self.outcount == 3:
                print("3 outs. Score of this inning: {}".format(self.inningscore))
                print("Go to next inning")
                print("------------------------------------------------")                    
            elif self.outcount < 3:
                return self.showbases() 
                      
    # A method for batting             
    def batting(self):
        # Making random pickup of batting result which meet each % of the instance
        battinglist = []
        onebasetimes = int(self.playerlist[self.batterorder].one_base_ave*1000)
        twobasetimes = int(self.playerlist[self.batterorder].two_base_ave*1000)
        threebasetimes = int(self.playerlist[self.batterorder].three_base_ave*1000)
        homeruntimes = int(self.playerlist[self.batterorder].home_run_ave*1000)
        outtimes = 1000 - (onebasetimes + twobasetimes + threebasetimes + homeruntimes)
        for i in range(0, onebasetimes):
            battinglist.append("onebase")
        for i in range(0, twobasetimes):
            battinglist.append("twobase")
        for i in range(0, threebasetimes):
            battinglist.append("threebase")
        for i in range(0, homeruntimes):
            battinglist.append("homerun")
        for i in range(0, outtimes):
            battinglist.append("out")
        
        battingresult = random.choice(battinglist)
        
        # In case of Single hit
        if battingresult == "onebase":
            print("{} hit one-base hit !!".format(self.playerlist[self.batterorder].name))
            if self.thirdbase != None:
                self.inningscore += 1
            self.thirdbase = self.secondbase
            self.secondbase = self.firstbase
            self.firstbase = self.playerlist[self.batterorder]
            
            if self.batterorder == 8:
                self.batterorder = 0
            else:
                self.batterorder += 1
                
            return self.showbases() 

        # In case of 2-base hit              
        if battingresult == "twobase":
            print("{} hit two-base hit !!".format(self.playerlist[self.batterorder].name))
            if self.thirdbase != None:
                self.inningscore += 1
            if self.secondbase != None:
                self.inningscore += 1
                
            self.thirdbase = self.firstbase
            self.secondbase = self.playerlist[self.batterorder]
            self.firstbase = None
            
            if self.batterorder == 8:
                self.batterorder = 0
            else:
                self.batterorder += 1
                
            return self.showbases() 

        # In case of 3-base hit           
        if battingresult == "threebase":
            print("{} hit three-base hit !!".format(self.playerlist[self.batterorder].name))
            if self.thirdbase != None:
                self.inningscore += 1
            if self.secondbase != None:
                self.inningscore += 1
            if self.firstbase != None:
                self.inningscore += 1
                               
            self.thirdbase = self.playerlist[self.batterorder]
            self.secondbase = None
            self.firstbase = None
            
            if self.batterorder == 8:
                self.batterorder = 0
            else:
                self.batterorder += 1
                
            return self.showbases() 

        # In case of homerun                        
        if battingresult == "homerun":
            print("{} hit homerun !!".format(self.playerlist[self.batterorder].name))
            if self.thirdbase != None:
                self.inningscore += 1
            if self.secondbase != None:
                self.inningscore += 1
            if self.firstbase != None:
                self.inningscore += 1
            self.inningscore += 1
                               
            self.thirdbase = None
            self.secondbase = None
            self.firstbase = None
            
            if self.batterorder == 8:
                self.batterorder = 0
            else:
                self.batterorder += 1
                
            return self.showbases() 

        # In case of batter out    
        if battingresult == "out":
            print("{} is out.".format(self.playerlist[self.batterorder].name))
            self.outcount += 1
            
            if self.batterorder == 8:
                self.batterorder = 0
            else:
                self.batterorder += 1           
            
            if self.outcount == 3:
                print("3 outs. Score of this inning: {}".format(self.inningscore))
                print("Go to next inning")
                print("------------------------------------------------")
                                
            elif self.outcount < 3:
                return self.showbases() 

    # A method to show runners' position and who is batting        
    def showbases(self):
        anyinput = input("Enter any key to proceed")
        
        if self.firstbase != None:
            firstbaserunner = self.firstbase.name
        else:
            firstbaserunner = ""
            
        if self.secondbase != None:
            secondbaserunner = self.secondbase.name
        else:
            secondbaserunner = ""
            
        if self.thirdbase != None:
            thirdbaserunner = self.thirdbase.name
        else:
            thirdbaserunner = ""           
        print("-----------------------------------------------------------")         
        print("""
#                                               #
  #                 {2:^10s}                #
    #                   #                   #
      #               #   #               #
        #           #       #           #
          #       #           #       #
            #   #               #   #
  {3:>10s}  #                   # {1:<10s}
                #               #  
                  #           #
                    #       #
                      #   #
                        #         Inning score : {5:<5d}
                    {0:^10s}    Out count    : {4:<1d} 　　　　　　　　　　　　
""".format(self.playerlist[self.batterorder].name, firstbaserunner, secondbaserunner, 
           thirdbaserunner, self.outcount, self.inningscore)
)
        print("-----------------------------------------------------------")          
        return self.decision()


class Game_Engine():
    def __init__(self):  
        # Viewing available players, selecting players, deciding batting order      
        team = MakingTeam()
        team.viewplayers()
        team.selectplayers()
        team.computerplayers()
        team.battingorder()
        
        # Going thru each inning from 1st top through 9th bottom
        t1 = Inning(teamplayers_list_order, "1st Top")
        t1.startingcall()
        you_score = t1.inningscore      
        print("          1   2   3   4   5   6   7   8   9   R")
        print("You       {0:<4d}{1:<4s}{2:<4s}{3:<4s}{4:<4s}{5:<4s}{6:<4s}{7:<4s}{8:<4s}{9:<4d}"\
              .format(t1.inningscore, "", "", "", "", "", "", "", "", you_score))
        print("Computer  {0:<4s}{1:<4s}{2:<4s}{3:<4s}{4:<4s}{5:<4s}{6:<4s}{7:<4s}{8:<4s}{9:<4s}"\
              .format("", "", "", "", "", "", "", "", "", ""))
        
        b1 = Inning(computerplayers_list, "1st Bottom", True)
        b1.startingcall()
        com_score = b1.inningscore      
        print("          1   2   3   4   5   6   7   8   9   R")
        print("You       {0:<4d}{1:<4s}{2:<4s}{3:<4s}{4:<4s}{5:<4s}{6:<4s}{7:<4s}{8:<4s}{9:<4d}"\
              .format(t1.inningscore, "", "", "", "", "", "", "", "", you_score))
        print("Computer  {0:<4d}{1:<4s}{2:<4s}{3:<4s}{4:<4s}{5:<4s}{6:<4s}{7:<4s}{8:<4s}{9:<4d}"\
              .format(b1.inningscore, "", "", "", "", "", "", "", "", com_score))
        
        t2 = Inning(teamplayers_list_order, "2nd Top", batterorder=t1.batterorder)
        t2.startingcall()
        you_score += t2.inningscore        
        print("          1   2   3   4   5   6   7   8   9   R")
        print("You       {0:<4d}{1:<4d}{2:<4s}{3:<4s}{4:<4s}{5:<4s}{6:<4s}{7:<4s}{8:<4s}{9:<4d}"\
              .format(t1.inningscore, t2.inningscore, "", "", "", "", "", "", "", you_score))
        print("Computer  {0:<4d}{1:<4s}{2:<4s}{3:<4s}{4:<4s}{5:<4s}{6:<4s}{7:<4s}{8:<4s}{9:<4d}"\
              .format(b1.inningscore, "", "", "", "", "", "", "", "", com_score))
        
        b2 = Inning(computerplayers_list, "2nd Bottom", computer=True, batterorder=b1.batterorder)
        b2.startingcall()
        com_score += b2.inningscore   
        print("          1   2   3   4   5   6   7   8   9   R")
        print("You       {0:<4d}{1:<4d}{2:<4s}{3:<4s}{4:<4s}{5:<4s}{6:<4s}{7:<4s}{8:<4s}{9:<4d}"\
              .format(t1.inningscore, t2.inningscore, "", "", "", "", "", "", "", you_score))
        print("Computer  {0:<4d}{1:<4d}{2:<4s}{3:<4s}{4:<4s}{5:<4s}{6:<4s}{7:<4s}{8:<4s}{9:<4d}"\
              .format(b1.inningscore, b2.inningscore, "", "", "", "", "", "", "", com_score))
        
        t3 = Inning(teamplayers_list_order, "3rd Top", batterorder=t2.batterorder)
        t3.startingcall()
        you_score += t3.inningscore    
        print("          1   2   3   4   5   6   7   8   9   R")
        print("You       {0:<4d}{1:<4d}{2:<4d}{3:<4s}{4:<4s}{5:<4s}{6:<4s}{7:<4s}{8:<4s}{9:<4d}"\
              .format(t1.inningscore, t2.inningscore, t3.inningscore, "", "", "", "", "", "", you_score))
        print("Computer  {0:<4d}{1:<4d}{2:<4s}{3:<4s}{4:<4s}{5:<4s}{6:<4s}{7:<4s}{8:<4s}{9:<4d}"\
              .format(b1.inningscore, b2.inningscore, "", "", "", "", "", "", "", com_score))
        
        b3 = Inning(computerplayers_list, "3rd Bottom", computer=True, batterorder=b2.batterorder)
        b3.startingcall()
        com_score += b3.inningscore   
        print("          1   2   3   4   5   6   7   8   9   R")
        print("You       {0:<4d}{1:<4d}{2:<4d}{3:<4s}{4:<4s}{5:<4s}{6:<4s}{7:<4s}{8:<4s}{9:<4d}"\
              .format(t1.inningscore, t2.inningscore, t3.inningscore, "", "", "", "", "", "", you_score))
        print("Computer  {0:<4d}{1:<4d}{2:<4d}{3:<4s}{4:<4s}{5:<4s}{6:<4s}{7:<4s}{8:<4s}{9:<4d}"\
              .format(b1.inningscore, b2.inningscore, b3.inningscore, "", "", "", "", "", "", com_score))
        
        t4 = Inning(teamplayers_list_order, "4th Top", batterorder=t3.batterorder)
        t4.startingcall()
        you_score += t4.inningscore    
        print("          1   2   3   4   5   6   7   8   9   R")
        print("You       {0:<4d}{1:<4d}{2:<4d}{3:<4d}{4:<4s}{5:<4s}{6:<4s}{7:<4s}{8:<4s}{9:<4d}"\
              .format(t1.inningscore, t2.inningscore, t3.inningscore, t4.inningscore, "", "", "", "", "", you_score))
        print("Computer  {0:<4d}{1:<4d}{2:<4d}{3:<4s}{4:<4s}{5:<4s}{6:<4s}{7:<4s}{8:<4s}{9:<4d}"\
              .format(b1.inningscore, b2.inningscore, b3.inningscore, "", "", "", "", "", "", com_score))
        
        b4 = Inning(computerplayers_list, "4th Bottom", computer=True, batterorder=b3.batterorder)
        b4.startingcall()
        com_score += b4.inningscore    
        print("          1   2   3   4   5   6   7   8   9   R")
        print("You       {0:<4d}{1:<4d}{2:<4d}{3:<4d}{4:<4s}{5:<4s}{6:<4s}{7:<4s}{8:<4s}{9:<4d}"\
              .format(t1.inningscore, t2.inningscore, t3.inningscore, t4.inningscore, "", "", "", "", "", you_score))
        print("Computer  {0:<4d}{1:<4d}{2:<4d}{3:<4d}{4:<4s}{5:<4s}{6:<4s}{7:<4s}{8:<4s}{9:<4d}"\
              .format(b1.inningscore, b2.inningscore, b3.inningscore, b4.inningscore, "", "", "", "", "", com_score))
        
        t5 = Inning(teamplayers_list_order, "5th Top", batterorder=t4.batterorder)
        t5.startingcall()
        you_score += t5.inningscore       
        print("          1   2   3   4   5   6   7   8   9   R")
        print("You       {0:<4d}{1:<4d}{2:<4d}{3:<4d}{4:<4d}{5:<4s}{6:<4s}{7:<4s}{8:<4s}{9:<4d}"\
              .format(t1.inningscore, t2.inningscore, t3.inningscore, t4.inningscore, t5.inningscore, "", "", "", "", you_score))
        print("Computer  {0:<4d}{1:<4d}{2:<4d}{3:<4d}{4:<4s}{5:<4s}{6:<4s}{7:<4s}{8:<4s}{9:<4d}"\
              .format(b1.inningscore, b2.inningscore, b3.inningscore, b4.inningscore, "", "", "", "", "", com_score))
        
        b5 = Inning(computerplayers_list, "5th Bottom", computer=True, batterorder=b4.batterorder)
        b5.startingcall()
        com_score += b5.inningscore     
        print("          1   2   3   4   5   6   7   8   9   R")
        print("You       {0:<4d}{1:<4d}{2:<4d}{3:<4d}{4:<4d}{5:<4s}{6:<4s}{7:<4s}{8:<4s}{9:<4d}"\
              .format(t1.inningscore, t2.inningscore, t3.inningscore, t4.inningscore, t5.inningscore, "", "", "", "", you_score))
        print("Computer  {0:<4d}{1:<4d}{2:<4d}{3:<4d}{4:<4d}{5:<4s}{6:<4s}{7:<4s}{8:<4s}{9:<4d}"\
              .format(b1.inningscore, b2.inningscore, b3.inningscore, b4.inningscore, b5.inningscore, "", "", "", "", com_score))
        
        t6 = Inning(teamplayers_list_order, "6th Top", batterorder=t5.batterorder)
        t6.startingcall()
        you_score += t6.inningscore      
        print("          1   2   3   4   5   6   7   8   9   R")
        print("You       {0:<4d}{1:<4d}{2:<4d}{3:<4d}{4:<4d}{5:<4d}{6:<4s}{7:<4s}{8:<4s}{9:<4d}"\
              .format(t1.inningscore, t2.inningscore, t3.inningscore, t4.inningscore, t5.inningscore, t6.inningscore,\
                      "", "", "", you_score))
        print("Computer  {0:<4d}{1:<4d}{2:<4d}{3:<4d}{4:<4d}{5:<4s}{6:<4s}{7:<4s}{8:<4s}{9:<4d}"\
              .format(b1.inningscore, b2.inningscore, b3.inningscore, b4.inningscore, b5.inningscore, "", "", "", "", com_score))
        
        b6 = Inning(computerplayers_list, "6th Bottom", computer=True, batterorder=b5.batterorder)
        b6.startingcall()
        com_score += b6.inningscore        
        print("          1   2   3   4   5   6   7   8   9   R")
        print("You       {0:<4d}{1:<4d}{2:<4d}{3:<4d}{4:<4d}{5:<4d}{6:<4s}{7:<4s}{8:<4s}{9:<4d}"\
              .format(t1.inningscore, t2.inningscore, t3.inningscore, t4.inningscore, t5.inningscore, t6.inningscore,\
                      "", "", "", you_score))
        print("Computer  {0:<4d}{1:<4d}{2:<4d}{3:<4d}{4:<4d}{5:<4d}{6:<4s}{7:<4s}{8:<4s}{9:<4d}"\
              .format(b1.inningscore, b2.inningscore, b3.inningscore, b4.inningscore, b5.inningscore, b6.inningscore, \
                      "", "", "", com_score))
        
        t7 = Inning(teamplayers_list_order, "7th Top", batterorder=t6.batterorder)
        t7.startingcall()
        you_score += t7.inningscore       
        print("          1   2   3   4   5   6   7   8   9   R")
        print("You       {0:<4d}{1:<4d}{2:<4d}{3:<4d}{4:<4d}{5:<4d}{6:<4d}{7:<4s}{8:<4s}{9:<4d}"\
              .format(t1.inningscore, t2.inningscore, t3.inningscore, t4.inningscore, t5.inningscore, t6.inningscore,\
                      t7.inningscore, "", "", you_score))
        print("Computer  {0:<4d}{1:<4d}{2:<4d}{3:<4d}{4:<4d}{5:<4d}{6:<4s}{7:<4s}{8:<4s}{9:<4d}"\
              .format(b1.inningscore, b2.inningscore, b3.inningscore, b4.inningscore, b5.inningscore, b6.inningscore, \
                      "", "", "", com_score))
        
        b7 = Inning(computerplayers_list, "7th Bottom", computer=True, batterorder=b6.batterorder)
        b7.startingcall()
        com_score += b7.inningscore      
        print("          1   2   3   4   5   6   7   8   9   R")
        print("You       {0:<4d}{1:<4d}{2:<4d}{3:<4d}{4:<4d}{5:<4d}{6:<4d}{7:<4s}{8:<4s}{9:<4d}"\
              .format(t1.inningscore, t2.inningscore, t3.inningscore, t4.inningscore, t5.inningscore, t6.inningscore,\
                      t7.inningscore, "", "", you_score))
        print("Computer  {0:<4d}{1:<4d}{2:<4d}{3:<4d}{4:<4d}{5:<4d}{6:<4d}{7:<4s}{8:<4s}{9:<4d}"\
              .format(b1.inningscore, b2.inningscore, b3.inningscore, b4.inningscore, b5.inningscore, b6.inningscore, \
                      b7.inningscore, "", "", com_score))
        
        t8 = Inning(teamplayers_list_order, "8th Top", batterorder=t7.batterorder)
        t8.startingcall()
        you_score += t8.inningscore      
        print("          1   2   3   4   5   6   7   8   9   R")
        print("You       {0:<4d}{1:<4d}{2:<4d}{3:<4d}{4:<4d}{5:<4d}{6:<4d}{7:<4d}{8:<4s}{9:<4d}"\
              .format(t1.inningscore, t2.inningscore, t3.inningscore, t4.inningscore, t5.inningscore, t6.inningscore,\
                      t7.inningscore, t8.inningscore, "", you_score))
        print("Computer  {0:<4d}{1:<4d}{2:<4d}{3:<4d}{4:<4d}{5:<4d}{6:<4d}{7:<4s}{8:<4s}{9:<4d}"\
              .format(b1.inningscore, b2.inningscore, b3.inningscore, b4.inningscore, b5.inningscore, b6.inningscore, \
                      b7.inningscore, "", "", com_score))
        
        b8 = Inning(computerplayers_list, "8th Bottom", computer=True, batterorder=b7.batterorder)
        b8.startingcall()
        com_score += b8.inningscore       
        print("          1   2   3   4   5   6   7   8   9   R")
        print("You       {0:<4d}{1:<4d}{2:<4d}{3:<4d}{4:<4d}{5:<4d}{6:<4d}{7:<4d}{8:<4s}{9:<4d}"\
              .format(t1.inningscore, t2.inningscore, t3.inningscore, t4.inningscore, t5.inningscore, t6.inningscore,\
                      t7.inningscore, t8.inningscore, "", you_score))
        print("Computer  {0:<4d}{1:<4d}{2:<4d}{3:<4d}{4:<4d}{5:<4d}{6:<4d}{7:<4d}{8:<4s}{9:<4d}"\
              .format(b1.inningscore, b2.inningscore, b3.inningscore, b4.inningscore, b5.inningscore, b6.inningscore, \
                      b7.inningscore, b8.inningscore, "", com_score))
        
        t9 = Inning(teamplayers_list_order, "9th Top", batterorder=t8.batterorder)
        t9.startingcall()
        you_score += t9.inningscore       
        print("          1   2   3   4   5   6   7   8   9   R")
        print("You       {0:<4d}{1:<4d}{2:<4d}{3:<4d}{4:<4d}{5:<4d}{6:<4d}{7:<4d}{8:<4d}{9:<4d}"\
              .format(t1.inningscore, t2.inningscore, t3.inningscore, t4.inningscore, t5.inningscore, t6.inningscore,\
                      t7.inningscore, t8.inningscore, t9.inningscore, you_score))
        print("Computer  {0:<4d}{1:<4d}{2:<4d}{3:<4d}{4:<4d}{5:<4d}{6:<4d}{7:<4d}{8:<4s}{9:<4d}"\
              .format(b1.inningscore, b2.inningscore, b3.inningscore, b4.inningscore, b5.inningscore, b6.inningscore, \
                      b7.inningscore, b8.inningscore, "", com_score))
        
        if com_score > you_score:
            print("")
            print("Computer won!!")
            print("---------------FINAL RESULT---------------")
            print("          1   2   3   4   5   6   7   8   9   R")
            print("You       {0:<4d}{1:<4d}{2:<4d}{3:<4d}{4:<4d}{5:<4d}{6:<4d}{7:<4d}{8:<4d}{9:<4d}"\
                  .format(t1.inningscore, t2.inningscore, t3.inningscore, t4.inningscore, t5.inningscore, t6.inningscore,\
                      t7.inningscore, t8.inningscore, t9.inningscore, you_score))
            print("Computer  {0:<4d}{1:<4d}{2:<4d}{3:<4d}{4:<4d}{5:<4d}{6:<4d}{7:<4d}X   {8:<4d}"\
                  .format(b1.inningscore, b2.inningscore, b3.inningscore, b4.inningscore, b5.inningscore, b6.inningscore, \
                      b7.inningscore, b8.inningscore, com_score))

        else:
            b9 = Inning(computerplayers_list, "9th Bottom", computer=True, batterorder=b8.batterorder)
            b9.startingcall()
            com_score += b9.inningscore

            if you_score > com_score:
                print("")
                print("You won!!")
                print("")
            elif you_score == com_score:
                print("")
                print("Draw!!")
                print("")

            print("--------------------------FINAL RESULT--------------------------")
            print("          1   2   3   4   5   6   7   8   9   R")
            print("You       {0:<4d}{1:<4d}{2:<4d}{3:<4d}{4:<4d}{5:<4d}{6:<4d}{7:<4d}{8:<4d}{9:<4d}"\
                  .format(t1.inningscore, t2.inningscore, t3.inningscore, t4.inningscore, t5.inningscore, t6.inningscore,\
                      t7.inningscore, t8.inningscore, t9.inningscore, you_score))
            print("Computer  {0:<4d}{1:<4d}{2:<4d}{3:<4d}{4:<4d}{5:<4d}{6:<4d}{7:<4d}{8:<4d}{9:<4d}"\
                  .format(b1.inningscore, b2.inningscore, b3.inningscore, b4.inningscore, b5.inningscore, b6.inningscore, \
                      b7.inningscore, b8.inningscore, b9.inningscore, com_score))  

import random

player_list = []
teamplayers_list = []
teamplayers_list_order = [None, None, None, None, None, None, None, None, None]
computerplayers_list = []

# Making instances of Player
betts = Player("Betts", 25, 0.346, 0.185, 0.09, 0.01, 0.061, 0.8)
martinez = Player("Martinez", 20, 0.33, 0.186, 0.065, 0.004, 0.075, 0.2)
yelich = Player("Yelich", 12, 0.326, 0.192, 0.059, 0.012, 0.063, 0.7)
altuve = Player("Altuve", 13, 0.316, 0.234, 0.054, 0.004, 0.024, 0.7)
trout = Player("Trout", 26, 0.312, 0.17, 0.051, 0.008, 0.083, 0.8)
gennett = Player("Gennett", 12, 0.31, 0.214, 0.051, 0.005, 0.04, 0.1)
freeman = Player("Freeman", 10, 0.309, 0.194, 0.071, 0.006, 0.038, 0.3)
brantley = Player("Brantley", 8, 0.309, 0.212, 0.063, 0.004, 0.03, 0.4)
machado = Player("Machado", 15, 0.297, 0.179, 0.055, 0.005, 0.058, 0.5)
duffy = Player("Duffy", 8, 0.294, 0.241, 0.044, 0.002, 0.007, 0.4)
simmons = Player("Simmons", 16, 0.292, 0.217, 0.047, 0.009, 0.019, 0.6)
kemp = Player("Kemp", 4, 0.29, 0.19, 0.054, 0, 0.046, 0.1)
stanton = Player("Stanton", 18, 0.266, 0.147, 0.055, 0.002, 0.062, 0.3)
bellinger = Player("Bellinger", 4, 0.26, 0.153, 0.05, 0.013, 0.044, 0.6)
cruz = Player("Cruz", 3, 0.256, 0.148, 0.035, 0.002, 0.071, 0.1)
crawford = Player("Crawford", 4, 0.254, 0.171, 0.053, 0.004, 0.026, 0.4)
polanco = Player("Polanco", 2, 0.254, 0.121, 0.069, 0.013, 0.051, 0.5)
taylor = Player("Taylor", 2, 0.254, 0.142, 0.065, 0.015, 0.032, 0.5)
odor = Player("Odor", 2, 0.253, 0.162, 0.049, 0.004, 0.038, 0.3)
hernandez = Player("Hernandez", 2, 0.253, 0.198, 0.025, 0.005, 0.025, 0.3)
rojas = Player("Rojas", 3, 0.252, 0.203, 0.027, 0, 0.022, 0.3)
pillar = Player("Pillar", 3, 0.252, 0.141, 0.078, 0.004, 0.029, 0.3)
alonso = Player("Alonso", 2, 0.25, 0.169, 0.037, 0, 0.044, 0.1)
contreras = Player("Contreras", 0, 0.249, 0.16, 0.057, 0.011, 0.021, 0.1)
sanchez = Player("Sanchez", 0, 0.242, 0.155, 0.057, 0.017, 0.013, 0.1)
hamilton = Player("Hamilton", 0, 0.236, 0.179, 0.032, 0.018, 0.007, 0.1)
escobar = Player("Escobar", 0, 0.231, 0.171, 0.045, 0.006, 0.009, 0.1)
davis = Player("Davis", 0, 0.168, 0.109, 0.026, 0, 0.033, 0.1)

Game_Engine()