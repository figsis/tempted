#from project._builtin import Page, WaitPage
from ._builtin import Page, WaitPage
from .models import Constants
from .models import Player


def vars_for_all_templates(self):
    return {
        'treatment': self.session.vars["treatment"]}


class SummaryTask1_(Page):
    pass


class Button(Page):
    form_model = 'player'
    form_fields = ['button','store_time']
    timeout_seconds = Constants.timer


    def before_next_page(self):
        self.player.set_payoffs()




class Payment(Page):
    form_model = 'player'
    def vars_for_template(self):
        return dict(
            payoff2_self=self.player.participant.vars["payoff2_self"],
            payoff2_charity=self.player.participant.vars["payoff2_charity"],
            too_long=self.player.participant.vars["too_long"]
        )

    #def get_questions(self):
     #   return self.player.get_questions_method()

class Survey(Page):
    form_model = 'player'
    form_fields = []

    #'q1_press', 'q_diff_press', 'q1_notpress', 'q_diff_notpress'

    def get_form_fields(self):

        if self.player.button==1:
            return ['q1', 'q11']

        elif self.player.button == 0:
            return ['q2', 'q22']
            #form_fields = []
        #if self.player.button==1:
             #   form_fields.append()
        #elif self.player.button==0 :
            #    form_fields.append('q1_notpress')
               # form_fields.append('q1_diff_notpress')
        #return form_fields


page_sequence = [SummaryTask1_,
    Button,
    Payment,
    Survey
]
