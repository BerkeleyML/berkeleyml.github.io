---
layout: page
title: Calendar
nav_order: 4
description: Calendars with times for all course events.
---

# Calendar

{: .note }

> If you are having trouble viewing the calendars below and are using Safari, we suggest switching to an alternate browser (like Chrome). Alternatively, you can go to Safari settings and switch “Prevent cross-site tracking” off, or you can see the _Course Calendar_ [here](https://calendar.google.com/calendar/embed?src=cs189-instructors%40berkeley.edu&ctz=America%2FLos_Angeles).

{% assign button_groups = site.data.calendar.categories | map: "name" | uniq %}

If you would like to view this calendar outside of the course website, click "Open in Google Calendar" below.

[Open in Google Calendar]({{ site.data.calendar.google_calendar_embed_link }}){: .btn .btn-outline .fs-3 }

{% include calendar.html %}

<div id="calendarContainer">
  Alongside tab navigation, the following keyboard shortcuts are available for use on this page:
  <div id="calendarShortcuts" class="justify-content-between">
    <span class="shortcut"><kbd aria-label="Left Arrow" title="Left Arrow" style="margin-right: 0.2em;">￩</kbd> Jump to Previous Period</span>
    <span class="shortcut"><kbd aria-label="Right Arrow" title="Right Arrow" style="margin-right: 0.2em;">￫</kbd> Jump to Next Period</span>
    <span class="shortcut"><kbd style="margin-right: 0.2em;">t</kbd> Jump to Today</span>
    <span class="shortcut"><kbd style="margin-right: 0.2em;">d</kbd> Switch to Day View</span>
    <span class="shortcut"><kbd style="margin-right: 0.2em;">w</kbd> Switch to Week View</span>
  </div>
  <div id="calendarControls" class="btn-toolbar justify-content-between" role="toolbar" aria-label="Calendar control toolbar">
    Use the following toggles to customize your calendar view. If you'd like to hide a category of events, click on the respective button to do so. The calendar will immediately update to reflect your selection. To re-enable that category, click again.
    <span style="display: block; height: 1rem;"></span>
    <div class="input-group mb-3" role="group" aria-label="Calendar category toggles" style="text-align: center;">
      {% for group in button_groups %}
        <button class="btn btn-outline-primary" data-action="toggle-category-{{ group | downcase | replace: " ", "-" }}" aria-label="Toggle {{ group }}" >{{ group }}</button>
      {% endfor %}
    </div>
  </div>
</div>

<script>
  document.addEventListener("DOMContentLoaded", function() {
    initCalendar();
  });
</script>
