---
layout: page
title: Home / Schedule
nav_order: 1
description: A week-to-week description of the content covered in the course.
course:
  edstem: https://edstem.org/us/courses/81430
  faq: https://ds100.org/faqs/sp25
currWeekNumber: 1
---

# CS 189/289A: Intro to Machine Learning

## UC Berkeley, Spring 2026

{: .mb-2 .fs-6 .text-grey-dk-000 style="margin-top: 0;" }

{: .highlight }

> **Warning:** This webpage for Spring 2026 is under construction. There may be misleading information from past semesters on other parts of this website that are no longer true.


[Lecture Link](https://berkeley.zoom.us/j/6324076985){:target="_blank" .btn .btn-blue .mr-1 }

<!-- 
[Ed](TBD){:target="\_blank" .btn .btn-ed .mr-1 }
[Gradescope](https://www.gradescope.com/courses/1229310){:target="\_blank" .btn .btn-gradescope .mr-1 }
[Lectures Playlist](TBD){:target="\_blank" .btn .btn-youtube .mr-1}
[Additional Accommodations](TBD){:target="\_blank" .btn .btn-blue .mr-1 }
[Office Hours Queue](TBD){:target="\_blank" .btn .btn-oh .mr-1}
[Content Repository](TBD){:target="\_blank" .btn .btn-repo .mr-1}
[Class Drive](TBD){:target="\_blank" .btn .btn-drive .mr-1} -->
<!-- TBD this section -->

<!-- <span class="btn btn-ed mr-1">Ed</span>
<span class="btn btn-gradescope mr-1">Gradescope</span> -->
<!-- <span class="btn btn-youtube mr-1">Lectures Playlist</span> -->
<!-- <span class="btn btn-blue mr-1">Additional Accommodations</span> -->
<!-- <span class="btn btn-oh mr-1">Office Hours Queue</span> -->
<div>
{% assign instructors = site.staffers | where: 'role', 'Instructor' | sort: 'order' %}
  <div class="role">
    {% for staffer in instructors %}
    <!-- {% assign staffer.photo = staffer.photo | replace: '../', '' %} -->
    {{ staffer }}
    {% endfor %}
  </div>
</div>

- Our course staff email is [cs189-instructors@berkeley.edu](mailto:{{cs189-instructors@berkeley.edu}}). This email is monitored by the instructors, the head TAs, and a few lead TAs.

{: .highlight }

> Welcome to [Week {{page.currWeekNumber}}](#week-{{page.currWeekNumber}}) of CS 189/289A!

<!-- > Lectures will be broadcast at this [link](https://berkeley.zoom.us/j/92596950563). -->

<!-- > **Please note that the size of this course is not expanding, and we cannot predict whether you will get off the waitlist.** -->

<!-- {: .note }
> <span style="color:red">**Enrollment: As of Jan. 23, 2024, Data C100/200 is closed and no further enrollment is possible.**</span>  -->

<a name="schedule"></a>

## Schedule

{% for module in site.modules %}
{{ module }}
{% endfor %}

<script>
/**
 * Auto-scroll to current week on page load
 */
document.addEventListener('DOMContentLoaded', function() {
    // Find the current week module and welcome banner
    const currentWeekModule = document.querySelector('.module.current-week');
    const welcomeBanner = document.querySelector('.highlight');
    
    if (currentWeekModule && welcomeBanner) {
        // Add click handler to welcome banner
        welcomeBanner.style.cursor = 'pointer';
        welcomeBanner.addEventListener('click', function() {
            // Get the position of the current week module
            const rect = currentWeekModule.getBoundingClientRect();
            const absoluteElementTop = rect.top + window.pageYOffset;
            const middle = absoluteElementTop - (window.innerHeight / 2) + (rect.height / 2);
            
            // Smooth scroll with custom easing
            window.scrollTo({
                top: Math.max(0, middle),
                behavior: 'smooth'
            });
            
            // Add a very subtle animation to draw attention after scroll completes
            setTimeout(function() {
                currentWeekModule.style.animation = 'currentWeekPulse 3s ease-in-out';
            }, 800);
        });
    }
});

// Add CSS animation for the pulse effect
const style = document.createElement('style');
style.textContent = `
    @keyframes currentWeekPulse {
        0% { transform: scale(1); opacity: 1; }
        50% { transform: scale(1.005); opacity: 0.95; }
        100% { transform: scale(1); opacity: 1; }
    }
`;
document.head.appendChild(style);
</script>
