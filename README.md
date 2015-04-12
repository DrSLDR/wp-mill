# wp-mill
WordPress XML-export splitter
***
## What does it do?
wp-mill is a quick-and-dirty fix to pick apart a large WordPress XML/WXR export
  file into smaller, more manageable chunks. It takes the path to the XML/WXR
  file as an argument and spits out numbered XML files in its own directory,
  each containing 10 export items (this can be changed in the script).

## How do I use it?
    $ python3 wp-mill.py path/to/export.xml
It has been tested on Debian-based Linux but ought to work on Windows/OSX too. I
    guarantee nothing, however.

## What's it good for?
My WordPress site (or hosting provider; either or) didn't like having to import
  hundreds and hundreds of items in one go, and the import ended up crashing. To
  get around this, I read somewhere that splitting the import into smaller
  chunks would help. This was a rather daunting manual task, however, so I wrote
  wp-mill to do it for me.

## Can I use it?
Knock yourself out. It's under the MIT license, so you're free to use it
  commercially, noncommercially, modify it, distribute it, embed it in something
  else, or print it out and make paper airplanes. Just keep the license and
  copyright notice and don't come running to me if it breaks something.

## Dude, your python-skills are awful!
The words "quick-and-dirty" mean anything to you? Don't complain. Or, better
  yet, fix it and send me a pull request.

## I have more questions!
[Send them my way!](mailto:drsldr@sldr.se?subject=wp-mill)