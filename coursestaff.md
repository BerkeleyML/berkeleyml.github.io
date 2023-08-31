---
layout: page
title: Course Staff
permalink: /coursestaff/
nav_order: 4
---

# Staff
Below is the course staff for the semester. Please make an Ed post before emailing GSIs and instructors. If you have a very private matter, you may email the instructors and Head GSIs.

## Instructors

{% assign instructors = site.staffers | where: 'role', 'Instructor' %}
{% for staffer in instructors %}
{{ staffer }}
{% endfor %}

## Head GSIs

{% assign headgsis = site.staffers | where: 'role', 'Head GSI' %}
{% for staffer in headgsis %}
{{ staffer }}
{% endfor %}

## GSIs

{% assign gsis = site.staffers | where: 'role', 'GSI' %}
{% for staffer in gsis %}
{{ staffer }}
{% endfor %}

## Readers

{% assign readers = site.staffers | where: 'role', 'Reader' %}
{% for staffer in readers %}
{{ staffer }}
{% endfor %}
