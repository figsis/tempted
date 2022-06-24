from ._builtin import Page
from .models import Constants
from .stuff import UnderstandingQuestionsPage
import random





class InstructionsTask1(Page):
    form_model = 'player'



class Task1(Page):
    form_model = 'player'
    form_fields = ['task1','timeSpent']
    timer_text = 'Time remaining:'


   # def is_displayed(self):
    #    return self.player.task1 is None

    def before_next_page(self):
        self.player.set_payoffs1()
        payoff1_self=self.player.payoff1_self
        payoff1_charity=self.player.payoff1_charity


    #def app_after_this_page(player, dana_timed, the_button):
     #   if player.treatment=="No Button":
      #      return dana_timed
       # else:
        #    return the_button

#class SummaryTask1(Page):
 #   form_model = 'player'

  #  def vars_for_template(self):
   #     return dict(
    #                payoff1_self=self.player.payoff1_self,
      #              payoff1_charity=self.player.payoff1_charity,
     #               )

    #def before_next_page(self):
     #   import time
        # start timer to find out how long a person is stuck on next wait page
        #  self.player.participant.vars["wait_page_arrival"] = time.time()
        # self.player.participant.vars["too_long"] = False

page_sequence = [


    InstructionsTask1,
    Task1,
    #SummaryTask1
]
