---
layout: page
title: Course Staff
permalink: /coursestaff/
nav_order: 4
---

# Staff
Below is the course staff for the semester. Please make an Ed post before emailing TAs and instructors. If you have a very private matter, you may email the instructors and Head TA.

## Instructors

{% assign instructors = site.staffers | where: 'role', 'Instructor' %}
{% for staffer in instructors %}
{{ staffer }}
{% endfor %}

## Head TA

{% assign headta = site.staffers | where: 'role', 'Head TA' %}
{% for staffer in headta %}
{{ staffer }}
{% endfor %}

<!-- ## GSIs -->

{% assign tas = site.staffers | where: 'role', 'TA' %}
{% for staffer in tas %}
{{ staffer }}
{% endfor %}

<!-- ## Readers -->

{% assign readers = site.staffers | where: 'role', 'Reader' %}
{% for staffer in readers %}
{{ staffer }}
{% endfor %}
