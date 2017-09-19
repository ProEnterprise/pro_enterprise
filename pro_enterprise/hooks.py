# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "pro_enterprise"
app_title = "Pro Enterprise"
app_publisher = "Pro Enterprise Limited"
app_description = "ERP Applications for SMEs"
app_icon = "octicon octicon-file-directory"
app_color = "orange"
app_email = "enterprisezambia@gmail.com"
app_license = "MIT"
app_include_js = "/assets/pro_enterprise/hide_help_menu.js"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/pro_enterprise/css/pro_enterprise.css"
# app_include_js = "/assets/pro_enterprise/js/pro_enterprise.js"

# include js, css files in header of web template
# web_include_css = "/assets/pro_enterprise/css/pro_enterprise.css"
# web_include_js = "/assets/pro_enterprise/js/pro_enterprise.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "pro_enterprise.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "pro_enterprise.install.before_install"
# after_install = "pro_enterprise.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "pro_enterprise.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"pro_enterprise.tasks.all"
# 	],
# 	"daily": [
# 		"pro_enterprise.tasks.daily"
# 	],
# 	"hourly": [
# 		"pro_enterprise.tasks.hourly"
# 	],
# 	"weekly": [
# 		"pro_enterprise.tasks.weekly"
# 	]
# 	"monthly": [
# 		"pro_enterprise.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "pro_enterprise.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "pro_enterprise.event.get_events"
# }

