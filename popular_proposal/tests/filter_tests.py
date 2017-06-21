# coding=utf-8
from popular_proposal.filters import (ProposalWithoutAreaFilter,
                                      ProposalWithAreaFilter)
from popular_proposal.tests import ProposingCycleTestCaseBase
from popular_proposal.models import PopularProposal
from elections.models import Area
from popular_proposal.forms.form_texts import TOPIC_CHOICES


class PopularProposalFilterTestCase(ProposingCycleTestCaseBase):
    def setUp(self):
        super(PopularProposalFilterTestCase, self).setUp()
        self.algarrobo = Area.objects.get(id='algarrobo-5602')
        self.p1 = PopularProposal.objects.create(proposer=self.fiera,
                                                 area=self.algarrobo,
                                                 data=self.data,
                                                 title=u'P1',
                                                 clasification=TOPIC_CHOICES[1][0]
                                                 )
        self.p2 = PopularProposal.objects.create(proposer=self.fiera,
                                                 area=self.algarrobo,
                                                 data=self.data,
                                                 title=u'P2',
                                                 clasification=TOPIC_CHOICES[2][0]
                                                 )
        self.p3 = PopularProposal.objects.create(proposer=self.fiera,
                                                 area=self.algarrobo,
                                                 data=self.data,
                                                 title=u'P3',
                                                 clasification=TOPIC_CHOICES[3][0]
                                                 )

    def test_filter_proposals(self):
        data = {'clasification': TOPIC_CHOICES[1][0]}
        f = ProposalWithoutAreaFilter(data=data)
        self.assertIn(self.p1, f.qs)
        self.assertNotIn(self.p2, f.qs)
        self.assertNotIn(self.p2, f.qs)

    def test_filter_with_area(self):

        data = {'clasification': TOPIC_CHOICES[1][0], 'area': self.algarrobo}
        f = ProposalWithAreaFilter(data=data)
        self.assertIn(self.p1, f.qs)
        self.assertNotIn(self.p2, f.qs)
        self.assertNotIn(self.p2, f.qs)

        data = {'area': self.algarrobo}
        f = ProposalWithAreaFilter(data=data)
        self.assertIn(self.p1, f.qs)
        self.assertIn(self.p2, f.qs)
        self.assertIn(self.p2, f.qs)