# Powerline eXtenstion for rbenv

This is a fork of [rbenv segment plugin](https://github.com/tilljoel/powerlinex-segment-rbenv) by [tilljoel](https://github.com/tilljoel), changed to work with rbenv.

# Installation

First install the addon:

    pip install -U --user git+https://github.com/duien/powerlinex-segment-rvm.git

If you make a theme, you can include a custom `segment_data`:

    "version": {
        "before": "ⓔ  "
    },

And then add this to your prefered spot under `segments`:

    {
        "module": "powerlinex.segment.rvm",
        "name": "version"
    },


The `highlight_group` of the segment returned is `ruby_version`, `virtualenv`,
in that order. This will be highlighted in the same way as `virtualenv`, unless
you specify something else in the `ruby_version` color.
