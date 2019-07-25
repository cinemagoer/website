After cloning the repository, install prerequisites::

  pip install -r requirements.txt

Start the live development server::

  lektor server

Browse to the reported URL.

Edit the files and see the results in the browser.
Don't use the admin panel (the pencil button) if you're not
familiar with lektor.

When you're done, push your changes and Travis will automatically
build and deploy the site. If you don't want to trigger a build
include the text `[skip ci]` on a separate line in the commit message.
