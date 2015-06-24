## @mainpage Writing Milters in Python
#
# At the lowest level, the <code>milter</code> module provides a thin wrapper
# around the <a href="milter_api/index.html"> sendmail
# libmilter API</a>.  This API lets you register callbacks for a number of
# events in the process of sendmail receiving a message via SMTP.  These
# events include the initial connection from a MTA, the envelope sender and
# recipients, the top level mail headers, and the message body.  There are
# options to mangle all of these components of the message as it passes through
# the milter.
# 
# At the next level, the <code>Milter</code> module (note the case difference)
# provides a Python friendly object oriented wrapper for the low level API.  To
# use the Milter module, an application registers a 'factory' to create an
# object for each connection from a MTA to sendmail.  These connection objects
# must provide methods corresponding to the libmilter callback events.
# 
# Each event method returns a code to tell sendmail whether to proceed with
# processing the message.  This is a big advantage of milters over other mail
# filtering systems.  Unwanted mail can be stopped in its tracks at the
# earliest possible point.
# 
# The <code>Milter.Base</code> class provides default implementations for
# event methods that do nothing, and also provides wrappers for the libmilter
# methods to mutate the message.  It automatically negotiates with MTA
# which protocol steps need to be processed by the milter, based on
# which callback methods are overridden.
#
# The <code>Milter.Milter</code> class provides an alternate default
# implementation that logs the main milter events, but otherwise does nothing.
# It is provided for compatibility.
# 
# The <code>mime</code> module provides a wrapper for the Python email package
# that fixes some bugs, and simplifies modifying selected parts of a MIME
# message.
#
# @section threading
#
# The libmilter library which pymilter wraps 
# <a href="milter_overview#SignalHandling">handles
# all signals</a> itself, and expects to be called from a single main thread.
# It handles SIGTERM, SIGHUP, and SIGINT, mapping the first two to 
# <a href="milter_api/smfi_stop.html">smfi_stop</a>
# and the last to an internal ABORT.
#
# If you use python threads or threading modules, then signal handling gets
# confused.  Threads may still be useful, but you may need to provide an
# alternate means of causing graceful shutdown.
#
# You may find the
# <a href="http://docs.python.org/release/2.6.6/library/multiprocessing.html">
# multiprocessing</a> module useful.  It can be a drop-in
# replacement for threading as illustrated in @ref milter-template.py.
