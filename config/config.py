# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse_lazy

variables = {

    'topmenu' : {
        'administrators' : (
            {'title' : u'Главная', 'url' : u'/base/dashboard'},
            {'title' : u'Сообщения', 'url' : u'/messages'},
            {'title' : u'Пользователи', 'url' : u'/users'},
            {'title' : u'Анкета', 'url' : reverse_lazy('profile-view-self')},
            {'separator' : True},
            {'title' : u'Проекты и заявки', 'url' : u'/project/dashboard', 'disabled': True},
            {'title' : u'Все ресурсы', 'url' : u'/project/resources'},
            {'title' : u'Форум', 'url' : u'/forum', 'disabled': True}
        ),
        'moderators' : (
            {'title' : u'Главная', 'url' : u'/base/dashboard'},
            {'title' : u'Контакты', 'url' : u'/contacts', 'disabled': True},
            {'title' : u'Сообщения', 'url' : u'/messages', 'disabled': True},
            {'title' : u'Анкета', 'url' : reverse_lazy('profile-view-self')},
            {'separator' : True},
            {'title' : u'Проекты и заявки', 'url' : u'/project/dashboard', 'disabled': True},
            {'title' : u'Все ресурсы', 'url' : u'/project/resources', 'disabled': True},
            {'title' : u'Форум', 'url' : u'/forum', 'disabled': True}
        ),
        'customers' : (
            {'title' : u'Главная', 'url' : u'/base/dashboard'},
            {'title' : u'Контакты', 'url' : u'/contacts'},
            {'title' : u'Сообщения', 'url' : u'/messages'},
            {'title' : u'Мои ресурсы', 'url' : reverse_lazy('project-resource-my-list')},
            {'title' : u'Портфолио', 'url' : u'/project/portfolio'},
            {'title' : u'Анкета', 'url' : reverse_lazy('profile-view-self')},
            {'separator' : True},
            {'title' : u'Проекты и заявки', 'url' : u'/project/dashboard'},
            {'title' : u'Все ресурсы', 'url' : u'/project/resources'},
            {'title' : u'Форум', 'url' : u'/forum'}
        ),
        'members' : (
            {'title' : u'Главная', 'url' : u'/base/dashboard'},
            {'title' : u'Контакты', 'url' : u'/contacts', 'disabled': True},
            {'title' : u'Сообщения', 'url' : u'/messages', 'disabled': True},
            {'title' : u'Мои ресурсы', 'url' : reverse_lazy('project-resource-my-list')},
            {'title' : u'Портфолио', 'url' : u'/project/portfolio', 'disabled': True},
            {'title' : u'Анкета', 'url' : reverse_lazy('profile-view-self')},
            {'separator' : True},
            {'title' : u'Проекты и заявки', 'url' : u'/project/dashboard', 'disabled': True},
            {'title' : u'Все ресурсы', 'url' : u'/project/resources', 'disabled': True},
            {'title' : u'Форум', 'url' : u'/forum', 'disabled': True}
        ),
        'guests' : (
            {'title' : u'Учащемуся', 'url' : u'/base/page/about_student', 'disabled': True},
            {'separator' : True},
            {'title' : u'О проекте', 'url' : u'/base/page/about_project', 'disabled': True},
            {'separator' : True},
            {'title' : u'Школам', 'url' : u'/base/page/about_school', 'disabled': True},
            {'title' : u'Вузам', 'url' : u'/base/page/about_highschool', 'disabled': True},
            {'separator' : True},
            {'title' : u'Социальным заказчикам', 'url' : u'/base/page/about_customer', 'disabled': True},
            {'separator' : True},
            {'title' : u'О ресурсах', 'url' : u'/base/page/about_resources', 'disabled': True}
        ),
    },

    'dashboard-menu' : {
        'moderators' : (
#            {'title' : u'Стена новостей', 'url': reverse_lazy('base-dashboard')},
            {'title' : u'Заявки на контроле', 'url': reverse_lazy('project-invoice-undercontrol-list'), 'counter_name': 'invoice_count'},
#            {'title' : u'Проекты на контроле', 'url': reverse_lazy('project-undercontrol-list'), 'counter_name': 'project_count'},
            {'title' : u'Реурсы на контроле', 'url': reverse_lazy('project-resource-undercontrol-list'), 'counter_name': 'resource_count'}
        ),
        'members' : (
#            {'title' : u'Стена новостей', 'url': reverse_lazy('base-dashboard')},
#            {'title' : u'Проекты, где я участвую', 'url': reverse_lazy('project-my-list'), 'counter_name': 'project_count'},
            {'title' : u'Мои заявки на проект', 'url': reverse_lazy('project-invoice-my-list'), 'counter_name': 'invoice_count'},
#            {'title' : u'Интересное', 'url': reverse_lazy('project-resource-undercontrol-list')}
        ),
    },


    'users' : {
        'groups' : ('administrators', 'moderators', 'members'),
        'default_group' : 'members',
    }
}

