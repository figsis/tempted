
from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)
import random


doc = """
This is the button game. 
"""


class Constants(BaseConstants):
    name_in_url = 'the_button'
    num_rounds = 1
    players_per_group=None
    # Button payoffs
    optionA = [5, 15]  # bonus payments NO CLICK [receiver, charity]
    optionB = [10, 0]  # bonus payment CLICK
    optionA0=optionA[0]
    optionA1=optionA[1]
    optionB0=optionB[0]
    optionB1=optionB[1]
    timer = 30  # in seconds

class Subsession(BaseSubsession):
    def creating_session(self):
        for player in self.get_players():
                #if 'treatment' in self.session.config:
                    #player.treatment = self.session.config["treatment"]
                    #else:
                    #player.treatment = random.choice(["ButtonA", "ButtonB"])
                    #        self.session.vars["treatment"] = player.treatment

            player.treatment = random.choice(["ButtonA", "ButtonB"])
            self.session.vars["treatment"] = player.treatment
            player.participant.vars["payoff2_self"] = ""
            player.participant.vars["payoff2_charity"] = ""
            player.participant.vars["payoff2_self_p"] = ""
            player.participant.vars["payoff2_charity_p"] = ""
            player.participant.vars["too_long"] = False


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    treatment = models.StringField()
    button = models.BooleanField(initial=0)
    store_time = models.FloatField()  # for the timer
    payoff2_self = models.StringField()  # payoff task 2 (button)
    payoff2_charity = models.StringField()  # payoff task 2 (button)
    q1 = models.StringField(label='Why did you decide to press the button?')
    q11 = models.StringField(label='How difficult was it to decide to press the button?', choices=[[1, "Very difficult"], [2, "Difficult"], [3, "Not difficult"],
                   [4, "Easy"], [5, "Very easy"]])
    q2= models.StringField(label='Why did you decide not to press the button?')
    q22 = models.StringField(label='How difficult was it to decide not to press the button?', choices=[[1, "Very difficult"], [2, "Difficult"], [3, "Not difficult"],
                   [4, "Easy"], [5, "Very easy"]])
   # english = models.IntegerField(
    #    label="Please rate your English on a percentage scale between 0 and 100.",
     #   min=0,
      #  max=100,
       # blank=True,
    #initial=None
    #)
    #def get_questions_method(self):
     #   if self.button == 1:
      #      questions = [{
       #         'question': ,    },
            #{
             #   'question': 'How difficult was it to decide to press the button?',
              #  'choices': [[1, "Very difficult"], [2, "Difficult"], [3, "Not difficult"],
               #            [4, "Easy"], [5, "Very easy"]]
           # }]
        #elif self.button == 0:
         #   questions = [{
          #      'question': 'Why did you decide to press the button?',
           # },
            #{
            #    'question': 'How difficult was it to decide to press the button?',
            #   'choices': [[1, "Very difficult"], [2, "Difficult"], [3, "Not difficult"],
            #               [4, "Easy"], [5, "Very easy"]]
            #}]
            #return questions


    def set_payoffs(self):
        if not self.participant.vars["too_long"]:
            #if self.session.vars["treatment"] == "ButtonA":
            if self.treatment== "ButtonA":
                if self.button==1: #presing yields selfish option b
                    self.participant.vars["payoff2_self"] = Constants.optionB[0] #10
                    self.participant.vars["payoff2_charity"] = Constants.optionB[1] #0
                    self.participant.vars["payoff2_self_p"] = str(self.participant.vars["payoff2_self"]) + ' pound'
                    self.participant.vars["payoff2_charity_p"] = str(self.participant.vars["payoff2_charity"]) + 'pence'
                else: #not presing yields prosocial option a
                    self.participant.vars["payoff2_self"] = Constants.optionA[0] #5
                    self.participant.vars["payoff2_charity"] = Constants.optionA[1] #15
                    self.participant.vars["payoff2_self_p"] = str(self.participant.vars["payoff2_charity"]) + ' pence'
                    self.participant.vars["payoff2_charity_p"] = str(self.participant.vars["payoff2_self"]) + ' pence'
                self.payoff2_self = str(self.participant.vars["payoff2_self"])  # to store to the oTree database
                self.payoff2_charity = str(self.participant.vars["payoff2_charity"])
            #elif self.session.vars["treatment"] == "ButtonB":
            elif self.treatment == "ButtonB":
                if self.button==1: #pressing the button yields the prosocial action
                    self.participant.vars["payoff2_self"] = Constants.optionA[0]  #5
                    self.participant.vars["payoff2_charity"] = Constants.optionA[1] #15
                    self.participant.vars["payoff2_self_p"] = str(self.participant.vars["payoff2_charity"]) + ' pence'
                    self.participant.vars["payoff2_charity_p"] = str(self.participant.vars["payoff2_self"]) + ' pence'
                else: #not pressing the button yields the selfish action
                    self.participant.vars["payoff2_self"] = Constants.optionB[0] #10
                    self.participant.vars["payoff2_charity"] = Constants.optionB[1] #0
                    self.participant.vars["payoff2_self_p"] = str(self.participant.vars["payoff2_self"]) + ' pound'
                    self.participant.vars["payoff2_charity_p"] = str(self.participant.vars["payoff2_charity"]) + 'pence'
                self.payoff2_self = str(self.participant.vars["payoff2_self"])  # to store to the oTree database
                self.payoff2_charity = str(self.participant.vars["payoff2_charity"])
           # elif self.session.vars["treatment"] == "No Button":
            #    if self.task2 == "A":
             #       self.payoff2_self = Constants.dana2A_self
              #      self.payoff2_charity = Constants.dana2A_other
               # elif self.task2 == "B":
                #    self.payoff2_self = Constants.dana2B_self
                 #   self.payoff2_charity = Constants.dana2B_other
                    # to store for next app (button task + final payoffs)
               # self.payoff2_self = str(self.participant.vars["payoff2_self"])  # to store to the oTree database
                #self.payoff2_charity = str(self.participant.vars["payoff2_charity"])