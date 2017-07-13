djangocms-slider-easy-uploadcare
================

A simple django cms slideshow plugin. Fork of https://github.com/urga/djangocms-slider, but using uploadcare.

Features:

* There are 2 plugins: SlideShow and Slide. A SlideShow can only contains Slides. Those can be arranged in the order you want just like any other plugin.
* Each image can have a url specified (creating an anchor around the image)
* By default, creates a [flexslider](http://www.woothemes.com/flexslider/) slideshow.
* Uses the uploadcare 3.0.1 widget to enable free cropping (currently no setting to enable self-defined cropping dimensions)

Installation
------------

This plugin requires `django CMS 3.0` or higher to be properly installed and configured.

To install:

* run `pip install djangocms-slider-easy-uploadcare` on your virtualenv
* Make sure `pyuploadcare` is configured with the `UPLOADCARE` setting
* add `djangocms_slider_uploadcare` to your `INSTALLED_APPS` setting (mind the underscore)
* Run `./manage.py migrate djangocms_slider_uploadcare`


### Why use this plugin?

- Uploadcare is pretty great with an awesome widget, and very good at serving images *fast*
- If you've stumbled upon the well-known performance issues regarding cloud storage in combination with `easy-thumbnails` and `sorl-thumbnail`

### Own Flexslider config?
This can be done by overriding the `slider.html` template.

- Place a `djangocms_slider_uploadcare` directory with a `slider.html` in your `templates` directory
- In this `slider.html`, copy the original contents of `slider.html` and edit the Flexslider config included in it
