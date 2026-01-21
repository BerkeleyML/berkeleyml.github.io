---
layout: page
title: Syllabus
nav_order: 2
description: >-
  Introduction to Machine Learning
markdown: kramdown
course:
  semester: Spring 2026
  edstem: https://edstem.org/us/courses/81430
  bcourses: ""
  comms_email: cs189-instructors@berkeley.edu
  email: cs189-instructors@berkeley.edu
---

# Syllabus

{:.no_toc}

<a name = 'about'></a>

## About CS 189/289A

Machine learning is at the core of modern artificial intelligence, transforming how we approach problems in vision, language, robotics, recommendation systems, and countless other areas. This course introduces the theoretical foundations, algorithms, and applications of machine learning, combining mathematical rigor with practical experience.

Throughout the semester, we will explore the full pipeline of machine learning from problem formulation and working with data, to designing models and optimizing them. We will begin with a discussion of what machine learning is, how problems are framed and categorized, and the taxonomy of common learning paradigms. We will review the mathematical background necessary for the course, including probability and optimization concepts.

We will then study unsupervised learning methods, including clustering with k-means and Expectation–Maximization, and dimensionality reduction with Principal Components Analysis (PCA). We will discuss regression in detail, starting with objective functions and then moving to linear regression and its Maximum Likelihood Estimation (MLE) interpretation, and then exploring how regression connects to classification.

The deep learning portion of the course will begin with neural network fundamentals, including building non-linear models, choosing architectures and activation functions, and defining loss functions. We will cover PyTorch implementations, backpropagation, batch normalization, initialization strategies, and regularization. We will then survey other deep architectures such as Convolutional Neural Networks (CNNs), Recurrent Neural Networks (RNNs), and transformers — along with generative models such as Large Language Models (LLMs), autoencoders, and Generative Adversarial Networks (GANs).

Finally, the course will include guest lectures from leading researchers, discussions of emerging topics in the field, and opportunities to connect theoretical concepts to cutting-edge research and applications.

### Goals

- Provide a rigorous foundation in the mathematics, algorithms, and concepts of machine learning.
- Prepare students for advanced coursework and research in artificial intelligence, deep learning, computer vision, and natural language processing.
- Enable students to implement machine learning algorithms and apply them to real-world problems.

<a name = 'prereq'></a>

### Prerequisites

This course assumes strong preparation in mathematics and programming. The required prerequisites are:

- **Multivariable Calculus**: MATH 53
- **Linear Algebra**: MATH 54 or equivalent
- **Probability and Discrete Mathematics**: COMPSCI 70 or equivalent

You should be comfortable with vector calculus (including gradients and the multivariate chain rule), matrix operations, probability theory (including conditional probability and Bayes’ rule), and writing/debugging complex programs in Python. If you lack preparation in these areas, you are likely to struggle.

### Textbook

