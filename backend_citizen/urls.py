from django.conf.urls import patterns, url
from backend_citizen.views import (IndexView,
                                   PopularProposalTemporaryDataUpdateView,
                                   UpdateUserView,
                                   OrganizationDetailView,
                                   OrganizationCreateView,
                                   DoYouBelongToAnOrgView,
                                   )
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required


urlpatterns = patterns('',
                       url(r'^$',
                           IndexView.as_view(),
                           name='index'),
                       url(r'^organization/(?P<slug>[-\w]+)/?$',
                           OrganizationDetailView.as_view(),
                           name='organization'),
                       url(r'^update/?$',
                           UpdateUserView.as_view(),
                           name='update_my_profile'),
                       url(r'^create_organization/?$',
                           OrganizationCreateView.as_view(),
                           name='create_org'),
                       url(r'^do_you_belong_to_an_org/?$',
                           DoYouBelongToAnOrgView.as_view(),
                           name='do_you_belong_to_an_org'),
                       url(r'^update_temporary_data/(?P<pk>[\d]+)/?$',
                           PopularProposalTemporaryDataUpdateView.as_view(),
                           name='temporary_data_update'),
                       )
