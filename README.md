# CS 189/289A Fall 2025 Website

Taken from the Data 100 Spring 2025 Website

[![Deploy Jekyll site to Pages](https://github.com/berkeleyml/cs189-fa25-website/actions/workflows/jekyll.yml/badge.svg)](https://github.com/berkeleyml/cs189-fa25-website/actions/workflows/jekyll.yml) •
[![a11y specs](https://github.com/berkeleyml/cs189-fa25-website/actions/workflows/rspec.yml/badge.svg)](https://github.com/berkeleyml/cs189-fa25-website/actions/workflows/rspec.yml)

## Course Information

## Installation

Prerequisites:

- You have everything that [Jekyll requires](https://jekyllrb.com/docs/installation/)
- You have installed [Bundler](https://bundler.io/): `gem install jekyll bundler`

After cloning this repository and navigating into the directory, run the following command to install dependencies

```
cd cs189-fa25-website
bundle install
```

## Usage

To run the site locally, run:

```
bundle exec jekyll serve
```

The site will be available at `http://localhost:4000/fa25/`

## Testing

Before pushing changes, run these checks locally to ensure deployment tests will pass:

### Accessibility Tests

Check that all pages meet WCAG 2.1 AA standards:

```bash
bundle exec rspec spec/accessibility_spec.rb
```

### Linting Tests

Run code quality and formatting checks:

```bash
bundle exec rspec spec/linters_spec.rb
```

### All Tests

Run the complete test suite:

```bash
bundle exec rspec
```

### Build Test

Verify the site builds successfully:

```bash
bundle exec jekyll build
```

**Expected Results:**

- Accessibility tests should show `116 examples, 0 failures, 32 pending`
- All pages should `meet WCAG 2.1` and `meet WCAG 2.2`
- Linting tests should pass without errors
- Build should complete with `Site build complete.`

If any tests fail, fix the issues before pushing to prevent GitHub Actions failures.

## Deployment

This site is deployed via a [GitHub Action Workflow](.github/workflows/jekyll.yml). For more information see [GitHub Pages](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/about-github-pages-and-jekyll).

## Repository

**Note**: Update the GitHub repository URL in the badges above once you create the GitHub repository. The current badges point to `berkeleyml/cs189-fa25-website` as an example.

## Repository Structure

This section explains how to update and manage different parts of the course website.

### Adding/Updating Staff

**Location**: `_staffers/`

To add a new staff member, create a new `.md` file in the `_staffers` directory:

```yaml
---
name: Full Name
role: Instructor | Lead TA | UCS2 | UCS1
email: email@berkeley.edu
photo: Photo_Name.jpg
pronouns: He/Him | She/Her | They/Them
website: https://example.com (optional)
oh: Office hours description with location
order: 1 (for ordering, instructors typically use 1-2)
---
```

**Staff Photos**: Place photos in `resources/assets/staff_pics/` with dimensions 300x300px.

**Roles Available**:

- `Instructor` - Course instructors
- `Lead TA` - Lead teaching assistants
- `UCS2` - Undergraduate course staff (advanced)
- `UCS1` - Undergraduate course staff (entry level)

### Managing Course Schedule

**Location**: `_modules/`

The course schedule is managed through weekly module files (`week-01.md`, `week-02.md`, etc.).

**Module Structure**:

```markdown
---
title: Week X
---

Mon Jan 01
: **First Day of Classes**{: .label .label-deadline }

Tue Jan 02
: **Lecture 1**{: .label .label-lecture } [Topic] : [Notes](link), [Slides](link), [Notebook](link)

Wed Jan 03
: **Discussion 1**{: .label .label-disc } [Topic](link)

Thu Jan 04
: **Lecture 2**{: .label .label-lecture } [Topic] : [Notes](link), [Slides](link), [Notebook](link)

Fri Jan 05
: **Homework 1**{: .label .label-hw } [Assignment](link) (due TBD)
: **HW0 due**{: .label .label-due } Description
```

**Available Labels**:

- `.label-lecture` - Lectures (light blue)
- `.label-disc` - Discussions (light green)
- `.label-hw` - Homework assignments (light orange)
- `.label-due` - Due dates (light yellow)
- `.label-proj` - Projects (light peach)
- `.label-deadline` - Special dates/holidays (light blue)
- `.label-exam` - Exams (light gray)

### Adding/Updating Lectures

**Location**: `lecture/`

Each lecture has its own markdown file (`lec01.md`, `lec02.md`, etc.):

```markdown
---
layout: page
title: Lecture X – Topic Name
nav_exclude: true
---

# Lecture X – Topic Name

Content by many dedicated CS 189/289A instructors at UC Berkeley. See our [Acknowledgments](../../acks) page.

- [slides](link){:target="\_blank"}
- [code](datahub-link){:target="\_blank"}
- [code HTML](../../resources/assets/lectures/lecXX/lecXX.html){:target="\_blank"}
- [recording](youtube-link){:target="\_blank"}
```

**Lecture Resources**: Place Jupyter notebooks and exports in `resources/assets/lectures/lecXX/`

### Site Configuration

**Main Config**: `_config.yml`

- Site title, description, authors
- Base URL and deployment settings
- Navigation links
- Course-specific variables

**Key Settings to Update**:

```yaml
title: CS 189/289A - Introduction to Machine Learning
description: Introduction to Machine Learning
author: Instructor Names
baseurl: "/fa25"
url: "https://berkeleyml.github.io"
```

### Styling and Design

**Custom Styles**: `_sass/custom/`

- `module.scss` - Schedule badge colors and layout
- `course_overrides.scss` - Staff badge colors and general overrides

**Badge Colors**: Modify in `_sass/custom/module.scss` to change schedule item colors.

### Content Pages

**Main Pages**:

- `index.md` - Homepage with schedule
- `staff.md` - Staff directory
- `syllabus.md` - Course syllabus
- `calendar.md` - Office hours and events calendar
- `resources.md` - Course resources
- `setup.md` - Setup instructions
- `acks.md` - Acknowledgments

**Project Pages**:

- `gradproject.md` - Graduate project overview
- `gradproject-cv.md` - Computer vision track
- `gradproject-nlp.md` - NLP track

### Announcements

**Location**: `_announcements/`

Create `.md` files for course announcements:

```markdown
---
title: Announcement Title
week: X (optional)
date: 2025-01-15
---

Announcement content here.
```

### Assets and Resources

**Directory Structure**:

```
resources/
├── assets/
│   ├── staff_pics/        # Staff photos (300x300px)
│   ├── lectures/          # Lecture notebooks and exports
│   ├── favicon/           # Site icons
│   └── images/            # General images
```

### Testing and Validation

Before making changes:

1. Test locally: `bundle exec jekyll serve`
2. Run accessibility tests: `bundle exec rspec spec/accessibility_spec.rb`
3. Check linting: `bundle exec rspec spec/linters_spec.rb`
4. Verify build: `bundle exec jekyll build`

### Common Tasks

**Update semester**: Change `baseurl` in `_config.yml` and update dates in modules
**Add new assignment**: Create entry in appropriate week module with correct label
**Update office hours**: Modify the embedded calendar URLs in `calendar.md`
**Change course links**: Update the button URLs in `index.md`

## License

[MIT](LICENSE)
