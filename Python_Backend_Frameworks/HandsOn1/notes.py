#1) REQUEST-RESPONSE CYCLE
#Browser sends GET /api/courses/ request to the server
#Request is routed through URL router - urls.py
#The urls.py selects which view should handle the request based on the URL pattern
#The view function is called, which processes the request and interacts with the database if necessary
#The view function returns a response, which is sent back to the browser

#2)MIDDLEWARE
#It acts as a bridge between the request and response, processing requests before 
#they reach the view and responses before they are sent to the client. 
# It can be used for tasks like authentication, logging, and modifying request/response objects.

#3)WSGI vs ASGI
# WSGI (Web Server Gateway Interface) is a standard interface
# between web servers and Python web applications. It is designed
# for synchronous request processing and is suitable for traditional
# web applications.
#
# ASGI (Asynchronous Server Gateway Interface) is the successor to
# WSGI and supports asynchronous programming. It enables features
# such as WebSockets, long-lived connections, and real-time
# communication.

# 4. MVC AND DJANGO MVT ARCHITECTURE

# MVC stands for Model, View, and Controller. The Model manages the
# application's data, the View represents the user interface, and
# the Controller handles application logic and user requests.
#
# Django follows the MVT (Model-View-Template) architecture. In
# Django, the Model performs the same role as the Model in MVC.
# Django's View performs the responsibilities of the Controller in
# MVC by handling requests and business logic. The Template
# represents the presentation layer and corresponds to the View in
# the MVC architecture.
#
# Therefore, MVC Model maps directly to Django Model, MVC Controller
# maps to Django View, and MVC View maps to Django Template.