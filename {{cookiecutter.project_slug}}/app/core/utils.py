from django.conf import settings


def get_required_setting(setting, value_re, invalid_msg):
    """
    Return a constant from ``django.conf.settings``.  The `setting`
    argument is the constant name, the `value_re` argument is a regular
    expression used to validate the setting value and the `invalid_msg`
    argument is used as exception message if the value is not valid.
    """
    try:
        value = getattr(settings, setting)
    except AttributeError:
        raise CoreException("%s setting: not found" % setting)
    if value is None:
        raise CoreException("%s setting is set to None" % setting)
    value = str(value)
    if not value_re.search(value):
        raise CoreException("%s setting: %s: '%s'" % (setting, invalid_msg, value))
    return value


class CoreException(Exception):
    """
    Raised when an exception occurs in any core code that should
    be silenced in templates.
    """
    silent_variable_failure = True

# region Typekit

class TypekitException(Exception):
    """
    Raised when an exception occurs that should be silenced in templates.
    """
    silent_variable_failure = True

# endregion Typekit


# region Wagtail

def wagtail_children_live_in_menu_all(root_page, active_page):
    """
    Recursively find all live pages that have attribute In Menu flipped on.

    :param root_page: The root_page page to start the search
    :param active_page: The page currently being requested
    :return: The filtered QuerySet of pages that are in the menu
    """
    menu_items = root_page.get_children().live().in_menu()

    for item in menu_items:
        item.active = item.url == active_page.url
        item.children = wagtail_children_live_in_menu_all(item, active_page)

    return menu_items


def wagtail_children_live_in_menu_top(root_page, active_page):
    """
    Find top live pages that have attribute In Menu flipped on.

    :param root_page: The root page to start the search
    :param active_page: The page currently being requested
    :return: The filtered QuerySet of pages that are in the menu
    """
    menu_items = root_page.get_children().live().in_menu()

    for item in menu_items:
        item.active = item.url == active_page.url
        item.children = item.get_children().live().in_menu()

    return menu_items

# endregion
