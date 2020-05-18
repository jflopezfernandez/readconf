#!/usr/bin/env python

# Import and initialize the Sentry SDK
import sentry_sdk

sentry_sdk.init(dsn='https://d21f3ef0e6964685906c6a934a6aaf58@o221862.ingest.sentry.io/5244161')
sentry_sdk.capture_exception(Exception('This is an example of an error message.'))

print("Hello, world!")
