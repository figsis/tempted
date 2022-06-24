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



doc = """
This is the Dana task.
"""


class Constants(BaseConstants):
    name_in_url = 'dana'
    players_per_group = None
    num_rounds = 1

    # Dana payoffs
    danaA_self = 5
    danaB_self = 10
    danaA_other = 15
    danaB_other = 0


class Subsession(BaseSubsession):
    def creating_session(self):
        pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    timeSpent = models.FloatField()
    #browser = models.StringField()
    #understanding_questions_wrong_attempts = models.PositiveIntegerField()  # for all tasks
  #  uq_wrong_dana = models.PositiveIntegerField()  # storing UQ Dana
   # uq_wrong_dana2 = models.PositiveIntegerField()  # storing UQ Dana 2
    #reveal = models.BooleanField(blank=True)  # whether participant decides to reveal information in Dana task
    task1 = models.StringField(blank=True)  # whether participant takes selfish choice in Dana task
    #payoff_optionB = models.StringField()
    #total_payoff = models.FloatField()
    payoff1_self = models.IntegerField()  # payoff task 1 (dana)
    payoff1_charity = models.IntegerField()  # payoff task 1 (dana)



    def set_payoffs1(self):   # payoffs Task 1 (Dana)
        if self.task1 == "A":
            self.payoff1_self = Constants.danaA_self
            self.payoff1_charity = Constants.danaA_other
        elif self.task1 == "B":
            self.payoff1_self = Constants.danaB_self
            self.payoff1_charity = Constants.danaB_other
        # to store for next app (button task + final payoffs)
        self.participant.vars["payoff1_self"] = self.payoff1_self
        self.participant.vars["payoff1_charity"] = self.payoff1_charity