The required textbook for this semester is **Deep Learning Foundations and Concepts**, Christopher M. Bishop and Hugh Bishop, 2024 edition (Springer). You can get a PDF by going to [this page](https://link-springer-com.libproxy.berkeley.edu/book/10.1007/978-3-031-45468-4), log in with your CalNet ID.

## Course Components

Below is a high-level “typical week in the course” for {{page.course.semester}}.

| Mo           | Tu                                                 | We                                                 | Th                                            | Fr                                                       |
| ------------ | -------------------------------------------------- | -------------------------------------------------- | --------------------------------------------- | -------------------------------------------------------- |
|              | <span style="color:Green">Live Lecture</span>      |                                                    | <span style="color:Green">Live Lecture</span> |                                                          |
|              | <span style="color:Blue">Discussion Section</span> | <span style="color:Blue">Discussion Section</span> |                                               |                                                          |
| Office Hours |                                                    |                                                    | Office Hours                                  | Office Hours                                             |
|              |                                                    |                                                    |                                               | <span style="color: #c91d1d">**Homework N-1 due**</span> |
|              |                                                    |                                                    |                                               | <span style="color:#c91d1d">Homework N released</span>   |

- **All deadlines are subject to change.**
- A more detailed schedule of Lectures, Discussions, Exams, and Office Hours is available on the [Calendar page](../calendar).
- Lectures, discussions, assignments, and exams are scheduled on the [Home page](..).

### Lecture
<!-- TBD location -->
There are two live lectures per week, held on **Tuesdays and Thursdays from 2:00–3:30 PM** in Wheeler 150. Attendance is in person and live-streamed on Zoom, and we strongly recommend coming to class, as lectures include worked examples, interactive questions, and discussions that are difficult to replicate from the slides alone. 

Recordings, slides, and any in-class materials will be posted on the course website within 24 hours whenever possible.

**Lecture participation**: While synchronous lecture attendance (in-person or through Zoom) is not mandatory, we expect you to "participate" in lecture by answering lecture poll questions in one of two ways: (1) synchronously during the lecture as poll questions are launched; or (2) asynchronously using a link provided after lecture.

- Lecture participation is graded using poll responses on a 0/1 basis.
  - Synchronous Participation: complete at least one participation poll question during the live lecture timeslot (2:00pm-3:30pm, Tuesdays and Thursdays). As long as you submit a response to at least one poll question in this timeframe, you will receive synchronous attendance credit.
  - Asynchronous Participation: complete all participation poll questions from the link provided on the course website within one week of the corresponding lecture.
  - In both cases, participation is graded on completion, not correctness.
- See the [Policies](#policies) section for lecture participation drops.

### Discussion

Discussion sections provide an opportunity to work through problems, clarify concepts, and gain hands-on experience with the material. Discussion sections are ungraded, but attendance is strongly encouraged. The goal of these TA-led sessions is to reinforce course concepts, develop your problem solving skills, and provide an additional space to ask questions and dive deeper into the course material. The problems that you solve as part of discussion are important in understanding course material.
We will hold three one hour-long discussion sections this semester on Tuesdays and Wednesdays. Times and locations are available on the [Calendar](../calendar) page. If you would like to attend a discussion section, please indicate your interest and availability in the [Pre-Semester](TBD) Survey by TBD. We will assign you to a section based on your response to this form during the second week of classes. Due to limited room capacities, you should only attend discussion at your assigned time.

### Homework and Projects

There will be **5 homework assignments** over the semester. Each homework spans **three weeks** and consists of two parts:

- **Part 1: Warmup** — shorter, designed to introduce the concepts and techniques needed for the main assignment. Typically due within **1–2 weeks** of release.
- **Part 2: Main Homework** — more in-depth, building on the warmup and requiring a deeper application of the material. Due **three weeks** after the homework is first released.

Both the warmup and the main homework will be **released at the same time**, so you can plan your work across the full three-week period.

Homework assignments might include both **mathematical derivations** and **coding tasks**, submitted on Gradescope. Some components will be autograded, while others will be graded manually for correctness and clarity.

While collaboration is encouraged for discussing approaches, all solutions must be written up individually in your own words and code, in accordance with the [Collaboration Policy](#collaboration-policy-and-academic-honesty).

- All homeworks must be submitted to Gradescope by their posted deadlines. There may be separate coding and written Gradescope portals for the same assignment; please check that you are submitting the right part.
- Homeworks and projects have both public (visible) and hidden autograder tests. The public tests are mainly sanity checks. For example, a sanity check might verify that the answer you entered is a number as expected, and not a word. The hidden tests generally check for correctness, and are invisible to students while they are completing the assignment.
- The primary form of support students will have for homeworks and projects are **office hours** and **Ed**.
- Homeworks must be completed individually, without the usage of any unauthorized resources (CourseHero, etc). See the [Collaboration Policy](#collaboration-policy-and-academic-honesty) for more details.

### Exams

There will be two exams in this course:

{: .important}

> - **Midterm** on **TBD** during TBD

- **Final** on **TBD** during TBD

**All exams must be taken in-person.** There will be no alternate exams offered.

### Graduate Final Project

All students enrolled in the graduate version of the course (CS289) will be graded according to the Graduate grading scheme, which includes a team-based **Graduate Final Project** distributed in the second half of the semester. More details to come.

## Office Hours and Communication

We want to enable everyone to succeed in this course. We encourage you to discuss course content with your friends, classmates, and course staff throughout the semester, particularly during **office hours**.

- All office hours will be updated on the Calendar.
- Please refer to the [Calendar](../calendar) page for all locations and times of office hours.
- In general, students can come to staff office hours for any questions on course assignments or material.
- Instructor office hours are generally reserved for conceptual questions, course review, course logistics, research opportunities, and career planning.

Course Communication:

- **EdStem**, or **Ed** for short, is our course forum this semester. **_All course announcements will be through Ed._** 

  - Ed is a formal, academic space. We must demonstrate appropriate respect, consideration, and compassion for others. Please be friendly and thoughtful; our community draws from a wide spectrum of valuable experiences. For further reading, please reference [Berkeley’s Principles of Community](https://diversity.berkeley.edu/principles-community){:target="\_blank"} and the [Berkeley Campus Code of Student Conduct](https://conduct.berkeley.edu/code-of-conduct/){:target="\_blank"}.

  - Ed is your primary platform for asking questions about the class. It is monitored daily by course staff, so questions posted to Ed will likely receive the fastest response. If you need to discuss a more sensitive matter, the following emails are monitored by a smaller subset of the teaching team:

- For sensitive questions: our course staff email is [cs189-instructors@berkeley.edu](mailto:{{page.course.email}}). This email is monitored by the instructors, the head TAs, and a few lead TAs.
- For course accomodations/DSP: student accommodation requests will be handled via the [Additional Accommodations Form](https://TBD){:target="\_blank"}. Our staff email for student support and DSP accommodations is [cs189-instructors@berkeley.edu](<(mailto:{{page.course.comms_email}})>).
  - Please only contact the course instructors directly for matters that require strict privacy and their personal attention.

## Policies

### Grading Scheme

| Category               | CS 189 | CS 289A | Details                                                                  |
| ---------------------- | ------ | ------- | ------------------------------------------------------------------------ |
| Homework               | TBD    | TBD     |                                                                          |
| Midterm Exam           | TBD    | TBD     |                                                                          |
| Final Exam             | TBD    | TBD     |                                                                          |
| Lecture Attendance     | TBD    | TBD     | Based on in-class polls or sign-ins. One attendance drop is allowed. TBD |
| Graduate Final Project | —      | TBD     | CS 289 only.                                                             |

**To pass this course, students must achieve a total weighted average percentage of at least 50% across the midterm and final exams.** This means that even if a student excels in other components of the course, a total weighted average below 50% on these exams will result in a failing grade for the course.

While we do not have homework drops this semester, we will offer slip days for homeworks, as well as an [Additional Accommodations Form](https://TBD){:target="\_blank"}. See the next sections for more details.

### On-Time Submission

All assignments are due at **_11:59 PM Pacific Time_** on the due date specified on the [Home / Schedule](..) page. The date and time of this deadline are firm. Submitting even a minute past is considered late.

### Slip Days

Each student gets an extension budget of **10** total slip days for the 10 homework deadlines (so use them wisely). You can apply these slip days to homework during the semester.

Slip days are automatically applied based on the additional hours you take to submit any assignment after its given deadline. Slip days are rounded up to the next day. For instance, 1 minute late counts as 1 day late. We will use the submission time as displayed on Gradescope.

{: .note }

> If all 10 slip days are used for the first two homework assignments (for example), you are out of slip days and cannot ask us to not consider one of the slip days previously used.

Each homework can have a maximum of **4** slip days applied. After 4 days of the assignment due date, we will be not able to accept your submission unless you have additional accommodations. Slip days should be reserved for unforeseen circumstances. You should not plan to use your slip days regularly.

### Additional Accommodations

We recognize that our students come from varied backgrounds and have widely-varying experiences. If you require any additional accommodations any time in the semester, please do not hesitate to let us know. The sooner we are made aware, the more options we have available for us to help you.

The **[Additional Accommodations Form](https://TBD){:target="\_blank"}** is for any circumstances that cannot be resolved via slip days and drops. Within two business days of filling out the form, a member of course staff will reach out to you and provide a space for conversation, as well as to arrange course/grading accommodations as necessary. For more information, please email [cs189-instructors@berkeley.edu](mailto:cs189-instructors@berkeley.edu).

We recognize that at times, it can be difficult to manage your course performance - particularly at Berkeley’s high standards. Sometimes emergencies just come up (personal health emergency, family emergency, etc.). The [Additional Accommodations Form](https://TBD){:target="\_blank"} is meant to lower the barrier to reaching out to us, as well as build your independence in managing your academic career long-term. So please do not hesitate to reach out.

Note that you **cannot** use the Additional Accommodations Form if you encounter a logistical oversight, such as Gradescope tests not passing, submitting only one portion of the homework, submitting to the wrong assignment portal, or not properly tagging pages on Gradescope. It is the students’ responsibility to identify and resolve these issues well in advance of the on-time deadline.
We will not grant accommodations for these cases; instead, please use slip days to cushion these submission errors.

Finally, simply submitting a request does not guarantee you will receive an extension. You must submit your requests before running out of slip days. **Even if your work is incomplete, please submit before the deadline so you can receive credit for the work you did complete.**

### DSP Accommodations

{: .important }

If you are registered with the Disabled Students’ Program (DSP), you will receive an email from us during the first week of classes. Otherwise, email [cs189-instructors@berkeley.edu](mailto:cs189-instructors@berkeley.edu). Students may request extensions through the **[Additional Accommodations Form](https://TBD){:target="\_blank"}**. For DSP students, extension requests of up to **2 days** are automatically approved (though all students must still submit the request). Please note: for any single assignment, the total of all extensions plus slip days cannot exceed **7 days**. Beyond **7 days**, you are required to meet with a staff member for additional support.

You are responsible for reasonable communication with course staff. If you make a request close to the deadline, we can not guarantee that you will receive a response before the deadline. Additionally, simply submitting a request does not guarantee you will receive an extension. **Even if your work is incomplete, please submit before the deadline so you can receive work for the work you did complete.**

### Regrade Requests

Students will be allowed to submit regrade requests for the autograded and written portions of assignments in cases in which the rubric was incorrectly applied or the autograder scored their submission incorrectly. Regrades for the written portions of assignments will be handled through Gradescope, and autograder regrades via a Google Form. The deadline for regrade requests (autograded and written) is one week after the grades are released for the corresponding assignment.

**Always check that the autograder executes correctly!** Gradescope will show you the output of the public tests. If you see a discrepancy, ensure that you have exported the assignment correctly and, if there is still an issue, post on Ed _as soon as possible_.

Regrade requests will **not** be considered in cases in which:

- A student uploads the incorrect file to the autograder.
- The autograder fails to execute and the student does not notify the course staff _before the regrade request window closes_.
- A student fails to save their notebook before exporting and uploads an old version to the autograder.
- A situation arises in which the course staff cannot ensure that the student’s work was done before the assignment deadline.

### Collaboration Policy and Academic Honesty

We follow the EECS Academic Misconduct policy: using work or resources that are not your own or that are not permitted by the course may result in disciplinary actions, including a failing grade in the course. We use plagiarism and similarity detection on all submissions.
**Working with others on assignments:**

- You are encouraged to discuss concepts and approaches with classmates, TAs, and instructors.
- You must write all code and all text yourself, in your own words. Do not share or receive code, write-ups, screenshots, or autograder outputs. Discuss ideas verbally/at a whiteboard only.
- Never post solutions publicly (including GitHub). You may not store or disseminate solutions after the course ends.

**External resources:**
You may consult official documentation, textbooks, or tutorials to learn background material. You must not copy code or text. If an outside source influenced your approach, include a short citation (URL or title) in your write-up.

**GenAI policy (careful use allowed, not authorship):**
We recognize GenAI tools are ubiquitous and can help you learn, but your submission must be your own original work. In this course, GenAI is a consulting tool, not an author.

#### Allowed (with citation)

- Asking for clarification of error messages, APIs, or unfamiliar library behavior.
- Asking for conceptual explanations (“What does cross-entropy measure?”), or workflow planning (“What steps to check for data leakage?”).
- Tab based code completion is okay as long as you understand the process and could replicate the answer independently. (For your learning purposes, we recommend trying to re-implement any significant tab completions.)
  When you use GenAI in allowed ways, include an Acknowledgement (see template below) describing what tool you used and for what purpose.

#### Not allowed

- Pasting any assignment text, dataset identifiers, or prompts directly into GenAI.
- No Vibe coding. You should not blindly paste output or rely on agents to implement your assignments. YOLO – do it yourself.
- Using GenAI (ChatGPT/Copilot/etc) to summarize/interpret your own analysis for inclusion.
- Requesting solutions, proofs, derivations, or code for assignment parts without understanding the concepts.
- If in doubt, please reach out to staff by posting a question on Edstem!

**Required acknowledgement format:**
Place this near the top of your submission if you used GenAI in any allowed way:

**_I acknowledge the use of [tool + link] to [specific purpose]. I used the outputs to [e.g., understand an error message / clarify pandas behavior]. I have the ability to explain and even independently replicate the work done in this document if asked by an instructor._**

**Enforcement**
We randomly require a brief Zoom interview. If you cannot explain your work, we may assign a 0 on the assignment and investigate other submissions.

### Grading & verification for assignments

Grades are based on test cases, written responses, and, at random, a short Zoom interview with staff or a recorded walkthrough. If, during the interview (or walkthrough), you are unable to explain your approach or reasonably answer related questions, we reserve the right to assign a score of 0 for that homework and review other submissions.

### Exams (midterm & final)

Cheating on exams is a serious offense. We have methods of detecting and investigating academic misconduct. Students caught cheating on any exam will fail the course. GenAI or electronic assistance of any kind is prohibited on exams.

### Reporting & consequences

Plagiarism or other violations of Berkeley’s Code of Conduct will be reported to the Center for Student Conduct (CSC). We reserve the right to give you a negative full score (-100%) or lower on the assignments in question. It isn’t worth it.

### Be Aware of Your Actions

Sometimes, the little things add up to creating an unwelcoming culture to some students. For example, you and a friend may think you are sharing a private joke about other races, majors, genders, abilities, cultures, etc. but this can have adverse effects on classmates who overhear it. There is a great deal of research on something called “stereotype threat”: research finds that simply reminding someone that they belong to a particular culture or share a particular identity (on whatever dimension) can interfere with their course performance.

Stereotype threat works both ways: you can assume that a student will struggle based on who they appear to be, or you can assume that a student is doing great based on who they appear to be. Both are potentially harmful.

Bear in mind that diversity has many facets, some of which are not visible. Your classmates may have medical conditions (physical or mental), personal situations (financial, family, etc.), or interests that aren’t common to most students in the course. Another aspect of professionalism is avoiding comments that (likely unintentionally) put down colleagues for situations they cannot control. Bragging in open space that an assignment is easy or “crazy,” for example, can send subtle cues that discourage classmates who are dealing with issues that you can’t see. Please take care, so we can create a class in which all students feel supported and respected.

### Be Respectful

Beyond the slips that many of us make unintentionally are a host of behaviors that the course staff, department, and university do not tolerate. These are generally classified under the term harassment; sexual harassment is a specific form that is governed by federal laws known as Title IX.

{: .note }

> UC Berkeley’s [**Title IX website**](https://ophd.berkeley.edu/){:target="\_blank"} provides many resources for understanding the terms, procedures, and policies around harassment. Make sure you are aware enough of these issues to avoid crossing a line in your interactions with other students. For example, repeatedly asking another student out on a date after they have said no can cross this line.

Your reaction to this topic might be to laugh it off, or to make or think snide remarks about “political correctness” or jokes about consent or other things. You might think people just need to grow a thicker skin or learn to take a joke. This isn’t your decision to make. Research shows the consequences (emotional as well as physical) on people who experience harassment. When your behavior forces another student to focus on something other than their education, you have crossed a line. You have no right to take someone else’s education away from them.

### Communicate Issues with Course Staff and/or the Department

**We take all complaints about unprofessional or discriminatory behavior seriously.** Professionalism and respect for diversity are not just matters between students; they also apply to how the course staff treat the students. The staff of this course will treat you in a way that respects our differences. However, despite our best efforts, we might slip up, hopefully inadvertently. If you are concerned about classroom environment issues created by the staff or overall class dynamic, please feel free to talk to us about it. The instructors in particular welcome any comments or concerns regarding conduct of the course and the staff. See [below](#office-hours-and-communication) for how to best reach us.

### Device Lending options

Students can access device lending options through the Student Technology Equity Program [STEP program](https://studenttech.berkeley.edu/devicelending){:target="\_blank"}.

### Community Standards

Ed is a formal, academic space. Posts in this forum must relate to the course and be in alignment with [Berkeley’s Principles of Community](https://diversity.berkeley.edu/principles-community){:target="\_blank"} and the [Berkeley Campus Code of Student Conduct](https://conduct.berkeley.edu/code-of-conduct/){:target="\_blank"}. We expect all posts to demonstrate appropriate respect, consideration, and compassion for others. Please be friendly and thoughtful; our community draws from a wide spectrum of valuable experiences. Posts that violate these standards will be removed.

As course staff, we are committed to creating a learning environment welcoming of all students that supports a diversity of thoughts, perspectives and experiences and respects your identities and backgrounds (including race, ethnicity, nationality, gender identity, socioeconomic class, sexual orientation, language, religion, ability, and more.) To help accomplish this:

- If your name and/or pronouns differ from those that appear in your official records, please let us know.
- If you feel like your performance in the class is being affected by your experiences outside of class (e.g., family matters, current events), please don’t hesitate to come and talk with us. We want to be resources for you.
- We (like many people) are still in the process of learning about diverse perspectives and identities. If something was said in class (by anyone) that made you feel uncomfortable, please talk to us about it.

## Academic and Wellness Resources

Our [Resources](../resources) page lists not only course-specific academic resources. Our staff will also refer to this page when supporting you through this course.

## We want you to succeed!

If you are feeling overwhelmed, visit our office hours and talk with us, or fill out the Additional Accommodations Form. We know college can be stressful and we want to help you succeed.

{: .important }
We are committed to being a resource to you, but it is important to note that all members of the teaching staff for this course are [responsible employees](https://svsh.berkeley.edu/responsible-employee){:target="\_blank"}, meaning that **we must disclose any incidents of sexual harassment or violence to campus authorities**. If you would like to speak to a confidential advocate, please consider reaching out to the [Berkeley PATH to Care Center](https://care.berkeley.edu/){:target="\_blank"}.

Finally, the main goal of this course is that you should learn and have a fantastic experience doing so. Please keep that goal in mind throughout the semester. Welcome to CS 189/289A!

## Acknowledgments

Some language in this syllabus is adapted from [Data 100](https://ds100.org/){:target="\_blank"}. Course Culture inspired and adapted with permission from [Fall 2021 CS 164 Syllabus](https://inst.eecs.berkeley.edu/~cs164/fa21/syllabus.html){:target="\_blank"}.
