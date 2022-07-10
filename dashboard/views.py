from django import shortcuts
from django.views import generic, View
from . import models
from bookingsys import models
from django.http import HttpResponse, JsonResponse
import json
from django.core.serializers import serialize
from datetime import datetime
# Create your views here.

current_date = datetime.now().date()

class DashboardHome(View):

    def get(self, request, *args, **kwargs):
        page_title = 'Home | Dashboard'
        page_type = 'dashboard'
        current_date = datetime.now().date()
        try:
            list_today_bookings = shortcuts.get_list_or_404(models.Booking.objects.filter(status=0))
            for i in list_today_bookings:
                time_slot = (i.timeslot.all())
                time_slot_date = (time_slot[0].date)
                if time_slot_date == current_date:
                    list_bookings.append(time_slot_date)
        except:
            list_today_bookings = 'No Data'

        list_bookings = []
        bookings_len = len(list_bookings)

        if request.user.is_staff:
            return shortcuts.render(
                request,
                "dashboard/home.html",
                {
                    'page_title': page_title,
                    'current_date': current_date,
                    'bookings_len': bookings_len,
                    'page_type': page_type,
                }
            )
        else:
            return shortcuts.redirect("account_login")

class DashboardTables(View):
    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            data_from_post = json.load(request)['post_data']
            print(data_from_post)
            post_type = data_from_post[0]
            post_data = data_from_post[1]
            if post_type == 'add-form':
                models.Table.objects.create(
                    table_id=post_data[0],
                    table_capacity=post_data[1],
                )
                return HttpResponse(status=200)
            elif post_type == 'non-form':
                tableId = kwargs['table_id']
                print(tableId, kwargs,'heyy')
                table = shortcuts.get_object_or_404(models.Table, pk=tableId)
                table.delete()
                return HttpResponse(status=200)
        else:
            return shortcuts.redirect("account_login")

    def get(self, request, *args, **kwargs):
        page_title = 'Tables | Dashboard'
        page_type = 'dashboard'

        table_objects = models.Table.objects.all()
        print(table_objects)


        if request.user.is_staff:
            return shortcuts.render(
                request,
                "dashboard/tables.html",
                {
                    'page_title': page_title,
                    'page_type': page_type,
                    'current_date': current_date,
                    'tables': table_objects,

                }
            )
        else:
            return shortcuts.redirect("account_login")

class DashboardTimes(View):
    def get(self, request, *args, **kwargs):
        page_title = 'Times | Dashboard'
        page_type = 'dashboard'

        if request.user.is_staff:
            return shortcuts.render(
                request,
                "dashboard/times.html",
                {
                    'page_title': page_title,
                    'page_type': page_type,
                    'current_date': current_date,
                }
            )
        else:
            return shortcuts.redirect("account_login")


class DashboardSchedule(View):
    def get(self, request, *args, **kwargs):
        page_title = 'Schedule | Dashboard'
        page_type = 'dashboard'

        if request.user.is_staff:
            return shortcuts.render(
                request,
                "dashboard/schedule.html",
                {
                    'page_title': page_title,
                    'page_type': page_type,
                    'current_date': current_date,
                }
            )
        else:
            return shortcuts.redirect("account_login")


class DashboardBookings(View):
    def get(self, request, *args, **kwargs):
        page_title = 'Bookings | Dashboard'
        page_type = 'dashboard'

        if request.user.is_staff:
            return shortcuts.render(
                request,
                "dashboard/bookings.html",
                {
                    'page_title': page_title,
                    'page_type': page_type,
                    'current_date': current_date,
                }
            )
        else:
            return shortcuts.redirect("account_login")


class DashboardMenu(View):
    def get(self, request, *args, **kwargs):
        page_title = 'Menu | Dashboard'
        page_type = 'dashboard'

        if request.user.is_staff:
            return shortcuts.render(
                request,
                "dashboard/menu.html",
                {
                    'page_title': page_title,
                    'page_type': page_type,
                    'current_date': current_date,
                }
            )
        else:
            return shortcuts.redirect("account_login")


class DashboardMessages(View):
    def get(self, request, *args, **kwargs):
        page_title = 'Messages | Dashboard'
        page_type = 'dashboard'

        if request.user.is_staff:
            return shortcuts.render(
                request,
                "dashboard/messages.html",
                {
                    'page_title': page_title,
                    'page_type': page_type,
                    'current_date': current_date,
                }
            )
        else:
            return shortcuts.redirect("account_login")


class DashboardHelp(View):
    def get(self, request, *args, **kwargs):
        page_title = 'Help | Dashboard'
        page_type = 'dashboard'

        if request.user.is_staff:
            return shortcuts.render(
                request,
                "dashboard/help.html",
                {
                    'page_title': page_title,
                    'page_type': page_type,
                    'current_date': current_date,
                }
            )
        else:
            return shortcuts.redirect("account_login")
