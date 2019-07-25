## Installation and Usage

After cloning the repository, install the prerequisites:

```
pip install -r requirements.txt
```

Start the live development server:

```
lektor server
```

Browse to the reported URL.

Edit the files and see the results in the browser.
Don't use the admin panel (the pencil button) if you're not
familiar with lektor.

When you're done, push your changes and Travis will automatically
build and deploy the site. If you don't want to trigger a build
include the text `[skip ci]` on a separate line in the commit message.

## Files

The site content is under the `content` directory. There is
one directory per page. The content of the page is placed
into the `contents.lr` file in the corresponding directory.

News items have to be placed into the `news` directory.
Just copy an existing news item and edit the `contents.lr`
file of the new item.

The `ecosystem` page consists of `project` elements.
To add a new project copy an existing project and
edit the `contents.lr` file.
