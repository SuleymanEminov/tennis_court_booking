from django import template

register = template.Library()

@register.filter
def make_range(start,end):
    return range(start,end+1)

@register.filter(name='event_filter')
def event_filter(events, args):
    """
    A custom filter to get an event from a list of events
    based on the court and start time.
    """
    args = args.split(',')
    court = args[0]
    hour = int(args[1])
    minute = int(args[2])
    # Filter the events based on the court and start time
    filtered_events = [event for event in events if event['court'] == court and
                       event['start'].hour == hour and event['start'].minute == minute]

    # Return the first event, or None if no events found
    return filtered_events[0] if filtered_events else None